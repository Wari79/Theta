import discord
from discord.ext import commands
import os
import pickle
import random
import asyncio
import json
from discord.ext.commands import (
    has_permissions,
    MissingPermissions,
    has_role,
    MissingRole,
    cooldown,
    BucketType,
    NotOwner,
    CommandNotFound,
    MissingRequiredArgument,
)

arr = "<a:right:1028269253285122068>"
comp = "<a:upvote:1028269240844816505>"
sold = "<:Soldier_Buzz:966705306342129704>"
res = "<:Resources:994990321240912052>"
tank = "<:tank:994712805448093696>"
tank2 = "<:tank2:995097737974521948>"
hearts = ":helmet_with_cross:"
dead = "<:dead:1021894878294183987>"
wall = "<:wall:1006892740375760959>"
strike = "<:strike:1025877750298452028>" 
ca = "<:ca:1036338258629632020>"
crate = "<:crate:1036330635238842478>"
medal = "🏅"
spy = "🕵️"

warzone = "<#939972628205154327>"
data_filename4 = "currency files/specials"
data_filename5 = "currency files/medals"
data_filename2 = "currency files/data.pickle"
data_filename = "currency files/data.pickle2"
data_filename3 = "currency files/quest2"
data_filename6 = "currency files/counter"
green = 0x567d46
red = 0xFF0000
yellow = 0xFFD700

class Data:
      def __init__(self, resources, soldiers, tanks, spy, wall, strikes, mesg, s, r, scrap, crate, ca, medals, cfc, cfca):
        self.resources = resources
        self.soldiers = soldiers
        self.tanks = tanks
        self.spy = spy
        self.wall = wall
        self.strikes = strikes
        self.mesg = mesg
        self.s = s
        self.r = r
        self.crate = crate
        self.medals = medals
        self.scra = scrap
        self.ca = ca
        self.cfc = cfc
        self.cfca = cfca
        

