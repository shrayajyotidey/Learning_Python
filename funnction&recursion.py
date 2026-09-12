# def ph():
#     return ("Hello...")

# ph()  # will show nothing because returned value is not stored and passed 
# output = ph()
# print(output)

# def ph():
#     print("Hello")
# ph()
# op = ph()  #will show none if we print the op because nothing is returned by the function
# print(op)

# li = [
#     1,2,3,4,5,6
# ]
# def printList(list):
#     print(len(list))

# printList(li)

# n = int(input("Enter n: "))
# def fact(no):
#     i = 1
#     f = 1
#     while(i<=no):
#         f *= i
#         i+=1;
#     print(f);

# fact(n);

# def changeCurrency(money):
#     ind = money * 95
#     print(ind)

# changeCurrency(100)

# def checkOddEven(num):
#     if(num%2==0):
#         print("Even")
#     else:
#         print("Odd");

# checkOddEven(5)
# checkOddEven(2)

# def sumNatural(no):
#     if(no==0):
#         return 0
#     else:
#         return (no + sumNatural(no-1));

# print(sumNatural(5))

# def displayListElement(list, i):
#     if(i==-1):
#         return
#     else:
#         print(list[i], end=" ")
#         return displayListElement(li,i-1)

# li = [1,2,3,4,5,7,6]
# i = len(li) - 1
# print(i)
# displayListElement(li,i)

def displayListElement(lst, i =0):
    if(i==len(lst)):
        return
    else:
        print(lst[i], end=" ")
        return displayListElement(lst,i+1)

li = [1,2,3,4,5,7,6]
displayListElement(li)