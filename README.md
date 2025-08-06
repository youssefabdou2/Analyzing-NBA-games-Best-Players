# Analyzing NBA Games: Best Players

This repository contains a Python script (`Analyzing_NBA_Games_Best_Players.py`) that connects to an NBA boxscore SQLite database and performs the following analyses:

- **Suspended Players**: Lists players marked as suspended.
- **Stephen Curry's PIE**: Retrieves and visualizes Stephen Curry's Player Impact Estimate (PIE).
- **Scoring Category**: Categorizes players based on points scored in a specific game.
- **Visualizations**: Generates plots for PIE distribution, suspended players count, and scoring category distribution by team.

## Requirements

- Python 3.x
- `pandas`
- `matplotlib`
- `seaborn`
- `sqlite3` (included with Python)

## Usage

1. Clone the repository.
2. Ensure the SQLite database (`NBA-Boxscore-Database.db`) is located relative to the script.
3. Install required packages:
   ```bash
   pip install pandas matplotlib seaborn
   ```
4. Run the analysis:
   ```bash
   python Analyzing_NBA_Games_Best_Players.py
   ```
