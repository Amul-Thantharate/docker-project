user_name = input("Enter your name to store in the file: ")
if user_name: 
    with open("user_info.txt", "a") as file:
        file.write(user_name + "\n")
show_info = input("Do you want to see the list of users? (y/n): ")
if show_info == "y":
    try:
        with open("user_info.txt", "r") as file:
            content = file.readlines()
    except Exception as e:
        print("Error: ", e)
    else:
        for line in content: 
            print(f"{line.strip()}")


