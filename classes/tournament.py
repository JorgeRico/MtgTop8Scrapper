from functions.db import Db

class Tournament():
    
    def __main__(self, name, date):
        self.name = name
        self.date = date

    def getName(self):
        return self.name
    
    def getDate(self):
        return self.date
    
    def getTournamentData(self, soup, idTournament, tournamentName, idLeague):
        for tournament in soup.findAll('div', attrs={"class": 'S14'}):
            num = 0
            for tournamentDivs in tournament.findAll('div'):
                if num == 1:
                    if tournamentDivs.text is not None:
                        text           = tournamentDivs.text
                        textSplit      = text.split(' - ')
                        tournamentDate = textSplit[1]
                        players        = textSplit[0].replace('players', '')
                    break
                num += 1
            break

        return self.saveTournament(idTournament, tournamentName, tournamentDate, idLeague, players)
    
    def saveTournament(self, idTournament, name, date, idLeague, players):
        db         = Db()
        connection = db.connection()
        query      = 'INSERT INTO tournament (idTournament, name, date, idLeague, players) VALUES ( "%s", "%s", "%s", "%s", "%s" );' %(idTournament, name, date, idLeague, players)
        
        return db.executeInsertQuery(connection, query)
    
    def existsTournamentOnDB(self, idTournament):
        db         = Db()
        connection = db.connection()
        query      = 'SELECT id as id FROM tournament WHERE idTournament = %s;' %(idTournament)
        
        return db.selectQuery(connection, query)
