##f1 = open("sample.txt", "w")
##f1.writelines("Hello\n")
##f1.writelines("Hello 2")
##f1.close()
##
rf = open("sample.txt", "r")
for string in rf:
    string = rf.readline()
    string = string.strip("\n")
    spl = string.split(", ")
    print(spl)

#number = input("Enter a number: ")
#print(number)

#Write a program that asks a user for a number of
#inputs, then ask the user for that number of inputs
#store all the inputs into a .txt file seperated by
#newlines.

##NoI = int(input("Number of drinks: "))
##file = open("sample.txt", "w")
##for x in range(0, NoI):
##    drink = input("Enter drink name: ")
##    num = input("Enter number of " + drink + ": ")
##    file.writelines(drink + ", " + num + "\n")
##file.close()

rf = open("sample.txt", "r")
ListOfDrinks = []
for string in rf:
    string = string.strip("\n")
    spl = string.split(", ")
    spl[1] = int(spl[1])
    ListOfDrinks.append(spl)

print(ListOfDrinks)
##print(spl)

