import random


async def help_cmd(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, embed_color, guild_result, args, help_lc):
    try:
        subargs = args[1]
    except:
        subargs = None
    if subargs == None or subargs == "help":
        if localization[0] == "Russian":
            tips = [
                'С помощью Effective bot можно проводить голосования?',
                'Все наши ссылки находятся в `info`?',
                'Узнать погоду можно в `weather`?',
                'Просмотреть рандомные фото можно в `photo`? Вдруг пригодится поставить обои на свой рабочий стол?',
                'Поступили две новости в `=tnews`?',
            ]
        else:
            tips = [
                'All our links on `info` command',
                'Starting with Effective bot 01R8 (November 5, 2021), has it become possible to change prefixes, get experiences for messages, etc?'
            ]
        try:
            if guild_result[6] == botconfig['prefix']:
                custom_prefix = ""
            else:
                custom_prefix = " `" + guild_result[6] + "`"
            if custom_prefix is None:
                custom_prefix = ""
        except Exception as e:
            print(e)
            custom_prefix = ""
        lucky_num = random.randint(0, len(tips) - 1)
        help_content = discord.Embed(description=str(botconfig['name'] + localization[1][0][0]).format(botconfig['prefix'], custom_prefix, tips[lucky_num]),color=embed_color)
        help_content.add_field(name=str(localization[1][0][1][0]),value=str(localization[1][0][1][1]),inline=True)
        help_content.add_field(name=str(localization[1][0][2][0]),value=str(localization[1][0][2][1]),inline=True)
        help_content.add_field(name=str(localization[1][0][3][0]),value=str(localization[1][0][3][1]),inline=True)
        help_content.add_field(name=str(localization[1][0][4][0]),value=str(localization[1][0][4][1]),inline=True)
        help_content.set_footer(text='Ver. ' + botconfig['version'])
    else:
        if help_lc[subargs] != None:
            help_content = discord.Embed(title=str(help_lc[subargs]['title']), description=str(help_lc[subargs]['description']),color=embed_color)
        try:
            help_content.add_field(name=str(localization[1][0][6][0]),value=str(help_lc[subargs]['requirements']),inline=True)
        except:
            pass
        try:
            help_content.add_field(name=str(localization[1][0][6][1]),value=str(help_lc[subargs]['instruction']).format(guild_result[6]),inline=True)
        except:
            try:
                help_content.add_field(name=str(localization[1][0][6][1]),value=str(help_lc[subargs]['instruction']).format('='),inline=True)
            except:
                try:
                    help_content.add_field(name=str(localization[1][0][6][1]),value=str(help_lc[subargs]['instruction']),inline=True)
                except:
                    pass
        try:
            help_content.add_field(name=str(localization[1][0][6][2]),value=str(help_lc[subargs]['parameters']),inline=True)
        except:
            pass
    await message.channel.send(embed=help_content)

