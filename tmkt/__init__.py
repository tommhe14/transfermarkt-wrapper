from .api import TMKTAPIClient

from typing import Dict, Any, Optional

class TMKT:
    """Main Transfermarkt-Wrapper API wrapper interface"""
    
    def __init__(self):
        self._api = TMKTAPIClient()
    
    async def __aenter__(self):
        """Enter async context manager"""
        await self._api._ensure_session()  
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit async context manager"""
        await self._api.close()

    async def close(self):
        """Close context manager"""
        await self._api.close()

    async def get_player_transfers(self, playerId: int)  -> Dict[str, Any]:
        """
        Get a players full transfer history
        """
        return await self._api._get(f"/transfer/history/player/{playerId}")
    
    async def get_club_transfers(self, clubId: int)  -> Dict[str, Any]:
        """
        Get a clubs full transfer history
        """
        return await self._api._get(f"/transfer/history/club/{clubId}")
    
    async def get_competition_transfers(self, competitionId: str)  -> Dict[str, Any]:
        """
        Get a competitions full transfer history
        """
        return await self._api._get(f"/transfer/history/competition/{competitionId}")
    
    async def get_player(self, playerId: int)  -> Dict[str, Any]:
        """
        Get a players profile with general data.
        """
        return await self._api._get(f"/player/{playerId}")
    
    async def get_club(self, clubId: int)  -> Dict[str, Any]:
        """
        Get a clubs profile with general data.
        """
        return await self._api._get(f"/club/{clubId}")
    
    async def get_competition(self, competitionId: str)  -> Dict[str, Any]:
        """
        Get a competitions profile with general data.
        """
        return await self._api._get(f"/competition/{competitionId}")
    
    async def get_player_injuries(self, playerId: int)  -> Dict[str, Any]:
        """
        Get a players full injury list.
        """
        return await self._api._get(f"/player/{playerId}/injury")
    
    async def get_club_stadium(self, clubId: int)  -> Dict[str, Any]:
        """
        Get a clubs stadium basic info
        """
        return await self._api._get(f"/club/{clubId}/stadium")
    
    async def get_competition_clubs(self, competitionId: str)  -> Dict[str, Any]:
        """
        Get a competitions list of clubs
        """
        return await self._api._get(f"/competition/{competitionId}/club")
    
    async def get_competition_table(self, competitionId: str)  -> Dict[str, Any]:
        """
        Get a clubs table standings.
        """
        return await self._api._get(f"/competition/{competitionId}/table")
    
    async def get_club_squad(self, clubId: int)  -> Dict[str, Any]:
        """
        Get a clubs full squad
        """
        return await self._api._get(f"/club/{clubId}/squad")
    
    async def get_all_transfers(self)  -> Dict[str, Any]:
        """
        Get a recent transfers
        """
        return await self._api._secondary_get(f"/ceapi/LatestTransfers/list/all")
    
    async def team_search(self, query: str) -> Dict[str, Any]:
        """
        Search for a team by name (e.g., "Arsenal").
        Example URL: https://www.transfermarkt.co.uk/news/search?index=clubs_lang_new&q=arsenal
        """
        params = {
            "index": "clubs_lang_new",
            "q": query
        }
        return await self._api._secondary_get("/news/search", params=params)
    
    async def player_search(self, query: str) -> Dict[str, Any]:
        """
        Search for a player by name (e.g., "Saka").
        Example URL: https://www.transfermarkt.co.uk/spieler/searchSpielerDaten?q=saka
        """
        params = {
            "q": query
        }
        return await self._api._secondary_get("/spieler/searchSpielerDaten", params=params, clean_html_name=True)
    
    async def league_search(self, query: str) -> Dict[str, Any]:
        """
        Search for a league by name (e.g., "La Liga").
        Example URL: https://www.transfermarkt.co.uk/bundesliga/searchwettbewerb/wettbewerb/L1?q=la+liga
        """
        params = {
            "q": query
        }
        return await self._api._secondary_get("/bundesliga/searchwettbewerb/wettbewerb/L1", params=params, clean_html_name=True)
    
    async def get_player_stats(self, playerId: int, season: int = None) -> Dict[str, Any]:
        """
        Get a players stats for the current season or a specific season
        """
        url = f"/player/{playerId}/performance?season={season}" if season else f"/player/{playerId}/performance"
        return await self._api._get(url) 
    
    async def get_current_season(self, competitionId: str) -> int:
        """
        Get a competition's current season id to use elsewhere
        """
        leagueData = await self.get_competition(competitionId)

        if leagueData:
            return leagueData.get("data", {}).get("currentSeason", {}).get("id", None)
        
        return None
    
    async def get_match(self, matchId: int) -> Dict[str, Any]:
        """
        Get match details. Game actions are in German (DE) but can be easily translated 
        using a library such as deep-translator 
        """
        return await self._api._get(f"/game/{matchId}")