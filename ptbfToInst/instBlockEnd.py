from ptbfToInst.protoInstruction import ProtoInstruction

class InstBlockEnd(ProtoInstruction):
    def __init__(self, data):
        super().__init__(data)

    def isBlockEnd(self):
        return True