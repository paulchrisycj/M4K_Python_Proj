##file = open("sample.txt", "w")
##file.writelines("Hello\n")
##file.writelines("Hello 2")
##file.close()
##
##rf = open("sample.txt")
##print(rf.readline())
##print(rf.readline())

##num = input("Enter a number: ")

#Write a program that asks a user for a number of
#inputs, then ask the user for that number of inputs
#store all the inputs into a .txt file seperated by
#newlines.

##NoI = int(input("Enter number of drinks: "))
##file = open("sample.txt", "w")
##for i in range(0, NoI):
##    drinkName = input("Drinks name: ")
##    drinkNum = input("Amount of " + drinkName + ": ")
##    file.writelines(drinkName + ", " + drinkNum + "\n")
##file.close()

LoD = []
rf = open("sample.txt")
for string in rf:
    string = string.strip("\n")
    D = string.split(", ")
    LoD.append(D)
print(LoD)
