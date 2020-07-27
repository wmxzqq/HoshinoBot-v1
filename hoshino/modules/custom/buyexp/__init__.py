from hoshino import R, Service, Privilege as Priv
import pytz
from datetime import datetime


svcn = Service('buyexp-reminder-cn', manage_priv=Priv.ADMIN, enable_on_default=False)
svjp = Service('buyexp-reminder-jp', manage_priv=Priv.ADMIN, enable_on_default=False)


buyexpimg = R.img("priconne/买药小助手.jpg").cqcode



@svcn.scheduled_job('cron', hour='*/6', minute='0')
async def buyexp_cn():
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    if 0 == now.hour or 6 == now.hour:
        return  # 宵禁 免打扰
    await svcn.broadcast(f'{buyexpimg}', 'pcr-reminder-cn', 0.2)

@svjp.scheduled_job('cron', hour='5, 11, 17, 23', minute='0')
async def buyexp_jp():
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    if 23 == now.hour or 5 == now.hour:
        return  # 宵禁 免打扰
    await svjp.broadcast(f'{buyexpimg}', 'pcr-reminder-jp', 0.2)