class quest(commands.Cog):
    def __init__(self, client): 
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def add(self, ctx, amount, member:discord.Member):
      member_data = load_member_data(member.id)
      
      member_data.mesg += int(amount)
      save_member_data(member.id, member_data)
      sub = discord.Embed(description=f"Successfully added {amount} progress to {member.name}", color=green)
      sat = discord.Embed(description="Sorry for the inconvenience however due to data loss, you were given an aid to your on going `Quest 1`", color=red)
      await ctx.send(embed=sub)
      await member.send(embed=sat)

  
    @commands.command()
    @commands.is_owner()
    async def add_q2(self, ctx, amount, member:discord.Member=None):
      if member == None:
        member = ctx.author
      member_data3 = load_member_data3(member.id)
      
      member_data3.s += int(amount)
      save_member_data3(member.id, member_data3)
      sub = discord.Embed(description=f"Successfully added {amount} progress to {member.name}", color=green)
      sat = discord.Embed(description="Sorry for the inconvenience however due to data loss, you were given an aid to your on going `Quest 2`", color=red)
      await ctx.send(embed=sub)
      await member.send(embed=sat)

  
    @commands.command()
    @commands.is_owner()
    async def add_q3(self, ctx, amount, member:discord.Member=None):
      if member == None:
        member = ctx.author
      member_data3 = load_member_data3(member.id)
      
      member_data3.r += int(amount)
      save_member_data3(member.id, member_data3)
      sub = discord.Embed(description=f"Successfully added {amount} progress to {member.name}", color=green)
      sat = discord.Embed(description="Sorry for the inconvenience however due to data loss, you were given an aid to your on going `Quest 2`", color=red)
      await ctx.send(embed=sub)
      await member.send(embed=sat)


  
    @commands.command()
    @commands.is_owner()
    async def subtract_q3(self, ctx, amount, member:discord.Member=None):
      if member == None:
        member = ctx.author
      member_data3 = load_member_data3(member.id)
      member_data3.r -= int(amount)
      save_member_data3(member.id, member_data3)
      sub = discord.Embed(description=f"Successfully subtracted {amount} from {member.name}", color=red)
      await ctx.send(embed=sub)
      ss1 = discord.Embed(description=f"Commander, you were subtracted {amount} points in your on-going ` Quest 3 ` by the system operators.", color=yellow)
      await member.send(embed=ss1)

  
    @commands.command()
    @commands.is_owner()
    async def subtract_q2(self, ctx, amount, member:discord.Member=None):
      if member == None:
        member = ctx.author
      member_data3 = load_member_data3(member.id)
      member_data3.s -= int(amount)
      save_member_data3(member.id, member_data3)
      sub = discord.Embed(description=f"Successfully subtracted {amount} from {member.name}", color=red)
      await ctx.send(embed=sub)
      ss1 = discord.Embed(description=f"Commander, you were subtracted {amount} points in your on-going ` Quest 2 ` by the system operators.", color=yellow)
      await member.send(embed=ss1)


      

  
    @commands.command()
    @commands.is_owner()
    async def subtract_q1(self, ctx, amount, member:discord.Member):
      member_data = load_member_data(member.id)
      member_data.mesg -= int(amount)
      save_member_data(member.id, member_data)
      sub = discord.Embed(description=f"Successfully subtracted {amount} from {member.name}", color=red)
      await ctx.send(embed=sub)
      ss1 = discord.Embed(description=f"Commander, you were subtracted {amount} points in your on-going ` Quest 1 ` by the system operators.", color=yellow)
      await member.send(embed=ss1)





  
    @commands.Cog.listener()
    async def on_message(self, message):
      member_data2 = load_member_data2(message.author.id)
      member_data3 = load_member_data3(message.author.id)
      member_data6 = load_member_data6(message.author.id)
      if member_data3.s >= 150:
        with open("Quests/(B)quest.json") as json_file:
              data = json.load(json_file)
        try:
            if data["members"][str(message.author.id)]:
              pass
        except KeyError:
            imports = {
            "member": message.author.id, 
            "name": message.author.name,
            "checkability": "Completed"
            }
            data["members"][message.author.id] = imports
            with open("Quests/(B)quest.json", "w") as j:
              json.dump(data, j, indent=4)
            member_data2 = load_member_data2(message.author.id)
            member_data2.strikes += 4
            save_member_data2(message.author.id, member_data2)
            reward2 = discord.Embed(description=f"**Quest Completed**\n-\n> You recieved 4 {strike} for completing a quest.", color=green)
            await message.author.send(embed=reward2)
      else:
        pass

      if member_data3.r >= 150:
        with open("Quests/(C)quest.json") as json_file:
              data = json.load(json_file)
        try:
            if data["members"][str(message.author.id)]:
              pass
        except KeyError:
            imports = {
            "member": message.author.id, 
            "name": message.author.name,
            "checkability": "Completed"
            }
            data["members"][message.author.id] = imports
            with open("Quests/(C)quest.json", "w") as j:
              json.dump(data, j, indent=4)
            member_data2 = load_member_data2(message.author.id)
            member_data2.strikes += 2
            member_data2.wall += 2
            save_member_data2(message.author.id, member_data2)
            reward3 = discord.Embed(description=f"**Quest Completed**\n-\n> You recieved 2 {wall} & 2 {strike} for completing a quest.", color=green)
            await message.author.send(embed=reward3)
      else:
        pass
      if member_data6.cfca >= 3:
        with open("Quests/(D)quest.json") as json_file:
              data = json.load(json_file)
        try:
            if data["members"][str(message.author.id)]:
              pass
        except KeyError:
            imports = {
            "member": message.author.id, 
            "name": message.author.name,
            "checkability": "Completed"
            }
            data["members"][message.author.id] = imports
            with open("Quests/(D)quest.json", "w") as j:
              json.dump(data, j, indent=4)
            member_data2 = load_member_data2(message.author.id)
            member_data2.resources += 1750
            save_member_data2(message.author.id, member_data2)
            reward2 = discord.Embed(description=f"**Quest Completed**\n-\n> You recieved 1750 {res} for completing a quest.", color=green)
            await message.author.send(embed=reward2)


      

      if message.channel.id == 939972628205154327:
        member_data = load_member_data(message.author.id)
        member_data.mesg += 1
        save_member_data(message.author.id, member_data)
        if member_data.mesg >= 150:
          with open("Quests/(A)quest.json") as json_file:
              data = json.load(json_file)
          try:
            if data["members"][str(message.author.id)]:
              pass
          except KeyError:
            imports = {
            "member": message.author.id, 
            "name": message.author.name,
            "checkability": "Completed"
            }
            data["members"][message.author.id] = imports
            with open("Quests/(A)quest.json", "w") as j:
              json.dump(data, j, indent=4)
            member_data2 = load_member_data2(message.author.id)

            member_data2.resources += 2555
            save_member_data2(message.author.id, member_data2)
            reward = discord.Embed(description=f"**Quest Completed**\n-\n> You recieved 2555 {res} for completing a quest.", color=green)
            await message.author.send(embed=reward)

            return
        else:
          pass
      



  
    @commands.command()
    @commands.guild_only()
    async def view(self, ctx, quests=None):
      if quests != "quests":
        return
      member_data = load_member_data(ctx.author.id)
      member_data3 = load_member_data3(ctx.author.id)
      member_data6 = load_member_data6(ctx.author.id)



      #neither completed
      if member_data.mesg < 150 and member_data3.s < 150 and member_data3.r < 150 and member_data6.cfca < 3:
        progress1 = discord.Embed(title="Quests", description=f"> **Send 150 messages in <#939972628205154327>**\n{arr} ` {member_data.mesg}/150 `\nReward: 2555 {res}\n-\n> **Recruit soldiers 150 times**\n{arr} ` {member_data3.s}/150 `\nReward: 2 {strike}\n-\n> **Gain resources 150 times**\n{arr} ` {member_data3.r}/150 `\nReward: 2 {strike} & 2 {wall}\n-\n> **Strike 3 commanders using the special Combat Airstrike**\n{arr} ` {member_data6.cfca}/3 `\nReward: 1750 {res}", color=green)
        await ctx.reply(embed=progress1)
        return


      #resources completed
      if member_data.mesg < 150 and member_data3.s < 150 and member_data6.cfca < 3 and member_data3.r >= 150:
        progress1 = discord.Embed(title="Quests", description=f"> **Send 150 messages in <#939972628205154327>**\n{arr} ` {member_data.mesg}/150 `\nReward: 2555 {res}\n-\n> **Recruit soldiers 150 times**\n{arr} ` {member_data3.s}/150 `\nReward: 2 {strike}\n-\n> **Strike 3 commanders using the special Combat Airstrike**\n{arr} ` {member_data6.cfca}/3 `\nReward: 1750 {res}", color=green)
        await ctx.reply(embed=progress1)
        return



      #all completed
      if member_data.mesg >= 150 and member_data3.s >= 150 and member_data3.r >= 150 and member_data6.cfca >= 3:
        completed = discord.Embed(title="Quests", description=f"> **All Quests completed {comp}**", color=green)
        await ctx.reply(embed=completed)
        return
      
      #soldier completed
      if member_data.mesg < 150 and member_data3.r < 150 and member_data6.cfca < 3 and member_data3.s >= 150:
        progress1 = discord.Embed(title="Quests", description=f"> **Send 150 messages in <#939972628205154327>**\n{arr} ` {member_data.mesg}/150 `\nReward: 2555 {res}\n-\n> **Gain resources 150 times**\n{arr} ` {member_data3.r}/150 `\nReward: 2 {strike} & 2 {wall}\n-\n> **Strike 3 commanders using the special Combat Airstrike**\n{arr} ` {member_data6.cfca}/3 `\nReward: 1750 {res}", color=green)
        await ctx.reply(embed=progress1)
        return

      
      #message completed
      if member_data3.s < 150 and member_data3.r < 150 and member_data6.cfca < 3 and member_data.mesg >= 150:
        progress1 = discord.Embed(title="Quests", description=f"> **Recruit soldiers 150 times**\n{arr} ` {member_data3.s}/150 `\nReward: 4 {strike}\n-\n> **Gain resources 150 times**\n{arr} ` {member_data3.r}/150 `\nReward: 2 {strike} & 2 {wall}\n-\n> **Strike 3 commanders using the special Combat Airstrike**\n{arr} ` {member_data6.cfca}/3 `\nReward: 1750 {res}", color=green)
        await ctx.reply(embed=progress1)
        return

      #cfca completed
      if member_data3.s < 150 and member_data3.r < 150 and member_data.mesg < 150 and member_data6.cfca >= 3:
        progress1 = discord.Embed(title="Quests", description=f"> **Send 150 messages in <#939972628205154327>**\n{arr} ` {member_data.mesg}/150 `\nReward: 2555 {res}\n-\n> **Recruit soldiers 150 times**\n{arr} ` {member_data3.s}/150 `\nReward: 2 {strike}\n-\n> **Gain resources 150 times**\n{arr} ` {member_data3.r}/150 `\nReward: 2 {strike} & 2 {wall}", color=green)
        await ctx.reply(embed=progress1)
        return
        

        






















































