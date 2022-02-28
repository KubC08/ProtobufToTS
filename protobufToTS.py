import argparse

from os import path

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
