#  Python 3 - Functions

#Calling a Function
def callFunc():
    # Function definition is here
    def printme(str):
        "This prints a passed string into this function"
        print(str)
        return

    # Now you can call printme function
    printme("This is first call to the user defined function!")
    printme("Again second call to the same function")
#Pass by Reference vs Value
def passByReference():
    # Function definition is here
    def changeme(mylist):
        "This changes a passed list into this function"
        print("Values inside the function before change: ", mylist)

        mylist[2] = 50
        print("Values inside the function after change: ", mylist)
        return

    # Now you can call changeme function
    mylist = [10, 20, 30]
    changeme(mylist)
    print("Values outside the function: ", mylist)
def passByValue():
    # Function definition is here
    def changeme(mylist):
        "This changes a passed list into this function"
        mylist = [1, 2, 3, 4]  # This would assi new reference in mylist
        print("Values inside the function: ", mylist)
        return

    # Now you can call changeme function
    mylist = [10, 20, 30]
    changeme(mylist)
    print("Values outside the function: ", mylist)
# Function Arguments
#Required Arguments
def reqArgument():
    # Function definition is here
    def printme(str):
        "This prints a passed string into this function"
        print(str)
        return

    # Now you can call printme function
    printme()
    #Traceback (most recent call last):
    #File "test.py", line 11, in <module>
    #printme();
    #TypeError: printme() takes exactly 1 argument (0 given)
#Keyword Arguments
def keywordArgument():
    # Function definition is here
    def printme(str):
        "This prints a passed string into this function"
        print(str)
        return

    # Now you can call printme function
    printme(str="My string")

    # Function definition is here
    def printinfo(name, age):
        "This prints a passed info into this function"
        print("Name: ", name)
        print("Age ", age)
        return

    # Now you can call printinfo function
    printinfo(age=50, name="miki")
#Default Arguments
def defaultArgument():
    # Function definition is here
    def printinfo(name, age=35):
        "This prints a passed info into this function"
        print("Name: ", name)
        print("Age ", age)
        return

    # Now you can call printinfo function
    printinfo(age=50, name="miki")
    printinfo(name="miki")
#Variable-length Arguments
def varLenArgument():
    # Function definition is here
    def printinfo(arg1, *vartuple):
        "This prints a variable passed arguments"
        print("Output is: ")
        print(arg1)

        for var in vartuple:
            print(var)
        return

    # Now you can call printinfo function
    printinfo(10)
    printinfo(70, 60, 50)
#The Anonymous Functions
def anonymousFunc():
    # Function definition is here
    sum = lambda arg1, arg2: arg1 + arg2

    # Now you can call sum as a function
    print("Value of total : ", sum(10, 20))
    print("Value of total : ", sum(20, 20))
#The return Statement
def returnStatement():
    # Function definition is here
    def sum(arg1, arg2):
        # Add both the parameters and return them."
        total = arg1 + arg2
        print("Inside the function : ", total)
        return total

    # Now you can call sum function
    total = sum(10, 20)
    print("Outside the function : ", total)
# Scope of Variables
#Global vs. Local variables
def globalAndLocalVariableTask():
    total = 0  # This is global variable.

    # Function definition is here
    def sum(arg1, arg2):
        # Add both the parameters and return them."
        total = arg1 + arg2;  # Here total is local variable.
        print("Inside the function local total : ", total)
        return total

    # Now you can call sum function
    sum(10, 20)
    print("Outside the function global total : ", total)
if __name__ == '__main__':
    # callFunc()
    # passByReference()
    # passByValue()
    # reqArgument()
    # keywordArgument()
    # defaultArgument()
    # varLenArgument()
    # anonymousFunc()
    # returnStatement()
    globalAndLocalVariableTask()