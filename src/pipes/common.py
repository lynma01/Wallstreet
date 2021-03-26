#test the info, debug purposes
def log_assert_type(objt: list, typ):
    return (f"assert list is all {typ}: {all(isinstance(objt, typ) for item in objt)}")
