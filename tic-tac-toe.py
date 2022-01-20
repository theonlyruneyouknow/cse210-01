print("Hello, World!\n Welcome to Tic-Tac-Toe")
tac = [1,2,3,4,5,6,7,8,9]
left = [1,2,3,4,5,6,7,8,9]
whosturn = "Px"
winner = ""
while winner != 0:
    ans = 0
    while not ans:
        try:
            # ans = int(input('Out of these options\(1, 2, 3), which is your favourite?'))
            print("\n",tac[0],"|",tac[1],"|",tac[2],"\n --+---+--\n",tac[3],"|",tac[4],"|",tac[5],"\n --+---+--\n",tac[6],"|",tac[7],"|",tac[8])
            if     (tac[0] == 'x' and tac[1] == 'x' and tac[2] == 'x') \
                or (tac[3] == 'x' and tac[4] == 'x' and tac[5] == 'x') \
                or (tac[6] == 'x' and tac[7] == 'x' and tac[8] == 'x') \
                or (tac[0] == 'x' and tac[3] == 'x' and tac[6] == 'x') \
                or (tac[1] == 'x' and tac[4] == 'x' and tac[7] == 'x') \
                or (tac[2] == 'x' and tac[5] == 'x' and tac[8] == 'x') \
                or (tac[0] == 'x' and tac[4] == 'x' and tac[8] == 'x') \
                or (tac[6] == 'x' and tac[4] == 'x' and tac[2] == 'x'):
                print ("X wins")
                winner = 1
                break
            # if tac[0] == 'o' and tac[1] == 'o':
            #     print ("O wins")
            #     break
            if     (tac[0] == 'o' and tac[1] == 'o' and tac[2] == 'o') \
                or (tac[3] == 'o' and tac[4] == 'o' and tac[5] == 'o') \
                or (tac[6] == 'o' and tac[7] == 'o' and tac[8] == 'o') \
                or (tac[0] == 'o' and tac[3] == 'o' and tac[6] == 'o') \
                or (tac[1] == 'o' and tac[4] == 'o' and tac[7] == 'o') \
                or (tac[2] == 'o' and tac[5] == 'o' and tac[8] == 'o') \
                or (tac[0] == 'o' and tac[4] == 'o' and tac[8] == 'o') \
                or (tac[6] == 'o' and tac[4] == 'o' and tac[2] == 'o'):
                print ("O wins")
                
                winner = 1
                break

            # if tac[0] == 'x':
            #     print ("X wins")
            if whosturn == 'Px':
                
                if len(left) == 0:
                    print ("Cat's Game. No winner. Do you want to play again?")
                else:
                    print("tac[0] = ", tac[0])
                    
                    print("left[all] = ", left)
                    y = x = int(input("x's turn to choose a square (1-9):"))
                    
                    if y not in left:
                        raise ValueError
                    else:
                        x = x-1
                        # if (tac[x] == 'x') or (tac[x] == 'o'):
                        #     y = x = int(input("Try Again. X's turn to choose a square (1-9):"))
                        #     print("tac[y] = ", tac[y])
                        #     print("left[y] = ", left)
                        # else:
                        tac.pop(x)
                        left.remove(y)
                        tac.insert(x,"x")
                        print ("input was " , y)
                        print("left[y] = ", left)
                        print("numbers left", len(left))
                        # if len(left) == 0:
                        #     print ("Cat's Game. No winner. Do you want to play again?")
                        whosturn = "Po"
            elif whosturn == 'Po':
                if len(left) == 0:
                    print ("Cat's Game. No winner. Do you want to play again?")
                    break
                else:

                    y = o = int(input("o's turn to choose a square (1-9):"))
                    o = o-1
                    if y not in left:
                        raise ValueError
                # else:
                # if (tac[o] == 'x') or (tac[o] == 'o'):
                #     o = x = int(input("Try Again. O's turn to choose a square (1-9):"))
                #     print("tac[y] = ", tac[y])
                #     print("left[y] = ", left)
                    else:
                        tac.pop(o)
                        left.remove(y)
                        tac.insert(o,"o")
                        print ("input was " , y)
                        print("left[yo] = ", left)
                        
                        print("numbers left", len(left))
                        if len(left) == 0:
                            print ("Cat's Game. No winner. Do you want to play again?")
                            break
                        whosturn = "Px"   
            else:
                print("Game Over")
                break
            # print("\n",tac[0],"|",tac[1],"|",tac[2],"\n --+---+--\n",tac[3],"|",tac[4],"|",tac[5],"\n --+---+--\n",tac[6],"|",tac[7],"|",tac[8])

        except ValueError:
            y = 0
            print("That's not an option!")
    if len(left) == 0:
        print ("Cat's Game. No winner. Do you want to play again?")
    break