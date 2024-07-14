import discord 

from discord import app_commands, utils 
from discord.ext import commands 

class aclient(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents = intents)
        self.synced = False 
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id = id_servera))
            self.synced = True
            
client = aclient()            
tree = app_commands.CommandTree(client)
prefix = '/'


class choise(discord.ui.View):
    @discord.ui.button(label = "Принять", style = discord.ButtonStyle.success)
    async def button_success(self, interaction:discord.Interaction, button):
        if self.member == interaction.user:#Проверяет, какой пользователь нажимает кнопку.
            await interaction.response.send_message(f"{Fight_choice1.iuser.mention} Ты ходишь первым!", view = Fight_choice1(), delete_after= 5)#Через сколько секунд удалится это сообщение.
    @discord.ui.button(label = "Отказаться", style = discord.ButtonStyle.danger)
    async def button_danger(self, interaction:discord.Interaction, button):
        if self.member == interaction.user:#Проверяет, какой пользователь нажимает кнопку.
            await interaction.response.send_message(f"{choise.member.mention} отказался от игры!")
            
class Fight_choice1(discord.ui.View):#Ход первого игрока
    xod1 = ''
    @discord.ui.button(label = "Камень", style = discord.ButtonStyle.success)
    async def stone1(self, interaction:discord.Interaction, button):
        if Fight_choice1.iuser == interaction.user:
            Fight_choice1.xod1 = "stone"
            await interaction.response.send_message(f"{choise.member.mention} теперь твой ход", view = Fight_choise2(), delete_after = 5)
    @discord.ui.button(label = "Ножницы", style = discord.ButtonStyle.danger)
    async def nojn1(self, interaction:discord.Interaction, button):
        if Fight_choice1.iuser == interaction.user:
            Fight_choice1.xod1 = "nojn"
            await interaction.response.send_message(f"{choise.member.mention} теперь твой ход", view = Fight_choise2(), delete_after = 5)
    @discord.ui.button(label = "Бумага", style = discord.ButtonStyle.success)
    async def paper1(self, interaction:discord.Interaction, button):
        if Fight_choice1.iuser == interaction.user:
            Fight_choice1.xod1 = "paper"
            await interaction.response.send_message(f"{choise.member.mention} теперь твой ход", view = Fight_choise2(), delete_after = 5)
            
            
class Fight_choise2(discord.ui.View):#Ход второго игрока и результат.
    @discord.ui.button(label = "Камень", style = discord.ButtonStyle.success)
    async def stone2(self, interaction:discord.Interaction, button):
        if choise.member == interaction.user:
            if Fight_choice1.xod1 == "stone":
                await interaction.response.send_message(f"{Fight_choice1.iuser.mention} выбрал камень и {choise.member.mention} выбрал камень. НИЧЬЯ!", delete_after = 5)
        if choise.member == interaction.user:
            if Fight_choice1.xod1 == "nojn":
                await interaction.response.send_message(f"{Fight_choice1.iuser.mention} выбрал ножницы и {choise.member.mention} выбрал камень. Победил 2 игрок!", delete_after = 5)
        if choise.member == interaction.user:
            if Fight_choice1.xod1 == "paper":
                await interaction.response.send_message(f"{Fight_choice1.iuser.mention} выбрал бумагу и {choise.member.mention} выбрал камень. Победил 1 игрок!", delete_after = 5)
    @discord.ui.button(label = "Ножницы", style = discord.ButtonStyle.danger)
    async def nojn2(self, interaction:discord.Interaction, button):
        if choise.member == interaction.user:
            if Fight_choice1.xod1 == "stone":
                await interaction.response.send_message(f"{Fight_choice1.iuser.mention} выбрал камень и {choise.member.mention} выбрал ножницы. Победил 1 игрок!", delete_after = 5)
        if choise.member == interaction.user:
            if Fight_choice1.xod1 == "nojn":
                await interaction.response.send_message(f"{Fight_choice1.iuser.mention} выбрал ножницы и {choise.member.mention} выбрал ножницы. Ничья!", delete_after = 5)
        if choise.member == interaction.user:
            if Fight_choice1.xod1 == "paper":
                await interaction.response.send_message(f"{Fight_choice1.iuser.mention} выбрал бумагу и {choise.member.mention} выбрал ножницы. Победил 2 игрок!", delete_after = 5)
    @discord.ui.button(label = "Бумага", style = discord.ButtonStyle.blurple)
    async def paper2(self, interaction:discord.Interaction, button):
        if choise.member == interaction.user:
            if Fight_choice1.xod1 == "stone":
                await interaction.response.send_message(f"{Fight_choice1.iuser.mention} выбрал камень и {choise.member.mention} выбрал бумагу. Победил 2 игрок!", delete_after = 5)
        if choise.member == interaction.user:
            if Fight_choice1.xod1 == "nojn":
                await interaction.response.send_message(f"{Fight_choice1.iuser.mention} выбрал ножницы и {choise.member.mention} выбрал бумагу. Победил 1 игрок!", delete_after = 5)
        if choise.member == interaction.user:
            if Fight_choice1.xod1 == "paper":
                await interaction.response.send_message(f"{Fight_choice1.iuser.mention} выбрал бумагу и {choise.member.mention} выбрал бумагу. Ничья!", delete_after = 5)
                
    


@tree.command(guild = discord.Object(id = id_servera), name = 'rps', description = "камень, ножницы, бумага")
@app_commands.checks.cooldown(1, 30.0, key = lambda i: (i.guild_id, i.user.id))
async def invate(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(f"{interaction.user.mention} предлагает сыграть {member.mention} в камень, ножницы, бумагу!", view = choise(), delete_after=5)
    choise.member = member
    Fight_choice1.iuser = interaction.user
    



client.run('TOKEN')
