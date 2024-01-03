import time
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='>', self_bot=True, help_command=None) #do not change anything here except the prefix

@bot.event
async def on_ready():
    print(f'Connected to Discord!')
    print(f'=' * 35)
    print(f'Username: {bot.user.name}')
    print(f'User ID: {bot.user.id}')
    print(f'=' * 35)
    print('Written by kevin')

@bot.command()
async def ping(ctx):
    start_time = time.time()
    sent_msg = await ctx.send("`Pinging...`", delete_after=1)
    end_time = time.time()
    response_time = round(end_time - start_time) * 1000 / 1000
    await ctx.reply(f'`Response time: {response_time}ms`')

@bot.command()
async def whois(ctx, member: discord.Member):
    #await ctx.reply(f'`Username: {member.name}\nUser ID: {member.id}\nJoined Discord: {member.created_at}\n`{member.avatar.url}') #without pfp because some servers block urls!
    await ctx.reply(f'`Username: {member.name}\nUser ID: {member.id}\nJoined Discord: {member.created_at}\n`')

@bot.command()
async def pfp(ctx, member: discord.Member):
    await ctx.send(f'{member.avatar.url}')

@bot.command()
async def spam(ctx, *, text):
    global spam_flag
    spam_flag = True
    await ctx.send("`Staring spam...`", delete_after=1)
    time.sleep(1) #increase upon rate limit :)
    while spam_flag:
        await ctx.send(text)

@bot.command()
async def stop(ctx):
    global spam_flag
    spam_flag = False
    await ctx.send("`Stopping spam...`", delete_after=1)

@bot.command()
async def help(ctx):
    await ctx.reply("`prefix: >\nping - show bot response time\nwhois - show member info\npfp - show user avatar\nspam - spam a message\nstop - stop spamming\nraid - start raid\nstopraid - stop raid`")

@bot.command()
async def raid(ctx):
    global raid_flag
    raid_flag = True
    await ctx.send("`Starting raid...`", delete_after=1)
    #time.sleep(1)
    while raid_flag:
        guild = ctx.guild
        message = "RAIDED BY GIH @everyone" #change this to your message
        channel_name = "raided-by-gih" #change this to your channel name
        await ctx.guild.create_text_channel(channel_name)
        await ctx.send(message)

@bot.command()
async def raidstop(ctx):
    global raid_flag
    raid_flag = False
    await ctx.send("`Stopping raid...`", delete_after=1)

bot.run("token") #where token is your user account token

