import getpass

data = {'chocho':'1234','mama':'0912'}
username = input('Enter Your Username : ')
password = getpass.getpass('Enter Your Password : ')

for i in data.keys():
    if username == i:
        while password != data.get(i):
            password = getpass.getpass('Enter Your Password again : ')
        break
print('Verified')