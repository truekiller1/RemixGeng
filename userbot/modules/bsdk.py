ported from X-TRA-TELEGRAM by @sudo_zeref

import random, re
import asyncio
from telethon import events
from userbot.events import register
from asyncio import sleep
import time
from userbot import CMD_HELP


@register(pattern=".bhsdk")

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1.5

    animation_ttl = range(0, 103)

    #input_str = event.pattern_match.group(1)

    #if input_str == "bhsdk":

    await event.edit("Abe lawde apna kaam kr")

    animation_chars = [

            "Bhsdk gaand",

            "Maardunga",

            "Tab",

            "Maanega",

            "Kya",

            "Maiya",

            "Chodu",

            "Saala",

            "Nikal",

            "Lawde",
        
            "Bhsdk gaand Mardunga Tab Maanega Kya Maiya Chodu Saala Nikal Lawde"

        ]

    for i in animation_ttl:
        
        await asyncio.sleep(animation_interval)
        
        await event.edit(animation_chars[i % 103])

CMD_HELP.update({
  "bhsdk":
   "`.bhsdk`\
\nUsage: This is a very good plugin to abuse someone."
})            
