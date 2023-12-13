## Get integer for input
try:
    x = int(input("Define the value of x "))
## Error Message if integer is not received
except ValueError:
    print("x is not an integer")
## Print the value of x
else:
    print(f"x is {x}")