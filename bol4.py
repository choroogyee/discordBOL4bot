import discord
import asyncio
import datetime
from datetime import date
import time
import bs4
from urllib.request import urlopen, Request
import urllib
import urllib.request
import random

intents = discord.Intents.default()
intents.members = True
client =  discord.Client(intents=intents)
botname = 'BOL4봇'
token = 'Your_token'
uptime = time.time()

@client.event
async def on_ready():
    bol4 = (date.today() - date(2016, 4, 22)).days

    print(client.user.name)
    print(client.user.id)

    server = len(client.guilds)
    users = 0
    for now_guild in client.guilds:
        users = users + len(now_guild.members)
    
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game('`볼사봇 도움말` 입력!'))
        await asyncio.sleep(10)
        await client.change_presence(status=discord.Status.online, activity=discord.Game('`볼사봇 도움` 으로도 확인가능!'))
        await asyncio.sleep(10)
        await client.change_presence(status=discord.Status.online, activity=discord.Game(str(server)+'개의 서버 | '+str(users)+'명의 유저'))
        await asyncio.sleep(10)
        await client.change_presence(status=discord.Status.online, activity=discord.Game('지금은 볼사가 데뷔한지 '+str(bol4)+'일째!'))
        await asyncio.sleep(10)

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith('볼사봇 도움말') or message.content.startswith('볼사봇 도움'):
        e = discord.Embed(title=botname+'의 도움말', description=botname+'의 기능을 알려드립니다.', color=0xffc0cb)
        e.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/180306_Bolbbalgan4_at_a_fansinging_%281%29.jpg/250px-180306_Bolbbalgan4_at_a_fansinging_%281%29.jpg')
        e.add_field(name='볼사봇 도움말/도움', value=botname+'의 기능을 알려드립니다.', inline=False)
        e.add_field(name='볼사봇 안지영/안졍/졍쓰', value='안지영의 정보를 알려드립니다.', inline=False)
        e.add_field(name='볼사봇 우지윤/우쥰/낯선아이', value='우지윤의 정보를 알려드립니다.', inline=False)
        e.add_field(name='볼사봇 볼빨간사춘기/볼사', value='볼빨간사춘기의 정보를 알려드립니다.', inline=False)
        e.add_field(name='볼사봇 정보', value='볼사봇의 정보를 보여줍니다.', inline=False)
        e.add_field(name='볼사봇 서버', value='볼사봇이 가입되어있는 서버 리스트를 알려드립니다.', inline=False)
        e.add_field(name='볼사봇 기능문의/오류제보', value='개발자에 연락처로 기능문의나 오류제보를 할 수 있습니다.', inline=False)
        e.add_field(name='볼사봇 랜덤사진/사진', value='볼빨간사춘기의 랜덤사진을 보여줍니다.', inline=False)
        e.add_field(name='볼사봇 초대/초대하기', value='볼사봇의 초대링크를 생성합니다.', inline=False)
        e.add_field(name='볼사봇 노래/노래추천', value='볼빨간사춘기의 노래를 랜덤으로 추천해줍니다. (커버곡, 참여곡 제외)', inline=False)
        e.set_footer(text='%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.author.send(embed=e)
        await message.channel.send('도움말을 DM으로 전송하였습니다.')
        print('%s#%s님이 도움말을 확인하였습니다.' % (message.author.name, message.author.discriminator))

    if message.content.startswith('볼사봇 안지영') or message.content.startswith('볼사봇 안졍') or message.content.startswith('볼사봇 졍쓰'):
        e = discord.Embed(title='안지영의 정보', description='안지영의 정보를 알려드립니다.', color=0xffc0cb)
        e.set_thumbnail(url='https://cdnweb01.wikitree.co.kr/webdata/editor/202004/02/img_20200402203302_0ab77b1b.webp')
        e.add_field(name='이름', value='안지영', inline=True)
        e.add_field(name='출생', value='1995년 9월 14일 (25세)\n경상북도 영주시', inline=True)
        e.add_field(name='국적', value='대한민국', inline=True)
        e.add_field(name='본관', value='순흥 안씨', inline=True)
        e.add_field(name='신체', value='165cm, 45kg, A형, 손 길이 17.5cm', inline=True)
        e.add_field(name='학력', value='영주동부초등학교\n동산여자중학교\n영주여자고등학교\n성신여자대학교', inline=True)
        e.add_field(name='소속그룹', value='볼빨간사춘기', inline=True)
        e.add_field(name='소속사', value='소파르뮤직', inline=True)
        e.add_field(name='데뷔', value='2016년 4월 22일\n볼빨간사춘기 EP엘범 RED lCKLE', inline=True)
        e.set_footer(text='%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)
        print('%s#%s님이 안지영의 정보를 확인하였습니다.' % (message.author.name, message.author.discriminator))

    if message.content.startswith('볼사봇 우지윤') or message.content.startswith('볼사봇 우쥰') or message.content.startswith('볼사봇 낯선아이'):
        e = discord.Embed(title='우지윤의 정보', description='우지윤의 정보를 알려드립니다.', colour=0xffc0cb)
        e.set_thumbnail(url='https://www.yeongnam.com/mnt/file/202006/20200619001337434_1.jpg')
        e.add_field(name='이름', value='우지윤', inline=True)
        e.add_field(name='예명', value='낯선아이', inline=True)
        e.add_field(name='출생', value='1966년 1월 6일 (25세)\n경상북도 영주시', inline=True)
        e.add_field(name='국적', value='대한민국', inline=True)
        e.add_field(name='신체', value='160cm, 44kg, A형', inline=True)
        e.add_field(name='소속사', value='ID:ODD', inline=True)
        e.add_field(name='데뷔', value='2016년 볼빨간사춘기 EP 앨범 RED lCKLE', inline=True)
        e.add_field(name='경력', value='볼빨간사춘기(2016년 4월 22일 ~ 2020년 4월 2일)', inline=True)
        e.add_field(name='종교', value='개신교', inline=True)
        e.set_footer(text='%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)
        print('%s#%s님이 우지윤의 정보를 확인하였습니다.' % (message.author.name, message.author.discriminator))

    if message.content.startswith('볼사봇 볼빨간사춘기') or message.content.startswith('볼사봇 볼사'):
        bol4 = (date.today() - date(2016, 4, 22)).days

        e = discord.Embed(title='볼빨간사춘기의 정보', description='볼빨간사춘기의 정보를 알려드립니다.', color=0xffc0cb)
        e.set_thumbnail(url='https://pds.joins.com/news/component/htmlphoto_mmdata/202004/02/4f5ea1bd-1e9c-466c-a735-d44a5f9dbc1d.jpg')
        e.add_field(name='그룹명', value='볼빨간사춘기', inline=True)
        e.add_field(name='멤버', value='안지영, 우지윤(탈퇴)', inline=True)
        e.add_field(name='결성 연도 및 지역', value='2011년, 경상북도 영주시', inline=True)
        e.add_field(name='데뷔', value='2016년 4월 22일 EP 앨범 RED lCKLE', inline=True)
        e.add_field(name='데뷔일', value='D+'+str(bol4), inline=True)
        e.add_field(name='팬덤', value='러볼리', inline=True)
        e.set_footer(text='%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)
        print('%s#%s님이 볼빨간사춘기의 정보를 확인하였습니다.' % (message.author.name, message.author.discriminator))

    if message.content == '볼사봇 정보':
        end = time.time()-uptime
        ut = int(end)
        min = int(ut/60)
        hour = int(min/60)
        day = str(int(hour/24))
        hour = str(hour%24)
        ut = str(ut%60)
        min = str(min%60)

        e=discord.Embed(title='볼사봇의 정보', description='볼사봇의 정보입니다.', color=0xffc0cb)
        e.add_field(name='업타임', value=day+'일 '+hour+'시간 '+min+'분 '+ut+'초', inline=True)
        e.add_field(name='Since', value='2021년 7월 4일', inline=True)
        e.add_field(name='자료 출처', value='나무위키 볼빨간사춘기, 안지영, 우지윤 문서', inline=True)
        e.add_field(name='개발자', value='초롱이#3632', inline=False)
        e.add_field(name='봇이름', value=botname, inline=True)
        e.set_thumbnail(url='https://i.ibb.co/4YfRj8r/profile.jpg')
        e.set_footer(text='%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)
        print('%s#%s님이 BOL4봇 정보를 확인하였습니다.' % (message.author.name, message.author.discriminator))

    if message.content == '볼사봇 서버':
        e = discord.Embed(title=botname+' 서버리스트', description=botname+'이 가입되어있는 서버 리스트입니다.', color=0xffc0cb)
        for i,s in enumerate(client.guilds):
            e.add_field(name=i+1, value=s.name, inline=False)
            e.set_footer(text='%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)
        print('%s#%s님이 BOL4봇이 가입되어있는 서버목록을 확인하였습니다.' % (message.author.name, message.author.discriminator))

    if message.content.startswith('볼사봇 기능문의') or message.content.startswith('볼사봇 오류제보'):
        e=discord.Embed(title='기능문의는 여기에!', description='기능뿐만 아니라 오류 제보도 부탁드려요.', color=0xffc0cb)
        e.add_field(name='개발자 디스코드', value='초롱이#3632', inline=False)
        e.add_field(name='개발자 카카오톡', value='Love_Bol4', inline=False)
        e.add_field(name='개발자 개인 페이스북', value='https://facebook.com/bakbugeun', inline=False)
        e.add_field(name='개발자 이메일', value='pbk050207@kakao.com', inline=False)
        e.set_footer(text='%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)
        await message.channel.send(':warning: 해당 개인정보를 기능문의나 오류제보가 아닌 타 목적으로 사용할 경우 법적으로 처벌받을수 있음을 안내드립니다. ')
        print('%s#%s님이 기능을 문의하였거나 오류를 제보하였습니다.' % (message.author.name, message.author.discriminator))

    if message.content.startswith('볼사봇 랜덤사진') or message.content.startswith('볼사봇 사진'):
        photo = ['https://i.ibb.co/TKx79hS/random-1.gif', 'https://i.ibb.co/NsMPTSG/random-1.jpg', 'https://i.ibb.co/QQ99dRc/random-1.jpg', 'https://i.ibb.co/Rb22ymS/random-1.jpg', 'https://i.ibb.co/KqgjfWM/random-2.jpg', 'https://i.ibb.co/nw42fxM/random-2.jpg', 'https://i.ibb.co/YBg7HFf/random-3.gif', 'https://i.ibb.co/1MXDySj/random-3.jpg', 'https://i.ibb.co/g752hJt/random-3.jpg', 'https://i.ibb.co/0VPbk0P/random-4.gif', 'https://i.ibb.co/njrJhtZ/random-4.jpg', 'https://i.ibb.co/x2f9qQF/random-4.jpg', 'https://i.ibb.co/F8ZZ7Fx/random-5.gif', 'https://i.ibb.co/Dk73ckR/random-5.jpg', 'https://i.ibb.co/M9RvsrK/random-5.jpg', 'https://i.ibb.co/dPJg3GT/random-6.gif', 'https://i.ibb.co/KqB2gtb/random-6.jpg', 'https://i.ibb.co/w4fm9rj/random-6.jpg', 'https://i.ibb.co/R485DZd/random-7.gif', 'https://i.ibb.co/t4wX3rx/random-7.jpg', 'https://i.ibb.co/CmL3yjw/random-7.jpg', 'https://i.ibb.co/Jjh8J0s/random-8.gif', 'https://i.ibb.co/dWpVmbk/random-8.jpg', 'https://i.ibb.co/52SGR3d/random-8.jpg', 'https://i.ibb.co/NYLx1v9/random-9.gif', 'https://i.ibb.co/Vms2Ygd/random-9.jpg', 'https://i.ibb.co/Xk31Bc4/random-10.gif', 'https://i.ibb.co/jbMC1hZ/random-10.jpg', 'https://i.ibb.co/vYRSBH8/random-11.gif', 'https://i.ibb.co/c1G9LhP/random-11.jpg', 'https://i.ibb.co/GpJNVt3/random-12.gif', 'https://i.ibb.co/s6tRNYF/random-12.jpg', 'https://i.ibb.co/r0cKn2y/random-13.gif', 'https://i.ibb.co/ZXswKkN/random-13.jpg', 'https://i.ibb.co/9G7Wcfh/random-14.gif', 'https://i.ibb.co/S3cYLz0/random-14.jpg', 'https://i.ibb.co/Y238rPD/random-15.gif', 'https://i.ibb.co/4YfRj8r/profile.jpg', 'https://i.ibb.co/x21zkDt/random-16.gif', 'https://i.ibb.co/djTF0dF/random-16.jpg', 'https://i.ibb.co/kS1vKYQ/random-17.gif', 'https://i.ibb.co/XDYKQ7c/random-17.jpg', 'https://i.ibb.co/GTpwc1K/random-18.jpg', 'https://i.ibb.co/zm093Ft/random-19.jpg', 'https://i.ibb.co/w4qnvBM/random-20.jpg', 'https://i.ibb.co/QK8kzZk/random-21.jpg', 'https://i.ibb.co/g6M7c5t/random-22.jpg', 'https://i.ibb.co/gDzLjxx/random-23.jpg', 'https://i.ibb.co/1fbj64j/random-24.jpg', 'https://i.ibb.co/hcJDnX7/random-25.jpg', 'https://i.ibb.co/txxdYRD/random-26.jpg', 'https://i.ibb.co/WvX0Ygc/random-27.jpg', 'https://i.ibb.co/NsWzsW8/random-28.jpg']
        photo2 = random.choice(photo)
        e=discord.Embed(title='볼빨간사춘기 랜덤사진', description='볼빨간사춘기 랜덤사진입니다.', color=0xffc0cb)
        e.set_image(url=photo2)
        e.set_footer(text='%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)
        await message.channel.send('추가하고 싶은 사진이 있으신분은 문의에 있는 연락처로 사진을 보낼시 검토후 반영하도록 하겠습니다.')
        print('%s#%s님이 볼빨간사춘기 랜덤사진 기능을 사용하였습니다.' % (message.author.name, message.author.discriminator))

    if message.content.startswith('볼사봇 초대') or message.content.startswith('볼사봇 초대하기'):
        e=discord.Embed(title='볼사봇 초대하기', description='볼사봇 초대는 여기서 하실수 있습니다.', color=0xffc0cb)
        e.add_field(name=botname+' 초대하기', value='https://url.kr/kzh6qo', inline=False)
        e.set_footer(text='%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)
        print('%s#%s님이 %s의 초대링크를 생성하였습니다.' % (message.author.name, message.author.discriminator, botname))
        
        
    if message.content.startswith('볼사봇 노래') or message.content.startswith('볼사봇 노래추천'):
        song = ['우주를 줄게', '싸운날', 'You(=I)', '심술', '나만 안되는 연애', '초콜릿', '프리지아', 'X Song', '반지', '사랑에 빠졌을때', '가끔식', '썸 탈꺼야', '고쳐주세요', '상상', '나의 사춘기에게', '바람사람', '여행', '야경', '안녕, 곰인형', 'Clip', 'Lonely', '나들이 갈까', '나만, 봄', '별 보러 갈래?', 'Seattle Alone', 'Mermaid', '워커홀릭', '25', 'Taste', '낮 (Day off)', 'XX (Acoustic Ver.)', '빈칸을 채워주시오', '품', '나비와 고양이 (Feat.백현 (BAEKHYUN))', '카운슬링', '민들레', '좋다고 말해', '남이 될 수 있을까', '#첫사랑', 'Dejavu', "6 o'clock", '빨간립스틱', 'Dancing Cartoon']
        song2 = random.choice(song)

        e=discord.Embed(title='볼빨간사춘기 노래추천', description='오늘은 이노래 어떠세요?', color=0xffc0cb)
        e.add_field(name='볼빨간사춘기 노래추천', value='볼빨간사춘기 - '+song2, inline=False)
        e.set_footer(text='%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)
        await message.channel.send('볼빨간사춘기 신곡이 나왔을경우 제보를 해주면 확인후 반영 하도록 하겠습니다. (커버곡, 참여곡 제외)')


    





client.run(token)
