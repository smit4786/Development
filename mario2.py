## Print x blocks of code
def main():
    number = get_number()
    print_square(number)
## Get user input 
def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            return n
        
# for each row in square
def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()