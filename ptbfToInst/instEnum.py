from ptbfToInst.protoInstruction import ProtoInstruction

class InstEnum(ProtoInstruction):
    def __init__(self, data):
        super().__init__(data)

        splitData = self.data.split(' ')
        self.__enumName = splitData[1]

    def isEnum(self):
        return True
    def hasBlockStart(self):
        return True

    def enumName(self):
        return self.__enumName