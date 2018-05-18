#python3
user = []
userInput = []
while True:
    userInput = input()
    if userInput != 'end':
        user.append(userInput.split())
    else:
        break;
print(user)

for i in range(len(user)):
    print(i)
    for j in range(len(user[i])):
        sum = user[j:][i]
        print(sum, end=" ")
    print("\n")
#print(user)