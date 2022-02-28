class ProtoInstruction:
    def __init__(self, data):
        self.data = data.strip()

        self.__commentAttribute = None
        commentSector = self.data.split('//')
        if len(commentSector) > 1:
            self.__commentAttribute = '//'.join(commentSector[1:])

    def isOneof(self):
        return False
    def isMessage(self):
        return False
    def isExtension(self):
        return False
    def isVariableDef(self):
        return False
    def isEnum(self):
        return False
    def isKeyVal(self):
        return False
    def isBlockStart(self):
        return False
    def isBlockEnd(self):
        return False

    def commentAttribute(self):
        return self.__commentAttribute

    def hasBlockStart(self):
        return False