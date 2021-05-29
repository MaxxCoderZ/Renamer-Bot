import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
import json
import math
import os
import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
from pyrogram import filters
from pyrogram import Client as CoderzHEX
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant, UserBannedInChannel 


@CoderzHEX.on_message(pyrogram.filters.command(["start"]))
async def text(bot, update):
    if update.from_user.id in Config.BANNED_USERS:
        await update.reply_text("You are Banned")
        return
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text(" Sorry, You are **B A N N E D**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="**Please Join My Update Channel Before Using Me..**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        else:
            await update.reply_text(Translation.START_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton("Help", callback_data = "ghelp")
                ],
                [
                    InlineKeyboardButton('Support Channel', url='https://t.me/CoderzHEX'),
                    InlineKeyboardButton('Feedback', url='https://t.me/MaxxCoderZ')
                ],
                [
                    InlineKeyboardButton('Other Bots', url='https://t.me/CoderzHEX/65'),
                    InlineKeyboardButton('Source', url='https://t.me/MaxxCoderz/Renamer-Bot')
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )
            return 
