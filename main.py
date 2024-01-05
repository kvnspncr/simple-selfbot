import time
import discord
from discord.ext import commands
import requests
bot = commands.Bot(command_prefix='>', self_bot=True, help_command=None)
token = "your_token_here"

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
    await ctx.message.delete()
    start_time = time.time()
    sent_msg = await ctx.send("`Pinging...`", delete_after=1)
    end_time = time.time()
    response_time = round((end_time - start_time) * 1000)
    await ctx.send(f'`Response time: {response_time}ms`')

@bot.command()
async def whois(ctx, member: discord.Member):
    await ctx.message.delete()
    await ctx.send(f'`Username: {member.name}\nUser ID: {member.id}\nJoined Discord: {member.created_at}\n`')

@bot.command()
async def pfp(ctx, member: discord.Member):
    await ctx.message.delete()
    await ctx.send(f'{member.avatar.url}')

@bot.command()
async def spam(ctx, *, text):
    await ctx.message.delete()
    global spam_flag
    spam_flag = True
    await ctx.send("`Starting spam...`", delete_after=1)
    while spam_flag:
        await ctx.send(text)

@bot.command()
async def stop(ctx):
    await ctx.message.delete()
    global spam_flag
    spam_flag = False
    await ctx.send("`Stopping spam...`", delete_after=1)

@bot.command()
async def help(ctx):
    await ctx.send("`prefix: >\nping - show bot response time\nwhois - show member info\npfp - show user avatar\nspam - spam a message\nstop - stop spamming\nraid - start raid\nstopraid - stop raid\ntype - start typing forever\nstoptype - stop typing forever`")

@bot.command()
async def raid(ctx):
    await ctx.message.delete()
    global raid_flag
    raid_flag = True
    await ctx.send("`Starting raid...`", delete_after=1)
    while raid_flag:
        guild = ctx.guild
        try:
            #change these to your messages or whatever
            message = "RAIDED BY GIH @everyone"
            channel_name = "raided-by-gih"
            server_name = "RAIDED BY GIH"
            await ctx.guild.edit(name=server_name)
            await ctx.guild.create_text_channel(channel_name)
            await ctx.guild.create_text_channel(channel_name)
            await ctx.guild.create_text_channel(channel_name)
            await ctx.send(message)
            await ctx.send(message)
            await ctx.send(message)
        except discord.Forbidden:
            await ctx.send('`No perms`')
            break

@bot.command()
async def stopraid(ctx):
    await ctx.message.delete()
    global raid_flag
    raid_flag = False
    await ctx.send("`Stopping raid...`", delete_after=1)


@bot.command()
async def type(ctx):
    await ctx.message.delete()
    global type_flag
    type_flag = True
    #await ctx.send("`Typing forever...`", delete_after=1) #just verbose
    while type_flag:
            channel_id = ctx.channel.id
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Authorization': f'{token}',
                'X-Discord-Locale': 'en-US',
                'X-Discord-Timezone': 'UTC',
                'X-Debug-Options': 'bugReporterEnabled',
                'Origin': 'https://discord.com',
                'DNT': '1',
                'Sec-GPC': '1',
                'Connection': 'keep-alive',
                'Referer': f'https://discord.com/channels/{ctx.guild.id}/{channel_id}',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Content-Length': '0',
                'TE': 'trailers'
            }

            requests.post(f'https://discord.com/api/v9/channels/{channel_id}/typing', headers=headers)
            #time.sleep(7) #rate limit? uncomment

@bot.command()
async def stoptype(ctx):
    await ctx.message.delete()
    global type_flag
    type_flag = False
    #await ctx.send("`Not typing anymore...`", delete_after=1) #just verbose

bot.run(token)
