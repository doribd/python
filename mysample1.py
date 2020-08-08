class FactorialArgumentException(Exception):
    def _init_(self, arg):
        self._arg = arg

    def __str__(self):
        return "provided argument %s is wrong" % self._arg

    def get_arg(self):
        return self._arg


def factorial(n):
    try:
        if not isinstance(n, int) or n < 0:
            raise FactorialArgumentException(n)
    except FactorialArgumentException as e:
        print("Expecting positive number but got %s" % type(e.get_arg()))
    else:
        temp = 1
        for i in range(n, 0, -1):
            temp = temp * i
        return temp


def main():
    print("Solving factorial in the long way")
    print(factorial(5))

    print("Solving factorial in the short lambda way")
    fact = lambda x: 1 if x == 0 else x * fact(x - 1)
    print(fact(5))


main()
