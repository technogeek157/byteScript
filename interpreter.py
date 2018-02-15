from sys import *

def open_file(filename):
	if filename[-5:] == '.byte':
		data = open(filename, 'r').read()
		data += "\n"
		return data
	else:
		print "Error: File extention is not .byte. Please use .byte files only."

def lex(filecontents):
	#turnes plaintext into a list of tokens

	#variables for tokens, strings, etc.
	tok = ''
	stringState = False
	string = ""
	tokens = []
	lastChar = ""


	filecontents = list(filecontents)
	for char in filecontents:		

		if char == "'":
			if stringState == False:
				stringState = True
				string = ""

			elif stringState == True:
				tokens.append(["string", string])
				stringState = False

		elif char == ';':
					tokens.append([';'])
					tok = ''

		elif char == ' ' or char == "\n":
			if stringState == False and lastChar != "'":
				if tok == "p":
					tokens.append(["p"])

				else:
					if char != "'":
						try:
							stuff = float(tok)
							tokens.append(["value", stuff])
						except:
							tokens.append(["variable", tok])
			tok = ''

		else:
			tok += char
			string += char

		lastChar = char

		finalTokens = []

	for i in tokens:
		if i[0] == "variable":
			if i[1] == "":
				a = 1
			else:
				finalTokens.append(i)
		else:
			finalTokens.append(i)

	return finalTokens

def parse(tokenizedList):
	commands = []
	count = 0
	currentCommand = 0

	for i in tokenizedList:
		tag = i[0]
		#if the first time running, or a new command, add a new item to list
		if count == 0:
			commands.append([])

		if tag == ';':
			commands.append([])
			currentCommand += 1

		elif tag == 'p':
			commands[currentCommand].append(tag)

		elif tag == 'value':
			commands[currentCommand].append(i)

		elif tag == 'string':
			commands[currentCommand].append(i)

		count += 1

	del commands[-1]
	return commands	

def formulate(listOfCommands):
	for i in listOfCommands:
		command = i[0]

		if command == "p":
			identity = i[1][0]
			toPrint = i[1][1]
			finalPrint = ''
			if identity == "string":
				for i in toPrint:
					if i == '_':
						finalPrint += " "
					else:
						finalPrint += i

				print finalPrint

			if identity == "value":
				print toPrint

def run():
	data = open_file(argv[1])
	tokens = lex(data)
	commands = parse(tokens)
	formulate(commands)

run()
