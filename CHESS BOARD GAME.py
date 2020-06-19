adp = {'W':0,'B':7}

di = {'W':'B','B':'W'}

fallen = []

alpha_chk = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}

#This fn is simply a printer of the chess board
def print_board(chess,fallen):
	i = 0
	for I in range(8):
		print("\t+----+----+----+----+----+----+----+----+")
		print("\t",end = "")
		for J in range(8):
			print("| "+chess[J][I],end=" ")
		print("| ", str(i))
		i+=1
	print("\t+----+----+----+----+----+----+----+----+")
	print("\t   a    b    c    d    e    f    g    h  ")
	print("\n\n")
	if not fallen:
		print("There are no fallen spawns.")
	else:
		print("The fallen are:")
		print(", ".join(fallen))
		print()
			
#print_board(chess,fallen)

#This fn takes both args as list.
# Code 0 is True
# Code 1 is player getting two turns
# Code 2 means string input error
# Code 3 means can't move spawn at the same location
def str_verifier(string,prev_str,castreq = 0,col = 0,pos = 0):
	if castreq == 0:
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
	else:
		if col in ['B','W'] and pos in ['L','R']:
			return 0
		else:
			return 2

# This fn has the duty to verify that the position mentioned is a valid move irrespective of position of other spawns	
def pos_verifier(string,chess,enpass = ['',False,'']):
	if enpass[1] == True and string[1] == 'S':
		if string[2]+string[3] in enpass[0] and string[6] == enpass[2][0]:
			if string[0] == 'B' and int(string[3]) - int(string[7]) == 1:
				return True
			elif string[0] == "W" and int(string[7]) - int(string[3]) == 1:
				return True
			else:
				return False
		else:
			return False
	if string[1] == 'S':
		if string[0] == 'B':
			if string[3] == '6':
				if string[2] == string[6] and int(string[3]) - int(string[7]) == 2 and chess[alpha_chk[string[6]]][int(string[7])] == "  ":
					return True
			if string[2] == string[6] and int(string[3]) - int(string[7]) == 1 and chess[alpha_chk[string[6]]][int(string[7])] == "  ":
				return True
			if abs(alpha_chk[string[6]] - alpha_chk[string[2]]) == 1 and int(string[3]) - int(string[7]) == 1 and chess[alpha_chk[string[6]]][int(string[7])][0] == 'W':
				return True
		if string[0] == 'W':
			if string[3] == '1':
				if string[2] == string[6] and int(string[7]) - int(string[3]) == 2 and chess[alpha_chk[string[6]]][int(string[7])] == "  ":
					return True
			if string[2] == string[6] and int(string[7]) - int(string[3]) == 1 and chess[alpha_chk[string[6]]][int(string[7])] == "  ":
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
def pos_mover(string,chess,enpass):
	if enpass[1] == True:
		dex = chess[alpha_chk[enpass[2][0]]][int(enpass[2][1])]
		chess[alpha_chk[enpass[2][0]]][int(enpass[2][1])] = "  "
		chess[alpha_chk[string[6]]][int(string[7])] = chess[alpha_chk[string[2]]][int(string[3])]
		chess[alpha_chk[string[2]]][int(string[3])] = "  "
	else:
		dex = chess[alpha_chk[string[6]]][int(string[7])]
		chess[alpha_chk[string[6]]][int(string[7])] = chess[alpha_chk[string[2]]][int(string[3])]
		chess[alpha_chk[string[2]]][int(string[3])] = "  "
	#list(chess[alpha_chk[string[6]]][int(string[7])]) == [string[4],string[5]]
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
def road_chk(string,chess,orient,chk_mate):
	L = []
	if orient == "knight":
		if chess[alpha_chk[string[6]]][int(string[7])][0] == string[0]:
			return ['',False]
		else:
			return ['',True]
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
			if chk_mate == 1:
				chk = chkmate(chr(atr+65)+string[3], di[string[0]])
				if chk[1] == True:
					L.append(chr(atr+65)+string[3])
			atr = alpha_chk[string[2]] + (i*d)
		if chess[alpha_chk[string[6]]][int(string[3])][0] == string[0]:
			c = 1
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
			if chk_mate == 1:
				chk = chkmate(string[2]+str(atr), di[string[0]])
				if chk[1] == True:
					L.append(string[2]+chr(atr+65))
			atr = int(string[3]) + (i*d)
		if chess[alpha_chk[string[2]]][int(string[7])][0] == string[0]:
			c = 1
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
			if chk_mate == 1:
				chk = chkmate(chr(ho+65)+str(ve), string[0])
				if chk[1] == True:
					L.append(chr(ho+65)+str(ve))
			ho += h
			ve += v
		if chess[alpha_chk[string[6]]][int(string[7])][0] == string[0]:
			c = 1
	if c == 1:
		return ['',False]		
	else:
		return [L,True]

