# task1 -  Basic Syntax
# task1 -  Variable Types
# task1 -  Basic Operators
def task1v1():
    print("Hello World.");
# === === ===== Basic Syntax ===== === ===
# --- Lines and Indentation ---
def task1v2():
    if True:
        print (" is True")
    else :
        print (" is False")
# --- Multi - Line Statement ---
def task1v3():
    a = "Hello"
    b = " World"
    total = a + \
            b
    print(total)
    days = ['one', 'two',
            'three']
    print(days)
# --- Quotation in Python ---
def task1v4():
    word = 'word'
    sentence = "This is a sentence."
    paragraph = """This is a paragraph. It is
    made up of multiple lines and sentences."""
    print(paragraph)
# --- Comments in Python ---
def task1v5():

    print("word")  # print(sentence)
# --- Using Blank Lines ---
# --- Waiting for the User ---
def task1v6():
    # raw_input("\n\nPress the enter key to exit.") - Python 2
    input("\n\nPress the enter key to exit.")
# --- Multiple Statements on a Single Line ---
def task1v7():
    import sys;x = 'foo';sys.stdout.write(x + '\n')
# --- Multiple Statement Groups as Suites ---
def task1v8():
    a = 3
    b = 3
    if a > b:
        print("#flag1")
    elif a < b:
        print("#flag2")
    else:
        print("#flag3")
# === === ===== Variable Types ===== === ===
# --- Assigning Values to Variables ---
def task1v9():
    counter = 100  # An integer assignment
    miles = 1000.0  # A floating point
    name = "John"  # A string
    print (counter)
    print (miles)
    print (name)
# --- Multiple Assignment ---
def task1v10():
    a = b = c = 1
    msg = str(a) + " -> " + str(b) + " -> " + str(c)
    print(msg)
    a, b, c = 1, 2, "john"
    msg = str(a) + " -> " + str(b) + " -> " + str(c)
    print (msg)
# --- Standard Data Types ---
    # 1. Numbers
    # 2. String
    # 3. List
    # 4. Tuple - 元組
    # 5. Dictionary - 字典
# --- Python Numbers ---
    # int (signed integers)
    # long (long integers, they can also be represented in octal and hexadecimal)
    # float (floating point real values)
    # complex (complex numbers)
def task1v11():
    var1 = 1
    var2 = 12
    # del var2
    print(var1)
    print(var2)
# --- Python Strings ---
def task1v12():
    str = 'Hello World!'
    print (str)  # Prints complete string
    print (str[0])  # Prints first character of the string
    print (str[2:5])  # Prints characters starting from 3rd to 5th
    print (str[2:])  # Prints string starting from 3rd character
    print (str * 2)  # Prints string two times
    print (str + "TEST")  # Prints concatenated string
# --- Python Lists ---
def task1v13():
    list = ['abcd', 786, 2.23, 'john', 70.2]
    tinylist = [123, 'john']
    print (list)  # Prints complete list
    print (list[0])  # Prints first element of the list
    print (list[1:3])  # Prints elements starting from 2nd till 3rd
    print (list[2:])  # Prints elements starting from 3rd element
    print (tinylist * 2)  # Prints list two times
    print (list + tinylist)  # Prints concatenated lists
# --- Python Tuples ---
def task1v14(): # Read-only
    tuple = ('abcd', 786, 2.23, 'john', 70.2)
    tinytuple = (123, 'john')
    print(tuple)  # Prints complete list
    print(tuple[0]) # Prints first element of the list
    print(tuple[1:3])  # Prints elements starting from 2nd till 3rd
    print(tuple[2:])  # Prints elements starting from 3rd element
    print(tinytuple * 2)  # Prints list two times
    print(tuple + tinytuple)  # Prints concatenated lists
# --- Python Dictionary ---
def task1v15(): # hash table
    dict = {}
    dict['one'] = "This is one"
    dict[2] = "This is two"
    tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
    print(dict['one'])  # Prints value for 'one' key
    print(dict[2])  # Prints value for 2 key
    print(tinydict) # Prints complete dictionary
    print(tinydict.keys())  # Prints all the keys
    print(tinydict.values())    # Prints all the values
# --- Data Type Conversion ---
def task1v16():
    x = "15"
    y = int(x)
    print(y)
    msg = str(y)
    print(msg)
# === === ===== Basic Operators ===== === ===
# --- Python Arithmetic Operators ---
def task1v17():
    a = 10
    b = 5
    c = 0
    c = a + b
    print("Line 1 - Value of c is ", c)
    c = a - b
    print("Line 2 - Value of c is ", c)
    c = a * b
    print("Line 3 - Value of c is ", c)
    c = a / b
    print("Line 4 - Value of c is ", c)
    c = a % b
    print("Line 5 - Value of c is ", c)
    b = 3
    c = a ** b # 指數
    print("Line 6 - Value of c is ", c)
    a = 10
    b = 5
    c = a // b # 9 // 2 = 4 ， 9.0 // 2.0 = 4.0 ， -11 // 3 = -4 ， -11.0 // 3 = -4.0
    print("Line 7 - Value of c is ", c)
