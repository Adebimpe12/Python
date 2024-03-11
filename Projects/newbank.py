import bank1
from bank1 import Bank
# import time
from time import sleep
import datetime as dt
import random
import pandas as pd
import numpy as np
import pwinput
from colorama import init, Fore, Back, Style

init()
from prettytable import PrettyTable
table = PrettyTable()


different types of sql database
sqllite
mysql


init()
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

tim = dt.datetime.now()
print(tim.time())

account_no = random.randint(8100000000, 8190000000)
print('+234' + str(account_no))
print(random.choice(['Maimunah', 'Richard', 'Mary']))

password = pwinput.pwinput()
print(password)


# itedtuyukyjh
# itedtuyukyjh
# itedtuyukyjh
# itedtuyukyjh
# itedtuyukyjh
# itedtuyukyjh
# itedtuyukyjh






from time import sleep

class newBranch(Bank):
    def __init__(self):
        super().__init__()
        self.branch = 'Ogbomoso'

        print('Loading...')
        # time.sleep(3)
        sleep(3)


new = newBranch()
new.home()