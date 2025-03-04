from classes.card import Card
from functions.db import Db
from functions.functions import Scrapping

class Deck:
    def __init__(self):
        self.cards = []

    def getDeckCards(self):
        return self.cards

    def getDeck(self, idDeck, soup):
        for cards in soup.findAll('div', attrs={"class": 'deck_line hover_tr'}):
            board = cards.get('id')[:2]

            if cards.text[1] == ' ':
                num  = cards.text[0]
                name = cards.text[2:].strip()
            if cards.text[2] == ' ':
                num  = cards.text[:2]
                name = cards.text[3:].strip()
            
            cardType = self.getCardType(name)
            
            card = Card(num, name, idDeck, board, cardType)
            self.cards.append(card)
            self.saveDeckCard(card)

    def getCardType(self, cardName):
        soup     = Scrapping()
        cardName = soup.convertCardName(cardName)

        try:
            soup = soup.getJsonSoup(soup.getScryfallUrlCardData(cardName))
        except Exception:
            print(soup.getScryfallUrlCardData(cardName))
            return ''
        
        if 'planeswalker' in soup['type_line'].lower():
            return 'planeswalker'
        if 'creature' in soup['type_line'].lower():
            return 'creature'
        if 'land' in soup['type_line'].lower():
            return 'land'
        if 'artifact' in soup['type_line'].lower():
            return 'artifact'
        if 'enchantment' in soup['type_line'].lower():
            return 'enchantment'
        if 'sorcery' in soup['type_line'].lower():
            return 'sorcery'
        if 'instant' in soup['type_line'].lower():
            return 'instant'        

    def savePlayerDeck(self, name, idPlayer):
        db         = Db()
        connection = db.connection()
        query      = 'INSERT INTO deck (name, idPlayer) VALUES ( "%s", "%s" );' %(name, idPlayer)
        return db.executeInsertQuery(connection, query)

    def saveDeckCard(self, card):
        db         = Db()
        connection = db.connection()
        query      = 'INSERT INTO cards (name, num, idDeck, board, cardType) VALUES ( "%s", "%s", "%s", "%s", "%s" );' %(card.getName().strip(), card.getNum(), card.getIdDeck(), card.getBoard(), card.getCardType())
        db.executeInsertQuery(connection, query)
    
    def printDeckCards(self):
        for item in self.cards:
            print(item.textCard)