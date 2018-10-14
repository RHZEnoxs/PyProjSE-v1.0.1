# task2 -  Decision Making

# === === ===== Decision Making ===== === ===
# --- Single Statement Suites ---
def task2v1():
    var = 100
    if (var == 100): print ("Value of expression is 100")
    print ("Good bye!")
# --- Python IF Statement ---
def task2v2():
    var1 = 100
    if var1:
        print("1 - Got a true expression value")
        print(var1)
    var2 = 0
    if var2:
        print("2 - Got a true expression value")
        print(var2)
    print("Good bye!")
# --- Python IF...ELIF...ELSE Statements ---
def task2v3():
    var1 = 100
    if var1:
        print("1 - Got a true expression value")
        print(var1)
    else:
        print("1 - Got a false expression value")
        print(var1)
    var2 = 0
    if var2:
        print("2 - Got a true expression value")
        print(var2)
    else:
        print("2 - Got a false expression value")
        print(var2)
    print("Good bye!")
# --- Python nested IF statements ---
def task2v4():
    var = 100
    if var < 200:
        print("Expression value is less than 200")
        if var == 150:
            print("Which is 150")
        elif var == 100:
            print("Which is 100")
        elif var == 50:
            print("Which is 50")
        elif var < 50:
            print("Expression value is less than 50")
    else:
        print("Could not find true expression")
    print("Good bye!")
# ---  Loops ---
# ---  while Loop Statements ---
def task2v5():
    count = 0
    while (count < 9):
        print('The count is:', count)
        count = count + 1
    print("Good bye!")
# ---  The Infinite Loop ---
def task2v6():
    var = 1
    while var == 1:  # This constructs an infinite loop
        num = input("Enter a number  :")
        print("You entered: ", num)
    print( "Good bye!")
# --- Using else Statement with Loops ---
def task2v7():
    count = 0
    while count < 5:
        print(count, " is  less than 5")
        count = count + 1
    else:
        print(count, " is not less than 5")
# --- Single Statement Suites ---
def task2v8():
    flag = 1
    while (flag): print('Given flag is really true!')
    print("Good bye!")
# ---  for Loop Statements ---
def task2v9():
    for letter in 'Python':  # First Example
        print('Current Letter :', letter)
    fruits = ['banana', 'apple', 'mango']
    for fruit in fruits:  # Second Example
        print('Current fruit :', fruit)
    print("Good bye!")
# --- Iterating by Sequence Index ---
def task2v10():
    fruits = ['banana', 'apple', 'mango']
    for index in range(len(fruits)):
        print('Current fruit :', fruits[index])
    print("Good bye!")
# --- Using else Statement with Loops ---
def task2v11():
    for num in range(10, 20):  # to iterate between 10 to 20
        for i in range(2, num):  # to iterate on the factors of the number
            if num % i == 0:  # to determine the first factor
                j = num / i  # to calculate the second factor
                print('%d equals %d * %d' % (num, i, j))
                break  # to move to the next number, the #first FOR
        else:  # else part of the loop
            print(num, 'is a prime number')
    print("task2v11 - II")
    ctrl = 1
    while ctrl:
        num = int(input("Enter a number  :"))
        if num == 0 :
            ctrl = 0
        for i in range(2, num):  # to iterate on the factors of the number
            print("flag#1",i)
            if num % i == 0:  # to determine the first factor
                j = num / i  # to calculate the second factor
                print('flag#2 %d equals %d * %d' % (num, i, j))
                break  # to move to the next number, the #first FOR
        else:  # else part of the loop
            print("flag#3 ", num, 'is a prime number')

# ---  nested loops ---

# ---  ---
# ---  ---
# ---  ---
# ---  ---
# ---  ---
# ---  ---
# ---  ---
# ---  ---
# ---  ---
# ---  ---

if __name__ == '__main__':
    # task2v1()
    # task2v2()
    # task2v3()
    # task2v4()
    # task2v5()
    # task2v6()
    # task2v7()
    # task2v8()
    # task2v9()
    # task2v10()
    task2v11()
