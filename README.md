# Albion Quick Battlelog

A simple tool to analyze Albion Online battle data using battle IDs.

## Overview

Albion Quick Battlelog fetches and analyzes battle data from the Albion Online API using battle IDs. It provides aggregated statistics for each guild involved in battles, including:

- Number of kills
- Number of deaths
- Kill/Death ratio
- Number of participating members
- List of participating members

## Features

- Process single battle analysis
- Process and combine data from multiple battles at once
- Color-coded output for better readability
- Sorted results with top-performing guilds first

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
   - For multiple battles, enter IDs separated by spaces
3. The tool will retrieve and analyze the battle data
4. Review the aggregated results showing guild performance
5. Choose whether to check another battle or exit the tool

## Example Usage - Single Battle

```
Enter Battle ID(s) (space-separated for multiple battles): 44928871
Processing battle ID: 44928871

===== Battle Results =====

============================================================
Guild: ExampleGuild1
├─ Kills: 25
├─ Deaths: 10
├─ K/D Ratio: 2.50
├─ Members: 15
└─ Member List: Player1,Player2,Player3,...
------------------------------------------------------------
Guild: ExampleGuild2
├─ Kills: 10
├─ Deaths: 25
├─ K/D Ratio: 0.40
├─ Members: 20
└─ Member List: PlayerA,PlayerB,PlayerC,...
------------------------------------------------------------
Would you like to check another battle? (yes/no): 
```

## Example Usage - Multiple Battles

```
Enter Battle ID(s) (space-separated for multiple battles): 44928871 44928872
Processing battle ID: 44928871
Processing battle ID: 44928872

===== Combined Results from Multiple Battles =====

============================================================
Guild: ExampleGuild1
├─ Kills: 50
├─ Deaths: 22
├─ K/D Ratio: 2.27
├─ Members: 18
└─ Member List: Player1,Player2,Player3,...
------------------------------------------------------------
Guild: ExampleGuild2
├─ Kills: 22
├─ Deaths: 50
├─ K/D Ratio: 0.44
├─ Members: 25
└─ Member List: PlayerA,PlayerB,PlayerC,...
------------------------------------------------------------
Would you like to check another battle? (yes/no): 
```

## Requirements

If you want to run the script using `python main.py`:
- Python 3.6+
- Requests library (`pip install requests`)

If you're using the executable (`main.exe`), no additional requirements are needed.