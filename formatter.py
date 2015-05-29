#!/usr/bin/env python3

# 5/29/15
# Written by Kevin Boyette

##############################################
# Automated Formatter for  C style languages #
##############################################

import re


def main():
    fileName, backUpFileName = getInput()
    myList = fileOpener(fileName)

    newList = addNewLines(myList)
    string = stringBuilder(newList)
    string = fixComments(string)

    fileWriter(backUpFileName, string)

def getInput():
    ''' Gets both a file and backup file from the user
         and returns both in a tuple '''
    fileName = input('Enter a file for formatting: ')
    backUpFileName = input('Enter a backup file name: ')
    if fileName == backUpFileName:
        print("Error: You entered the same file twice")
        return

    print('formatting file...')
    return (fileName, backUpFileName)


def fileOpener(fileName):
    '''opens file and stores contents in a list, filtering all lines
    '''
    myList = []
    with open(fileName, 'r') as myFile:
        for eachLine in myFile:
            eachLine = re.sub('\s+', ' ', eachLine)
            myList.append(str(eachLine).lstrip())
    return myList

def fileWriter(backUpFileName, string):
    '''Writes a string to a backup file'''
    with open(backUpFileName, 'w') as anotherFile:
        anotherFile.write(string)

    print('formatting complete')
    print('saved in file: ' + str(backUpFileName))



def addNewLines(myList):
    ''' Adds new lines to tokens'''
    newList = []
    for i in myList:
        for j in i:
            if j == '{':
                j = '{\n'
            elif j == '}' and i != j and '};' not in i:
                j = '\n}\n'
            elif j == '}' and i != j:
                j = '\n}'
            elif j == ';' and 'for' not in i:
                j = ';\n'

            newList.append(j)
    return newList


def stringBuilder(newList):
    newList = ''.join(newList)
    newList = newList.split('\n')

    string = ''
    leftBraceCount = 0
    for i in newList:
        if '}' in i:
            leftBraceCount -= 1
        i = (leftBraceCount * '\t') + i
        for j in i:
            if j == '{':
                leftBraceCount += 1
        i += '\n'
        string += str(i)
    return string


def fixComments(string):
    ''' Adds new lines to comments '''
    ##########################################
    # TODO deletes C style comments for now. #
    ##########################################

    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
    # first group captures quoted strings (double or single)
    # second group captures comments (//single-line or /* multi-line */)
    regex = re.compile(pattern, re.MULTILINE | re.DOTALL)

    def _replacer(match):
        if match.group(2) is not None:
            return ""
        else:
            return match.group(1)
    return regex.sub(_replacer, string)


def removeComments(string):
    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
    # first group captures quoted strings (double or single)
    # second group captures comments (//single-line or /* multi-line */)
    regex = re.compile(pattern, re.MULTILINE | re.DOTALL)

    def _replacer(match):
        if match.group(2) is not None:
            return ""
        else:
            return match.group(1)
    return regex.sub(_replacer, string)


def listToString(myList):
    ''' Turns a list to a string'''
    string = ''
    for i in myList:
        string += str(i)
    return string


main()
