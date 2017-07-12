#Check build status
def check_build_status(path):
    fails_counter = 0
    success_counter = 0
    with open(path) as log:
        for str in log:
            success_counter += 1 if str.find("BUILD SUCCESSFUL") != -1 else 0
            fails_counter += 1 if str.find("BUILD FAILED") != -1 else 0
        return fails_counter, success_counter

def checkFields(*args):
    for fld in args:
        if fld == "":
            result =  False
            break
        else:
            result =  True
    return result


def buildTime(val):
    m, s = divmod(val, 60)
    h, m = divmod(m, 60)
    return h,m,s