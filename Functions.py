# block of code that does a specific task

# def- decorator def to start function, initialize function (def addition(): )

# parametized functions v non-parametized function
# declare, initialize/defination and invoke functions  
# when calling ypur function if parametized it includes argument, (addition(value1 = int(input('enter the first value: '), value2 = int(input('enter the second value: ')))
# )

def addition():
    value1 = int(input('enter first value: '))
    value2 = int(input('enter second value: '))
    result = value1 + value2
    print(f"ans: {result}")
addition()

# parametized function
def addition(value1, value2):
    result = value1 + value2
    print(f' ans: {result}')

addition(value1 = int(input('enter the first value: '), value2 = int(input('enter the second value: ')))

def addition(value1, value2=10):
    result = value1 + value2
    print(f' ans: {result}')

addition(value1 = int(input('enter the first value: '), value2=10))

# global and local variables
# global variable eg global val1 is accessible by the whole document, not just functions beneath it.
val1 = 12
def addition (val3):
    global val2 = 10+
    result = val1 + val2 + val3
    print(f'ans: {result} nice')
    subtraction()

def subtraction():
    results = val1 - val2
    print(f'ans: {results} amazing')
addition(int(input(f'enter value 3: ')))