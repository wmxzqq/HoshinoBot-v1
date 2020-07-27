###来自奇怪的雪雪

import requests
import os
import asyncio
import aiohttp
import re
from io import BytesIO
from PIL import Image
from hoshino.service import Service
from nonebot import on_command, CommandSession, MessageSegment, NoneBot



sv = Service('setu_xuexue', enable_on_default=False, visible=False)

##换成你的api
apikey=''
r18 = '0'
keyword = ''
num = '1'
size1200 = 'True'
apiPath=r'https://api.lolicon.app/setu'

params = {'apikey':apikey,'r18':r18,'keyword':keyword,'num':num,'size1200':size1200}

async def get_url():
    global params
    res = requests.get(apiPath,params = params,timeout=20)
    url = res.json()['data'][0]['url']
    return url

async def get_pic():
    url = await get_url()
    try:
        timeout = aiohttp.ClientTimeout(total=30)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as resp:
                content = await resp.read()
    ###根据你酷q和docker的共享目录的位置进行调整
                filePath = os.path.join('/root/coolq/setu','temp.jpg')
                with open(filePath,'wb') as f:
                    f.write(content)
                    f.close()
    except Exception as ex:
        print(ex)
    return 

@sv.on_rex(re.compile(r'不够[涩瑟色]|[涩瑟色]图|来一?[点份张].*[涩瑟色]|再来[点份张]|看过了|铜'), normalize=True)
async def send_pic(bot:NoneBot, ctx ,match):
    pic = await get_pic()
    ###根据你酷q和docker的共享目录的位置进行调整
    msg = MessageSegment.image('file:///Z:\\home\\user\\coolqpro\\setu\\temp.jpg')
    await bot.send(ctx,msg)

