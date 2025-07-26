import aiohttp

from .utils import clean_html

from typing import Dict, Any, Optional

class TMKTAPIClient:
    def __init__(self):
        self.base_url = "https://tmapi-alpha.transfermarkt.technology"
        self.secondary_url = "https://www.transfermarkt.co.uk"
        self.headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9",
            "origin": "https://www.transfermarkt.co.uk",
            "referer": "https://www.transfermarkt.co.uk",
            "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
        self.session = None  

    async def _ensure_session(self):
        """Ensure we have an active session"""
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession(headers=self.headers)

    async def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Base request method"""
        await self._ensure_session()  
        
        url = f"{self.base_url}{endpoint}"
        try:
            async with self.session.get(url, params=params) as response:
                response.raise_for_status()
                return await response.json()
        except Exception as e:
            raise Exception(f"API request to {url} failed: {str(e)}")
        
    async def _secondary_get(
        self, 
        endpoint: str, 
        params: Optional[Dict[str, Any]] = None,
        clean_html_name: bool = False  
    ) -> Dict[str, Any]:
        """Fetches data and optionally cleans HTML names."""
        await self._ensure_session()
        url = f"{self.secondary_url}{endpoint}"
        
        try:
            async with self.session.get(url, params=params) as response:
                response.raise_for_status()
                data = await response.json()
                
                if clean_html_name and isinstance(data, list):
                    return clean_html._clean_transfermarkt_html(data)
                return data
        except Exception as e:
            raise Exception(f"Request to {url} failed: {str(e)}")

    async def close(self):
        """Close the session"""
        if self.session and not self.session.closed:
            await self.session.close()