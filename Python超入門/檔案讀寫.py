#file_object = open('D:\MyProject\python.txt', 'w')
#file_object.write('this is sample of python.')
#file_object.close()

#file_object = open('D:\MyProject\python.txt', 'r')
#content = file_object.read()

#print(content)
#file_object.close()

#file_object = open('D:\MyProject\python.txt', 'a')
#file_object.write('\nAdd data from program.')
#file_object.close()

with open('D:\MyProject\python.txt', 'r+') as file_object:
    content = file_object.write('using with!')
    print(content)