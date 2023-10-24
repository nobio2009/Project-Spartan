import time
def save(username, user_id, ai_name, ai_id):
        f = open("save.py", "w")
        f.write(f"username = {username}" + "\n")
        f.write(f"userid = {user_id}" + "\n")
        f.write(f"AIname = {ai_name}" + "\n")
        f.write(f"AIid = {ai_id}" + "\n")
        f.close()


print('Setting up your ai\n')

username = input('\nPlease input your name: ')
time.sleep(1)
user_id = input('\nPlease input your desired id: ')
time.sleep(1)
ai_name = input('\nPlease input your desired name for the ai: ')
time.sleep(1)
ai_id = input('\nPlease input desired id for ai')
time.sleep(1)
save(username, user_id, ai_name, ai_id)
