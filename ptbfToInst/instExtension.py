from ptbfToInst.protoInstruction import ProtoInstruction

class InstExtension(ProtoInstruction):
    def __init__(self, data):
        super().__init__(data)

    def isExtension(self):
        return True