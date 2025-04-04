str = input()
isPel = True;
for i in range(0, len(str)):
    if str[i] != str[len(str) - 1 - i]:
        isPel = False;
if(isPel == True):
    print(1)
else:
    print(0)