#To make ease in checking route of spawn in movement
def pos_avail_chk(string,chess,chk_mate = 0):
	if string[2] == string[6]:
		orientation = "vertical"
	elif string[3] == string[7]:
		orientation = "horizontal"
	elif abs(alpha_chk[string[2]] - alpha_chk[string[6]]) == abs(int(string[3]) - int(string[7])):
		#print("D")
		orientation = "diagonal"
	else:
		orientation = "knight"
	return road_chk(string,chess,orientation,chk_mate)

#This function follows the respawn protocol
prom = ["N","R","B","Q"]
def promote_inp(col,chess):
	for A in range(8):
		i = chess[A][adp[col]]
		if i == "BS":
			print("You can Promote a soldier. Enter the code for the the replacing spawn.\n If you dont want to promote, enter 'none'.")
			print("You can Promote from:\n"+di[col])
			(" " + di[col]).join(prom)
			while c == 0:
				promoter = input()
				promoter = promoter.upper()
				if promoter == "none":
					break
				elif promoter[1] not in prom:
					print("The spawn not in the list.")
				elif promoter[0] != 'B':
					print("You're not allowed to respawn this spawn")
				else:
					c = 1
					print("The respawn request is accepted.")
			if promoter != "none":
				chess[A][adp[col]] = promoter
				break
	return True


#This fn's duty is to check if the castling input is valid or not
def cast_allow_chk(col,pos):
	if pos == 'L':
		for i in range(3):
			if chess[i+1][adp[col]] != "  ":
				return False
		stringerK = 'C' + str(adp[col])
		stringerR = 'D' + str(adp[col])
		if chkmate(stringerK,col)[1] == True or chkmate(stringerR,col)[1] == True:
			return False
		else:
			return True
	elif pos == 'R':
		for i in range(2):
			if chess[i+5][adp[col]] != "  "	:
				return False
		stringerK = 'G' + str(adp[col])
		stringerR = 'H' + str(adp[col])
		if chkmate(stringerK,col)[1] == True or chkmate(stringerR,col)[1] == True:
			return False
		else:
			return True
	if chkmate('E'+str(adp[col]), col)[1] == False:
		return True
	else:
		return False

