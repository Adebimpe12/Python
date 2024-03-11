'''
Ask how many students are taking the test
'''
user_number = int(input('How many student are taking the test?: '))
'''
Register each student
'''
student_list = [input(f'Name of student{student + 1}: ') for student in range(user_number)]
print(student_list)

score_list = []
'''
Call each student one after the other to take the test
'''
for each_student in student_list:
    print(f'\n{each_student}, Its time for your test.\n')

    '''The test'''
    score = 0
    questions = ['1. What is my name\na.) Arise Damilare b.)Arise Damilare', 
                 '2. Am I Male\na.) Yes b.) No', 
                 '3. Do you love your president? \na.) Yes b.) No'
                 ]
    answers = ['a', 'a', 'a']
    for question, answer in zip(questions, answers):
        print(question)
        user_ans = input ('Answer: ').strip().lower()

        if user_ans == answer:
            print('correct')
            score += 5
    print(f'Thank you for taking the test, your total score is {score}' )
    score_list.append(score)

print(student_list)
print(score_list)

zip(student_list,score_list)
for student_list, score_list in zip(student_list, score_list):
    print (f'{student_list}--{score_list}')



# scores = [2, 4, 5 ,9 ,1, 8]
# max = scores[0]
# for score in scores:
#     if score > max:
#         max = score
# print(max)

# minimum_score_student = min(scores)
# print ('minimum score, minimum_score_student')