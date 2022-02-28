class ProtoInstruction:
    def __init__(self, data):
        self.data = data.strip()

        self.__isOneof = False
        self.__isMessage = False
        self.__isExtension = False
        self.__isVariableDef = False
        self.__isEnum = False
        self.__isKeyVal = False
        self.__isBlockStart = False
        self.__isBlockEnd = False

        self.__commentAttribute = None
        commentSector = self.data.split('//')
        if len(commentSector) > 1:
            self.__commentAttribute = '//'.join(commentSector[1:])

        self.__hasBlockStart = False

        """
        if self.data.startswith('oneof'):
            self.__isOneof = True
        elif self.data.startswith('message'):
            self.__isMessage = True
        elif self.data.startswith('extensions'):
            self.__isExtension = True
        elif self.data != '' and self.data != None:
            self.__isVariableDef = True"""

    def isOneof(self):
        return self.__isOneof
    def isMessage(self):
        return self.__isMessage
    def isExtension(self):
        return self.__isExtension
    def isVariableDef(self):
        return self.__isVariableDef
    def isEnum(self):
        return self.__isEnum
    def isKeyVal(self):
        return self.__isKeyVal
    def isBlockStart(self):
        return self.__isBlockStart
    def isBlockEnd(self):
        return self.__isBlockEnd

    def commentAttribute(self):
        return self.__commentAttribute

    def hasBlockStart(self):
        return self.__hasBlockStart