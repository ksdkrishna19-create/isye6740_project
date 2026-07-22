"""
Club metadata: colors, abbreviations for EPL and La Liga teams.
Used across all notebooks for branded visualizations.
"""

# All EPL teams appearing in 2015-16 through 2024-25 (names match football-data.co.uk)
EPL_CLUBS = {
    'Arsenal':          {'primary': '#EF0107', 'secondary': '#063672', 'short': 'ARS'},
    'Aston Villa':      {'primary': '#670E36', 'secondary': '#95BFE5', 'short': 'AVL'},
    'Bournemouth':      {'primary': '#DA291C', 'secondary': '#000000', 'short': 'BOU'},
    'Brentford':        {'primary': '#E30613', 'secondary': '#FBB800', 'short': 'BRE'},
    'Brighton':         {'primary': '#0057B8', 'secondary': '#FFCD00', 'short': 'BHA'},
    'Burnley':          {'primary': '#6C1D45', 'secondary': '#99D6EA', 'short': 'BUR'},
    'Cardiff':          {'primary': '#0070B5', 'secondary': '#D11524', 'short': 'CAR'},
    'Chelsea':          {'primary': '#034694', 'secondary': '#DBA111', 'short': 'CHE'},
    'Crystal Palace':   {'primary': '#1B458F', 'secondary': '#C4122E', 'short': 'CRY'},
    'Everton':          {'primary': '#003399', 'secondary': '#FFFFFF', 'short': 'EVE'},
    'Fulham':           {'primary': '#000000', 'secondary': '#CC0000', 'short': 'FUL'},
    'Huddersfield':     {'primary': '#0E63AD', 'secondary': '#FFFFFF', 'short': 'HUD'},
    'Hull':             {'primary': '#F5A12D', 'secondary': '#000000', 'short': 'HUL'},
    'Ipswich':          {'primary': '#0044AA', 'secondary': '#FFFFFF', 'short': 'IPS'},
    'Leeds':            {'primary': '#FFCD00', 'secondary': '#1D428A', 'short': 'LEE'},
    'Leicester':        {'primary': '#003090', 'secondary': '#FDBE11', 'short': 'LEI'},
    'Liverpool':        {'primary': '#C8102E', 'secondary': '#00B2A9', 'short': 'LIV'},
    'Luton':            {'primary': '#F78F1E', 'secondary': '#002D62', 'short': 'LUT'},
    'Man City':         {'primary': '#6CABDD', 'secondary': '#1C2C5B', 'short': 'MCI'},
    'Man United':       {'primary': '#DA291C', 'secondary': '#FBE122', 'short': 'MUN'},
    'Middlesbrough':    {'primary': '#E11B22', 'secondary': '#FFFFFF', 'short': 'MID'},
    'Newcastle':        {'primary': '#241F20', 'secondary': '#FFFFFF', 'short': 'NEW'},
    'Norwich':          {'primary': '#00A650', 'secondary': '#FFF200', 'short': 'NOR'},
    "Nott'm Forest":    {'primary': '#DD0000', 'secondary': '#FFFFFF', 'short': 'NFO'},
    'Sheffield United': {'primary': '#EE2737', 'secondary': '#000000', 'short': 'SHU'},
    'Southampton':      {'primary': '#D71920', 'secondary': '#130C0E', 'short': 'SOU'},
    'Stoke':            {'primary': '#E03A3E', 'secondary': '#1B449C', 'short': 'STK'},
    'Sunderland':       {'primary': '#EB172B', 'secondary': '#000000', 'short': 'SUN'},
    'Swansea':          {'primary': '#000000', 'secondary': '#FFFFFF', 'short': 'SWA'},
    'Tottenham':        {'primary': '#132257', 'secondary': '#FFFFFF', 'short': 'TOT'},
    'Watford':          {'primary': '#FBEE23', 'secondary': '#ED2127', 'short': 'WAT'},
    'West Brom':        {'primary': '#122F67', 'secondary': '#FFFFFF', 'short': 'WBA'},
    'West Ham':         {'primary': '#7A263A', 'secondary': '#1BB1E7', 'short': 'WHU'},
    'Wolves':           {'primary': '#FDB913', 'secondary': '#231F20', 'short': 'WOL'},
}

