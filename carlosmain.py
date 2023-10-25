
def menu():
    game = True

    num_diction = {
        "0":"3",
        "1":"4",
        "2":"5",
        "3":"6",
        "4":"7",
        "5":"8",
        "6":"9",
        "7":"0",
        "8":"1",
        "9":"2"

    }
    encoded_string =""

    while game:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        print("Please enter an option: ", end="")
        num_input = int(input())


        if num_input == 1:
            num_num = input("Please enter your password to encode:")
            for char in num_num:
                char = num_diction[char]
                encoded_string += char
            print("Your password has been encoded and stored!")


        elif num_input == 2:
            print(f'The encoded password is {encoded_string}, and the original password is {num_num}.')


        elif num_input == 3:
            game = False







menu()