#This fn is to check for checkmate but is made general purpose to check for dangers for pawns other than king.
def chkmate(loc,co):
	col = alpha_chk[loc[0]]-1
	row = int(loc[1])-1
	while col>=0 and row>=0:
		if chess[col][row] != "  ":
			if chess[col][row][0] == di[co]:
				stringer = chess[col][row] + chr(col+65) + str(row) + chess[col][row] + loc
				if pos_verifier(stringer,chess) == True:
					return [chr(col+65)+str(row),True]
				else:
					break
			else:
				break
		col-=1
		row-=1
	col = alpha_chk[loc[0]]-1
	row = int(loc[1])+1	
	while col>=0 and row<=7:
		if chess[col][row] != "  ":
			if chess[col][row][0] == di[co]:
				stringer = chess[col][row] + chr(col+65) + str(row) + chess[col][row] + loc
				if pos_verifier(stringer,chess) == True:
					return [chr(col+65)+str(row),True]
				else:
					break
			else:
				break
		col-=1
		row+=1
	col = alpha_chk[loc[0]]+1
	row = int(loc[1])-1
	while col<=7 and row>=0:
		if chess[col][row] != "  ":
			if chess[col][row][0] == di[co]:
				stringer = chess[col][row] + chr(col+65) + str(row) + chess[col][row] + loc
				if pos_verifier(stringer,chess) == True:
					return [chr(col+65)+str(row),True]
				else:
					break
			else:
				break
		col+=1
		row-=1
	col = alpha_chk[loc[0]]-1
	row = int(loc[1])
	while col>=0:
		if chess[col][row] != "  ":
			if chess[col][row][0] == di[co]:
				stringer = chess[col][row] + chr(col+65) + str(row) + chess[col][row] + loc
				if pos_verifier(stringer,chess) == True:
					return [chr(col+65)+str(row),True]
				else:
					break
			else:
				break
		col-=i
	col = alpha_chk[loc[0]]
	row = int(loc[1])-1
	while row>=0:
		if chess[col][row] != "  ":
			if chess[col][row][0] == di[co]:
				stringer = chess[col][row] + chr(col+65) + str(row) + chess[col][row] + loc
				if pos_verifier(stringer,chess) == True:
					return [chr(col+65)+str(row),True]
				else:
					break
			else:
				break
		row-=1
	col = alpha_chk[loc[0]]
	row = int(loc[1])+1
	while row<=7:
		if chess[col][row] != "  ":
			if chess[col][row][0] == di[co]:
				stringer = chess[col][row] + chr(col+65) + str(row) + chess[col][row] + loc
				if pos_verifier(stringer,chess) == True:
					return [chr(col+65)+str(row),True]
				else:
					break
			else:
				break
		row+=1
	col = alpha_chk[loc[0]]+1
	row = int(loc[1])
	while col<=7:
		if chess[col][row] != "  ":
			if chess[col][row][0] == di[co]:
				stringer = chess[col][row] + chr(col+65) + str(row) + chess[col][row] + loc
				if pos_verifier(stringer,chess) == True:
					return [chr(col+65)+str(row),True]
				else:
					break
			else:
				break
		col+=1
	col = alpha_chk[loc[0]]+1
	row = int(loc[1])+1
	while col<=7 and row<=7:
		if chess[col][row] != "  ":
			if chess[col][row][0] == di[co]:
				stringer = chess[col][row] + chr(col+65) + str(row) + chess[col][row] + loc
				if pos_verifier(stringer,chess) == True:
					return [chr(col+65)+str(row),True] 
				else:
					break
			else:
				break
		col+=1
		row+=1
	col = alpha_chk[loc[0]]
	row = int(loc[1])
	if col-2>=0 and row-1>=0 and chess[col-2][row-1] == di[co]+'N':
		return [chr(col-2+65)+str(int(row)-1),True]
	if col+2<=7 and row-1>=0 and chess[col+2][row-1] == di[co]+'N':
		return [chr(col+2+65)+str(int(row)-1),True]
	if col-1>=0 and row-2>=0 and chess[col-1][row-2] == di[co]+'N':
		return [chr(col-1+65)+str(int(row)-2),True]
	if col-1>=0 and row+2<=7 and chess[col-1][row+2] == di[co]+'N':
		return [chr(col-1+65)+str(int(row)+2),True]
	if col-2>=0 and row+1<=7 and chess[col-2][row+1] == di[co]+'N':
		return [chr(col-2+65)+str(int(row)+1),True]
	if col+2<=7 and row+1<=7 and chess[col+2][row+1] == di[co]+'N':
		return [chr(col+2+65)+str(int(row)+1),True]
	if col+1<=7 and row-2>=0 and chess[col+1][row-2] == di[co]+'N':
		return [chr(col+1+65)+str(int(row)-2),True]
	if col+1<=7 and row+2<=7 and chess[col+1][row+2] == di[co]+'N':
		return [chr(col+1+65)+str(int(row)+2),True]
	return ['',False]

