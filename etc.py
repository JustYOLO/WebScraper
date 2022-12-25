def linecut():
    print("\n/////////////////////////////////////////////////////////")


def strClean(target, toDelete=None):
    if toDelete == None:
        return target.replace("\n", "").replace("  ", "")
    else:
        return target.replace(toDelete, "").replace("\n", "").replace("  ", "")
