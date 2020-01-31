def hello(name,loud=False):
    if loud:
        print('Hello %s' %name.upper())
    else:
        print('Hello %s' %name.upper())

hello('Bob')
hello('Jack',loud=True)
