"""
Notebook 01 equivalent: Data Collection & Feature Engineering
Downloads match data from football-data.co.uk and engineers features.
"""
import pandas as pd
import numpy as np
import json, os, io, urllib.request

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
os.makedirs(DATA_DIR, exist_ok=True)
BASE_URL = "https://www.football-data.co.uk/mmz4281"
# 10 seasons: 2015-16 through 2024-25
SEASONS = [
    ('1516', '2015-2016'), ('1617', '2016-2017'), ('1718', '2017-2018'),
    ('1819', '2018-2019'), ('1920', '2019-2020'), ('2021', '2020-2021'),
    ('2122', '2021-2022'), ('2223', '2022-2023'), ('2324', '2023-2024'),
    ('2425', '2024-2025'),
]
DOWNLOADS = {}
for code, label in SEASONS:
    DOWNLOADS[('ENG-Premier League', label)] = f"{BASE_URL}/{code}/E0.csv"
    DOWNLOADS[('SPA-La Liga',        label)] = f"{BASE_URL}/{code}/SP1.csv"

# Download
all_dfs = []
for (league, season), url in DOWNLOADS.items():
    print(f"Fetching {league} {season}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read().decode('utf-8-sig')
    df = pd.read_csv(io.StringIO(raw))
    df['league'] = league
    df['season'] = season
    print(f"  → {len(df)} matches")
    all_dfs.append(df)

raw_df = pd.concat(all_dfs, ignore_index=True)
raw_df.to_csv(os.path.join(DATA_DIR, 'raw_football_data.csv'), index=False)
print(f"Total raw: {len(raw_df)} matches")

# Reshape to team-match level
rows = []
for _, m in raw_df.iterrows():
    date = m.get('Date',''); league = m.get('league',''); season = m.get('season','')
    home = m.get('HomeTeam',''); away = m.get('AwayTeam',''); ftr = m.get('FTR','')
    ref = m.get('Referee','')
    common = dict(date=date, league=league, season=season, referee=ref,
                  odds_over25=m.get('Avg>2.5', m.get('B365>2.5', np.nan)),
                  odds_under25=m.get('Avg<2.5', m.get('B365<2.5', np.nan)))
    h = {**common, 'squad': home, 'opponent': away, 'venue': 'Home',
         'goals_for': m.get('FTHG'), 'goals_against': m.get('FTAG'),
         'ht_goals_for': m.get('HTHG'), 'ht_goals_against': m.get('HTAG'),
         'shots': m.get('HS'), 'shots_on_target': m.get('HST'),
         'corners': m.get('HC'), 'fouls': m.get('HF'),
         'yellow_cards': m.get('HY'), 'red_cards': m.get('HR'),
         'opp_shots': m.get('AS'), 'opp_shots_on_target': m.get('AST'),
         'opp_corners': m.get('AC'), 'opp_fouls': m.get('AF'),
         'odds_win': m.get('AvgH', m.get('B365H')),
         'odds_draw': m.get('AvgD', m.get('B365D')),
         'odds_loss': m.get('AvgA', m.get('B365A')),
         'result': 'W' if ftr=='H' else ('D' if ftr=='D' else 'L')}
    a = {**common, 'squad': away, 'opponent': home, 'venue': 'Away',
         'goals_for': m.get('FTAG'), 'goals_against': m.get('FTHG'),
         'ht_goals_for': m.get('HTAG'), 'ht_goals_against': m.get('HTHG'),
         'shots': m.get('AS'), 'shots_on_target': m.get('AST'),
         'corners': m.get('AC'), 'fouls': m.get('AF'),
         'yellow_cards': m.get('AY'), 'red_cards': m.get('AR'),
         'opp_shots': m.get('HS'), 'opp_shots_on_target': m.get('HST'),
         'opp_corners': m.get('HC'), 'opp_fouls': m.get('HF'),
         'odds_win': m.get('AvgA', m.get('B365A')),
         'odds_draw': m.get('AvgD', m.get('B365D')),
         'odds_loss': m.get('AvgH', m.get('B365H')),
         'result': 'W' if ftr=='A' else ('D' if ftr=='D' else 'L')}
    rows.extend([h, a])

team_df = pd.DataFrame(rows)
team_df['date'] = pd.to_datetime(team_df['date'], format='%d/%m/%Y', errors='coerce')
team_df = team_df.sort_values(['league','season','squad','date']).reset_index(drop=True)

# Convert numerics
num_cols = ['goals_for','goals_against','ht_goals_for','ht_goals_against',
            'shots','shots_on_target','corners','fouls','yellow_cards','red_cards',
            'opp_shots','opp_shots_on_target','opp_corners','opp_fouls',
            'odds_win','odds_draw','odds_loss','odds_over25','odds_under25']
for c in num_cols:
    team_df[c] = pd.to_numeric(team_df[c], errors='coerce')

# Feature engineering
team_df['shot_accuracy'] = team_df['shots_on_target'] / team_df['shots'].replace(0, np.nan)
team_df['shot_conversion'] = team_df['goals_for'] / team_df['shots'].replace(0, np.nan)
team_df['opp_shot_accuracy'] = team_df['opp_shots_on_target'] / team_df['opp_shots'].replace(0, np.nan)
team_df['shot_dominance'] = team_df['shots'] / (team_df['shots'] + team_df['opp_shots']).replace(0, np.nan)
team_df['corner_dominance'] = team_df['corners'] / (team_df['corners'] + team_df['opp_corners']).replace(0, np.nan)
team_df['discipline_index'] = 10 * team_df['yellow_cards'].fillna(0) + 25 * team_df['red_cards'].fillna(0)
team_df['foul_rate'] = team_df['fouls']
team_df['second_half_goals'] = team_df['goals_for'] - team_df['ht_goals_for'].fillna(0)
team_df['clean_sheet'] = (team_df['goals_against'] == 0).astype(int)

# Implied probabilities from odds
for col, odd in [('implied_win_prob','odds_win'),('implied_draw_prob','odds_draw'),('implied_loss_prob','odds_loss')]:
    team_df[col] = 1.0 / team_df[odd].replace(0, np.nan)
prob_sum = team_df[['implied_win_prob','implied_draw_prob','implied_loss_prob']].sum(axis=1)
for col in ['implied_win_prob','implied_draw_prob','implied_loss_prob']:
    team_df[col] = team_df[col] / prob_sum.replace(0, np.nan)

team_df['over25_implied'] = 1.0 / team_df['odds_over25'].replace(0, np.nan)
ou_sum = team_df['over25_implied'].fillna(0) + (1.0 / team_df['odds_under25'].replace(0, np.nan)).fillna(0)
team_df['over25_implied'] = team_df['over25_implied'] / ou_sum.replace(0, np.nan)

# Rolling features
points_map = {'W': 3, 'D': 1, 'L': 0}
team_df['match_points'] = team_df['result'].map(points_map)
for feat, src in [('rolling_form_5','match_points'),('rolling_goals_5','goals_for'),('rolling_conceded_5','goals_against')]:
    team_df[feat] = team_df.groupby(['league','season','squad'])[src].transform(lambda x: x.rolling(5, min_periods=1).mean())

print(f"Team-match observations: {len(team_df)}")

# Feature columns for clustering
FEATURE_COLS = ['shots','shots_on_target','corners','fouls','yellow_cards',
                'shot_accuracy','shot_conversion','shot_dominance','corner_dominance',
                'opp_shot_accuracy','discipline_index','implied_win_prob','over25_implied']

# Fill NaN with median
for f in FEATURE_COLS:
    team_df[f] = team_df[f].fillna(team_df[f].median())

# Validate
print("\nVALIDATION:")
for league in team_df['league'].unique():
    for season in team_df['season'].unique():
        sub = team_df[(team_df['league']==league)&(team_df['season']==season)]
        nt = sub['squad'].nunique()
        mpt = sub.groupby('squad').size()
        print(f"  {league} {season}: {nt} teams, {mpt.min()}-{mpt.max()} matches/team")

# Export
team_df.to_csv(os.path.join(DATA_DIR, 'match_data_clean.csv'), index=False)
with open(os.path.join(DATA_DIR, 'feature_columns.json'), 'w') as f:
    json.dump(FEATURE_COLS, f, indent=2)
team_df[team_df['league']=='ENG-Premier League'].to_csv(os.path.join(DATA_DIR, 'epl_match_data.csv'), index=False)
team_df[team_df['league']=='SPA-La Liga'].to_csv(os.path.join(DATA_DIR, 'laliga_match_data.csv'), index=False)

print(f"\nExported:")
print(f"  match_data_clean.csv: {len(team_df)} rows")
print(f"  feature_columns.json: {len(FEATURE_COLS)} features")
print(f"  epl_match_data.csv: {(team_df['league']=='ENG-Premier League').sum()} rows")
print(f"  laliga_match_data.csv: {(team_df['league']=='SPA-La Liga').sum()} rows")
print("✓ Done!")
