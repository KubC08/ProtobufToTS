from ptbfToInst.protoInstruction import ProtoInstruction

class InstVariableDef(ProtoInstruction):
    def __init__(self, data):
        super().__init__(data)

        sections = self.data.split('=')
        sections[0] = sections[0].strip()
        sections[1] = sections[1].strip() # We don't really care about this at the moment

        attribParts = sections[0].split(' ')
        self.__varName = attribParts[len(attribParts) - 1]
        self.__varType = attribParts[len(attribParts) - 2]
        self.__isOptional = False
        self.__isRequired = False
        self.__isRepeated = False
        if len(attribParts) >= 3:
            if attribParts[0] == 'optional':
                self.__isOptional = True
            elif attribParts[0] == 'required':
                self.__isRequired = True
            elif attribParts[0] == 'repeated':
                self.__isRepeated = True

    def isVariableDef(self):
        return True

    def varName(self):
        return self.__varName
    def varType(self):
        return self.__varType
    def isOptional(self):
        return self.__isOptional
    def isRequired(self):
        return self.__isRequired
    def isRepeated(self):
        return self.__isRepeated