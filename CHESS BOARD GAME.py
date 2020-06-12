chess = [["WR","WS","  ","  ","  ","  ","BS","BR"],
		 ["WN","WS","  ","  ","  ","  ","BS","BN"],
		 ["WB","WS","  ","  ","  ","  ","BS","BB"],
		 ["WK","WS","  ","  ","  ","  ","BS","BK"],
		 ["WQ","WS","  ","  ","  ","  ","BS","BQ"],
		 ["WB","WS","  ","  ","  ","  ","BS","BB"],
		 ["WN","WS","  ","  ","  ","  ","BS","BN"],
		 ["WR","WS","  ","  ","  ","  ","BS","BR"]]

fallen = []

alpha_chk = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}

#This fn is simply a printer of the chess board
def print_board(chess,fallen):
	i = 0
	for I in range(8):
		print("+----+----+----+----+----+----+----+----+")
		for J in range(8):
			print("| "+chess[J][I],end=" ")
		print("| ", str(i))
		i+=1
	print("+----+----+----+----+----+----+----+----+")
	print("   a    b    c    d    e    f    g    h  ")
	print("\n\n")
	if not fallen:
		print("There are no fallen spawns.")
	else:
		for A in fallen:
			print(A,end = " ")
			
#print_board(chess,fallen)

#This fn takes both args as list.
# Code 0 is True
# Code 1 is player getting two turns
# Code 2 means string input error
# Code 3 means can't move spawn at the same location
def str_verifier(string,prev_str):
	if string[0] == prev_str[0]:
		return 1
	if string[0] not in ['B','W'] or string[4] not in ['B','W']:
		return 2
	if string[1] not in ['B','N','R','K','Q','S'] or string[5] not in ['B','N','R','K','Q','S']:
		return 2
	if string[2] not in ['A','B','C','D','E','F','G','H'] or string[6] not in ['A','B','C','D','E','F','G','H']:
		return 2
	if string[3] not in ['1','2','3','4','5','6','7','0'] or string[7] not in ['1','2','3','4','5','6','7','0']:
		return 2
	if str([string[0],string[1]]) != str([string[4],string[5]]):
		return 2
	if str([string[2],string[3]]) == str([string[6],string[7]]):
		return 3
	return 0

# This fn has the duty to verify that the position mentioned is a valid move irrespective of position of other spawns	
def pos_verifier(string,chess):
	if string[1] == 'S':
		if string[0] == 'B':
			if string[3] == '6':
				if string[2] == string[6] and int(string[3]) - int(string[7]) == 2:
					return True
			if string[2] == string[6] and int(string[3]) - int(string[7]) == 1:
				return True
			if abs(alpha_chk[string[6]] - alpha_chk[string[2]]) == 1 and int(string[3]) - int(string[7]) == 1 and chess[alpha_chk[string[6]]][int(string[7])][0] == 'W':
				return True
		if string[0] == 'W':
			if string[3] == '1':
				if string[2] == string[6] and int(string[7]) - int(string[3]) == 2:
					return True
			if string[2] == string[6] and int(string[7]) - int(string[3]) == 1:
				return True
			if abs(alpha_chk[string[6]] - alpha_chk[string[2]]) == 1 and int(string[7]) - int(string[3]) == 1 and chess[alpha_chk[string[6]]][int(string[7])][0] == 'B':
				return True
		elif string[0] in 'W':
			return True	
	elif string[1] in 'N':
		if abs(alpha_chk[string[6]]-alpha_chk[string[2]]) == 1 and abs(int(string[7]) - int(string[3])) == 2:
			return True
		elif abs(alpha_chk[string[6]]-alpha_chk[string[2]]) == 2 and abs(int(string[7]) - int(string[3])) == 1:
			return True
	elif string[1] in 'K':
		if abs(alpha_chk[string[6]]-alpha_chk[string[2]]) <= 1 and abs(int(string[7]) - int(string[3])) <= 1 and not (alpha_chk[string[6]]-alpha_chk[string[2]] == 0 and abs(int(string[7]) - int(string[3])) == 0):
			return True
	elif string[1] in 'Q':
		if abs(alpha_chk[string[6]]-alpha_chk[string[2]]) == 0 and abs(int(string[7]) - int(string[3])) != 0:
			return True
		elif abs(int(string[7]) - int(string[3])) == 0 and abs(alpha_chk[string[6]]-alpha_chk[string[2]]) != 0:
			return True
		elif abs(alpha_chk[string[6]]-alpha_chk[string[2]]) == abs(int(string[7]) - int(string[3])):
			return True
	elif string[1] in 'R':
		if abs(alpha_chk[string[6]]-alpha_chk[string[2]]) == 0 and abs(int(string[7]) - int(string[3])) != 0:
			return True
		elif abs(int(string[7]) - int(string[3])) == 0 and abs(alpha_chk[string[6]]-alpha_chk[string[2]]) != 0:
			return True
	elif string[1] in 'B':
		if abs(alpha_chk[string[6]]-alpha_chk[string[2]]) == abs(int(string[7]) - int(string[3])):
			return True
	return False		

