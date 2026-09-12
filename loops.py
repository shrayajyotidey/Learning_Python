# i=1;
# while(i<100):
#     print(i);
#     i+=1;

# j=100;
# while(j>0):
#     print(j);
#     j-=1;

# x = int(input('Enter a Number: '));
# y=1;
# while(y<=10):
#     print(f"{x} * {y} = {x*y}")
#     y+=1;

# list = [1,2,34,6,9,5,26,45,100];
# k=0
# while(k<len(list)):
#     print(list[k])
#     k+=1;

# tuple = (
#     4,5,54,58,12,40,130,100,12,15,8
# )
# print(tuple);
# l=0
# while(l<len(tuple)):
#     if(tuple[l]==100):
#         print(f'Number is Found in index {l}');
#         break
#     else:
#         print("finding...")
#     l+=1;

# i=0
# while(i<=10):
#     if(i%2 == 0):
#         i+=1
#         continue
#     print(i)
#     i+=1

# list = [1,2,34,6,9,5,26,45,100];
# for el in list:
#     print(el)
# else:
#     print("End")

# tuple = (
#     4,5,54,58,12,40,130,100,12,15,8,4
# )

# for el in tuple:
#     print(el)
# else:
#     print("End")
# x=4;
# i = 0;
# for el in tuple:
#     if(el == x):
#         print("Found at index",i)
#         break
#     i+=1
# else:
#     print("End")

# for i in range(1,101):
#     print(i)

# for i in range(100,0,-1):
#     print(i)

# n =5;

# for i in range(1,11):
#     print(n*i)

# n= int(input("Enter Number: "))
# sum = 0 
# # for i in range(n+1):
# #     sum += i
# # print(sum)
# i=0;
# while(i<=n):
#     sum += i
#     i+=1
# print(sum)

n= int(input("Enter Number: "))
fact = 1
for i in range(1,n+1):
    fact *= i;
print(fact)
# i=1
# while(i<=n):
#     fact *= i
#     i+=1
# print(fact)