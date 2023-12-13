def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
## Get integer for input
    while True:
        try:
            return int(input("Define the value of x "))
## Error Message if integer is not received
        except ValueError:
            print("x is not an integer")
            pass
main()