score = 0

question1 = input("what is the colour of the sky \n"
             "a) red \n"
             "b) blue \n"
             "c) green  \n \n"
             "Please enter a , b or c: ")

if question1 == "b":
    score += 1



question2 = input("what is the colour of the mango \n"
             "a) red \n"
             "b) yellow \n"
             "c) green  \n \n"
             "Please enter a , b or c: ")

if question2 == "b":
    score += 1

question3 = input("what is the colour of the carrot \n"
             "a) red \n"
             "b) blue \n"
             "c) green  \n \n"
             "Please enter a , b or c: ")

if question3 == "a":
    score += 1

question4 = input("what is the colour of the grass \n"
             "a) red \n"
             "b) blue \n"
             "c) green  \n \n"
             "Please enter a , b or c: ")

if question4 == "c":
    score += 1

print (" you have got {} / 4 right".format(score))
