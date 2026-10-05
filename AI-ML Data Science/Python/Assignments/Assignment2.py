# salary = int(input("Enter your current salary:"))

# if (salary<30000):
#     tax = (salary*5)/100
#     print("5% tax laga")
# elif (salary>=30000 and salary<=70000):
#     tax = (salary*15)/100
#     print("15% tax laga")
# else:
#     tax = (salary*25)/100
#     print("25% tax laga")

# print(tax)

# def even_num(a,b):
#     for i in range(a,b+1):
#         if(i%2==0):
#             print(i)
# print(even_num(1,10))


# def digit(n):
#     while(n!=0):
#         digit = n % 10
#         print(digit)
#         n = n//10

# digit(2345)

# def count_dig(n):
#     count=0
#     while(n!=0):
#         digit = n % 10
#         count += 1
#         n = n // 10
#     return count

# print(count_dig(2143255))


# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact*i
    
#     return fact
# print(factorial(6))


# def digit_sum(n):
#     sum = 0
#     while(n!=0):
#         digit= n % 10
#         sum+= digit
#         n = n/10

#     return sum

# print(digit_sum(234))

# for i in range(1, 101):
#     if(i%3==0 and i%5==0):
#         print(i)


# while(True):
#     user_input = input("Enter your number, or type (quit) to exit:")

#     if(user_input.lower() == "quit"):
#         print("terminated")
#         break

#     n = int(user_input)
#     if(n>0):
#         print("positive")
#     elif(n<0):
#         print("negative")
#     else:
#         print("number is zero")
