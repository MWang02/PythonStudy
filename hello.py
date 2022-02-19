# where I practice some python

def main():
    hello()
    print(fibonacci(10))
    towers(3)


# prints hello world
def hello():
    print("Hello World!")


# returns the n'th term in the fibonacci sequence
def fibonacci(n: int) -> int:
    # base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # recursive case
    return fibonacci(n-1) + fibonacci(n-2)


# prints out the steps of towers of hinoi
def towers(n: int):
    # prints the tower contents
    def printtow(x: list, y: list, z: list):
        print(x)
        print(y)
        print(z)

    tow1 = list(n-i for i in range(n))
    tow2 = tow3 = list()
    printtow(tow1, tow2, tow3)


if __name__ == "__main__":
    main()
