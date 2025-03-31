from functions.functions import Scrapping
from classes.player import Player
class Top8:
    def __init__(self):
        self.topPlayers = []

    def getTopPlayers(self):
        return self.topPlayers
    
    def setTopPlayer(self, deckName, playerName, deckHref, idTournament):
        scrapping = Scrapping()
        if deckName != '' and playerName != '' and deckHref != '':
            num    = len(self.topPlayers)
            player = Player(num+1, playerName, deckName, scrapping.getPlayerDeckUrl(deckHref), idTournament)
            self.topPlayers.append(player)
            
            return True
        
        return False

    def scrapTopPlayers(self, soup, className, idTournament):
        for set in soup.findAll('div', attrs={"class": className}):
            num = 0

            for link in set.find_all('a'):

                if link.text != '':
                    if num == 0:
                        deckName = link.text
                        deckHref = link.get('href')
                    if num == 1:
                        playerName = link.text
                        # print("%s - %s" %(playerName, soup.original_encoding))
                        if (soup.original_encoding == 'cp850'):
                            name = playerName.encode('cp850')
                            playerName = name.decode(encoding="ISO-8859-1",errors="ignore")
                        if(soup.original_encoding == "windows-1250"):
                            name = playerName.encode('windows-1250')
                            playerName = name.decode(encoding="ISO-8859-1",errors="ignore")
                    num+=1
            
            if self.setTopPlayer(deckName, playerName, deckHref, idTournament) == True:
                deckName   = ''
                playerName = ''
    
    def setTop8Players(self, soup, idTournament):
        self.scrapTopPlayers(soup, "chosen_tr", idTournament)
        self.scrapTopPlayers(soup, "hover_tr", idTournament)
        self.saveTop8Data(str(idTournament))

    def setTop8PlayersDecks(self):
        for player in self.topPlayers:
            player.setPlayerDeck()
    
    def saveTop8Data(self, idTournament):
        for item in self.topPlayers:
            if (len(item.existsPlayerOnDB(idTournament)) == 0):
                print(' - Insert %s - %s' %(item.getPlayerNum(),item.getPlayerName()))
                item.savePlayer(idTournament)

    def printTopPlayers(self):
        for item in self.topPlayers:
            print(' - ' + str(item.getPlayerNum()) + ' ||| ' + item.getPlayerName() + ' ||| ' + item.getPlayerDeckName() + ' ||| ' + item.getPlayerDeckHref())