"""Shouts a message in MEME way
usage: .sos message
"""

import asyncio
import random
import re
import time

from collections import deque

import requests

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon import events

from uniborg.util import admin_cmd

@borg.on(admin_cmd("sos ?(.*)", outgoing=True))
async def king(e):
    await e.edit(
        "\n▒▒▒▒▒▒▒▒▒"
        "\n▒███████▒"
        "\n▒▒▒▒▒▒▒▒▒"
        "\n▒▒█████▒▒"
        "\n▒█▒▒▒▒▒█▒"
        "\n▒█▒▒▒▒▒█▒"
        "\n▒▒█████▒▒"
        "\n▒▒▒▒▒▒▒▒▒"
        "\n▒███████▒"
        "\n▒▒▒▒▒▒▒▒▒"
        "\n▒███████▒"
        "\n▒▒▒▒▒▒▒▒▒"
        "\n▒███████▒"
        "\n▒▒▒▒▒▒▒▒▒"
        "\n▒▒█████▒▒"
        "\n▒█▒▒▒▒▒█▒"
        "\n▒█▒▒▒▒▒█▒"
        "\n▒▒█████▒▒"
        "\n▒▒▒▒▒▒▒▒▒"
        "\n▒███████▒"
        "\n▒▒▒▒▒▒▒▒▒"
        "\n▒███████▒"
        "\n▒▒▒▒▒▒▒▒▒"
        "\n▒███████▒"
        "\n▒▒▒▒▒▒▒▒▒"
        "\n▒▒█████▒▒"
        "\n▒█▒▒▒▒▒█▒"
        "\n▒█▒▒▒▒▒█▒"
        "\n▒▒█████▒▒"
        "\n▒▒▒▒▒▒▒▒▒"
        "\n▒███████▒"
        "\n▒▒▒▒▒▒▒▒▒")
        
