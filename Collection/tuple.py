# t=(10,20,["abc","bca"],40,50)
# print(t)
# l=[10,20]
# l.append("hello")
# print(l)
# # print(t[2].append("xyz"))
# t[2].append("hello")
# print(t)
# t[2].extend(l)
# print(t)

# list_1=[10,20,("hello","bca"),40,50]
# print(list_1)
# print(list_1[2])
# # list_1.append("hello")
# list_1[2].append("hello")
# print(list_1)

# nums = [1,2,3,4,5,6]
# evens = [x for x in nums if x%2==0]
# print(evens)

# list input
# l=list(map(int,input("Enter the number").split()))
# print(l)

# lst= input("Enter string : " ).split()
# print(lst)

# n= int(input("Enter the elements : "))
# lst=[]
# tup=[]
# tuple_even=tuple(tup)
# for i in range(n):
#     x=int(input("Enter value :"))
#     if x%2==0:
#         tup.append(x)

#     else:
#         lst.append(x+1)
#         tup.extend(lst)

# tuple_even=tuple(tup)
# print(lst)
# print(tup)
# print(tuple_even)

n = int(input("Enter size: "))
lst = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
print(lst)

