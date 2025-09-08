from classes.top8 import Top8
from functions.functions import Scrapping
from classes.tournament import Tournament
from classes.league import League

# tournaments
# league and name hardcoded
# ids from www.mtgtop8.com
# ########################################################################
# IMPORTANT :
# current league needs to be changed manually on DB when new season starts
# ########################################################################
tournaments = [
    {
        'league'   : 3,
        'name'     : 'LCL Ingenio 2025',
        'ids'      : [ 63650, 64751, 65832, 67365, 69508, 70087, 71150, 72000 ],
        'year'     : 2025,
        'isLegacy' : 1
    },
    {
        'league' : 4,
        'name'   : 'Lliga Minoria 2025',
        'ids'    :  [ 64013, 65170, 66796, 67852, 68848, 70270, 71416, 72225, 73371 ],
        'year'   : 2025,
        'isLegacy' : 1
    },
]

# scrapping data
def scrapping(id, name, idLeague):
    soup = Scrapping()
    top  = Top8()

    # scrapping
    soup = soup.getSoup(soup.getEventUrl(id))
    # Tournament info
    tournament = Tournament()

    # Check if tournament exists on DB
    result = tournament.existsTournamentOnDB(id)
    
    if (len(result) == 0):
        idTournament = tournament.getTournamentData(soup, id, name, idLeague)
    else:
        idTournament = result[0][0]

    # top 8 players
    top.setTop8Players(soup, idTournament)
    # decks and cards
    top.setTop8PlayersDecks()

# main function
def main(tournaments):
    for item in tournaments:
        print('   - Scrapping : %s' %(item['name']))
        league = League(item['league'], item['name'], item['year'], item['isLegacy'])
        league.saveLeague()
        for id in item['ids']:
            print('     * Scrapping tournament id: %s' %(id))
            scrapping(str(id), item['name'], item['league'])


# ---------------------------------
# Start
# ---------------------------------
print(' - Start scrapping !!!')
main(tournaments)
print(' - Finish scrapping !!!')

