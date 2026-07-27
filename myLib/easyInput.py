def get_and_check(msg : str, datatype):
    if datatype not in (int, str, bool, float):
        raise TypeError(f"Datatype must be in int, str, bool, float.\nExample : varName = get_and_check('Your message here', datatype)") 

    while True:
        if datatype is int:
            try:
                res = int(input(msg))
                return res
            except ValueError:
                print("Please enter a valid integer.")

        elif datatype is bool:
            try:
                res = input(msg)
                if res.lower() in ['true', 't', 'yes', 'y', '1']:
                    res = True 
                elif res.lower() in ['false', 'f', 'no', 'n', '0']:
                    res = False
                else:
                    raise ValueError("Must enter True or False.")
                return res
            except ValueError:
                print("Please enter a valid boolean.")

        elif datatype is float:
            try:
                res = float(input(msg))
                return res
            except ValueError:
                print("Please enter a valid float.")
        elif datatype is str:
            res = input(msg)
            break
    return res