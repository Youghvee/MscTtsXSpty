# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from typing import Union

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP, HERE_JOIN
from AlexaMusic import app


@Client.on_message(filters.incoming & filters.private, group=-1)
async def here_join_channel(bot: Client, msg: Message):
    if not HERE_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(HERE_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + HERE_JOIN
            else:
                chat_info = await bot.get_chat(HERE_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"Anda harus bergabung [Saluran ini]({link}) Untuk menggunakan saya. Jika sudah bergabung /start !",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Join Channel", url=link)]]
                    ),
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"ɪ'ᴍ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ HERE_JOIN ᴄʜᴀᴛ : {HERE_JOIN} !")
        
def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
            InlineKeyboardButton(text=_["S_B_2"], callback_data="settings_helper"),
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"),
                InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}")]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}")]
            )
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [InlineKeyboardButton(text=_["S_B_8"], callback_data="settings_back_helper")]
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"),
                InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}")]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}")]
            )
    buttons.append(
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ]
    )
    if GITHUB_REPO and OWNER:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_7"], user_id=OWNER),
                InlineKeyboardButton(text=_["S_B_6"], url=f"{GITHUB_REPO}"),
            ]
        )
    else:
        if GITHUB_REPO:
            buttons.append(
                [
                    InlineKeyboardButton(text=_["S_B_6"], url=f"{GITHUB_REPO}"),
                ]
            )
        if OWNER:
            buttons.append(
                [
                    InlineKeyboardButton(text=_["S_B_7"], user_id=OWNER),
                ]
            )
    buttons.append([InlineKeyboardButton(text=_["ST_B_6"], callback_data="LG")])
    return buttons
