from ptbfToInst.protoInstruction import ProtoInstruction

class InstOneof(ProtoInstruction):
    def __init__(self, data):
        super().__init__(data)

        splitData = self.data.split(' ')
        self.__oneofName = splitData[1]

    def isOneof(self):
        return True
    def hasBlockStart(self):
        return True

    def oneofName(self):
        return self.__oneofName