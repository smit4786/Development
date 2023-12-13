## Determine if a number is even or odd
def main():
    x = int(input("What is the value of x? "))
    if is_even(x):
        print("x is Even")
    else:
        print("x is Odd")

def is_even(n):
    return n % 2 == 0
main()