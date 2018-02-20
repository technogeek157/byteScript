from sys import *
import time

def open_file(filename):
    if filename[-5:] == '.byte':
        data = open(filename, 'r').read()
        data += "\n"
        return data
    else:
        print "Error: File extention is not .byte. Please use .byte files only."

def lex(filecontents):
    #turnes plaintext into a list of tokens
    curr = "" #the current token
    tokenList= [] #all the tokens
    stringState = False #if recording a string or not
    
    for char in filecontents:
        curr += char
        if char == ' ':
            detect = curr[:-1]
            if detect == '\np' or detect == 'p':
                tokenList.append(['p'])

            elif stringState == True:
                tokenList.append(['s', curr[1:-2]])
                stringState = False

            elif detect == ';':
                tokenList.append([';'])
        
            curr = ''

        elif char == "'":
            if stringState == False:
                stringState = True

    return tokenList

def parse(tokenList):
    commandList = []
    currCommand = []
    
    for i in tokenList:
        token = i[0]
        if token == ';':
            commandList.append(currCommand)
            currCommand = []

        else:
            currCommand.append(i)

    return commandList


def formulate(toFormulate):
	for i in toFormulate:
		if i[0][0] == 'p':
			if i[1][0] == 's':
				print i[1][1]

def run():
    data = open_file('test.byte')
    tokens = lex(data)
    commands = parse(tokens)
    formulate(commands)
    time.sleep(5)
run()
