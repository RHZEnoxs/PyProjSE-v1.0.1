#!/usr/bin/python
# task3 -  Python - Numbers
# === === ===== Python - Numbers ===== === ===
# --- Mathematical Functions ---
# --- Python Number abs() Method ---
def task3v1(): #絕對值 x 和 0 之間的距離
    print("abs(-45) : ", abs(-45))
    print("abs(100.12) : ", abs(100.12))
    print("abs(119L) : ", abs(119))#L

# --- Python Number ceil() Method ---
def task3v2(): #無條件進位
    import math  # This will import math module
    print("math.ceil(-45.17) : ", math.ceil(-45.17))
    print("math.ceil(100.12) : ", math.ceil(100.12))
    print("math.ceil(100.72) : ", math.ceil(100.72))
    print("math.ceil(119L) : ", math.ceil(119))
    print("math.ceil(math.pi) : ", math.ceil(math.pi))
# --- Python Number cmp() Method ---
# def task3v3(): #???
    # print("cmp(80, 100) : ", cmp(80, 100))
    # print("cmp(180, 100) : ", cmp(180, 100))
    # print("cmp(-80, 100) : ", cmp(-80, 100))
    # print("cmp(80, -100) : ", cmp(80, -100))
# --- Python Number exp() Method ---
def task3v4(): # e x 次方 ???
    import math  # This will import math module
    print("math.exp(1) : ", math.exp(1))
    print("math.exp(-45.17) : ", math.exp(-45.17))
    print("math.exp(100.12) : ", math.exp(100.12))
    print("math.exp(100.72) : ", math.exp(100.72))
    print("math.exp(119L) : ", math.exp(119))
    print("math.exp(math.pi) : ", math.exp(math.pi))
# --- Python Number fabs() Method ---
def task3v5(): #絕對值
    import math  # This will import math module
    print("math.fabs(-45.17) : ", math.fabs(-45.17))
    print("math.fabs(100.12) : ", math.fabs(100.12))
    print("math.fabs(100.72) : ", math.fabs(100.72))
    print("math.fabs(119L) : ", math.fabs(119))
    print("math.fabs(math.pi) : ", math.fabs(math.pi))
# --- Python Number floor() Method ---
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
    # task3v1()
    # task3v2()
    # task3v3()
    # task3v4()
    task3v5()