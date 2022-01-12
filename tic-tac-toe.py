print("Hello, World!\n Welcome to Tic-Tac-Toe")
tac = [1,2,3,4,5,6,7,8,9]

print("\n",tac[0],"|",tac[1],"|",tac[2],"\n --+---+--\n",tac[3],"|",tac[4],"|",tac[5],"\n --+---+--\n",tac[6],"|",tac[7],"|",tac[8])

x = int(input("x's turn to choose a square (1-9):"))
x = x-1
tac.pop(x)
tac.insert(x,"x")
print ("input was " , tac)
print("\n",tac[0],"|",tac[1],"|",tac[2],"\n --+---+--\n",tac[3],"|",tac[4],"|",tac[5],"\n --+---+--\n",tac[6],"|",tac[7],"|",tac[8])
