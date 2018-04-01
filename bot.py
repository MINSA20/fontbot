# Font Bot created by exofeel

"""
This bot takes on the idea of my previous bot. Comicsans
and makes it bigger and better.
"""


# Clean up for open-sourcing

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import PIL
from PIL import Image, ImageDraw, ImageFont
import sys
import os

debug_mode = True
bot = commands.Bot(command_prefix='$')
module_check = 'PIL' in sys.modules
proceed_font = False

# PLEASE CREATE DIRECTORIES BEFORE RUNNING!

PATH_DIR = ""


"""
I have decided that having a paid bot isn't worth all the hassle. 
I will keep the bot for free. 
"""

plus_enabled = True

"""
Maybe later I'll make it open-source for new developers to use and learn from.
"""

client = discord.Client()
clear = os.system("clear")

@bot.event
async def on_ready():
    print("fontbot is good to go.")
    print("fontbot is running with the id: " + bot.user.id)


@bot.command(pass_context=True)
async def connected(ctx):
    servers = list(client.servers)
    await bot.say("connected on " + str(len(client.servers)))
    for x in range(len(servers)):
        print(' ' + servers[x-1].name)

@bot.command(pass_context=True)
async def font(ctx, message, fontrequest="comicsans", color_text="white", fontsize=42):
    text = message
    await bot.delete_message(ctx.message)
    try:
        # 30 max unless you want text running over
        if len(text) >= 38:
            await bot.say("I'm sorry that message is too long. **38** is maximum character count.")

        else:
            pass
            image = Image.open(IMG_OPEN_DIR)
            font = fontrequest
            path = PATH_DIR + "/fontbot/fonts/"
            from pathlib import Path
            font_check = Path(path + "{}.ttf".format(fontrequest))        
            if font_check.is_file():
                font_type = ImageFont.truetype(PATH_DIR + '/fontbot/fonts/{}.ttf'.format(font),fontsize)
                draw = ImageDraw.Draw(image)
                draw.text(xy=(5,5),text=text,fill=("{}".format(color_text)),font=font_type)
                import uuid
                filename = str(uuid.uuid4())
                image.save(PATH_DIR + 'fontbot/output/{}.png'.format(filename))
                await bot.say("{} says:".format(ctx.message.author.mention))
                path = PATH_DIR + 'fontbot/output/{}.png'.format(filename)
                await bot.send_file(ctx.message.channel, path)
            else:
                font_type = ImageFont.truetype(PATH_DIR + 'fontbot/fonts/downloaded_fonts/{}.ttf'.format(fontrequest),42)
                draw = ImageDraw.Draw(image)
                draw.text(xy=(5,5),text=text,fill=("{}".format(color_text)),font=font_type)
                import uuid
                filename = str(uuid.uuid4())
                image.save(PATH_DIR + 'fontbot/output/{}.png'.format(filename))
                await bot.say("{} says:".format(ctx.message.author.mention))
                path = PATH_DIR + 'fontbot/output/{}.png'.format(filename)
                await bot.send_file(ctx.message.channel, path)
                os.remove(path)
    except OSError as e:
        if debug_mode == True:
            await bot.say(e.strerror)
        await bot.say("**Uh oh!** The font ``{}`` is not a font or not installed.".format(fontrequest))
        await bot.say("See ``$fontbot_help`` on how to use fontbot")

@bot.command(pass_context=True)
async def install(ctx, ttf_file, name):
    await bot.delete_message(ctx.message)
    try:
        if name.isalpha() and len(name) <= 15:
            if plus_enabled == True:
                path = PATH_DIR + 'fontbot/fonts/downloaded_fonts/"
                from pathlib import Path
                font_check = Path(path + "{}.ttf".format(name))
                if font_check.is_file():
                    print("font already exists")
                    await bot.say("Looks like that font already exists! Change the name or use {} in the command.".format(name))
                else:
                    pass
                    import urllib.request
                    filename = path + "{}.ttf".format(name)
                    print("Downloading {}...".format(name))
                    urllib.request.urlretrieve(ttf_file, filename)
                    print("Downloaded {}".format(name))
                    await bot.say("**Congratulations!** The font {} has been successfully installed. To use do ``#font 'Message' {} Color``".format(name, name))
            else:
                await bot.say("**Sorry!** This feature requires the Plus version.")
        else:
            await bot.say("Sorry, font name must only contain only alphanumerical characters and be under 15 characters..")

    except OSError:
            await bot.say("Error encountered. (112)")
    

