import os

# print(os.path.join('user', 'bin', 'spam')) #it will print out the file location with the separators according to the system os

myFiles = ['account.txt', 'details.txt', 'invite.docx']
for filename in myFiles:
    print(os.path.join("C:\\Users\\Kushagra_Dubey", filename))

#getting the current working directory
print(os.getcwd()) # it provides the current working directory
# print(os.chdir("path")) #it changes the directory

# print(os.makedirs('D:\\Automate_Boring_Stuff_Python\\hello')) # this will create a folder or file according to the instructions and filepath

#handling absolute and relative paths
print(os.path.abspath('slash.py'))
print(os.path.isabs('slash.py')) #checks whether the path is absolute or not
print(os.path.isabs(os.path.abspath('slash.py')))

print(os.path.relpath('slash.py'))
print(os.path.relpath('D:\\spam\\eggs'))

print(os.path.dirname('\\hello'))
print(os.path.basename('\\slash.py'))

calcFilePath = 'D:\\Automate_Boring_Stuff_Python\\slash.py'
print(os.path.split(calcFilePath)) #returns a tuple with the dirname and basename

print(calcFilePath.split(os.path.sep))
print('/usr/bin/path'.split(os.path.sep))

print('The size of this file is ' + str(os.path.getsize('.\\slash.py')) + ' bytes.')


os.listdir('D:\\Automate_Boring_Stuff_Python')
totalSize = 0
for filename in os.listdir('D:\\Automate_Boring_Stuff_Python'):
    totalSize += os.path.getsize(os.path.join("D:\\Automate_Boring_Stuff_Python", filename))

print("The total size of the D drive Automate Boring Stuff Folder is " + str((totalSize)/1024) + " MB.")


#checking path validity
print(os.path.exists('slash.py')) #ckeck if path exists
print(os.path.isfile('slash.py')) #check if file exists
print(os.path.isdir('hello')) #ckecks if given argument is folder or not
print(os.path.exists('D:\\'))