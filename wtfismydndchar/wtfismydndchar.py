import urllib
import re
import logging
import json
import random

from redbot.core import commands

log = logging.getLogger("red.burnacid.wtfismydndchar")

class Wtfismydndchar(commands.Cog):
    """Generates a random D&D Character idea"""

    @commands.command()
    async def wtfismydndchar(self, ctx):
        """Generates a random D&D Character idea"""
        
        with open('/data/cogs/CogManager/cogs/wtfismydndchar/wtfismydndchar.json') as f:
          j = json.load(f)

        header = random.choice(j['heading'])
        adjective = random.choice(j['adjective']).capitalize()
        race = random.choice(j['race'])
        dclass = random.choice(j['dclass'])
        location = random.choice(j['location'])
        backstory = random.choice(j['backstory'])

        # Your code will go here
        await ctx.send(header + ".\n"+ adjective +" "+ race +" "+ dclass +" from "+ location +" who "+ backstory +"")