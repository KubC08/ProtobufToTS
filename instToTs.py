def getProperType(type):
    pass

def GetCodeFromInstructions(instructions, shouldSplit):
    codes = {}
    requiredImports = {}

    oneOfCode = None
    blockQueue = []
    for instruction in instructions:
        currentBlock = None
        if len(blockQueue) > 0:
            currentBlock = blockQueue[len(blockQueue) - 1]

        if instruction.isMessage():
            name = instruction.msgName()

            blockQueue.append(name)
            requiredImports[name] = []
            codes[name] = 'export interface ' + name + ' '
        elif instruction.isOneof():
            oneOfCode = '\n\t' + instruction.varName() + ': '
        elif instruction.isVariableDef():
            properType = getProperType(instruction.varType())

            if properType == instruction.varType():
                requiredImports[currentBlock].append(properType)
            if oneOfCode == None:
                codes[currentBlock] += ('\n\t' +
                    instruction.varName() +
                    ('?: ' if instruction.isOptional() else ': ') +
                    properType +
                    ('[]' if instruction.isRepeated() else ''))
            else:
                oneOfCode += properType + ' | '
        elif instruction.isExtension():
            codes[currentBlock] += '\n\t' + 'ext?: any'
        elif instruction.isEnum():
            name = instruction.enumName()

            blockQueue.append(name)
            codes[name] = 'export enum ' + name + ' '
        elif instruction.isKeyVal():
            codes[currentBlock] += '\n\t' + instruction.key() + ' = ' + instruction.value()
        elif instruction.isBlockStart():
            if oneOfCode != None:
                continue
            codes[currentBlock] += '{'
        elif instruction.isBlockEnd():
            if oneOfCode != None:
                codes[currentBlock] += oneOfCode[:-3]
                oneOfCode = None
                continue

            codes[currentBlock] += '}'
            blockQueue.pop()
