print("Hello, World!\n Welcome to Tic-Tac-Toe")
tac = [1,2,3,4,5,6,7,8,9]
v1 = 1
v2 = 2
v3 = 3
v4 = 4
v5 = 5
v6 = 6
v7 = 7
v8 = 8
v9 = 9
print("\n",tac[0],"|",tac[1],"|",tac[2],"\n --+---+--\n",tac[3],"|",tac[4],"|",tac[5],"\n --+---+--\n",tac[6],"|",tac[7],"|",tac[8])

print("\n",v1,"|",v2,"|",v3,"\n --+---+--\n",v4,"|",v5,"|",v6,"\n --+---+--\n",v7,"|",v8,"|",v9)
x = int(input("x's turn to choose a square (1-9):"))
x = x-1
tac.pop(x)
tac.insert(x,"x")
print ("input was " , tac)
print("\n",tac[0],"|",tac[1],"|",tac[2],"\n --+---+--\n",tac[3],"|",tac[4],"|",tac[5],"\n --+---+--\n",tac[6],"|",tac[7],"|",tac[8])
