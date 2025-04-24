from functions.db import Db

class League:
    def __init__(self, id, name, year, isLegacy):
        self.id       = id
        self.name     = name
        self.year     = year,
        self.isLegacy = isLegacy

    def getLeagueId(self):
        return self.id
    
    def getLeagueName(self):
        return self.name
    
    def getLeagueYear(self):
        return self.year

    def saveLeague(self):
        db         = Db()
        connection = db.connection()
        
        query = 'INSERT INTO league (id, name, year, isLegacy, active) VALUES ( "%s", "%s", "%s", "%s", 1 ) ' %(self.id, self.name, self.isLegacy, self.year)
        query += 'ON DUPLICATE KEY UPDATE id="%s", name="%s", year="%s", isLegacy="%s";' %(self.id, self.name, self.year, self.isLegacy)
        db.executeInsertQuery(connection, query)
