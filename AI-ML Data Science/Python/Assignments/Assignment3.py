# pali_str = input("Enter your String:")
# rev_str = pali_str[::-1]

# if(pali_str == rev_str):
#     print("its palindrom")

# else:
#     print("not a palindrom")

# pali_str = input("Enter your String:").lower()
# i = 0
# j = len(pali_str)-1
# flag = 1
# while(i<j):
#     if(pali_str[i] != pali_str[j]):
#         flag = 0
#         break
#     else:
#         i = i + 1
#         j = j - 1

# if (flag == 1):
#     print("palindrom")
# else:
#     print("not palindrom")


# list = [4,34,67,2,7,23,24,78,37]
# count=0
# sum = 0
# for i in list:
#     count = count + 1
#     sum = sum + i 

# avg = sum/count
# print(avg)


# list1 = list(map(int,input("Enter your numbers:").split()))
# list2 = list(map(int,input("Enter your numbers:").split()))

# list3 = list1+list2
# list3.sort()
# print(list3)


# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# even_tup = ()
# odd_tup = ()
# for i in numbers:
#     if(i%2==0):
#         even_tup = even_tup + (i,)
#     else:
#         odd_tup = odd_tup + (i,)

# print(f"even tupple is: {even_tup}")
# print(f"odd tupple is: {odd_tup}")\


# dict={}
# while True:
#     print("\nA - Add a student")
#     print("B - Update marks")
#     print("C - Search for a student")
#     print("D - Display all students and marks")
#     print("E - Exit")

#     key = input("Enter your alphabet:")

#     # Add Student
#     if (key == 'A'):
#         Name = input("Enter student name:")
#         marks = int(input("Enter your marks:"))
#         dict[Name] = marks


#     # Update marks
#     elif(key == 'B'):
#         name = input("Enter your name:")
#         if name in dict:
#             marks = int(input("Enter your marks:"))
#             dict[name]= marks
#         else:
#             print("student not found")

#     #Search for a student
#     elif(key == 'C'):
#         name = input("Enter your name:")
#         if name in dict:
#             print("Name:", name, "Marks:", dict[name])
#         else:
#             print("student not found")

#     # Display
#     elif(key == 'D'):
#         if(len(dict)==0):
#             print("no dict")
#         else:
#             for key, value in dict:
#                 print(dict.items())


# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# dict={}
# for word in words:
#     count = 0
#     for letter in word:
#         count+=1
    
#     dict[word]=count

# print(dict)


# str = input("Enter your string:")
# count = 0
# for letter in str:
#     if(letter==" "):
#         count +=1
#         continue

# print(count)
    

# str = input("Enter your string:")
# set_str = set(str)
# print(set_str)

# count = 0
# for i in set_str:
#     count+=1
# print(count)
