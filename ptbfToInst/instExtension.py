from protoInstruction import ProtoInstruction

class InstExtension(ProtoInstruction):
    def __init__(self, data):
        super().__init__(data)

        self.__isExtension = True