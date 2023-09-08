names = []
phoneNumbers = []

num =int(input('Enter no of contact you want to save : '))
for i in range(num):
    name = input('Name :')
    phoneNumber = input('Phone Number : ')
    names.append(name)
    phoneNumbers.append(phoneNumber)
print('\n Name \t\t Phone Number \n')
for i in range(num):
    print("{}\t\t{}".format(names[i],phoneNumbers[i]))

searchTerm = input('\n Enter search term : ')
if searchTerm in names:
    index = names.index(searchTerm)
    phoneNumber = phoneNumbers[index]
    print("Name : {} ,Phone Number : {}".format(searchTerm,phoneNumber))
else:
    print("Name Not Found !")