# All La Liga teams appearing in 2015-16 through 2024-25 (names match football-data.co.uk)
LA_LIGA_CLUBS = {
    'Alaves':           {'primary': '#0060A9', 'secondary': '#FFFFFF', 'short': 'ALA'},
    'Almeria':          {'primary': '#EE1119', 'secondary': '#FFFFFF', 'short': 'ALM'},
    'Ath Bilbao':       {'primary': '#EE2523', 'secondary': '#FFFFFF', 'short': 'ATH'},
    'Ath Madrid':       {'primary': '#CB3524', 'secondary': '#272E61', 'short': 'ATM'},
    'Barcelona':        {'primary': '#A50044', 'secondary': '#004D98', 'short': 'BAR'},
    'Betis':            {'primary': '#00954C', 'secondary': '#FFFFFF', 'short': 'BET'},
    'Cadiz':            {'primary': '#FFD200', 'secondary': '#004A9F', 'short': 'CAD'},
    'Celta':            {'primary': '#8AC3EE', 'secondary': '#FFFFFF', 'short': 'CEL'},
    'Cordoba':          {'primary': '#FFFFFF', 'secondary': '#008B47', 'short': 'COR'},
    'Eibar':            {'primary': '#2B3795', 'secondary': '#C8102E', 'short': 'EIB'},
    'Elche':            {'primary': '#006633', 'secondary': '#FFFFFF', 'short': 'ELC'},
    'Espanol':          {'primary': '#007FC8', 'secondary': '#FFFFFF', 'short': 'ESP'},
    'Getafe':           {'primary': '#004FA3', 'secondary': '#FFFFFF', 'short': 'GET'},
    'Girona':           {'primary': '#CD2534', 'secondary': '#FFFFFF', 'short': 'GIR'},
    'Granada':          {'primary': '#E30613', 'secondary': '#FFFFFF', 'short': 'GRA'},
    'Huesca':           {'primary': '#27348B', 'secondary': '#C8102E', 'short': 'HUE'},
    'La Coruna':        {'primary': '#003DA5', 'secondary': '#FFFFFF', 'short': 'DEP'},
    'Las Palmas':       {'primary': '#FFE400', 'secondary': '#0054A6', 'short': 'LPA'},
    'Leganes':          {'primary': '#0033A0', 'secondary': '#FFFFFF', 'short': 'LEG'},
    'Levante':          {'primary': '#003DA5', 'secondary': '#C8102E', 'short': 'LEV'},
    'Mallorca':         {'primary': '#CE1126', 'secondary': '#000000', 'short': 'MLL'},
    'Malaga':           {'primary': '#005DAA', 'secondary': '#FFFFFF', 'short': 'MAL'},
    'Osasuna':          {'primary': '#D91A2A', 'secondary': '#0A1E5C', 'short': 'OSA'},
    'Real Madrid':      {'primary': '#FEBE10', 'secondary': '#00529F', 'short': 'RMA'},
    'Real Sociedad':    {'primary': '#143C8B', 'secondary': '#FFFFFF', 'short': 'RSO'},
    'Sevilla':          {'primary': '#D40E2B', 'secondary': '#FFFFFF', 'short': 'SEV'},
    'Sp Gijon':         {'primary': '#D71920', 'secondary': '#FFFFFF', 'short': 'GIJ'},
    'Valencia':         {'primary': '#EE3900', 'secondary': '#000000', 'short': 'VAL'},
    'Valladolid':       {'primary': '#6B2E7B', 'secondary': '#FFFFFF', 'short': 'VLL'},
    'Vallecano':        {'primary': '#E53027', 'secondary': '#FFFFFF', 'short': 'RAY'},
    'Villarreal':       {'primary': '#005187', 'secondary': '#FFE667', 'short': 'VIL'},
}

def get_all_clubs():
    """Return merged dict of all clubs."""
    all_clubs = {}
    all_clubs.update(EPL_CLUBS)
    all_clubs.update(LA_LIGA_CLUBS)
    return all_clubs
