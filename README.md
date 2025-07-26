# TMKT - Transfermarkt API Wrapper

A Python wrapper for the Transfermarkt API, providing easy access to football (soccer) data including players, clubs, competitions, transfers, and more.

## Features

- **Player Data**: Transfers, injuries, profiles
- **Club Data**: Squads, stadiums, transfers
- **Competition Data**: Tables, participating clubs
- **Search Functionality**: Players, clubs, leagues
- **Clean Data Parsing**: Automatic HTML-to-text conversion for search results

## Installation

```bash
pip install transfermarkt-wrapper
```

## Example usage

```py
from tmkt import TMKT
import asyncio

import json

async def main():
    async with TMKT() as tmkt:
        # Search for a league
        leagues = await tmkt.league_search("Premier League")
        print(json.dumps(leagues, indent = 4))

        # Get player data
        player = await tmkt.get_player(433177)  # Bukayo Saka
        print(json.dumps(player, indent = 4))

asyncio.run(main())
```