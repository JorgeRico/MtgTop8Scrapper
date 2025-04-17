from functions.db import Db

class League:
    def __init__(self, id, name, year):
        self.id   = id
        self.name = name
        self.year = year

    def getLeagueId(self):
        return self.id
    
    def getLeagueName(self):
        return self.name
    
    def getLeagueYear(self):
        return self.year

    def saveLeague(self):
        db         = Db()
        connection = db.connection()
        
        query = 'INSERT INTO league (id, name, year, active) VALUES ( "%s", "%s", "%s", 1 ) ' %(self.id, self.name, self.year)
        query += 'ON DUPLICATE KEY UPDATE id="%s", name="%s", year="%s";' %(self.id, self.name, self.year)
        db.executeInsertQuery(connection, query)
