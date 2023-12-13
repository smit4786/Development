def main():
    print_square(3)

# for each row in square
def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()