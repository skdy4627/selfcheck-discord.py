### import ###
import discord
import asyncio
import string
import random
from discord import activity
from discord.ext.commands.core import command
import hcskr
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.context import ComponentContext
from discord_slash.utils import manage_commands
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow
from discord_slash.model import ButtonStyle
from pymongo import MongoClient
from discordTogether import DiscordTogether

### basic setting ###
bot = commands.Bot(command_prefix="!", help_command=None, status=discord.Status.idle, activity=discord.Activity(name="", type=discord.ActivityType.listening))
slash = SlashCommand(bot, sync_commands=True)
togetherControl = DiscordTogether(bot)

### DB setting ###
con = MongoClient('mongodb://localhost:27017/')
user = con.user
user_users = user.users
num = con.num
num_nums = num.nums

### functions ###
color_green = 0x3CB371  # 그린
color_red = 0xB22222    # 레드
color_orange = 0xFF8C00 # 오렌지
color_yellow = 0xFFD700 # 옐로우
color_gray = 0x2F4F4F # 그레이
profile_img = "https://i.ibb.co/LxK0FF9/profile.jpg"

### bot.event ###
@bot.event
async def on_ready():
    print("               _  _              ")
    print("              | |(_)             ")
    print("  ___   _ __  | | _  _ __    ___ ")
    print(" / _ \\ | '_ \\ | || || '_ \\  / _ \\")
    print("| (_) || | | || || || | | | | __/")
    print(" \\___/ |_| |_||_||_||_| |_| \\___|")
    print(" ")

    try:
        num_nums.insert_one({
            "_id": "numid",
            "num": 0
        })
    except:
        return

### nomal command ###
@bot.command()
async def hellothisisverification(ctx):
    ctx.send("Think different#7777")


### slash commands ###
@slash.slash(name="핑", description="지연 시간을 표시합니다.")
async def ping(ctx: SlashContext):
    await ctx.send(f':ping_pong: `{round(bot.latency * 1000)}`ms')

@slash.slash(
    name="투게더",
    description="모두 같이 해보자.",
    options=[
        manage_commands.create_option(
            name="activity",
            description="수행할 동작을 알려줘.",
            option_type=int,
            required=True,
            choices=[
                manage_commands.create_choice(value=1, name="유튜브"),
                manage_commands.create_choice(value=2, name="포커"),
                manage_commands.create_choice(value=3, name="체스"), 
                manage_commands.create_choice(value=4, name="짭몽어스"),
                manage_commands.create_choice(value=5, name="낚시"),
            ],
        )
    ],
)
async def together(ctx: SlashContext, activity: int):
    if activity == 1:
        link = await togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
        await ctx.send(f"**Youtube Together** | 아래의 링크를 클릭해 주세요.\n{link}")
    elif activity == 2:
        link = await togetherControl.create_link(ctx.author.voice.channel.id, 'poker')
        await ctx.send(f"**Poker Night** | 아래의 링크를 클릭해 주세요.\n{link}")
    elif activity == 3:
        link = await togetherControl.create_link(ctx.author.voice.channel.id, 'chess')
        await ctx.send(f"**Chess in the Park | 아래의 링크를 클릭해 주세요.**\n{link}")
    elif activity == 4:
        link = await togetherControl.create_link(ctx.author.voice.channel.id, 'betrayal')
        await ctx.send(f"**Betrayal.io** | 아래의 링크를 클릭해 주세요.\n{link}")
    elif activity == 5:
        link = await togetherControl.create_link(ctx.author.voice.channel.id, 'fishing')
        await ctx.send(f"**Fishington.io | 아래의 링크를 클릭해 주세요.**\n{link}")

