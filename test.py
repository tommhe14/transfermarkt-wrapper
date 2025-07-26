from tmkt import TMKT

import asyncio
import json

tmkt = TMKT()

async def test():
    testRequest = await tmkt.league_search("premier league")
    print(json.dumps(testRequest, indent = 4))
    await tmkt.close()

asyncio.run(test())