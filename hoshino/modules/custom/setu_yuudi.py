from hoshino import Service, Privilege as Priv
import os
from hoshino.util import FreqLimiter, DailyNumberLimiter
sv = Service('setu-yuudi', visible=False, enable_on_default=False,
             manage_priv=Priv.ADMIN)
_nlmt = DailyNumberLimiter(10)
_flmt = FreqLimiter(15)



def getsetu():
    return f'[CQ:image,cache=0,url=https://xn--bsr.art/p.jpg]'


@sv.on_rex(r'^(不够[涩瑟色]|[涩瑟色]图|来一?[点份张].*[涩瑟色]|再来[点份张]|看过了)', normalize=True)
async def pushsetu(bot, ctx, match):
    uid = ctx['user_id']
    if not _nlmt.check(uid):
        await bot.send(ctx, "您今天已经冲了10次了,明天再来冲吧！", at_sender=True)
        return
    if not _flmt.check(uid):
        await bot.send(ctx, '您冲得太快了，小心人没了！', at_sender=True)
        return
    _flmt.start_cd(uid)
    _nlmt.increase(uid)
    try:
        msg = getsetu()
        await bot.send(ctx, msg)
    except:
        await bot.send(ctx, '它担心你的身体所以不来了。')
        return
