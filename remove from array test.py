import random

current_num = ""
print("Hello, World!\n Welcome to Hilo")
print(current_num)
score = 300

possiblenums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# number_list = [111, 222, 333, 444, 555]

while len(possiblenums) != 0:
    remo = random.choice(possiblenums)
    print(remo)
    print(possiblenums)
    # first_num = random.choice(possiblenums)
    # print("First number is: ",first_num)
    # possiblenums.remove(first_num)

    # current_num = random.choice(possiblenums)


    # dirx = input("Up or Down? ")
    # if (dirx == "U" or dirx == "u"):
    #     dirx = "Up"
    # if (dirx == "D" or dirx == "d"):
    #     dirx = "Down"
    # print ('(' , dirx, ')')
    # print (possiblenums)
    # # y = x = int(input("x's turn to choose a square (1-9):"))
    # # random item from list
    # print(current_num)
    # winner = ""
    # direction = ""
    # # score = 300

    # # Output 222
    # left = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    # if( current_num > first_num):
    #     direction = "Up"
    #     print(direction, "line 22")
    # else:
    #     direction = "Down"
    #     print(direction, "line 25")

    # if( dirx == direction):
    #     score += 100
    #     print(score, "line 29")
    # else:
    #     score -= 75
    #     print(score, "line 32")
    # first_num = current_num