#This fn's duty is to check if the spawn to be moved is in its mentioned place or not
def pos_spawn_chk(string,chess):
	if list(chess[alpha_chk[string[2]]][int(string[3])]) == [string[0],string[1]]:
		#print("t"+str(list(chess[alpha_chk[string[2]]][int(string[3])]))+" "+string[3]+" "+str([string[0],string[1]]))
		return True
	else:
		#print("f"+str(list(chess[alpha_chk[string[2]]][int(string[3])]))+" "+string[3]+" "+str([string[0],string[1]]))
		return False

# This fn takes the user input str (in list form) and chess board nested list to move the spawn and check for any removal
#dex[1] is used to verify if a king is fallen..If so then game ends
def pos_mover(string,chess):
	dex = chess[alpha_chk[string[6]]][int(string[7])]
	chess[alpha_chk[string[6]]][int(string[7])] = chess[alpha_chk[string[2]]][int(string[3])]
	chess[alpha_chk[string[2]]][int(string[3])] = "  "
	list(chess[alpha_chk[string[6]]][int(string[7])]) == [string[4],string[5]]
	if dex != "  ":
		fallen.append(dex)
	if dex != "  ":
		print("A spawn has been defeated.\nThe spawn is: ",end = '')
		if dex[0] in ['B']:
			print("A Black ",end ='')
		else:
			print("A White",end = ' ')
		if dex[1] == 'K':
			print("King")
		elif dex[1] == 'Q':
			print("Queen")
		elif dex[1] == 'R':
			print("Rook")
		elif dex[1] == 'B':
			print("Bishop")
		elif dex[1] == 'N':
			print("Knight")
		else:
			print("Soldier")
	return dex[1]

#This fn's main purpose is to check position and return it to pos_avail_chk functon
def road_chk(string,chess,orient):
	if orient == "knight":
		if chess[alpha_chk[string[6]]][int(string[7])][0] == string[0]:
			return False
		else:
			return True
	elif orient == "horizontal":
		if string[6] > string[2]:
			d = 1
		else:
			d = -1
		atr = alpha_chk[string[2]] + (1*d)
		i = 1
		c = 0
		while atr != alpha_chk[string[6]]:
			i += 1
			if chess[atr][int(string[3])] != "  ":
				c = 1
				break
			atr = alpha_chk[string[2]] + (i*d)
			if chess[alpha_chk[string[6]]][int(string[3])][0] == string[0]:
				c = 1
			if c == 1:
				return False
			else:
				return True
	elif orient == "vertical":
		if string[7]>string[3]:
			d = 1
		else:
			d = -1
		atr = int(string[3]) + d
		i = 1
		c = 0
		while atr != int(string[7]):
			i+=1
			if chess[alpha_chk[string[2]]][atr] != "  ":
				c = 1
				break
			atr = int(string[3]) + (i*d)
		if chess[alpha_chk[string[2]]][int(string[7])][0] == string[0]:
			c = 1
		if c == 1:
			return False
		else:
			return True
	elif orient == "diagonal":
		if string[2] > string[6]:
			h = -1
		else:
			h = 1
		if string[3] > string[7]:
			v = -1
		else:
			v = 1
		ho = alpha_chk[string[2]] + (1*h)
		ve = int(string[3]) + (1*v)
		c = 0
		while ho != alpha_chk[string[6]] and ve != int(string[7]):
			if chess[ho][ve] != "  ":
				c = 1
				break
			ho += h
			ve += v
		if chess[alpha_chk[string[6]]][int(string[7])][0] == string[0]:
			c = 1
		if c == 1:
			return False
		else:
			return True

