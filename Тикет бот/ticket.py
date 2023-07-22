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
                overwrites = {
                    interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
                    interaction.user: discord.PermissionOverwrite(view_channel = True, read_message_history = True, send_messages = True, attach_files = True, embed_links = True),
                    interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True), 
                }
                channel = await interaction.guild.create_text_channel(name = f"тикет-для-{interaction.user.name}-{interaction.user.discriminator}", overwrites=overwrites, reason = f"Тикет для {interaction.user}")
                await channel.send(f"{interaction.user.mention} Создан!")
                await interaction.response.send_message(f"Я открыл для вас тикет {channel.mention}!", ephemeral = True)


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
async def closee(interaction: discord.Interaction, role: discord.Role):
	if 'тикет-для-' in interaction.channel.name:
		embed = discord.Embed(title = 'Вы уверены, что хотите закрыть этот тикет?', color = discord.Colour.blurple())
		embed.set_footer(text = role.id)

		await interaction.response.send_message(embed = embed, view = confirm(), ephemeral = True)
	else:
		await interaction.response.send_message('Ошибка', ephemeral = True)


client.run('токен')
