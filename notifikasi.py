def xxx():
    a=10
    b=15
    c=20
    return a,b

def yyy():
    a,b = xxx()
    print a        ### value a from xxx()
    print b        ### value b from xxx()

yyy()