#This fn's duty is to check if the king can be saved fro any threats if the king is moved.
def KingSaver(loc,chess):
	pawn = chess[alpha_chk[loc[0]]][int(loc[1])]
	chk = pawn + loc + pawn + loc[0] + str(int(loc[1])-1)
	if str_verifier(chk,di[pawn[0]]) == 0 and pos_avail_chk(chk,chess)[1] == True and chkmate(loc[0]+str(int(loc[1])-1),pawn[0])[1] == False:
		return True
	chk = pawn + loc + pawn + chr(alpha_chk[loc[0]]-1+65) + str(int(loc[1])-1)
	if str_verifier(chk,di[pawn[0]]) == 0 and pos_avail_chk(chk,chess)[1] == True and chkmate(chr(alpha_chk[loc[0]]-1+65) + str(int(loc[1])-1),pawn[0])[1] == False:
		return True
	chk = pawn + loc + pawn + chr(alpha_chk[loc[0]]+1+65) + str(int(loc[1])-1)
	if str_verifier(chk,di[pawn[0]]) == 0 and pos_avail_chk(chk,chess)[1] == True and chkmate(chr(alpha_chk[loc[0]]+1+65) + str(int(loc[1])-1),pawn[0])[1] == False:
		return True
	chk = pawn + loc + pawn + loc[0] + str(int(loc[1])+1)
	if str_verifier(chk,di[pawn[0]]) == 0 and pos_avail_chk(chk,chess)[1] == True and chkmate(loc[0] + str(int(loc[1])+1),pawn[0])[1] == False:
		return True
	chk = pawn + loc + pawn + chr(alpha_chk[loc[0]]-1+65) + str(int(loc[1])+1)
	if str_verifier(chk,di[pawn[0]]) == 0 and pos_avail_chk(chk,chess)[1] == True and chkmate(chr(alpha_chk[loc[0]]-1+65) + str(int(loc[1])+1),pawn[0])[1] == False:
		return True
	chk = pawn + loc + pawn + chr(alpha_chk[loc[0]]+1+65) + str(int(loc[1])+1)
	if str_verifier(chk,di[pawn[0]]) == 0 and pos_avail_chk(chk,chess)[1] == True and chkmate(chr(alpha_chk[loc[0]]+1+65) + str(int(loc[1])+1),pawn[0])[1] == False:
		return True
	chk = pawn + loc + pawn + chr(alpha_chk[loc[0]]+1+65) + loc[1]
	if str_verifier(chk,di[pawn[0]]) == 0 and pos_avail_chk(chk,chess)[1] == True and chkmate(chr(alpha_chk[loc[0]]+1+65) + loc[1],pawn[0])[1] == False:
		return True
	chk = pawn + loc + pawn + chr(alpha_chk[loc[0]]-1+65) + loc[1]
	if str_verifier(chk,di[pawn[0]]) == 0 and pos_avail_chk(chk,chess)[1] == True and chkmate(chr(alpha_chk[loc[0]]-1+65) + loc[1],pawn[0])[1] == False:
		return True
	return False

#This fn checks for the possibility of en_passe
def enpass_possi(string,chess):
	col = alpha_chk[string[6]]
	row = int(string[7])
	passi = []
	if col != 7 and chess[col+1][row] == di[string[0]]+"S":
		passi.append(chr(col+1+65)+str(row))
	if col != 0 and chess[col-1][row] == di[string[0]]+"S":
		passi.append(chr(col-1+65)+str(row))
	#print("passi")
	#print(passi)
	if passi:
		return [passi,True]
	else:
		return ['',False]


game = 0
print("\t\t**********WELCOME TO ELECTRONIC CHESS**********")

print("\nMADE BY : SHUBHAM TIWARI\n\n")

