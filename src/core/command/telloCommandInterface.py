from abc import abstractclassmethod

class TelloCommandInterface():

    @abstractclassmethod
    def getCommand() -> str:
        pass

    @abstractclassmethod
    def getParameters(*values) -> list:
        pass

    @abstractclassmethod
    def isEditable() -> bool:
        pass

    @abstractclassmethod
    def hasResponse() -> bool:
        pass
