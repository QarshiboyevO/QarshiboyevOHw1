def typeBasedTransforms(**kwargs):
    transformed={}
    for key, value in kwargs.items():
        if isinstance(value, (int,float)):
            transformed[key]=value**2
        elif isinstance(value, str):
            transformed[key]=value[::-1]
        elif isinstance(value, (tuple,list)):
            transformed[key]=value[::-1]
        elif isinstance(value, bool):
            transformed[key]= not value

        else:
            transformed[key]=value

    return transformed