#To make ease in checking route of spawn in movement
def pos_avail_chk(string,chess):
	if string[2] == string[6]:
		orientation = "vertical"
	elif string[3] == string[7]:
		orientation = "horizontal"
	elif abs(alpha_chk[string[2]] - alpha_chk[string[6]]) == abs(int(string[3]) - int(string[7])):
		print("D")
		orientation = "diagonal"
	else:
		orientation = "knight"
	return road_chk(string,chess,orientation)
	
#This function follows the respawn protocol
def respawn_inp(fallen,chess):
	for A in range(8):
		i = chess[A][0]
		if i in ["BS","BR","BB","BK","BQ"]:
			print("You can respawn someone. Enter the code for the the spawn to be respawned.\n If you dont want to respawn someone enter 'none'.")
			print("You can respawn from: ")
			for j in fallen:
				print(j,end = " ")
			c = 0
			while c == 0:
				respawnner = input()
				if respawnner == "none":
					break
				elif respawnner not in fallen:
					print("The spawn not in the list.")
				elif respawnner[0] != 'B':
					print("You're not allowed to respawn this spawn")
				else:
					c = 1
					print("The respawn request is accepted.")
			if respawnner != "none":
				chess[0][chess[0].index[i]] = respawnner
				break
	for A in range(8):
		i = chess[A][7]
		if i in ["WS","WR","WB","WK","WQ"]:
			print("You can respawn someone. Enter the code for the the spawn to be respawned.\n If you dont want to respawn someone enter 'none'.")
			print("You can respawn from: ")
			for j in fallen:
				print(j,end = " ")
			c = 0
			while c == 0:
				respawnner = input()
				if respawnner == "none":
					break
				elif respawnner not in fallen:
					print("The spawn not in the list.")
				elif respawnner[0] != 'W':
					print("You're not allowed to respawn this spawn")
				else:
					c = 1
					print("The respawn request is accepted.")
			if respawnner != "none":
				chess[0][chess[0].index[i]] = respawnner
				break
	return True
	

king_dead = 0
i = 0
prev_string = 'W'
while king_dead == 0:
	print_board(chess,fallen)
	print("Player 1 is BLACK.Player 2 is WHITE.")		
	if i%2 == 0:
		print("Chance for Player 1:")
	else:
		print("Chance for Player 2:")
	string = input()
	if len(string) != 8 or " " in string:
		continue
	string = list(string)
	for j in range(8):
		if string[j].isalpha() == True:
			string[j] = string[j].upper()
	#print(str(string))
	c = 0
	if str_verifier(string,prev_string) == 0 and pos_spawn_chk(string,chess) == True and  pos_verifier(string,chess) == True and pos_avail_chk(string,chess) == True:
		qw = pos_mover(string,chess)
		if qw == 'K':
			king_dead = 1
			continue
		respawn_inp(fallen,chess)
		if prev_string == "B":
			prev_string = "W"
		else:
			prev_string = "B"
		c = 1
		i+=1
	if c == 0:
		if str_verifier(string,prev_string) == 1 and i == 0:
			print("Chance is for player 1 which is black. You are moving white")
		if str_verifier(string,prev_string) == 1:
			print("Two consecutive turns to a player is not allowed")
		if str_verifier(string,prev_string) == 2:
			print("String input error")
		if str_verifier(string,prev_string) == 3:
			print("Can't move spawn to it's current location")
		if pos_spawn_chk(string,chess) == False:
			print("The mentioned spawn is not located at the secified block.")
		if pos_verifier(string,chess) == False:
			print("The position mentioned is out of reach")
		if pos_avail_chk(string,chess) == False:
			print("The road for the spawns journey is not clear")
if "BK" in fallen:
	print("Player 2 wins!!!\n Turns = " + str(i//2))
else:
	print("Player 1 wins!!!\n Turns = " + str(i//2+1))
