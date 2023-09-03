class A:
    def __init__(self) -> None:
        pass

class B(A):
    pass
class C(A):
    pass


def get(a : A, b : A):
    print(type(a) != type(b))
get(B(),C())