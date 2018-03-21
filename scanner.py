import time
def getchar(words,pos):

	if pos<0 or pos>=len(words): return None
	if words[pos]>='0' and words[pos]<='9':
		return 'number'
	elif words[pos] == ':' or words[pos] == '.':
		return 'split'
	return 'Error'
	

def scan(text,transition_table,accept_states):
	""" Scans `text` while transitions exist in 'transition_table'.
	After that, if in a state belonging to `accept_states`,
	returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 'q0'
	
	while True:
		
		c = getchar(text,pos)	# get next char
		if state in transition_table and c in transition_table[state]:
			if state == 'q1' and c=='number':
				if text[pos-1]<='1' and text[pos-1] >='0':
					state = transition_table[state][c]	# set new state
					pos += 1	# advance to next char
				elif text[pos-1] == '2':
					if text[pos]<='3' and text[pos]>='0':
						state = transition_table[state][c]
						pos+=1
				else: return 'ERROR_TOKEN',pos
			elif state=='q1' and c=='split':
				state = transition_table[state][c]
				pos+=1
			elif state == 'q3' and text[pos]>='0' and text[pos]<='5':
					state = transition_table[state][c]
					pos+=1
			elif state=='q0' or state=='q2' or state=='q4':
				state = transition_table[state][c]
				pos+=1
			else:
				return 'ERROR_TOKEN',pos
		else:	# no transition found

			# check if current state is accepting
			if state in accept_states:
				return accept_states[state],pos

			# current state is not accepting
			return 'ERROR_TOKEN',pos
			
	
# the transition table, as a dictionary

# Αντικαταστήστε με το δικό σας λεξικό μεταβάσεων...
td = { 'q0':{ 'number':'q1' },
       'q1':{ 'number':'q2','split':'q3' },
       'q2':{ 'split':'q3' },
       'q3':{ 'number':'q4' },
       'q4':{ 'number':'q5' }
     } 

# the dictionary of accepting states and their
# corresponding token

# Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής...
ad = { 'q5':'TIME_TOKEN'  }


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:	# that is, while len(text)>0
	
	# get next token and position after last char recognized
	token,position = scan(text,td,ad)
	
	if token=='ERROR_TOKEN':
		print('unrecognized input at pos',position+1,'of',text)
		break
	
	print("token:",token,"string:",text[:position])
	
	# remaining text for next scan
	text = text[position:]
	
time.sleep(5)