@slash.slash(
    name="자가진단",
    description="귀찮은 자가진단 맡겨봐.",
    options=[
        manage_commands.create_option(
            name="action",
            description="수행할 동작을 알려줘",
            option_type=int,
            required=True,
            choices=[
                manage_commands.create_choice(value=1, name="추가 - 설정을 원하신다면 선택 해주세요."),
                manage_commands.create_choice(value=2, name="삭제 - 설정 정보를 삭제하며 자동 자가진단을 이용할 수 없습니다."),
                manage_commands.create_choice(value=3, name="재설정 - 재설정하는 방법에 대해 안내합니다."),
            ],
        )
    ],
)
async def selfcheck(ctx: SlashContext, action: int):
    if action == 1:
        id = ctx.author.id
        if user_users.find_one({"_id": id}):
            await ctx.send("<:notice:872099950534742077> DM을 확인해 주세요.")
            await ctx.author.send(f"<@{id}>")

            await ctx.author.send("지역을 입력해 주세요.\n> Ex) 서울시")
            await asyncio.sleep(0.2)
            try: y_area = (await bot.wait_for('message', timeout = 30)).content
            except: return await ctx.author.send('> 30초가 지나서 비활성화 됐습니다.') 

            await ctx.author.send("학교 종류를 입력해 주세요.\n> Ex) 중학교")
            await asyncio.sleep(0.2)
            try: y_level = (await bot.wait_for('message', timeout = 20)).content
            except: return await ctx.author.send('> 20초가 지나서 비활성화 됐습니다.')

            await ctx.author.send("학교 이름을 입력해 주세요.\n> Ex) 백석중학교")
            await asyncio.sleep(0.2)
            try: y_schoolname = (await bot.wait_for('message', timeout = 20)).content
            except: return await ctx.author.send('> 20초가 지나서 비활성화 됐습니다.')
            
            await ctx.author.send("이름을 입력해주세요.\n> Ex) 고동현")
            await asyncio.sleep(0.2)
            try: y_name = (await bot.wait_for('message', timeout = 20)).content
            except: return await ctx.author.send('> 20초가 지나서 비활성화 됐습니다.')

            await ctx.author.send("생년월일을 입력해 주세요. (6자리)\n> Ex) 030817")
            await asyncio.sleep(0.2)
            try: y_birthday = (await bot.wait_for('message', timeout = 20)).content
            except: return await ctx.author.send('> 20초가 지나서 비활성화 됐습니다.')
            
            await ctx.author.send("__**자가진단 비밀번호**__를 입력해 주세요. (4자리)\n> Ex) 1234")
            await asyncio.sleep(0.2)
            try: y_password = (await bot.wait_for('message', timeout = 20)).content
            except: return await ctx.author.send('> 20초가 지나서 비활성화 됐습니다.')

            try:
                await hcskr.asyncSelfCheck(y_name, y_birthday, y_area, y_schoolname, y_level, y_password, "seewoo")

                embed=discord.Embed(color=color_gray)
                embed.set_author(name="테스트 진행.", icon_url=profile_img)
                embed.add_field(name="테스트", value="테스트로 자가진단을 실행했습니다. 잘 진행되었는지 확인해주세요.", inline=False)
                await ctx.author.send(embed=embed)

                find_data = {"_id": "numid"}
                set_data = {"$inc":{"num": 1}}
                num_nums.update_one(find_data, set_data)

                user_users.insert_one({
                    "_id": id,
                    "name": y_name,
                    "birthday": y_birthday,
                    "area": y_area,
                    "schoolname": y_schoolname,
                    "level": y_level,
                    "password": y_password
                })
                
                embed=discord.Embed(color=color_green)
                embed.set_author(name="정보 저장 완료.", icon_url=profile_img)
                embed.add_field(name="⚠️ 주의", value="테스트로한 자가진단이 안되었다면 `/자가진단 삭제` 후 3분 뒤에 다시 시도 해주세요.\n__**오류로 인해 자동 자가진단이 안되어도 책임지지 않습니다.**__\n(자가진단은 평일 오전 5시 부터 순차적으로 진행됩니다)", inline=False)
                embed.add_field(name="⚡ 정보 재설정 방법", value="`/자가진단` 명령어에서 `삭제`옵션을 골라 삭제 후 다시 추가 해야 합니다.", inline=False)
                await ctx.author.send(embed=embed)
            except:
                embed=discord.Embed(color=color_red)
                embed.set_author(name="잘못된 정보.", icon_url=profile_img)
                embed.add_field(name="⚠️ 자가진단 테스트 실패", value="입력한 값이 잘못되었는지 확인해 주세요.\n잘못된게 없다면 마지막 테스트 3분 뒤에 시도 해주세요. ", inline=False)
                await ctx.author.send(embed=embed)
                return

        else:
            await ctx.send("이미 가입 되어 있습니다.\n> 재설정을 원하신다면 옵션에서 `재설정`을 선택해주세요. ", hidden=True)

    elif action == 2:
        id = ctx.author.id
        if user_users.find_one({"_id": id}):
            await ctx.send("<:notice:872099950534742077> DM을 확인해 주세요.")
            await ctx.author.send(f"<@{id}>")

            _LENGTH=5
            string_pool = string.ascii_letters + string.digits
            result = ""
            for i in range(_LENGTH):
                result += random.choice(string_pool)

            embed=discord.Embed(color=color_gray)
            embed.set_author(name="자가진단 정보 삭제.", icon_url=profile_img)
            embed.add_field(name="🔒 삭제", value=f"정보를 삭제 하시려면 `{result}`를 입력해주세요.", inline=False)
            await ctx.author.send(embed=embed)

            await asyncio.sleep(0.2)

            try: answer = (await bot.wait_for('message', timeout = 20)).content
            except: return await ctx.author.send('> 20초가 지나서 비활성화 됐습니다.')
            if answer == result:
                find_data = {"_id": "numid"}
                set_data = {"$inc":{"num": -1}}
                num_nums.update_one(find_data, set_data)

                user_users.delete_one({"_id": id})
                embed=discord.Embed(color=color_green)
                embed.set_author(name="정보 삭제 완료.", icon_url=profile_img)
                await ctx.author.send(embed=embed)
            else:
                await ctx.author.send("잘못된 값 입니다. `/자가진단 삭제`로 다시 시도 해주세요.")
            
        else:
            await ctx.send("가입되어 있지 않습니다.\n> 옵션에서 `추가`를 선택해 추가해 주세요.", hidden=True)

    elif action == 3:
        embed=discord.Embed(color=color_gray)
        embed.set_author(name="정보 재설정 방법.", icon_url=profile_img)
        embed.add_field(name="⚡ 정보 재설정 방법", value="`/자가진단` 명령어에서 `삭제`옵션을 골라 삭제 후 다시 추가 해야 합니다.", inline=False)
        await ctx.send(embed=embed, hidden=True)
            
    else:
        await ctx.send("오류가 일어난거 같아 다시 시도 해줘.", hidden=True)
    

# @bot.event
# async def on_component(ctx: select):
#    # ctx.selected_options is a list of all the values the user selected
#    await ctx.send(content=f"You selected {ctx.selected_options}")
    

@slash.slash(name="도움말", description="나에 대해 알아봐.")
async def help(ctx: SlashContext):
    embed=discord.Embed(color=color_gray)
    embed.set_thumbnail(url="https://i.ibb.co/LxK0FF9/profile.jpg")
    embed.set_author(name="Project seewoo", icon_url=profile_img)
    embed.add_field(name="/자가진단", value="귀찮은 자가진단 맡겨봐.\n`options: 추가, 삭제, 재설정`", inline=False)
    embed.add_field(name="/핑", value="지연 시간을 표시합니다.", inline=False)
    await ctx.send(embed=embed)




bot.run(!!! your token !!!)