print("HOW TO INPUT:\n e.g. : BNB7BNC5\nHereindex 0 and 1 collectively contains the spawn to be moved and also index 4 and 5.\nIndex 2 and 3 denote the current position of the spawn while 6 and 7 index denote the desired position of the spawn.")
print("If you want to do castling then your input should look like...'CASTLING W L',where 'castling' obviously points out that you are trying to do a castling move,\nW points out that you are trying to move white king and rook(Don't try to move other player's king as it won't happen)for black you must use 'B'.\nAnd finally L means left i.e. Left rook is to be moved, use 'R' for moving right rook\nIf you want to reset the game, then you can do so by typing 'reset' in the input.\nLET'S PLAY!!!")
while game == 0:
	king_dead = 0
	i = 0
	prev_string = 'W'
	cawhite = 0
	cablack = 0
	cdi = {"BK":0,"WK":0,"RW":0,"RB":0,"LW":0,"LB":0}
	Blocation = "E7"
	Wlocation = "E0"
	re = 0
	checkmate = ['',False]
	chess = [["WR","WS","  ","  ","  ","  ","BS","BR"],
			["WN","WS","  ","  ","  ","  ","BS","BN"],
			["WB","WS","  ","  ","  ","  ","BS","BB"],
			["WQ","WS","  ","  ","  ","  ","BS","BQ"],
			["WK","WS","  ","  ","  ","  ","BS","BK"],
			["WB","WS","  ","  ","  ","  ","BS","BB"],
			["WN","WS","  ","  ","  ","  ","BS","BN"],
			["WR","WS","  ","  ","  ","  ","BS","BR"]]
			
	fallen.clear()
	possi_loc = []
	enpass = ['',False,'']
	while king_dead == 0:
		print_board(chess,fallen)
		print("Player 1 is BLACK.Player 2 is WHITE.")		
		if i%2 == 0:
			print("Chance for Player 1:")
		else:
			print("Chance for Player 2:")
		string = input()
		castreq = 0
		col = 0
		pos = 0
		if string.upper() == "RESET":
			re = 1
			break
		elif string.split(" ",1)[0].upper() == "CASTLING":
			req,col,pos = string.split()
			req = req.upper()
			col = col.upper()
			pos = pos.upper()
			castreq = 1
		elif len(string) != 8 or " " in string:
			print("The string is Wrong. Please input again")
			continue
		string = list(string)
		for j in range(8):
				if string[j].isalpha() == True:
					string[j] = string[j].upper()
		Nmate = []
		if checkmate and checkmate[1] == True:
			checked_by = chess[alpha_chk[checkmate[0][0]]][int(checkmate[0][1])]
			loco = 0
			#print("FJFJFJFJsd")
			if i%2 == 0:
				loco = Blocation
			else:
				loco = Wlocation
			can_be_saved = KingSaver(loco,chess)
			print(can_be_saved)
			Nmate = chkmate(checkmate[0],prev_string)
			print(Nmate)
			if checked_by[1] == 'N':
				if Nmate[1] == True and can_be_saved == True:
					if string[1] == "K" and chkmate(string[6]+string[7],di[checked_by[0]])[1] != False:
						print("CAN'T MOVE KING TO ANOTHER MATE LOCATION...TRY AGAIN!!!")
						continue
					elif string[6]+string[7] != checkmate[0]:
						print("YOU MUST REMOVE YOUR CHECK FIRST...TRY AGAIN!!!")
						continue
				elif  Nmate[1] == True and can_be_saved == False:
					if string[6]+string[7] != checkmate[0]:
						print("YOU MUST REMOVE YOUR CHECK FIRST...TRY AGAIN!!!")
						continue
				elif Nmate[1] == False and can_be_saved == True:
					if string[1] == "K" and chkmate(string[6]+string[7],di[checked_by[0]])[1] != False:
						print("CAN'T MOVE KING TO ANOTHER MATE LOCATION...TRY AGAIN!!!")
						continue
					if string[1] != "K":
						print("CAN'T MOVE OTHER PAWN WHEN THE KING IS IN CHECK AND CAN BE SAVED...TRY AGAIN!!!")
						continue
				else:
					print("YOU ARE DOOMED!!!")
			else:
				possi_loc = pos_avail_chk(checked_by[0]+checked_by[1]+checkmate[0]+checked_by[0]+checked_by[1]+loco,chess,1)[0]
				if possi_loc and Nmate[1] == True:
					if string[6]+string[7] not in possi_loc and string[6]+string[7] != checkmate[0]:
						if can_be_saved == False:
							print("YOU MUST REMOVE YOUR CHECK FIRST...TRY AGAIN!!!")
							continue
						else:
							if string[1] != 'K':
								print("YOU MUST REMOVE YOUR CHECK FIRST...TRY AGAIN!!!")
								continue
							else:
								if chkmate(string[6]+string[7],string[0]) == False:
									print("CAN'T MOVE KING TO ANOTHER MATE LOCATION...TRY AGAIN!!!")
									continue
				if possi_loc and Nmate[1] == False and string[6]+string[7] not in possi_loc:
					if can_be_saved == False:
						print("YOU MUST REMOVE YOUR CHECK FIRST...TRY AGAIN!!!")
						continue
					else:
						if string[1] != 'K':
								print("YOU MUST REMOVE YOUR CHECK FIRST...TRY AGAIN!!!")
								continue
						else:
							if chkmate(string[6]+string[7],string[0]) == False:
								print("CAN'T MOVE KING TO ANOTHER MATE LOCATION...TRY AGAIN!!!")
								continue
				if not possi_loc and Nmate[1] == True:
					if can_be_saved == False:
						if string[6]+string[7] != checkmate[0]:
							print("CAN'T MOVE OTHER PAWN WHEN THE KING IS IN CHECK AND CAN BE SAVED...TRY AGAIN!!!")
							continue
					else:
						if string[1] == 'K':
							if string[6]+string[7] != checkmate[0] or chkmate(string[6]+string[7],string[0]) == True:
								print("CAN'T MOVE KING TO ANOTHER MATE LOCATION...TRY AGAIN!!!")
								continue
						else:
							if string[6]+string[7] != checkmate[0]:
								print("CAN'T MOVE OTHER PAWN WHEN THE KING IS IN CHECK AND CAN BE SAVED...TRY AGAIN!!!")
								continue
				if not possi_loc and Nmate[1] == False:
					if can_be_saved == True:
						if string[1] == "K" and chkmate(string[6]+string[7],string[0]) == True:
							print("CAN'T MOVE KING TO ANOTHER MATE LOCATION...TRY AGAIN!!!")
							continue
						elif string[1] != "K":
							print("CAN'T MOVE OTHER PAWN WHEN THE KING IS IN CHECK AND CAN BE SAVED...TRY AGAIN!!!")
							continue
					else:
						print("YOU ARE DOOMED!!!")
		#print(str(string))
		c = 0
		r = ''
		checkmate = ['',False]
		btrick = Blocation
		wtrick = Wlocation
		if enpass[0]:
			if string[6]!=enpass[2][0]:
				enpass = ['',False,'']
		#print(enpass)
		if castreq == 0 and str_verifier(string,prev_string) == 0 and pos_spawn_chk(string,chess) == True and pos_verifier(string,chess,enpass) == True and pos_avail_chk(string,chess)[1] == True: 
			qw = pos_mover(string,chess,enpass)
			if string[0]+string[1] == "BK":
				btrick = Blocation
				Blocation = string[6]+string[7]
			if string[0]+string[1] == "WK":
				wtrick = Wlocation
				Wlocation = string[6]+string[7]
			if chkmate(Blocation,"B")[1] == True and chkmate(Wlocation,"W")[1] == True:
				chess[alpha_chk[Blocation[0]]][int(Blocation[1])] = "  "
				chess[alpha_chk[Wlocation[0]]][int(Wlocation[1])] = "  "
				chess[alpha_chk[btrick[0]]][int(btrick[1])] = "BK"
				chess[alpha_chk[wtrick[0]]][int(wtrick[1])] = "WK"
				Blocation = btrick
				Wlocation = wtrick
				if qw != " ":
					if i%2==0:
						chess[alpha_chk[string[6]]][int(string[7])] = "W"+qw
						fallen.remove("W"+qw)
					else:
						chess[alpha_chk[string[6]]][int(string[7])] = "B"+qw
						fallen.remove("B"+qw)
				print("A KING CAN'T CHECK OTHER KING...TRY AGAIN!!!")
				continue
			if string[:4] == "BKE7":
				cdi["BK"] = 1
			elif string[:4] == "WKE0":
				cdi["WK"] = 1
			elif string[:4] == "BRA7":
				cdi["RB"] = 1
			elif string[:4] == "BRH7":
				cdi["LB"] = 1
			elif string[:4] == "WRA0":
				cdi["LW"] = 1
			elif string[:4] == "WRH0":
				cdi["RW"] = 1
			if string[0]+string[1] == "BK":
				Blocation = string[6]+string[7]
			if string[0]+string[1] == "WK":
				Wlocation = string[6]+string[7]
			enpass = ['',False,'']
			if string[1] == 'S' and abs(int(string[7])-int(string[3])) == 2:
				enpass = enpass_possi(string,chess)
				#print("enpass")
				#print(enpass)
				enpass.append(string[6]+string[7])
			if qw == 'K':
				king_dead = 1
				continue
			promote_inp(di[string[0]],chess)
			if i%2 == 0:
				if chkmate(Blocation,"B")[1] == True:
					print("\t\t*****CHECKMATE*****")
				checkmate = chkmate(Wlocation,"W")
				if checkmate[1] == True:
					print("\t\t\t*****CHECK*****") 
					r = "B"
			else:
				if chkmate(Wlocation,"W")[1] == True:
					print("\t\t*****CHECKMATE*****")
				checkmate = chkmate(Blocation,"B")
				if checkmate[1] == True:
					print("\t\t\t*****CHECK*****")
					r = "W"
			if checkmate[1] == True:
				if chess[alpha_chk[checkmate[0][0]]][int(checkmate[0][1])][1] == "K":
					retu = [string[0],string[1],string[6],string[7],string[0],string[1],string[2],string[3]]
					pos_mover(retu,chess,0)
					if qw!=" ":
						chess[alpha_chk[string[6]]][int(string[7])] = r+qw
			if prev_string == "B":
				prev_string = "W"
			else:
				prev_string = "B"
			c = 1
			i+=1
		elif castreq != 0:
			if str_verifier([],[],castreq,col,pos) == 0:
				if cdi[pos+col] == 0 and cdi[col+"K"] == 0:
					if cast_allow_chk(col,pos) == True:
						i+=1
						c = 1
						if prev_string == "B":
							prev_string = "W"
						else:
							prev_string = "B"
						if col == "W" and pos == "R":
							chess[6][0] = "WK"
							chess[5][0] = "WR"
							chess[7][0] = "  "
							chess[4][0] = "  "
							cawhite = 1
						elif col == "W" and pos == "L":
							chess[2][0] = "WK"
							chess[3][0] = "WR"
							chess[0][0] = "  "
							chess[4][0] = "  "
							cawhite = 1
						elif col == "B" and pos == "R":
							chess[6][7] = "BK"
							chess[5][7] = "BR"
							chess[7][7] = "  "
							chess[4][7] = "  "
							cablack = 1
						else:
							chess[2][7] = "BK"
							chess[3][7] = "BR"
							chess[0][7] = "  "
							chess[4][7] = "  "
							cablack = 1
					else:
						print("Casting is not allowed.")
						continue
				else:
					print("Castling is being done using moved king and/or rook")
					continue
			else:
				c = 0
		if c == 0:
			if str_verifier(string,prev_string,castreq,col,pos) == 1 and i == 0:
				print("Chance is for player 1 which is black. You are moving white")
			if str_verifier(string,prev_string,castreq,col,pos) == 1:
				print("Two consecutive turns to a player is not allowed")
			if str_verifier(string,prev_string,castreq,pos,col) == 2:
				print("String input error")
			if str_verifier(string,prev_string,castreq,pos,col) == 3:
				print("Can't move spawn to it's current location")
			if str_verifier(string,prev_string) == 0 and pos_spawn_chk(string,chess) == False:
				print("The mentioned spawn is not located at the secified block.")
			if str_verifier(string,prev_string) == 0 and pos_verifier(string,chess) == False:
				print("The position mentioned is out of reach")
			if str_verifier(string,prev_string) == 0 and pos_avail_chk(string,chess)[1] == False:
				print("The road for the spawns journey is not clear")
	print_board(chess,fallen)
	if "BK" in fallen:
		print("\n\nPlayer 2 wins!!!\nTurns = " + str(i//2))
	elif "WK" in fallen:
		print("\n\nPlayer 1 wins!!!\nTurns = " + str(i//2+1))
	if re == 1:
		continue
	if "BK" in fallen or "WK" in fallen:
		again = input("\nDo you want to play again?(input 'Y' for 'yes' and 'N' for 'no')\n")
		if again.upper() == "Y":
			continue
		else:
			print("\n\nTHANK YOU FOR PLAYING!!! HOPE YOU HAD A GOOD TIME. SEE YOU SOON :)")
			break