def setup(client):
    client.add_cog(quest(client))   

def load_data():
        if os.path.isfile(data_filename):
            with open(data_filename, "rb") as file:
              return pickle.load(file)
        else:
            return dict()


def load_member_data(member_ID):
    data = load_data()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]

def save_member_data(member_ID, member_data):
    data = load_data()

    data[member_ID] = member_data

    with open(data_filename, "wb") as file:
        pickle.dump(data, file)

#--------------------------------------------------------

def load_data2():
        if os.path.isfile(data_filename2):
            with open(data_filename2, "rb") as file:
              return pickle.load(file)
        else:
            return dict()

def load_member_data2(member_ID):
    data = load_data2()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]


def save_member_data2(member_ID, member_data2):
    data = load_data2()

    data[member_ID] = member_data2

    with open(data_filename2, "wb") as file:
        pickle.dump(data, file)


#-------------------------------------------------------------

def load_data3():
        if os.path.isfile(data_filename3):
            with open(data_filename3, "rb") as file:
              return pickle.load(file)
        else:
            return dict()

def load_member_data3(member_ID):
    data = load_data3()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]


def save_member_data3(member_ID, member_data3):
    data = load_data3()

    data[member_ID] = member_data3

    with open(data_filename3, "wb") as file:
        pickle.dump(data, file)



#--------------------------------

def load_data4():
        if os.path.isfile(data_filename4):
            with open(data_filename4, "rb") as file:
              return pickle.load(file)
        else:
            return dict()

def load_member_data4(member_ID):
    data = load_data4()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]


def save_member_data4(member_ID, member_data4):
    data = load_data4()

    data[member_ID] = member_data4

    with open(data_filename4, "wb") as file:
        pickle.dump(data, file)




def load_data5():
        if os.path.isfile(data_filename5):
            with open(data_filename5, "rb") as file:
              return pickle.load(file)
        else:
            return dict()

def load_member_data5(member_ID):
    data = load_data5()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]


def save_member_data5(member_ID, member_data5):
    data = load_data5()

    data[member_ID] = member_data5

    with open(data_filename5, "wb") as file:
        pickle.dump(data, file)






def load_data6():
        if os.path.isfile(data_filename6):
            with open(data_filename6, "rb") as file:
              return pickle.load(file)
        else:
            return dict()

def load_member_data6(member_ID):
    data = load_data6()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]


def save_member_data6(member_ID, member_data6):
    data = load_data6()

    data[member_ID] = member_data6

    with open(data_filename6, "wb") as file:
        pickle.dump(data, file)