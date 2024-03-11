# while loop iterates over a sequence, not a condition
# break the loop
# x = 1
# while x == 1:
#     print('yes')

#     x += 1

# x=10
# while x >= 1:
   
#     print('yes')

#     x -= 1

# x = 10
# while x >= 1:
#     print('yes')

#     x -= 1

# x = 10
# while x >= 1:
#     print(f'yes {x}')

#     x -= 1

# user = input('USSD: ').strip()
# while user != '*321#':
#     print ('Invalid ussd code.Try again')
#     user = input('USSD: ').strip()

# print('Welcome to myMTN')

# slot = 10
# admission_list = []

# while slot >= 1:
#     name = input('Aspirant name: ')
#     admission_list.append(name)

#     slot -= 1

# print(admission_list)

# x = 1 
# while True:
#     print(x)

#     if x == 10:
#         continue
#     if x == 20:
#         break

#     x += 1

ticket = 10
while ticket >= 1:
    age = int(input('Age: '))
    if age < 18:
        continue
    else:
        print(ticket)