# --- Comparison Operators ---
def task1v18():
    a = 21
    b = 10
    c = 0
    if (a == b):
        print("Line 1.1 - a is equal to b")
    else:
        print("Line 1.2 - a is not equal to b")
    if (a != b):
        print("Line 2.1 - a is not equal to b")
    else:
        print("Line 2.2 - a is equal to b")
    # if (a <> b): # Python no support
    #     print("Line 3 - a is not equal to b")
    # else:
    #     print("Line 3 - a is equal to b")
    if (a < b):
        print("Line 4.1 - a is less than b")
    else:
        print("Line 4.2 - a is not less than b")
    if (a > b):
        print("Line 5.1 - a is greater than b")
    else:
        print("Line 5.2 - a is not greater than b")
    a = 5;
    b = 20;
    if (a <= b):
        print("Line 6.1 - a is either less than or equal to  b")
    else:
        print("Line 6.2 - a is neither less than nor equal to  b")
    if (b >= a):
        print("Line 7.1 - b is either greater than  or equal to b")
    else:
        print("Line 7.2 - b is neither greater than  nor equal to b")
# --- Bitwise Operators ---
def task1v19():
    a = 60  # 60 = 0011 1100
    b = 13  # 13 = 0000 1101
    c = 0
    c = a & b;  # 12 = 0000 1100 - AND
    print("Line 1 - Value of c is ", c)
    c = a | b;  # 61 = 0011 1101 - OR
    print("Line 2 - Value of c is ", c)
    c = a ^ b;  # 49 = 0011 0001 - XOR
    print("Line 3 - Value of c is ", c)
    c = ~a;  # -61 = 1100 0011  - 'flipping' bits.
    print("Line 4 - Value of c is ", c)
    c = a << 2;  # 240 = 1111 0000
    print("Line 5 - Value of c is ", c)
    c = a >> 2;  # 15 = 0000 1111
    print("Line 6 - Value of c is ", c)
# --- Logical Operators ---
def task1v20():
    a = True # False
    b = True # False
    if(a and b):
        print("flag#1")
    elif(a or b):
        print("flag#2")
    elif(not (a and b)):
        print("flag#3")
    else:
        print("none")
# --- Membership Operators ---
def task1v21():
    a = 10
    b = 20
    list = [1, 2, 3, 4, 5];
    if (a in list):
        print("Line 1.1 - a is available in the given list")
    else:
        print("Line 1.2 - a is not available in the given list")
    if (b not in list):
        print("Line 2.1 - b is not available in the given list")
    else:
        print("Line 2.2 - b is available in the given list")
    a = 2
    if (a in list):
        print("Line 3.1 - a is available in the given list")
    else:
        print("Line 3.2 - a is not available in the given list")
# --- Identity Operators ---
def task1v22():
    a = 20
    b = 20
    if (a is b):
        print("Line 1.1 - a and b have same identity")
    else:
        print("Line 1.2 - a and b do not have same identity")
    if (id(a) == id(b)):
        print("Line 2.1 - a and b have same identity")
    else:
        print("Line 2.2 - a and b do not have same identity")
    b = 30
    if (a is b):
        print("Line 3.1 - a and b have same identity")
    else:
        print("Line 3.2 - a and b do not have same identity")
    if (a is not b):
        print("Line 4.1 - a and b do not have same identity")
    else:
        print("Line 4.2 - a and b have same identity")
# --- Operators Precedence ---
def task1v23():
    a = 20
    b = 10
    c = 15
    d = 5
    e = 0
    e = (a + b) * c / d  # ( 30 * 15 ) / 5
    print("Value of (a + b) * c / d is ", e)
    e = ((a + b) * c) / d  # (30 * 15 ) / 5
    print("Value of ((a + b) * c) / d is ", e)
    e = (a + b) * (c / d);  # (30) * (15/5)
    print("Value of (a + b) * (c / d) is ", e)
    e = a + (b * c) / d;  # 20 + (150/5)
    print("Value of a + (b * c) / d is ", e)
# --- ---
# --- ---
# --- ---
if __name__ == '__main__':
    task1v1()
    # task1v2()
    # task1v3()
    # task1v4()
    # task1v5()
    # task1v6()
    # task1v7()
    # task1v8()
    # task1v9()
    # task1v10()
    # task1v11()
    # task1v12()
    # task1v13()
    # task1v14()
    # task1v15()
    # task1v16()
    # task1v17()
    # task1v18()
    # task1v19()
    # task1v20()
    # task1v21()
    # task1v22()
    # task1v23()