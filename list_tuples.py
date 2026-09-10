# list = []
# list.append(input("Enter Your First Favourite Movie Name: "))
# list.append(input("Enter Your Second Favourite Movie Name: "))
# list.append(input("Enter Your Third Favourite Movie Name: "))

# # list =[l1,l2,l3]
# print(list)
# print(type(list))

# list = [1,2,3,2,1]

# listCopy = list.copy()
# listCopy.reverse()  # list.reverse returns none so we can not directly use this 
# if(list == listCopy):
#     print("Palindrome")

tup = ("A", "B", "E", "A", "C", "H", "G");
print(tup.count("A"))

list = []
# list.append(tup)
list.extend(tup)
list.sort()
print(list)