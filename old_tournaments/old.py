from classes.top8 import Top8
from functions.functions import Scrapping
from classes.tournament import Tournament
from classes.league import League

# tournaments
# league and name hardcoded
# ids from www.mtgtop8.com
tournaments = [
    {
        'league' : 1,
        'name'   : 'LCL Ingenio 2024',
        'ids'    : [ 51344, 52277, 53297, 54778, 55496, 56478, 57208, 58206, 59596, 60803, 61540, 62960 ]
    },
    {
        'league' : 2,
        'name'   : 'Lliga Minoria 2024',
        'ids'    :  [ 52033, 52633, 53585, 54411, 55694, 56867, 57385, 58500, 59909, 60407, 61872 ]
    },
    {
        'league' : 5,
        'name'   : 'Vintage 2024',
        'ids'    : [ 52512, 55027, 56037, 56876, 57792, 61051, 61959 ]
    }
]
