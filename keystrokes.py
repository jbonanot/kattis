password = input()
length = len(password)
newPass = ""
i=0
while length > 0:
    if password[i] == "L":
        newPass = password[i+1] + newPass
        length-=1
    if password[i] == "R":
        newPass = newPass + password[i+1]
        length-=1
    if password[i] == "B":
        newPass = newPass - password[i-1]
        length-=1
    else:
        newPass = newPass + password[i]
        length-=1
print(newPass)