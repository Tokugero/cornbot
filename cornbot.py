#!/usr/bin/env python3
from discord.ext import commands
import asyncio
import os
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger('cornbot.main')

#EnvironmentLoaders
botToken = os.environ['DISCORD_BOT_ID']

#Initializing bot
description = '''CubeBot Commands'''
bot = commands.Bot(command_prefix='corn$', description=description)

@bot.event
async def on_ready():
    logger.info('Logged in as')
    logger.info(bot.user.name)
    logger.info(bot.user.id)
    logger.info('------')

@bot.event
async def on_message(message):
    if message.author.id == 293146019238117376:
        emoji = ":lennyface:484237136862904320"
        await message.add_reaction(emoji)

bot.run(botToken)
