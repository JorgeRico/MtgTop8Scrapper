from functions.db import Db
from classes.deck import Deck
from functions.functions import Scrapping
class Player:
    def __init__(self, num, playerName, deckName, deckHref, idTournament):
        self.num          = num
        self.playerName   = playerName
        self.deckName     = deckName
        self.deckHref     = deckHref
        self.cards        = None
        self.idPlayer     = None
        self.idTournament = idTournament
        self.db           = Db()
    
    def getPlayerNum(self):
        return str(self.num)
    
    def getPlayerName(self):
        return str(self.playerName)
    
    def getPlayerDeckName(self):
        return str(self.deckName)
    
    def getPlayerDeckHref(self):
        return str(self.deckHref)
    
    def getPlayerDeck(self):
        return self.cards

    def getIdPlayer(self):
        if self.idPlayer is None:
            result = self.existsPlayerOnDB(self.idTournament)
            self.setIdPlayer(result[0][0])
            return result[0][0]
        else:
            return self.idPlayer

    def setIdPlayer(self, idPlayer):
        self.idPlayer = idPlayer

    def setPlayerDeck(self):
        deck   = Deck()
        result = self.playerHasIdDeckOnDB()

        if (result[0][0] is None):
            print(" - Insert deck player: %s - %s" %(self.getPlayerName(), self.getPlayerDeckName()))
            idDeck = deck.savePlayerDeck(self.getPlayerDeckName(), self.getIdPlayer())
            self.savePlayerIdDeck(idDeck)

            # scrap deck
            soup = Scrapping()
            soup = soup.getSoup(self.getPlayerDeckHref())
            deck.getDeck(idDeck, soup)
        else:
            print('deck exists')

    def savePlayer(self, idTournament):
        query = 'INSERT INTO player (name, position, idTournament) VALUES ( "%s", "%s", "%s" );' %(self.getPlayerName(), self.getPlayerNum(), idTournament)
        self.setIdPlayer(self.db.executeInsertQuery(self.db.connection(), query))
    
    def savePlayerIdDeck(self, idDeck):
        updateQuery = "UPDATE player SET idDeck = '%s' WHERE id = '%s'" %(idDeck, self.getIdPlayer())
        self.db.executeQuery(self.db.connection(), updateQuery)

    def printPlayerDeckCards(self):
        for item in self.cards:
            print(item.printCard())

    def existsPlayerOnDB(self, idTournament):
        query       = 'SELECT id as idPlayer FROM player WHERE name = "%s" and position = "%s" and idTournament = "%s";' %(self.getPlayerName(), self.getPlayerNum(), idTournament)
        
        return self.db.selectQuery(self.db.connection(), query)
    
    def playerHasIdDeckOnDB(self):
        query = 'SELECT idDeck as idDeck FROM player WHERE id = %s;' %(self.getIdPlayer())
        
        return self.db.selectQuery(self.db.connection(), query)
