## Get integer for input
while True:
    try:
        x = int(input("Define the value of x "))
## Error Message if integer is not received
    except ValueError:
        print("x is not an integer")
## Print the value of x
    else:
     break

print(f"x is {x}")