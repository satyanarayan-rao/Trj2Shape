
def autoconvert(s):
    for fn in (int, float):
        try:
            return fn(s)
        except ValueError:
            pass
    return s


