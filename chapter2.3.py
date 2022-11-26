computer_value=23
user=int(input("Enter a value b/w 1-56="))
if user==computer_value:
    print("YOU WON")
else:
    if computer_value>user:
        print("TOO LOW")
    elif computer_value<user:
        print("TOO HIGH")