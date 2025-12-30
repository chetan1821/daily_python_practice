# LEVEL 3: Mathematical Logic (Important)

# 1️⃣1️⃣ Find sum of numbers from 1 to 100

# sum = 0
# for num in range(1,101):
#     sum += num
# print("sum of numbers from 1 to 100 : ",sum)

# 1️⃣2️⃣ Find sum of even numbers from 1 to 100

# sum = 0
# for num in range (1,101):
#     if num%2==0:
#         sum += num

# print("sum of even numbers from 1 to 100 : ",sum)

# 1️⃣3️⃣ Find sum of odd numbers from 1 to 100

# sum = 0
# for num in range (1,101):
#     if num%2 != 0:
#         sum += num

# print("sum of odd numbers from 1 to 100 : ",sum)


# 1️⃣4️⃣ Find factorial of a number

# num = int (input("Enter number : "))
# fact = 1
# if num < 0:
#     print("factorial is not defined for negitive numbers")
# elif num == 0:
#     print("the factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         fact *= i
#     print(f"the factorial of {num} is {fact} ")

# 1️⃣5️⃣ Check whether a number is prime

# num = int(input("Enter the number"))
# flag=0
# for i in range(2,num):
#     if num%i==0:
#         flag=1
#         break

# if flag == 0:
#     print(f"{num} is prime")
# else:
#     print(f"{num} is not prime")