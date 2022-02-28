from ptbfToInst.protoInstruction import ProtoInstruction

class InstMessage(ProtoInstruction):
    def __init__(self, data):
        super().__init__(data)

        splitData = self.data.split(' ')
        self.__msgName = splitData[1]

    def isMessage(self):
        return True
    def hasBlockStart(self):
        return True

    def msgName(self):
        return self.__msgName