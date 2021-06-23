import discord
from discord.ext import commands

from Utils.UserClass import UserClass as User

permission_message = ["Guest [Permission Level : 0]", "User [Permission Level : 1]", "Developer [Permission Level : 2]", "Owner [Permission Level : 3]"]
async def check_permission(ctx, level):
    now_user = User(ctx.author)
    if now_user.permission >= level:
        return False
    else:
        embed = discord.Embed(title=f"User Permission Error", color=0xff0000)
        if now_user.permission == 0 and level == 1:
            embed.add_field(name = "Suggestion", value = "//AcceptTerm으로 약관 동의를 하시면, 'User [Permission Level : 1]' 권한을 얻으실 수 있어요! 이 명령어를 실행 하실 수 있게 되는거에요!", inline = False)
        embed.add_field(name = "Your Permission", value = f"{str(permission_message[int(now_user.permission)])}", inline = True)
        embed.add_field(name = "Command Executable Permission", value = f"{str(permission_message[int(level)])}", inline = True)
        await ctx.reply(embed=embed, mention_author = False)        
        return True