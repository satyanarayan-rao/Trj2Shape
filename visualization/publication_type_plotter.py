import os
import sys
from argparse import ArgumentParser
from math import ceil
from scipy.stats.stats import pearsonr
from scipy.stats import spearmanr
import seaborn as sns
import pandas as pd
from dotmap import DotMap
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
majorFormatter = FormatStrFormatter('%0.1f')
import yaml
import matplotlib
import string
from matplotlib.backends.backend_pgf import FigureCanvasPgf
matplotlib.backend_bases.register_backend('pdf', FigureCanvasPgf)## TeX preamble
preamble = [
    r'\usepackage{fontspec}',
    r'\fontspec{Arial}',
    r'\usepackage{color}',
    r'\usepackage{amsmath}',
    r'\usepackage{xcolor}',
    r'\definecolor{darkcyan}{rgb}{0.0, 0.55, 0.55}',
    r'\definecolor{lightmagenta}{HTML}{EF56DF}',
]

pgf_with_latex = {
    "text.usetex": True,            # use LaTeX to write all text
    "pgf.rcfonts": False,           # Ignore Matplotlibrc
    "pgf.preamble": preamble
}

matplotlib.rcParams.update(pgf_with_latex)
sns.set_style("white", {"ytick.major.size":"5",
                        "xtick.major.size":"5",
                        'font.family': [u'Arial']})#, rc={'text.usetex': True} )
sns.set_context('paper', font_scale=1.25)
__y_label_dict__ ={'MGW':r'$\text{MGW}$ [' + r'\textrm{\AA}' + ']',
                   'Roll':r'$\text{Roll}$ [' + r'$^\circ$' + ']',
                   'ProT':r'$\text{ProT}$ [' + r'$^\circ$' + ']',
                   'HelT':r'$\text{HelT}$ [' + r'$^\circ$' + ']'
                   }
__y_ticks_limit_dict__ = {
    'MGW': (2, 11),
    'Roll': (-20, 20),
    'ProT': (-20, 20),
    'HelT': (25, 40)
    }
__feature_type__ = {
        'bp': {'MGW', 'ProT'},
        'bp_step': {'Roll', 'HelT'}
        }

def plot_bp_feature(config_dict=None, feature=None, ax=None):
    df = pd.read_csv(config_dict.shape_features_data[feature],
            sep="\s+",
            header='infer')
    sub_df = df[3:17]
    sns.set_style("white", {"ytick.major.size":"5", "xtick.major.size":"5", 'font.family': [u'Arial']} )#, rc={'text.usetex': True} )
    sns.set_context('paper', font_scale=1.25)
    subplt = sns.pointplot(data=sub_df, x="ResId", y="Mean")
    x_coords = []
    y_coords = []
    for point_pair in subplt.collections:
        for x, y in point_pair.get_offsets():
            x_coords.append(x)
            y_coords.append(y)
    subplt.errorbar(x_coords, y_coords,
            yerr=sub_df["Std"].tolist(), ecolor="black",
            fmt='o', capsize=1.5, capthick=0.5, elinewidth=0.75)
    sns.despine ( offset = 0, trim = True )
    subplt.set(ylim=__y_ticks_limit_dict__[feature])
    subplt.set_ylabel(__y_label_dict__[feature])
    ax.yaxis.set_major_formatter(majorFormatter)
    subplt.set_xlabel('')
    nucs="TTTTCCTAAAATGT"
    subplt.set_xticklabels(labels=list(nucs))
    return subplt

def plot_bp_step_feature(config_dict=None, feature=None, ax=None):
    pass
def plot_shape(config_dict=None, ax=None):
    shape_features_data = config_dict.shape_features_data
    for feature in shape_features_data.keys():
        print (__feature_type__['bp'])
        if feature in __feature_type__['bp']:
            subplt = plot_bp_feature(config_dict, feature=feature, ax=ax)
        else:
            subplt = plot_bp_step_feature(config_dict, feature=feature, ax=ax)
    return subplt


__argument_parser__ = ArgumentParser("Plot average shape feature profiles")
__argument_parser__.add_argument('--config', dest='config', type=str,
                                 help='a yaml file containing names of files required')
__argument_parser__.add_argument('--out', dest='output', type=str,
                                 help='output figure filename; please use `.png` extension')
__args__ = __argument_parser__.parse_args()
if len(sys.argv) == 1:
    __argument_parser__.print_help()
    exit(-1)

__config_yaml_dict__ = yaml.load(open(__args__.config).read())
__config_yaml_dict__ = DotMap(__config_yaml_dict__)
__output_file__ = __args__.output


fig = plt.figure(figsize=(5,5))
grid_rows = 1
grid_cols = 1
c=1
ax = plt.subplot(grid_rows, grid_cols, c)
subplt = plot_shape(__config_yaml_dict__, ax=ax)
plt.tight_layout()
base, ext = os.path.splitext(__output_file__)
shape_feature='MGW'
shape_feature_output_file = "".join([base, ".", shape_feature, ext])
#plt.savefig(shape_feature_output_file, dpi=__config_yaml_dict__.dpi)
tmp_filename = "tmp"+'.'+ shape_feature + '.pdf'
plt.savefig(tmp_filename)
print("converting pdf to png - high resolution ...")
command_str = " ".join(["pdftoppm",  tmp_filename, "out", "-png", "-f 1", "-r " + "300"])
os.system(command_str)
print("trimming whitespace...")
command_str = " ".join(["convert", "out-1.png", "-trim", "out-trimmed.png"])
os.system(command_str)
print("adding small border ...")
command_str = " ".join(["convert", "-bordercolor", "white",
                        "-border", str(10),
                        "out-trimmed.png", shape_feature_output_file])
os.system(command_str)
