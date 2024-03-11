class Authorization:
    def __init__(self) -> None:
        user1 = {'username':'password'}
        
      

    self.home()

    def home(self):
    
        user = input((f'''
            Welcome to {self.bankname} {self.rc_no}, {self.branch} branch.
        1. Sign up
        2. Sign in
        #. Exit
        '''))

        if user == '1':
            self.Sign_up()

        elif user == '2':
            self.Sign_in()

        else:
            exit
            
        

    def Sign_in (self):
        input('Enter your username: ')
        int(input('Enter your password'))


    def Sign_up (self):
        username = input('Enter your username: ')
        password = int(input('Enter your password: '))
        user.update({username})
        user.update({password})

