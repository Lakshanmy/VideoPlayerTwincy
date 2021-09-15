#!/usr/bin/env python3
# Copyright (C) @subinps
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaDocument
from plugins.controls import is_admin
from pyrogram import Client, filters
from utils import update, is_admin
from config import Config
from logger import LOGGER
import os

HOME_TEXT = "<b>Hey  [{}](tg://user?id={}) 🙋‍♂️\n\nIam A Bot Built To Play or Stream Videos In Telegram VoiceChats.\nI Can Stream Any YouTube Video Or A Telegram File Or Even A YouTube Live.</b>"
admin_filter=filters.create(is_admin) 

@Client.on_message(filters.command(['start']))
async def start(client, message):
    buttons = [
        [
            InlineKeyboardButton('⚙️ Update Channel', url='https://t.me/UnlimitedWorldTeam'),
            InlineKeyboardButton('🧩 Support Group', url='https://t.me/unlimitedworld_TM_group')
        ],
        [
            InlineKeyboardButton('👨🏼‍🦯 Help', callback_data='help'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command(["help"]))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton('⚙️ Update Channel', url='https://t.me/UnlimitedWorldTeam'),
            InlineKeyboardButton('🧩 Support Group', url='https://t.me/unlimitedworld_TM_group'),
        ]
        ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if Config.msg.get('help') is not None:
        await Config.msg['help'].delete()
    Config.msg['help'] = await message.reply_text(
        Config.HELP,
        reply_markup=reply_markup
        )
@Client.on_message(filters.command(['info']))
async def repo_(client, message):
    buttons = [
        [
            InlineKeyboardButton('🧩 Support Group', url='https://t.me/unlimitedworld_TM_group'),
            InlineKeyboardButton('⚙️ Update Channel', url='https://t.me/UnlimitedWorldTeam'),
            
        ],
    ]
    await message.reply("<b>Bla Bla Bla 😕, U can't play here, Go here -> @SSH_Store</b>", reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_message(filters.command(['restart', 'update']) & admin_filter)
async def update_handler(client, message):
    await message.reply("Updating and restarting the bot.")
    await update()

@Client.on_message(filters.command(['logs']) & admin_filter)
async def get_logs(client, message):
    logs=[]
    if os.path.exists("ffmpeg.txt"):
        logs.append(InputMediaDocument("ffmpeg.txt", caption="FFMPEG Logs"))
    if os.path.exists("ffmpeg.txt"):
        logs.append(InputMediaDocument("botlog.txt", caption="Bot Logs"))
    if logs:
        await message.reply_media_group(logs)
        logs.clear()
    else:
        await message.reply("No log files found.")
