'''
Cracking Zip File password with python
'''

import zipfile

def crack_password(password_list, obj):
    test = 0
    with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    test += 1
                    obj.extractall(pwd=word)
                    print("password found in line", test)
                    print("passwords found and password is ", word.decode())
                    return True
                except:
                    continue

password_list = input("Enter the location of password list: ")
zip_file = input("Enter the location of zip file: ")
obj = zipfile.ZipFile(zip_file)
count = len(list(open(password_list)))
print("There are total ", count, "number of password to test.")
if crack_password(password_list, obj) == False:
    print("password not found in the list!")