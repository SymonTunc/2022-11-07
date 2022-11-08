actions = {
    int: lambda v: print('int is gwesn:', v),
    str: lambda v: print('str is gwesn:', v),
}

def foo(param):
    # if type(param) is int:
    #     print('int is gwesn:', param)
    # elif type(param) is str:
    #     print('str is gwesn:', param)
    # elif: ...
    
    actions[type(param)](param)

foo(42)
foo('42')
