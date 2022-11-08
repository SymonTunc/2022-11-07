def foo(*args):
    print(type(args), args)
    print('foo gscheit:', *args)

foo('Joerg', 'Faschingbauer')
foo('Joerg', 'Faschingbauer', 'Der Erste')
