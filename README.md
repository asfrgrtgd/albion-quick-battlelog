# Albion Quick Battlelog

A simple tool to analyze Albion Online battle data using battle IDs.

## Overview

Albion Quick Battlelog fetches and analyzes battle data from the Albion Online API using battle IDs. It provides aggregated statistics for each guild involved in a battle, including:

- Number of kills
- Number of deaths
- Number of participating members
- List of participating members

## How to Find Battle IDs

1. Visit [Albion Battles](https://eu.albionbattles.com/)
2. Browse or search for the battle you're interested in
3. Click on the battle to open its details
4. Look at the URL in your browser's address bar. The battle ID is the numeric value in the URL
   - Example: In `https://eu.albionbattles.com/battles/44928871`, the battle ID is `44928871`
5. Copy this battle ID to use with this tool

## How to Use This Tool

1. Run the script by either:
   - Using Python: `python main.py`
   - Or by launching the executable: `main.exe`
2. When prompted, paste or type the battle ID you found
3. The tool will retrieve and analyze the battle data
4. Review the aggregated results showing guild performance
5. Choose whether to check another battle or exit the tool

## Example Usage

```
Enter Battle ID (e.g., 44928871): 44928871
===== Aggregated Results =====
Guild: ExampleGuild1
  Kills: 25
  Deaths: 10
  Members: 15
  Member List: Player1,Player2,Player3,...
----------------------------------------
Guild: ExampleGuild2
  Kills: 10
  Deaths: 25
  Members: 20
  Member List: PlayerA,PlayerB,PlayerC,...
----------------------------------------
Would you like to check another battle? (yes/no): 
```

## Requirements

If you want to run the script using `python main.py`:
- Python 3.6+
- Requests library (`pip install requests`)

If you're using the executable (`main.exe`), no additional requirements are needed.