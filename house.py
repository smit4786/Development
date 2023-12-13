""" def main():
    #Gryffindor = ["Harry", "Ron", "Hermoine"]
    #Slytherin = ["Draco"]
    #Hufflepuff = ["Justin"]

    name = input("What is your name? ")
    if name == "Harry":
        print("Gryffindor")
    elif name == "Hermoine":
        print("Gryffindor")
    elif name == "Ron":
        print("Gryffindor")
    elif name == "Draco":
        print("Slytherin")
    else:
        print("Who?")
main() """

name = input("What is your name? ")
match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")