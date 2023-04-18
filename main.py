import discord
from discord.ext import commands 
from discord import ui
import os

client = commands.Bot(command_prefix = "/", intents = discord.Intents.all())

# CHANNEL_ID = hakoona mataata
# channel = client.get_channel(CHANNEL_ID)

# trying to set a case where if we send something other than /feedback or /bugreport
@client.event
async def on_message(message):
    if not message.author.bot:  # ignore messages sent by bots
        channel_id = jug.t.iti.h  # Replace with the ID of the channel where you want the bot to listen
        if message.channel.id == channel_id:
            # Check if the message is a command other than /feedback or /bugreport
            if message.content.startswith("/") and message.content not in ["/feedback", "/bugreport"]:
                response = "Grrrr! Gator here! Please use `/feedback` or `/bugreport`."
                await message.channel.send(response)
            else:
                # Respond to non-command messages
                response = "Grrrr! Gator here! Please use `/feedback` or `/bugreport`."
                await message.channel.send(response)

    await client.process_commands(message)  # process commands after checking the message





# # feedback modal
# class FeedbackModal(ui.Modal, title = "feedback/suggestion(s)"):
#   your_feedback = ui.TextInput(label="Enter your feedback/suggestion(s)", placeholder = "type in your feedback/suggestion(s) regarding community/user-experience...", style = discord.TextStyle.long)
#   async def on_submit(self, interaction: discord.Interaction):
#     await interaction.response.send_message(f"feedback/suggestion: {self.your_feedback}")

class FeedbackModal(ui.Modal, title="feedback/suggestion(s)"):

    your_feedback = ui.TextInput(
        label="Enter your feedback/suggestion(s)",
        placeholder="type in your feedback/suggestion(s) regarding community/user-experience...",
        style=discord.TextStyle.long
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer()
        channel = client.get_channel(san.tand.er.h)
        user = interaction.user
        await channel.send(f"{user.name} feedback/suggestion: {self.your_feedback}")


# reportbug modal
class ReportbugModal(ui.Modal, title = "bug-report regarding website/app"):
  your_bugreport = ui.TextInput(label="Enter the bug you encountered", placeholder = "bug you encountered...", style = discord.TextStyle.long)
  async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer()
        channel = client.get_channel(stan.dar.dcha.h)
        user = interaction.user
        await channel.send(f"{user.name} bug-report: {self.your_bugreport}")

# client = commands.Bot(command_prefix = "/", intents = discord.Intents.all())

@client.event
async def on_ready():
  await client.tree.sync()
  
@client.tree.command(name = "feedback")
async def feedback(interaction: discord.Interaction):
  await interaction.response.send_modal(FeedbackModal())

@client.tree.command(name = "bugreport")
async def bugreport(interaction: discord.Interaction):
  await interaction.response.send_modal(ReportbugModal())


# @client.command(aliases = ['hi'])
# async def hello(ctx):
#  await ctx.send("Hi there, Gator here for surveys. Use !feedback for feedbacks and !bugreport for... yeah you guessed it, bugreports.")

# @client.tree.command(name="feedback", description = "for feedbacks")
# async def feedback(interaction: discord.Interaction):
#   await interaction.response.send_message(content = "Hey")

@client.command()
async def licnepasahkciwnhoj(ctx):
  await ctx.send("Terminating the bot :(")
  await client.close()

client.run(os.getenv("TOKEN"))


