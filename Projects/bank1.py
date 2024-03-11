class Bank:
    def __init__(self) -> None:
        self.bankname = 'UBA'
        # self.rc_no = '20' + input('any 8 digit of your choice: ')
        self.rc_no = '2033356'
        self.branch = 'Abuja'

    def home(self):
        print(f'''
            Welcome to {self.bankname} {self.rc_no}, {self.branch} branch.
        1. Sign up
        2. Sign in
        ''')

bank = Bank()
bank.home()

class newBranch(Bank):
    def __init__(self):
        super().__init__()
        self.branch = 'Ogbomoso'

new = newBranch()
new.home()