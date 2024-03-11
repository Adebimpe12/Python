class CbtExam:
    def __init__(self):
        self.student_db = {}

    def no_students(self):
        self.num_students = int(input('How many students are taking the test? '))
        return self.num_students

    def student_database(self):
        self.num_students = self.no_students()
        x = 0 
        self.student_list = []
        
        for x in range(self.num_students):
            self.name = input(f"Student name {x + 1}: ")
            self.student_id = input(f"Student ID {x + 1}: ")
            
            self.student_list.append(self.name)
            self.student = {
                "name": self.name,
                "student_id": self.student_id
            } 
            
            self.student_db[f'student {x + 1}'] = self.student
            
        print(f'Student Database: {self.student_db}')
        print(self.student_list)
        
    def questions(self):
        self.score = 0
        self.score_list = []
        questions = ['1. What is my name\na.) Arise Damilare b.)Arise Damilare', 
                    '2. Am I Male\na.) Yes b.) No', 
                    '3. Do you love your president? \na.) Yes b.) No'
                    ]
        answers = ['a', 'a', 'a']
        
        for self.name in self.student_list:
            print(f'\n{self.name}, Its time for your test.\n')
            for question, answer in zip(questions, answers):
                print(question)
                user_ans = input ('Answer: ').strip().lower()

                if user_ans == answer:
                    print('correct')
                    self.score += 5
            print(f'Thank you for taking the test, your total score is {self.score}' )
            self.score_list.append(self.score)

            print(self.score_list)

        zip(self.student_list,self.score_list)
        for self.student_list, self.score_list in zip(self.student_list, self.score_list):
            print (f'{self.student_list}--{self.score_list}')

Cbt_exam = CbtExam()
Cbt_exam.student_database()
Cbt_exam.questions()









