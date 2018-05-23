

while True:
    print('Select the new password(letters and numbers only)')
    password = input()
    if password.isalnum():
        break
    print('Password can have only num and char')
