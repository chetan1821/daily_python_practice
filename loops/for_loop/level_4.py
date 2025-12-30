# LEVEL 4: Number-wise Logic (Exam Favourite)

# 1️⃣6️⃣ Print all prime numbers between 1 and 100

# for number in range(1, 101):

#     if number <= 1:
#         continue   
#     flag = 0
#     for i in range(2, number):
#         if number % i == 0:
#             flag = 1
#             break

#     if flag == 0:
#         print(number, "is prime")
#     else:
#         print(number, "is not prime")


# 1️⃣7️⃣ Check whether a number is Armstrong

# num = int(input("Enter number : "))
# digits = len(str(num))
# arm = 0
# temp = num

# while num>0:
#     rem = num%10
#     arm=arm+(rem ** digits)
#     num=num//10

# if temp == arm:
#     print("is armstrong")
# else:
#     print("is not armstrong")


# 1️⃣8️⃣ Reverse a given number

# num = int(input("Enter the number :"))
# rev=0
# temp=num
# while num>0:
#     rem=num%10 #rem
#     rev = rev * 10 + rem
#     num = num // 10

# print("Reverse number is :", rev)





# 1️⃣9️⃣ Check whether a number is palindrome

# num = int(input("Enter the number :"))
# rev=0
# temp=num
# while num>0:
#     rem=num%10 #rem
#     rev = rev * 10 + rem
#     num = num // 10

# # print("Reverse number is :", rev)

# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not palindrome")

# 2️⃣0️⃣ Find sum of digits of a number

# num = int(input("Enter the number : "))
# add_num = 0
# while num>0:
#     rem = num%10
#     add_num += rem
#     num = num // 10

# print(add_num)