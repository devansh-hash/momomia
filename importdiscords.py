import discord
import os
from keep_alive import keep_alive
from discord.ext import commands
import random
# Set up the bot with a command prefix
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='', intents=intents)
@bot.command(name='hello')
async def opton(ctx):
    momo_facts = [
       "I'm a bot that can tell you about Momo's life and some facts about her. to open command menu type showcommands:\n"
        
    ]
    response = random.choice(momo_facts)
    await ctx.send(response)

@bot.command(name='showcommands')
async def option(ctx):
    momo_facts = [
       "I'm a bot that can tell you about Momo's life and some facts about her.here are some commands you can use:\n"
        "1.momo-facts: get a facts about momoslife\n"
        "2.momo-pic:get a picture of momo\n"
        "3.momo-video:get a video of momo\n:"
        "4.momo-recepie:to get a recepies for momo\n:"    
    ]
    response = random.choice(momo_facts)
    await ctx.send(response)
# Event triggered when the bot is ready
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command(name='momo-facts')
async def momo(ctx):
    momo_facts = [
        "Momos are a type of steamed dumpling that originated in Tibet."
        "Momos can be filled with various ingredients like meat, vegetables, and cheese."
        "Momos are often served with a spicy dipping sauce called achar."
        "Momos are popular in Nepal, India, Bhutan, and Tibet."
        "Fried momos are a popular variation of the traditional steamed momos."
    ]
    response = random.choice(momo_facts)
    await ctx.send(response)
    @bot.command(name='momo-recipe')
    async def momo_recipe(ctx):
        recipe = """
        Simple Momo Recipe
        Ingredients:
        - 2 cups flour
        - 1/2 lb ground meat (chicken, pork, or beef)
        - 1/2 cup finely chopped onions
        - 1/4 cup chopped cilantro
        - 1/4 cup finely chopped garlic
        - 1/4 cup finely chopped ginger
        - Salt and pepper to taste

        Instructions:
        1. Mix the flour with water to make a soft dough. Cover and let it rest for 30 minutes.
        2. In a bowl, combine the meat, onions, cilantro, garlic, ginger, salt, and pepper.
        3. Roll the dough into small circles and place a spoonful of filling in the center.
        4. Fold and pinch the edges to seal the momo.
        5. Steam the momos for 10-15 minutes until the dough is cooked through.
        6. Serve hot with achar or your favorite dipping sauce.
        """
        await ctx.send(recipe)

@bot.command(name='momo-pic')
async def momo_pic(ctx):
    momo_image_url = "https://images.news18.com/ibnkhabar/uploads/2021/05/momos.jpg"  # Replace with an actual image URL
    await ctx.send(momo_image_url)

@bot.command(name='momo-video')
async def momo_pic(ctx):
    momo_image_url = "https://youtu.be/xeOlriV6RIA?si=cZT3D92LYFXvlOle"  # Replace with an actual image URL
    await ctx.send(momo_image_url)


# Command to respond with "Momo!"
keep_alive()
# Start the bot with your token
bot.run('MTI3MTA5ODA2MDQ5NTI2MTc4OA.GPLxlN.CT10hBJfw-eAUCOBcIVWfCU0nInKzRxz7WWs6w')





