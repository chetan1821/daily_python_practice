# Basic Syntax of Function

# def greet():
#     print("hello this is chetan !!")

# greet()

# def add(x,y):
#     z=x+y
#     return z

# z = add(10,20)
# print(z)

# def squre(n):
#     return (n*n)
# a=squre(5)
# b=squre(6)
# print(a,b,end=' ')

# 2.user define function => created by programmer
#     => Function Without Parameter & Without Return
print("Function Without Parameter & Without Return")
def say_hello():
    print("hello this is me !!")
say_hello()
      
#     => Function With Parameter & Without Return
print("Function With Parameter & Without Return")
def even_odd(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
even_odd(10)

#     => Function Without Parameter & With Return
print("Function Without Parameter & With Return")
def get_pi():
    return 3.14

x = get_pi()
print(x)


#     => Function With Parameter & With Return (MOST USED)
print("Function With Parameter & With Return")
def SI(p,r,t):
    # print((p*r*t)//100)
    return (p*r*t)//100
simple_interst= SI(10000,3,1)
print(simple_interst)




