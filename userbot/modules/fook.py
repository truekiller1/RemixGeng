# (c) @Unknown
# Original written by @Unknown edit by @sudo_zeref

from telethon import events
import asyncio
from collections import deque
from userbot.events import register

@register(outgoing=True, pattern="^.fook$")
async def fuck(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n╱┏━━━┓.. ┏┓╱┏┓╭━━━╮ ╱╱┏┓ `"
                     "`\n╱┃┏━━┛.. ┃┃╱┃┃┃╭━╮┃╱┃┃ `"
                     "`\n╱┃┗━┓╱.. ┃┃╱┃┃┃┃╱┗┛┃┃ `"
                     "`\n╱┃┏━┛╱...┃┃╱┃┃┃┃╱┏┓┃┃ `"
                     "`\n╱┃┃╱.╱.╱ ┃╰━╯┃┃╰━╯┃╱┃┃ `"
                     "`\n╱┗┛╱ ╱ ╱ ╰━━━╯╰━━━╯ ╱╱┗┛ `")
