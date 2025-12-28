myFile = open('myFile.txt', 'w')

print("Name: ", myFile.name)
print("Is closed: ", myFile.closed)
print("Mode: ", myFile.mode)

# write to file
myFile.write('I love python ')
myFile.write("And JavaScript")
myFile.close()


myFile = open('myFile.txt', 'a')
myFile.write("I also like php")
myFile.close()

myFile = open('myFile.txt', 'r+')
text = myFile.read(100) # 100 character
print(text)


