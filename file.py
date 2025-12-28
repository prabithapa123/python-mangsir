import os
# f = open("file.txt")
# print(f.read(2))
# print(f.readline())
# print(f.readline())
# print(f.readline())
# for i in f:
#     print(i)
    
# f.close()

# file = 'file.txt'
# with open(file, 'r') as a:
#     r = a.read()
#     print(r)


# try:
#     f = open('exist.txt')
#     print(f.read())
# except FileNotFoundError:
#     print("File doesnot exist")
# finally:
#     f.close()

# f = open("file.txt", 'a')
# f.write("This is append")
# f.close()

# f = open("file.txt")
# print(f.read())
# f.close()


# f = open('context.txt', 'w')
# f.write('Hello world')

# f.close()


# f = open('context.txt')
# print(f.read())
# f.close()

# f = open("name_list.txt", 'w')
# f.write('Hello guys')
# f.close()


# if not os.path.exists("prabee.txt"):
#     f = open('prabee.txt', 'x')
#     f.close()
    
# if os.path.exists('prabee.txt'):
#     os.remove('prabee.txt')
# else:
#     print("File doesnot exists")


with open('more_names.txt') as f:
    content = f.read()
    
with open('names.txt', 'a') as f:
    f.write(content)