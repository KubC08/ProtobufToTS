from protoInstruction import ProtoInstruction

class InstEnum(ProtoInstruction):
    def __init__(self, data):
        super().__init__(data)

        self.__isEnum = True
        self.__hasBlockStart = True

        splitData = self.data.split(' ')
        self.__enumName = splitData[1]

    def enumName(self):
        return self.__enumName