@bot.command(pass_context=True)
async def status(ctx):
    embed = discord.Embed(title="Current Status", description="for FontBot", color=0x9b9b9b)
    if debug_mode == True:
        embed.add_field(name="Debug Mode", value=":warning: Currently Active, I'm probably being worked on right now", inline=False)
    else:
        pass
    embed.add_field(name="Server Status", value=":white_check_mark: I'm currently connected to the server.", inline=False)
    if module_check == False:
        embed.add_field(name="Module Import Status", value=":no_entry: Modules are currently not active. Please contact @exofeel#5908!", inline=False)
    elif module_check == True:
        embed.add_field(name="Module Import Status", value=":white_check_mark: Modules are currently imported and running.", inline=False)       
    embed.add_field(name="Need any assistance?", value=":grey_question: DM @exofeel#5908 to ask any questions.", inline=False)
    embed.add_field(name="Bot Version", value="Current Bot Version: 2.5.8-beta", inline=False)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def fontbot_help(ctx):
    embed = discord.Embed(title="Quick guide on how to use fontbot!", colour=discord.Colour(0x9b9b9b), description="This should give you the low-down and in's and outs of using the bot.")

    embed.set_thumbnail(url="http://i68.tinypic.com/214gms.png")
    embed.set_footer(text="Fontbot 2.5.7-beta", icon_url="http://i68.tinypic.com/214gms.png")

    embed.add_field(name="Writing messages", value="If you want to write a message. It's simple.```\n$font 'Message' Fontname Color``` \nPlease note, the default colors and text can be changed. By using the command ```\nComing Soon!```")
    embed.add_field(name="Installing new fonts", value="You can also use new fonts as well. The great thing is that each server has it's own folder on my server. Meaning you can install personal or custom fonts. This also means you can use custom names! ```\n $install [linkto.ttf] nameOfFont``` \n Make sure it's a ``.ttf`` file. We **DO NOT SUPPORT ANY OTHER FORMAT**!. This isn't our fault.")
    embed.add_field(name="Checking the status of the bot", value="Sometimes, the bot can go down for numerous reasons. You can quickly check the status of the bot by doing ```$status```")
    embed.add_field(name="Any questions?", value="You're more than welcome. \n@exofeel_dev on Twiter", inline=True)
    embed.add_field(name="Would like to donate?", value="Thanks, but let me finish first ;)", inline=True)

    await bot.say(embed=embed)

"""
need to clean up

@bot.command(pass_context=True)
async def announcement(ctx, *, message: str):
    try:
        font_type = ImageFont.truetype(PATH_DIR + 'fontbot/fonts/unisans.otf',64)
        image = Image.open('/fontbot/mod_announcement.png')
        draw = ImageDraw.Draw(image)
        draw.text(xy=(61,141),text=message,fill=(137,255,111),font=font_type)
        import uuid
        filename = str(uuid.uuid4())
        image.save('/fontbot/output/mod_announcements/{}.png'.format(filename))
        path = '/fontbot/output/mod_announcements/{}.png'.format(filename)
        await bot.send_file(ctx.message.channel, path)
    except OSError:
        await bot.say(":warning: **OSError found. Please contact @exofeel**")
"""


"""
need to find a better way

@bot.command(pass_context=True)
async def fonts(ctx):
    import glob, os
    await bot.say("**Current Fonts Installed**")
    os.chdir(PATH_DIR + "fontbot/fonts/downloaded_fonts/")
    for file in glob.glob("*.ttf"):
        await bot.say(file)
"""

@bot.command(pass_context=True)
async def setup(ctx):
    guild = ctx.message.guild
    await guild.create_text_channel('cool-channel')
    await bot.say("Welcome to setup..")

bot.run('NDI1NjExODYyODY1MDg0NDE3.DZJ9ew.N0VwWMak6T4ecIR9JgzM4FnXymI')


