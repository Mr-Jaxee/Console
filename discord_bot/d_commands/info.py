async def info_cmd(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, embed_color):
  info_content = discord.Embed(title=botconfig['name'], color=embed_color)
  info_content.add_field(name=str(localization[1][15][0]), value=str(localization[1][15][1]), inline=False)
  info_content.add_field(name=str(localization[1][15][2]), value=str("Python with discord.py library"), inline=True)
  info_content.add_field(name=str(localization[1][15][3]), value="Jaxee (`" + bot.get_user(int(botconfig['owner'])).name + "#" + str(bot.get_user(int(botconfig['owner'])).discriminator) + "`)", inline=True)
  if bot.user.id == 901352871071715408:
  	info_content.add_field(name=str(localization[1][15][4]), value=str(localization[1][15][5]), inline=True)
  info_content.set_footer(text="© Jaxee, 2021-2021")
  await message.channel.send(embed=info_content)