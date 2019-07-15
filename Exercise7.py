from random import randint

while True:
    the_guess_number = randint(0, 26)
    number_tries = 0

    while number_tries <= 4:
        # incrementing number of tries here for DRY

        user_number = int(input("Please input a number between 1 and 25: "))
        number_tries += 1

       
        if user_number != the_guess_number:
            if user_number < the_guess_number:
                print ("your guess is lower than the number")
                continue


            elif user_number > the_guess_number:
                print ("your guess number is higher than the number")
                continue

            again = input("would you like to try again:yes/no").lower()

            if again == 'yes':
                continue
            else:
                quit()

        elif user_number == the_guess_number:
            print ("congralutaions you win in ", number_tries, " number of tries")
            print (the_guess_number)

    print("sorry you have exceeded the number of tries")

    again = input("would you like to play again:yes/no").lower()
    if again == "yes":
        continue
    else:
        break


