nameList = []
emailList = []
for i in range(0,5):
    name = input("enter names ? ")
    email = input("enter email ? ")
    nameList.append(name)
    nameList.append(email.lower())


print(nameList)
print(emailList)