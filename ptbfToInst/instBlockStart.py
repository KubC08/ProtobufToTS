from protoInstruction import ProtoInstruction

class InstBlockStart(ProtoInstruction):
    def __init__(self, data):
        super().__init__(data)

        self.__isBlockStart = True