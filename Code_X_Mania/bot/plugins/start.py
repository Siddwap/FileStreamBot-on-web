from Code_X_Mania.bot import StreamBot
from Code_X_Mania.vars import Var
from Code_X_Mania.utils.human_readable import humanbytes
from Code_X_Mania.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)
from pyshorteners import Shortener

def get_shortlink(url):
   shortlink = False 
   try:
      shortlink = Shortener().dagd.short(url)
   except Exception as err:
       print(err)
       pass
   return shortlink

@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="__𝓢𝓞𝓡𝓡𝓨, 𝓨𝓞𝓤 𝓐𝓡𝓔 𝓐𝓡𝓔 𝓑𝓐𝓝𝓝𝓔𝓓 𝓕𝓡𝓞𝓜 𝓤𝓢𝓘𝓝𝓖 𝓜𝓔. 𝓒ᴏɴᴛᴀᴄᴛ ᴛʜᴇ Owner__\n\n @Moksh_b658 **𝙃𝙚 𝙬𝙞𝙡𝙡 𝙝𝙚𝙡𝙥 𝙮𝙤𝙪**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>JOIN  CHANNEL TO USE ME 🔐</i>",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("JOIN🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>🤦🏻‍♂️ 𝐒𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠 𝐖𝐞𝐧𝐭 𝐖𝐫𝐨𝐧𝐠</i> <b> <a href='http://t.me/Moksh_b658'>CLICK HERE FOR SUPPORT </a></b>",
                    parse_mode="HTML",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text="""
<b>𝐀 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐅𝐢𝐥𝐞 𝐓𝐨 𝐋𝐢𝐧𝐤 𝐁𝐨𝐭 𝐖𝐢𝐭𝐡 𝐁𝐨𝐭𝐡 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 & 𝐒𝐭𝐫𝐞𝐚𝐦 𝐋𝐢𝐧𝐤 𝐒𝐮𝐩𝐩𝐨𝐫𝐭</b>\n
<b>𝐒𝐞𝐧𝐝 𝐚 𝐅𝐢𝐥𝐞 𝐨𝐫 𝐕𝐢𝐝𝐞𝐨 𝐚𝐧𝐝 𝐒𝐞𝐞 𝐌𝐲 𝐏𝐨𝐰𝐞𝐫 😅!</b>\n
<b>𝐂𝐥𝐢𝐜𝐤 𝐎𝐧 /help 𝐓𝐨 𝐆𝐞𝐭 𝐌𝐨𝐫𝐞 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 𝐚𝐛𝐨𝐮𝐭 𝐌𝐞</b>\n
<b><b>𝐈𝐭𝐬 𝐘𝐨𝐮𝐫 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐢𝐛𝐢𝐥𝐢𝐭𝐲 𝐭𝐨 𝐔𝐬𝐞 𝐓𝐡𝐞 𝐁𝐨𝐭 𝐖𝐢𝐬𝐞𝐥𝐲 𝐈 𝐃𝐨𝐧𝐭 𝐓𝐚𝐤𝐞 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐢𝐛𝐢𝐥𝐢𝐭𝐢𝐞𝐬 𝐨𝐟 𝐀𝐧𝐲 𝐕𝐨𝐢𝐥𝐚𝐭𝐢𝐨𝐧𝐬.</b>\n
<b>𝐖𝐚𝐫𝐧𝐢𝐧𝐠: 𝐃𝐨𝐧𝐭 𝐒𝐩𝐚𝐦 𝐌𝐲 𝐁𝐨𝐭 𝐁𝐲 𝐏𝐨𝐫𝐧</b>\n
<b>𝐌𝐚𝐢𝐧𝐭𝐚𝐢𝐧𝐞𝐝 𝐁𝐲: @GreyMatter_bots</b>""",
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup( [ [InlineKeyboardButton('Owner', url=f"https://t.me/Moksh_b658"),
                                                                                       InlineKeyboardButton('Follow Developer ', url='https://github.com/GreyMatter658') ] ]  ) )
                                                                                       
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ. Qᴜɪᴄᴋʟʏ ᴄᴏɴᴛᴀᴄᴛ** @Moksh_b658",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Pʟᴇᴀsᴇ Jᴏɪɴ  Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs Bᴏᴛ**!\n\n**Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ**!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Join Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ],
                            [
                                InlineKeyboardButton("🔄 Refresh / Try Again",
                                                     url=f"https://t.me/{Var.APP_NAME}.herokuapp.com/{usr_cmd}") # Chnage ur app name
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐌𝐞 𝐀𝐧𝐲 𝐅𝐢𝐥𝐞 𝐈 𝐖𝐢𝐥𝐥 𝐒𝐞𝐧𝐝 𝐘𝐨𝐮 𝐚 𝐃𝐢𝐫𝐞𝐜𝐭 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 & 𝐒𝐭𝐫𝐞𝐚𝐦 𝐋𝐢𝐧𝐤 𝐚𝐬 𝐒𝐨𝐨𝐧 𝐚𝐬 𝐏𝐨𝐬𝐬𝐢𝐛𝐥𝐞.\n\n 𝐅𝐨𝐫 𝐁𝐞𝐭𝐭𝐞𝐫 𝐒𝐩𝐞𝐞𝐝 𝐈 𝐖𝐢𝐥𝐥 𝐑𝐞𝐜𝐨𝐦𝐦𝐞𝐧𝐝 𝐘𝐨𝐮 𝐓𝐨 𝐔𝐬𝐞 𝐀𝐃𝐌 𝐨𝐫 𝐈𝐃𝐌 𝐀𝐩𝐩 𝐭𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐘𝐨𝐮𝐫 𝐅𝐢𝐥𝐞.\n\n 𝐌𝐚𝐢𝐧𝐭𝐚𝐢𝐧𝐞𝐝 𝐁𝐲 : @GreyMatter_bots",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = Var.URL + 'watch/' + str(log_msg.message_id)
        shortlink = get_shortlink(stream_link)
        if shortlink:
            stream_link = shortlink
        online_link = Var.URL + 'download/' + str(log_msg.message_id)
        shortlinka = get_shortlink(online_link)
        if shortlinka:
            online_link = shortlinka

        msg_text ="""
<i><u>𝐂𝐨𝐧𝐠𝐫𝐚𝐭𝐮𝐥𝐚𝐭𝐢𝐨𝐧𝐬 𝐘𝐨𝐮𝐫 𝐋𝐢𝐧𝐤 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 !</u></i>

<b>📂 𝐅𝐢𝐥𝐞 𝐍𝐚𝐦𝐞 :</b> <i>{}</i>

<b>⌛ 𝐅𝐢𝐥𝐞 𝐒𝐢𝐳𝐞 :</b> <i>{}</i>

<b>📥 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐋𝐢𝐧𝐤 :</b> <code>{}</code>

<b>🖥 𝐎𝐧𝐥𝐢𝐧𝐞 𝐒𝐭𝐫𝐞𝐚𝐦 𝐋𝐢𝐧𝐤 :</b> <code>{}</code>

<b>🚸 𝐒𝐩𝐞𝐜𝐢𝐚𝐥 𝐍𝐨𝐭𝐞 : 𝐋𝐈𝐍𝐊 𝐖𝐎𝐍'𝐓 𝐄𝐗𝐏𝐈𝐑𝐄 𝐔𝐍𝐓𝐈𝐋𝐋 𝐈 𝐃𝐄𝐋𝐄𝐓𝐄</b>

"""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, online_link, stream_link),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🖥STREAM", url=stream_link), #Stream Link
                                                InlineKeyboardButton('DOWNLOAD📥', url=online_link)]]) #Download Link
        )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ **\n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ FROM USING ᴍᴇ. Cᴏɴᴛᴀᴄᴛ ᴛʜᴇ Dᴇᴠᴇʟᴏᴘᴇʀ</i>",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Pʟᴇᴀsᴇ Jᴏɪɴ  Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs Bᴏᴛ!**\n\n__Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ!__",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐌𝐞 𝐀𝐧𝐲 𝐅𝐢𝐥𝐞 𝐈 𝐖𝐢𝐥𝐥 𝐒𝐞𝐧𝐝 𝐘𝐨𝐮 𝐚 𝐃𝐢𝐫𝐞𝐜𝐭 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 & 𝐒𝐭𝐫𝐞𝐚𝐦 𝐋𝐢𝐧𝐤 𝐚𝐬 𝐒𝐨𝐨𝐧 𝐚𝐬 𝐏𝐨𝐬𝐬𝐢𝐛𝐥𝐞.\n\n𝐅𝐨𝐫 𝐁𝐞𝐭𝐭𝐞𝐫 𝐒𝐩𝐞𝐞𝐝 𝐈 𝐖𝐢𝐥𝐥 𝐑𝐞𝐜𝐨𝐦𝐦𝐞𝐧𝐝 𝐘𝐨𝐮 𝐓𝐨 𝐔𝐬𝐞 𝐀𝐃𝐌 𝐨𝐫 𝐈𝐃𝐌 𝐀𝐩𝐩 𝐭𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐘𝐨𝐮𝐫 𝐅𝐢𝐥𝐞.\n\n𝐌𝐚𝐢𝐧𝐭𝐚𝐢𝐧𝐞𝐝 𝐁𝐲 : @GreyMatter_bots",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
   
    await message.reply_text(
       text="Send me any file/media from telegram, I'll provide external direct download link..",
            parse_mode="HTML",
            
          reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("😇Donate", url="https://t.me/greymatters_about/13")]
            ]
        )
    )
