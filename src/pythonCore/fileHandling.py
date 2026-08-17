#Note: To open the file, use the built-in open() function.The open() function returns a file object,
# which has a read() method for reading the content of the file:
print('============Read File============')
f = open("/Users/samirb/Documents/WorkSpace/PySpark/resource/text.txt")
print(f.read())
f.close()
print('============Read using With Statement============')
#Note: You can also use the with statement when opening a file:Then you do not have to worry about closing
# your files,the with statement takes care of that.

with open("/Users/samirb/Documents/WorkSpace/PySpark/resource/text.txt") as f:
    print(f.read(10),'Rohit')

'''Q3) Python
open the input.txt
go to the 5th line in the file
then go to the 5th word in that 5th line
print the "5th word and length of the word"
'''
print('============read 5 line from File============')
with open("/Users/samirb/Documents/GitHub/PythonRepo/src/resource/text3.txt") as f:
        for line_no, line in enumerate(f, start=1):
            print(line_no, line)
            if(line_no == 5):
                print('============read 5th word from File============')
                words=line.split()
                word = words[4]
                print('word:',word+', length of word:',len(word))


print('============Write File============')
# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exists
# "a" - Append - will create a file if the specified file does not exists
# "w" - Write - will create a file if the specified file does not exists

#Append file
with open("/Users/samirb/Documents/WorkSpace/PySpark/resource/text2.txt", "a") as f:
    f.write("Now the file has more content 1!")

#open and read the file after the appending:
with open("/Users/samirb/Documents/WorkSpace/PySpark/resource/text2.txt") as f:
    print(f.read())

#Override file
with open("/Users/samirb/Documents/WorkSpace/PySpark/resource/text2.txt", "w") as f:
    f.write("Now the file has more content 2!")
#open and read the file after the appending:
with open("/Users/samirb/Documents/WorkSpace/PySpark/resource/text2.txt") as f:
    print(f.read())

print('============Delete File============')
# Note: To delete a file, you must import the OS module, and run its os.remove() function:

f = open("/Users/samirb/Documents/WorkSpace/PySpark/resource/text3.txt", "x")
f.close()
import os
if os.path.exists("/Users/samirb/Documents/WorkSpace/PySpark/resource/text5.txt"):
    os.remove("/Users/samirb/Documents/WorkSpace/PySpark/resource/text5.txt")
    print("Delete successfully")
else:
    print("The file does not exist")

#Delete folder
import os
try:
    os.rmdir("myfolder")
except:
    print("THE folder does not exist")