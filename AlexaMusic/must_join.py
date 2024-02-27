from config import HERE_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def here_join_channel(bot: Client, msg: Message):
    if not HERE_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(HERE_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if HERE_JOIN.isalpha():
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
