import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the SQLite database
connection = sqlite3.connect("../NBA-Boxscore-Database.db")

# Check the connection with a small query
query_first_line = """
SELECT team, MP as 'minutes played'
FROM team_stats
LIMIT 1
"""
first_line_df = pd.read_sql_query(query_first_line, connection)
print(first_line_df.head())

# Suspended Players Query
query_suspended = """
SELECT
    player
FROM
    player_stats
WHERE
    MP = 'Player Suspended';
"""
ds_suspended = pd.read_sql_query(query_suspended, connection)
print(ds_suspended.head())

# Curry PIE Query
query_pie_curry = """
SELECT
    PIE
FROM
    player_stats
WHERE
    player = 'Stephen Curry';
"""
ds_pie_curry = pd.read_sql_query(query_pie_curry, connection)
print(ds_pie_curry.head())

# Performance: Scoring Category Query
query_score_category = """
SELECT
    player,
    team,
    CASE
        WHEN PTS < 10 THEN 'Low Scorer'
        WHEN PTS BETWEEN 10 AND 20 THEN 'Role Player'
        WHEN PTS BETWEEN 20 AND 30 THEN 'Starter'
        ELSE 'Star Player'
    END AS scoring_category
FROM
    player_stats
WHERE
    game_id = '131410290001';
"""
ds_score_category = pd.read_sql_query(query_score_category, connection)
print(ds_score_category.head())

# Plotting PIE distribution for Stephen Curry
plt.figure(figsize=(8, 4))
sns.histplot(ds_pie_curry['PIE'], bins=10, kde=True)
plt.title("Stephen Curry's PIE Distribution")
plt.xlabel('PIE')
plt.ylabel('Frequency')
plt.show()

# Plotting suspended players count
plt.figure(figsize=(6, 4))
ds_suspended['player'].value_counts().plot(kind='bar')
plt.title('Suspended Players Count')
plt.xlabel('Player')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Plotting scoring category distribution by team
pivot_df = ds_score_category.pivot_table(index='team', columns='scoring_category', aggfunc='size', fill_value=0)
pivot_df.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Number of Players in Each Scoring Category by Team')
plt.xlabel('Team')
plt.ylabel('Number of Players')
plt.legend(title='Scoring Category')
plt.xticks(rotation=45)
plt.show()

# Closing the connection
connection.close()
