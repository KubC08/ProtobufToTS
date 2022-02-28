from protoInstruction import ProtoInstruction

class InstOneof(ProtoInstruction):
    def __init__(self, data):
        super().__init__(data)

        self.__isOneof = True
        self.__hasBlockStart = True

        splitData = self.data.split(' ')
        self.__name = splitData[1]

    def name(self):
        return self.__name