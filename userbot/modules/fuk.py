# (c) @Unknown
# Original written by @Unknown edit by @Unbornkiller

from telethon import events
import asyncio
from collections import deque
from userbot.events import register

@register(outgoing=True, pattern="^.fuk$")
async def fuck(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n╱┏━━━┓.. ┏┓╱┏┓╭━━━╮ ╱╱┏┓ `"
                     "`\n╱┃┏━━┛.. ┃┃╱┃┃┃╭━╮┃╱┃┃ `"
                     "`\n╱┃┗━┓╱.. ┃┃╱┃┃┃┃╱┗┛┃┃ `"
                     "`\n╱┃┏━┛╱...┃┃╱┃┃┃┃╱┏┓┃┃ `"
                     "`\n╱┃┃╱.╱.╱ ┃╰━╯┃┃╰━╯┃╱┃┃ `"
                     "`\n╱┗┛╱ ╱ ╱ ╰━━━╯╰━━━╯ ╱╱┗┛ `")
