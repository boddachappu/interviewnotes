def operation(op):
    def inner(fn):
        def wrap(a, b):
            if op == '+':
                return a + b
            elif op == '*':
                return a * b

        return wrap

    return inner


@operation(op="*")
def performOperation(a, b):
    return


ob = performOperation(2, 3)
print(ob)


def check(fn):
    def wrap(a, b):
        if b == 0:
            raise ZeroDivisionError
        return a / b

    return wrap


@check
def divisin(a, b):
    return


ob = divisin(4, 2)
print(ob)


print(ord('a'))
print(chr(97))
