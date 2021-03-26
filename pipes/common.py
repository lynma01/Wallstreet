from collections import Sequence



#Remove non-informational items from dict
def munge_list_of_items(spam:list, box:dict):    
    for k in ["Documents", "Items"]:
        if k in box: 
            box.pop(k)


#test the info, debug purposes
def log_assert_type(objt: list, typ: type):
    return (f"assert list is all {typ}: {all(isinstance(objt, typ) for item in objt)}")
