import os

command = 'hey whiskey load test'

string = command 
split_string = string.split(' ')  
new_string_list = split_string[3:]
file = ' '.join(new_string_list).lower()

print(file)
#os.system(f'python scripts\{file}.py')