from bs4 import BeautifulSoup

from typing import Dict, Any, List

def _clean_transfermarkt_html(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Cleans Transfermarkt's HTML name fields while preserving IDs."""
    cleaned = []
    for item in items:
        if not isinstance(item.get("name"), str):
            cleaned.append(item)
            continue
            
        soup = BeautifulSoup(item["name"], "html.parser")
        
        if soup.find("img"):
            name = soup.find("img")["title"]
            country = soup.find("i").get_text(strip=True) if soup.find("i") else ""
            cleaned.append({
                "id": item["id"],
                "name": name,
                "country": country
            })
        
        else:
            name_div = soup.select_one("div[style*='float:left']")
            if name_div:
                name = name_div.get_text(" ", strip=True).split("\n")[0]
                club = name_div.find("i").get_text(strip=True) if name_div.find("i") else ""
                cleaned.append({
                    "id": item["id"],
                    "name": name,
                    "club": club
                })
        
    return cleaned