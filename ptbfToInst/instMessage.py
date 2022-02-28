from protoInstruction import ProtoInstruction

class InstMessage(ProtoInstruction):
    def __init__(self, data):
        super().__init__(data)

        self.__isMessage = True
        self.__hasBlockStart = True

        splitData = self.data.split(' ')
        self.__msgName = splitData[1]

    def msgName(self):
        return self.__msgName