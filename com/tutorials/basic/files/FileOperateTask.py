#  Python 3 - Files I/O

# Sample Example
#Printing to the Screen
def printToScreen():
    # !/usr/bin/python3
    print("Python is really a great language,", "isn't it?")

#The input Function
def inputFunc():
    x = input("input something:")
    print('x : ',x)

#The open Function
def openFunc():
    # Open a file
    fo = open("text#1.txt", "wb")
    print("Name of the file: ", fo.name)
    print("Closed or not : ", fo.closed)
    print("Opening mode : ", fo.mode)
    fo.close()

#The close() Method
def closeFunc():
    # Open a file
    fo = open("text#1.txt", "wb")
    print("Name of the file: ", fo.name)

    # Close opened file
    fo.close()

#The write() Method
def writeFunc():
    # Open a file
    fo = open("text#1.txt", "w")
    fo.write("Python is a great language.\nYeah its great!!\n")
    # Close opend file
    fo.close()

#The read() Method
def readFunc():
    # Open a file
    fo = open("text#1.txt", "r+")
    str = fo.read(10)
    print("Read String is : ", str)

    # Close opened file
    fo.close()

#File Positions
def filePositions():
    # Open a file
    fo = open("text#1.txt", "r+")
    str = fo.read(10)
    print("Read String is : ", str)

    # Check current position
    position = fo.tell()
    print("Current file position : ", position)

    # Reposition pointer at the beginning once again
    position = fo.seek(0, 0)
    str = fo.read(10)
    print("Again read String is : ", str)

    # Close opened file
    fo.close()

#The rename() Method
def renameFunc():
    import os

    # Rename a file from test1.txt to test2.txt
    os.rename("text#1.txt", "text#2.txt")

#The remove() Method
def removeFunc():
    import os

    # Delete file test2.txt
    os.remove("text.txt")
#The mkdir() Method
def mkdirFunc():
    import os

    # Create a directory "test"
    os.mkdir("txtFold/txt")
#The chdir() Method
def chdirFunc():
    # !/usr/bin/python3
    import os
    # Changing a directory to "/home/newdir"
    os.chdir("/Users/Enoxs/Mac_Document/MacWorkSpace/8.PycharmProject/")
    os.mkdir("txtFold")
#The getcwd() Method
def getcwdFunc():
    import os
    # This would give location of the current directory
    os.chdir("/Users/Enoxs/Mac_Document/MacWorkSpace/8.PycharmProject/")
    str = os.getcwd()
    print(str)
#The rmdir() Method
def rmdirFunc():
    # !/usr/bin/python3
    import os
    # This would  remove "/tmp/test"  directory.
    # os.rmdir("txtFold/txt")
    os.rmdir("txtFold")


# Python 3 - File Methods

#Python 3 -File close() Method
def fileClose():
    # Open a file
    fo = open("text#1.txt", "wb")
    print("Name of the file: ", fo.name)
    # Close opened file
    fo.close()
#Python 3 - File flush() Method
def fileFlush():
    # Open a file
    fo = open("text#2.txt", "wb")
    print("Name of the file: ", fo.name)
    # Here it does nothing, but you can call it with read operation.
    fo.flush()
    # Close opend file
    fo.close()
#Python 3 - File isatty() Method
def fileIsAtty():
    # Open a file
    fo = open("text#2.txt", "wb")
    print("Name of the file: ", fo.name)
    ret = fo.isatty()
    print("Return value : ", ret)
    # Close opend file
    fo.close()
#Python 3 - File fileno() Method
def fileNo():
    # Open a file
    fo = open("text#3.txt", "wb")
    print("Name of the file: ", fo.name)

    fid = fo.fileno()
    print("File Descriptor: ", fid)

    # Close opend file
    fo.close()
#Python 3 - File next() Method
def fileNext():
    # Open a file
    #text#1.txt:
        #Assuming that 'foo.txt' contains following lines
        #C++
        #Java
        #Python
        #Perl
        #PHP
    fo = open("text#1.txt", "r")
    print("Name of the file: ", fo.name)
    for index in range(5):
        line = next(fo)
        print("Line No %d - %s" % (index, line))
    # Close opened file
    fo.close()
