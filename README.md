# TMKT - Transfermarkt API Wrapper

A Python wrapper for the Transfermarkt API, providing easy access to football (soccer) data including players, clubs, competitions, transfers, and more.

[![PyPI Downloads](https://static.pepy.tech/badge/transfermarkt-wrapper)](https://pepy.tech/projects/transfermarkt-wrapper)

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

## Complete API Reference

### Player Endpoints

| Method | Description | Example |
|--------|-------------|---------|
| `get_player(playerId: int)` | Get player profile | `get_player(433177)` |
| `get_player_transfers(playerId: int)` | Get player's transfer history | `get_player_transfers(433177)` |
| `get_player_injuries(playerId: int)` | Get player's injury history | `get_player_injuries(433177)` |
| `get_player_stats(playerId: int, season: int = None)` | Get player's seasonal stats | `get_player_stats(262749)` |
| `player_search(query: str)` | Search players by name | `player_search("Saka")` |

### Club Endpoints

| Method | Description | Example |
|--------|-------------|---------|
| `get_club(clubId: int)` | Get club profile | `get_club(11)` (Arsenal) |
| `get_club_transfers(clubId: int)` | Get club's transfer history | `get_club_transfers(11)` |
| `get_club_squad(clubId: int)` | Get current squad | `get_club_squad(11)` |
| `get_club_stadium(clubId: int)` | Get stadium info | `get_club_stadium(11)` |
| `team_search(query: str)` | Search clubs by name | `team_search("Arsenal")` |

### Competition Endpoints

| Method | Description | Example |
|--------|-------------|---------|
| `get_competition(competitionId: str)` | Get competition profile | `get_competition("GB1")` |
| `get_competition_transfers(competitionId: str)` | Get competition transfers | `get_competition_transfers("GB1")` |
| `get_competition_clubs(competitionId: str)` | Get participating clubs | `get_competition_clubs("GB1")` |
| `get_competition_table(competitionId: str)` | Get current standings | `get_competition_table("GB1")` |
| `get_current_season(competitionId: str)` | Get league current season | `get_current_season("GB1")` |
| `league_search(query: str)` | Search leagues by name | `league_search("Premier League")` |

### Match Endpoints

| Method | Description | Example |
|--------|-------------|---------|
| `get_match(matchId: int)` | Get match details | `get_match(4625790)` |

### General Endpoints

| Method | Description | Example |
|--------|-------------|---------|
| `get_all_transfers()` | Get latest transfers | `get_all_transfers()` |
