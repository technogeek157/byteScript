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
            if detect == '\nprint' or detect == 'print':
                tokenList.append(['p'])

            elif detect == '\nadd' or detect == 'add':
                tokenList.append(['a'])

            elif detect == "\nifequal" or detect == 'ifequal':
                tokenList.append(['ie'])

            elif detect == "\nifgreater" or detect == 'ifgreater':
                tokenlist.append(['ig'])

            elif detect == '\ndeclare' or detect == 'declare':
                tokenList.append(['d'])

            elif stringState == True:
                tokenList.append(['s', curr[1:-2]])
                stringState = False

            elif detect == ';':
                tokenList.append([';'])

            else:
                try:
                    tokenList.append(['n', float(detect)])

                except:
                    tokenList.append(['v', detect])
        
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
    var = {}
    count = -1
    while True:
        count += 1
        i = toFormulate[count]
        command = i[0][0]
        valueType = i[1][0]
        valueValue = i[1][1]
        if command == 'p':
            if valueType == 's' or valueType == 'n':
                print valueValue

            elif valueType == 'v':
                if valueValue in var:
                    print var[valueValue]
                else:
                    print "Error, variable does not exist"
                    break

        elif command == 'd':
            if i[2][0] == 'v':
                var[i[1][1]] = var[i[2][1]]
            else:
                var[valueValue] = i[2][1]

        elif command == "a":
            var[i[3][1]] = var[i[1][1]] + var[i[2][1]]

        elif command == "ie":
            if var[valueValue] == i[2][1]:
                pass
            else:
                count += 1


        if count >= len(toFormulate) -1:
            break

    print var

def run():
    data = open_file('test.byte')
    tokens = lex(data)
    commands = parse(tokens)
    print commands
    formulate(commands)
    time.sleep(5)
run()
