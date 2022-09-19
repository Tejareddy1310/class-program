NumList = []
Even_Sum = 0
Odd_Sum = 0
j = 0
n = int(input("enter the total number of list elements: "))
for i in range(1, n + 1):
    value = int(input("enter the value of %d element : " %i))
    NumList.append(value)

while(j < n):
    if(NumList[j] % 2 == 0):
        Even_Sum = Even_Sum + NumList[j]
    else:
        Odd_Sum = Odd_Sum + NumList[j]
    j = j+ 1

print("\nThe Sum of Even Numbers in this List =  ", Even_Sum)
print("The Sum of Odd Numbers in this List =  ", Odd_Sum)
