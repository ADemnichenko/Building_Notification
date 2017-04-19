def check_build_status(path):
    log = open(path)
    fails_counter = 0
    success_counter = 0

    for str in log:
        success_counter += 1 if str.find("BUILD SUCCESSFUL") != -1 else 0
        fails_counter += 1 if str.find("BUILD FAILED") != -1 else 0

    log.close()
    return fails_counter, success_counter

