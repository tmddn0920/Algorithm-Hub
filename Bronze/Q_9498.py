score = int(input())
if(90 <= score and 100 >= score):
    print("A")
elif(80 <= score and 90 > score):
    print("B")
elif(70 <= score and 80 > score):
    print("C")
elif(60 <= score and 70 > score):
    print("D")
else:
    print("F")