from numpy import matrix
from numpy import linalg
tic = matrix( [[0,0,0],[0,0,0],[0,0,0]])
print tic
print ('abc')

def input(move1,move2):
   	#move1=raw_input("first player, input row\n")
	#move2=raw_input("input column\n")
	#print type(move1)
	tic[int(move1),int(move2)]=1
	print tic
	#tac[int(move1),int(move2)]=2

#conditions
def input_pl1(pl1):
	if pl1==1:
		move1=0
		move2=0
		input(move1,move2)
	elif pl1==2:
		move1=0
		move2=1
		input(move1,move2)
	elif pl1==3:
		move1=0
		move2=2
		input(move1,move2)
	elif pl1==4:
		move1=1
		move2=0
		input(move1,move2)
	elif pl1==5:
		move1=1
		move2=1
		input(move1,move2)
	elif pl1==6:
		move1=1
		move2=2
		input(move1,move2)
	elif pl1==7:
		move1=2
		move2=0
		input(move1,move2)
	elif pl1==8:
		move1=2
		move2=1
		input(move1,move2)
	elif pl1==9:
		move1=2
		move2=2
		input(move1,move2)
	else:
			print "invalid move"

moves=1
while moves<4:
	pl1=raw_input("input your move position\n")
	player1=int(pl1)
	input_pl1(player1)
	print moves
	pl2=raw_input('Input second player move\n')
	player2=int(pl2) 
	input_pl1(player2)
	print moves
	moves+=1
