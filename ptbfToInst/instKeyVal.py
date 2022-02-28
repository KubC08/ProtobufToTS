from protoInstruction import ProtoInstruction

class InstKeyVal(ProtoInstruction):
    def __init__(self, data):
        super().__init__(data)

        self.__isKeyVal = True

        sections = self.data.split('=')
        self.__key = sections[0].strip()
        self.__val = sections[1].strip()[:-1] # We have to remove the ";" symbol

    def key(self):
        return self.__key
    def value(self):
        return self.__val