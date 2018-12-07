

def Print(*args):
    'print helper'
    print(*args, sep='\n\n')

# decorators:
result = lambda f: f()


def func():
    return "[ I'm a function ]"


def data():
    return "[ I'm a string ]"
data = result(data)


@result
def text():
    return "[ I'm a string ]"


Print(
    func(),
    text,
    data,
)
