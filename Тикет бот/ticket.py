import discord
from discord import app_commands, utils



class ticket_launcher(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)

    @discord.ui.button(label = "Создать тикет", style = discord.ButtonStyle.green, custom_id = "ticket_button")
    async def ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
            ticket = utils.get(interaction.guild.text_channels, name = f"тикет-для-{interaction.user.name.lower().replace(' ', '-')}-{interaction.user.discriminator}")
            if ticket is not None: await interaction.response.send_message(f"тикет открыт {ticket.mention}!", ephemeral = True)
	    else:
		if type(client.ticket_mod) is not discord.Role:
			client.ticket_mod = interaction.guild.get_role(id модератора)
		overwrites = {
			interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
			interaction.user: discord.PermissionOverwrite(view_channel = True, read_message_history = True, send_messages = True, attach_files = True, embed_links = True),
			interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True),
			client.ticket_mod: discord.PermissionOverwrite(view_channel = True, read_message_history = True, send_messages = True, attach_files = True, embed_links = True),
			}
			try:
				channel = await interaction.guild.create_text_channel(name = f'тикет-для-{interaction.user.name}-{interaction.user.discriminator}', overwrites = overwrites, reason = f'Тикет для {interaction.user}')
			except:
				return await interaction.response.send_message('Ошибка', ephemeral = True)
			
			await channel.send(f"{client.ticket_mod.mention},{interaction.user.mention} тикет создан!", view = closes())
			await interaction.response.send_message(f'Я открыл тикет для вас {channel.mention}', ephemeral = True)


class confirm(discord.ui.View):
	def __init__(self) -> None:
		super().__init__(timeout = None)

	@discord.ui.button(label = 'Подтвердить', style = discord.ButtonStyle.red, custom_id = 'confirm')
	async def confirm_button(self, interaction: discord.Interaction, button: discord.ui.Button):
		try: await interaction.channel.delete()
		except: await interaction.response.send_message('Ошибка', ephemeral = True)


class closes(discord.ui.View):
	def __init__(self) -> None:
		super().__init__(timeout = None)

	@discord.ui.button(label = 'Закрыть', style = discord.ButtonStyle.red, custom_id = 'close')
	async def close(self, interaction: discord.Interaction, button: discord.ui.Button):
		embed = discord.Embed(title = 'Вы уверены, что хотите закрыть этот тикет?', color = discord.Colour.blurple())
		await interaction.response.send_message(embed = embed, view = confirm(), ephemeral = True)



class aclient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents = intents)
        self.synced = False
        self.added = False
	self.ticket_mod = id модератора

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id=server_id))
            self.synced = True
        if not self.added:
            self.add_view(ticket_launcher())
            self.added = True


client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(guild = discord.Object(id=server_id), name = 'Название', description='Текст с объяснением команды')
async def ticketing(interaction: discord.Interaction):
    embed = discord.Embed(title = "Текст, который будет показываться выше кнопки", color = discord.Colour.blue())
    await interaction.channel.send(embed = embed, view = ticket_launcher())
    await interaction.response.send_message("Система запускается", ephemeral = True)

@tree.command(guild = discord.Object(id = server_id), name = 'close', description = 'Данная команда закрывает тикет')
async def closee(interaction: discord.Interaction):
	if 'тикет-для-' in interaction.channel.name:
		embed = discord.Embed(title = 'Вы уверены, что хотите закрыть этот тикет?', color = discord.Colour.blurple())

		await interaction.response.send_message(embed = embed, view = confirm(), ephemeral = True)
	else:
		await interaction.response.send_message('Ошибка', ephemeral = True)

@tree.command(guild = discord.Object(id = server_id), name = 'add', description = 'Данная команда добавляет пользователя')
@app_commands.describe(user = 'пользователь+')
async def add(interaction: discord.Interaction, user: discord.Member):
    if "тикет-для-" in interaction.channel.name:
        await interaction.channel.set_permissions(user, view_channel = True, read_message_history = True, send_messages = True, attach_files = True, embed_links = True)
        await interaction.response.send_message(f"{user.mention} добавлен в **тикет** к{interaction.user.mention}")
    else: await interaction.response.send_message("Ошибка", ephemeral = True)


@tree.command(guild = discord.Object(id = server_id), name = 'remove', description = 'Данная команда удаляет пользователя')
@app_commands.describe(user = 'Пользователь -')
async def remove(interaction: discord.Interaction, user: discord.Member):
    if 'тикет-для-' in interaction.channel.name:
        if type(client.ticket_mod) is not discord.Role:client.ticket_mod = interaction.guild.get_role(ID модератора)
        
        if client.ticket_mod is not user.roles:
            await interaction.channel.set_permissions(user, overwrite = None)
            await interaction.response.send_message(f"{user.mention} был удалён из тикета", ephemeral = True)
        else:await interaction.response.send_message(f"{user.mention} Это модератор!", ephemeral=True)
    else:await interaction.response.send_message('Ошибка', ephemeral= True)

client.run('токен')
