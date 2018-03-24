#!/usr/bin/python3

testFile = open("test.txt", "a+")
print("File in use: ", testFile.name)
if(testFile.closed is True):
    print("closed")
else:
    print("open")    
#print("Open or closed?? ", testFile.closed)
print("current mode ", testFile.mode)
testFile.write("name :")
testFile.close()
if(testFile.closed is True):
    print("closed")
else:
    print("open")   