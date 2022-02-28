import argparse

from os import path
from ptbfToInst import GetInstructionsFromProtobuf

argParser = argparse.ArgumentParser(description='Convert a protobuf file into TypeScript definitions.')
argParser.add_argument('input', metavar='Input', type=str, help='The protobuf file to convert.')
argParser.add_argument('--split-to-files', dest='shouldSplit', action='store_true', help='Splits the TypeScript interfaces into their respective files.')
argParser.add_argument('--output', dest='output', type=str, default='./output', help='Where to put the output file/files.')
args = argParser.parse_args()

InputFile = args.input
ShouldSplitFiles = args.shouldSplit
OutputFile = args.output

if not path.exists(InputFile) or not path.isfile(InputFile):
    print('The specified input file does not exist or is not a file!')
    exit()

protoHandle = open(InputFile)
instructions = GetInstructionsFromProtobuf(protoHandle.read())
protoHandle.close()

fileHandle = open('test.txt', 'w')

#print(instructions)
for instruction in instructions:
    print(instruction)
    if instruction.isOneof():
        #print('ONEOF ' + instruction.oneofName())
        fileHandle.write('ONEOF ' + instruction.oneofName() + '\n')
    elif instruction.isMessage():
        #print('MESSAGE ' + instruction.msgName())
        fileHandle.write('MESSAGE ' + instruction.msgName() + '\n')
    elif instruction.isExtension():
        #print('EXTENSIONS')
        fileHandle.write('EXTENSIONS' + '\n')
    elif instruction.isVariableDef():
        attrib = ''
        if instruction.isOptional():
            attrib = '[OPTIONAL]'
        elif instruction.isRequired():
            attrib = '[REQUIRED]'
        elif instruction.isRepeated():
            attrib = '[REPEATED]'
        #print('VARIABLE ' + instruction.varName() + ' ' + instruction.varType() + ' ' + attrib)
        fileHandle.write('VARIABLE ' + instruction.varName() + ' ' + instruction.varType() + ' ' + attrib + '\n')
    elif instruction.isEnum():
        #print('ENUM ' + instruction.enumName())
        fileHandle.write('ENUM ' + instruction.enumName() + '\n')
    elif instruction.isKeyVal():
        #print('KV ' + instruction.key() + ' = ' + instruction.value())
        fileHandle.write('KV ' + instruction.key() + ' = ' + instruction.value() + '\n')
    elif instruction.isBlockStart():
        #print('BLOCK_START')
        fileHandle.write('BLOCK_START' + '\n')
    elif instruction.isBlockEnd():
        #print('BLOCK_END')
        fileHandle.write('BLOCK_END' + '\n')

    if instruction.commentAttribute() != None:
        #print('COMMENT ' + instruction.commentAttribute())
        fileHandle.write('COMMENT ' + instruction.commentAttribute() + '\n')
    
fileHandle.close()