from ptbfToInst.protoInstruction import ProtoInstruction
from . import instOneof
from . import instMessage
from . import instExtension
from . import instVariableDef
from . import instEnum
from . import instKeyVal
from . import instBlockStart
from . import instBlockEnd

def GetInstructionsFromProtobuf(protoData):
    instructions = []
    dataLines = protoData.split('\n')

    isInEnum = False

    for line in dataLines:
        cleanLine = line.strip()
        currentInstruction = None

        if len(cleanLine) < 1:
            continue

        if cleanLine.startswith('oneof '):
            currentInstruction = instOneof.InstOneof(cleanLine)
        elif cleanLine.startswith('message '):
            currentInstruction = instMessage.InstMessage(cleanLine)
        elif cleanLine.startswith('extensions '):
            currentInstruction = instExtension.InstExtension(cleanLine)
        elif cleanLine.startswith('enum '):
            currentInstruction = instEnum.InstEnum(cleanLine)
        elif cleanLine.startswith('{'):
            currentInstruction = instBlockStart.InstBlockStart(cleanLine)
        elif cleanLine.startswith('}'):
            currentInstruction = instBlockEnd.InstBlockEnd(cleanLine)
        elif cleanLine.startswith('//'):
            currentInstruction = ProtoInstruction(cleanLine)
        else:
            if isInEnum:
                currentInstruction = instKeyVal.InstKeyVal(cleanLine)
            else:
                currentInstruction = instVariableDef.InstVariableDef(cleanLine)
        
        if currentInstruction == None:
            continue

        if currentInstruction.isEnum():
            isInEnum = True
        if currentInstruction.isBlockEnd():
            isInEnum = False

        instructions.append(currentInstruction)
        if currentInstruction.hasBlockStart():
            instructions.append(instBlockStart.InstBlockStart(cleanLine))

    return instructions