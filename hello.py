#Define a function called hello, Default value of "World"
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("Hello,", to)
    
main()