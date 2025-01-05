class Card:
    def __init__(self, num, name, idDeck, board, cardType):
        self.num      = num
        self.name     = name
        self.board    = board
        self.idDeck   = idDeck
        self.cardType = cardType

    def getNum(self):
        return str(self.num)
    
    def getName(self):
        return str(self.name)
    
    def getBoard(self):
        return str(self.board)
    
    def getIdDeck(self):
        return self.idDeck
    
    def getCardType(self):
        return self.cardType
    
    def printCard(self):
        return str(self.board) + ': ' + str(self.idDeck) + ' ' + str(self.num) + ' ' + str(self.name) + ' ' + str(self.cardType)