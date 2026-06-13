


 
# class person:
#     def __init__(self, name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender 

# person1 = person("Hanad", 20, "male")
# print(person1.name)
# print(person1.gender)

# height = float(input("Enter height in Meter : "))
# weight = float( input("Enter weight in KG :"))
# bmi =  weight / (height)**2
# print(bmi)

# if bmi >= 30:
#     print("Obesity")
# elif bmi > 25 and bmi < 29:
#     print("Overweight")
# elif bmi >18.5 and  bmi <25:
#     print("Normal")
# elif bmi < 18.5:
#     print("underweight") 

# india= ["Mumbai", "Bangalore", "Chennai", "Delhi"]
# usa = ["New York","Chicago","Las Vegas", "San Francisco"]
# uk = ["London", "Manchester", "Liverpool", "Nottingham"]

# city = input("Enter a city name : ").strip()

# if city in india:
#  print("Your city is in india")
# elif city in usa:
#  print("city in usa")
# elif city in uk:
#  print("city in uk")
# else:
#  print("city is not in the list")


# for n in range(1, -6, -2):
#     print(n, end=', ')

# number of rows

# n = 5
# for i in range(n, 0, -1):      # controls rows
#     for j in range(1, i + 1):  # prints numbers
#         print(j, end=' ')
#     print()  # move to next line

# sum = 0
# for i in range(1,21):
#     if i%2 == 1:
#         continue
#     sum = sum+i

# print(sum)
total = 0
i = 1

# while i <= 20:
#     if i % 2 == 0:   # check even number
#         total = total + i
#     i += 1

# print("Sum =", total)
# dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
# six=0
# sixes=0
# ones = 0
# for i in dice_result:
#     if i==6 and i+1==6:
#         sixes= sixes+1
    
#     if i==1:
#         ones=ones+1


# print(f"you have 1s in {ones} times")
# print(f"you have two in {sixes} times")

# def print_pattern(n):

#     if n % 2 == 1:          # odd number
#         for i in range(1, n + 1):
#             print('* ' * i)

#     else:                   # even number (flipped)
#         for i in range(n, 0, -1):
#             print('* ' * i)


# # Example
# n = int(input("Enter n: "))
# print_pattern(n)

# def master_yoda(sentence):
#     words = sentence.split()   # split sentence into words
#     words.reverse()            # reverse word order
#     return " ".join(words)     # join words back into string


# # Example
# text = input("Enter a sentence: ")
# print(master_yoda(text))



# name = ('hanad' , 'ali', 'moha', 'rahmo')

# for n in name:
#     print(f"{name} : {len(n)}")


# my_expenses = dict()
# wife_expenses = dict()

# my_expenses['Clothes'] = 100
# my_expenses['Shoes'] = 1000
# my_expenses['Watch'] = 900
# my_expenses['Mobile Recharge'] = 699
# my_expenses['Petrol'] = 1980


# wife_expenses.update({
#     "Mobile Recharge" : 799,
#     "DTH recharge" : 999,
#     "Clothes" : 2310,
#     "Makeup" : 3670,
#     "Shoes" : 999
# })

# totol = 0
# for i in my_expenses.values():
#     totol = totol+ i
# print(totol)







