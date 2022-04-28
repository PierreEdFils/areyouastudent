students = ["John","Peter","George"]
welcome = input( " Are you a student? Lets find out…")
answer = None
while answer not in ("Are you a student?(yes/no)","yes", "no"):
    answer = input("Enter yes or no: ")
    if answer == "yes":
        name = input("What is your name ? ")

        if name == students :
            print("Welcome to class" + name)
        else:
            print("You’re not supposed to be here")

    elif answer == "no":
        print("Break")
    break