#Python 3 - File read() Method
def fileRead():
    # Open a file
    fo = open("text#2.txt", "r+")
    print("Name of the file: ", fo.name)

    line = fo.read(10)
    print("Read Line: %s" % (line))

    # Close opened file
    fo.close()
#Python 3 - File readline() Method
def fileReadline():
    # Open a file
    fo = open("text#2.txt", "r+")
    print("Name of the file: ", fo.name)

    line = fo.readline()
    print("Read Line: %s" % (line))

    line = fo.readline(5)
    print("Read Line: %s" % (line))

    # Close opened file
    fo.close()
#Python 3 - File readlines() Method
def fileReadlines():
    # Open a file
    fo = open("text#2.txt", "r+")
    print("Name of the file: ", fo.name)

    line = fo.readlines()
    print("Read Line: %s" % (line))

    line = fo.readlines(2)
    print("Read Line: %s" % (line))

    # Close opened file
    fo.close()
#Python 3 - File seek() Method
def fileSeek():
    # Open a file
    fo = open("text#2.txt", "r+")
    print("Name of the file: ", fo.name)

    line = fo.readlines()
    print("Read Line: %s" % (line))

    # Again set the pointer to the beginning
    fo.seek(0, 0)
    line = fo.readline()
    print("Read Line: %s" % (line))

    # Close opened file
    fo.close()
#Python 3 - File tell() Method
def fileTell():
    fo = open("text#2.txt", "r+")
    print("Name of the file: ", fo.name)

    line = fo.readline()
    print("Read Line: %s" % (line))

    pos = fo.tell()
    print("current position : ", pos)

    # Close opened file
    fo.close()
#Python 3 - File truncate() Method
def fileTruncate():
    fo = open("text#2.txt", "r+")
    print("Name of the file: ", fo.name)

    line = fo.readline()
    print("Read Line: %s" % (line))

    fo.truncate(1)
    line = fo.readlines()
    print("Read Line: %s" % (line))

    # Close opened file
    fo.close()
#Python 3 - File write() Method
def fileWrite():
    # Open a file in read/write mode
    fo = open("text#3.txt", "r+")
    print("Name of the file: ", fo.name)

    str = "This is 6th line"
    # Write a line at the end of the file.
    fo.seek(0, 2)
    line = fo.write(str)

    # Now read complete file from beginning.
    fo.seek(0, 0)
    for index in range(6):
        line = next(fo)
        print("Line No %d - %s" % (index, line))

    # Close opened file
    fo.close()
#Python 3 - File writelines() Method
def fileWritelines():
    # Open a file in read/write mode
    fo = open("text#3.txt", "r+")
    print("Name of the file: ", fo.name)

    seq = ["This is 6th line\n", "This is 7th line"]
    # Write sequence of lines at the end of the file.
    fo.seek(0, 2)
    line = fo.writelines(seq)

    # Now read complete file from beginning.
    fo.seek(0, 0)
    for index in range(7):
        line = next(fo)
        print("Line No %d - %s" % (index, line))

    # Close opened file
    fo.close()

# Python 3 - OS File/Directory Methods


if __name__ == '__main__':
#Sample Example
    # printToScreen()
    # inputFunc()
    # openFunc()
    # closeFunc()
    # writeFunc()
    # readFunc()
    # filePositions()
    # renameFunc()
    # removeFunc()
    # mkdirFunc()
    # chdirFunc()
    # getCwdFunc()
    # rmdirFunc()
#Python 3 -File close() Method
    # fileClose()
    # fileFlush()
    # fileIsAtty()
    # fileNext()
    # fileNo()
    # fileRead()
    # fileReadline()
    # fileReadlines()
    # fileSeek()
    # fileTell()
    # fileTruncate()
    # fileWrite()
    fileWritelines()