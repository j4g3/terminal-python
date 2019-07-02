
#Username
usuario = input('Username UNIX: ')
#Passing the user name to a file
files = open('dados.dll', 'w')
data = []
data.append(f'{usuario}@{usuario}')
files.writelines(dados)
files.close

print('New User created')