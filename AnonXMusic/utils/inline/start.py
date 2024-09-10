from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app
from datetime import datetime as dt
from datetime import timedelta, tzinfo, datetime
import datetime
import random
import loging
def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        
        [InlineKeyboardButton(text=_["S_B_11"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_7"], url=config.UPSTREAM_REPO),
        ],
    ]
    return buttons

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Ayaz ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Başlanğıc Mesajı

@app.on_message(filters.command("start") & filters.private)
async def start(bot: Client, message: Message):
    chat_id = message.chat.id
    first_name = message.from_user.mention
    user_id = message.from_user.id

    
    users_collection.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "user_id": user_id,
                "first_name": first_name,
                "username": message.from_user.username
            }
        },
        upsert=True
    )

    await bot.send_message(LOG_CHANNEL, f"""
#ÖZELDEN START VERDİ#

🤖 **Kullanıcı:** {first_name}
📛 **Kullanıcı Adı:** @{message.from_user.username}
🆔 **Kullanıcı ID:** `{message.from_user.id}`
""")
    msg = await message.reply_text("✨ **Lütfen Bekleyin...**")
    await asyncio.sleep(2)
    await msg.delete()
    await bot.send_message(
        chat_id,
        start_message.format(message.from_user.mention, BOT_USERNAME),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 Komutlar", callback_data="cvv"),
                ],
                
            ]
        ),
        disable_web_page_preview=True,
    )   



@app.on_callback_query(filters.regex("cvv"))
async def handler(bot: Client, query: CallbackQuery):
    await query.edit_message_text(
        "✨ **Hadi komutlarımı görelim! Merak ettiğin butona tıkla ve komutları öğren.**👇",
        reply_markup=InlineKeyboardMarkup(
            [
                [    
                    InlineKeyboardButton(
                        "🏷️ Tag Komutları", callback_data="tagger"),
                    InlineKeyboardButton(
                       "🎮 Eğlence Komutları", callback_data="eglence")
                ],
                [
                    InlineKeyboardButton(
                        "⚙️ Extra Komutlar", callback_data="extra"),

                       
                    InlineKeyboardButton(
                        "❤️‍🔥 Geliştirici Komutları", callback_data="sahip"),
                        
                ],
                [
                    InlineKeyboardButton(
                        "🏠 Ana Menü", callback_data="start"
                    )
                        
                ]
            ]
        )
    )
    


@app.on_callback_query(filters.regex("tagger"))
async def handler(bot: Client, query: CallbackQuery):
    await query.edit_message_text(
        tagger_commands,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔙 Geri", callback_data="cvv"),
                    InlineKeyboardButton(
                        "🏠 Ana Menü", callback_data="start"
                    )
                        
                ],
            ],
        ),
    )




@app.on_callback_query(filters.regex("eglence"))
async def handler(bot: Client, query: CallbackQuery):
    await query.edit_message_text(
        eglence,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔙 Geri", callback_data="cvv"),
                    InlineKeyboardButton(
                        "🏠 Ana Menü", callback_data="start"
                    )
                        
                ],
            ],
        ),
    )
   


@app.on_callback_query(filters.regex("extra"))
async def handler(bot: Client, query: CallbackQuery):
    await query.edit_message_text(
        extra,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔙 Geri", callback_data="cvv"),
                    InlineKeyboardButton(
                        "🏠 Ana Menü", callback_data="start"
                    )
                ],
            ],
        ),
    )
    

@app.on_callback_query(filters.regex("sahip"))
async def handler(client: Client, query: CallbackQuery):
    if query.from_user.id != OWNER_ID:
        await query.answer("Sen Sahibim degilsin!!", show_alert=True)
        return
    else:
        await query.edit_message_text(
            adminkom,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🔙 Geri", callback_data="cvv"
                            ),
                        InlineKeyboardButton(
                            "🏠 Ana Menü", callback_data="start"
                        )
                    ]
                ]
            ),
            disable_web_page_preview=True,
        )


# Başlanğıc Button
@app.on_callback_query(filters.regex("start"))
async def _start(bot: Client, query: CallbackQuery):
    await query.edit_message_text(
        start_message.format(query.from_user.mention, BOT_USERNAME),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Komutlar", callback_data="cvv"
                    ),
                ],
                
                [
                    InlineKeyboardButton(
                        "❤️‍🔥 Geliştirici", user_id=OWNER_ID
                    ),
                ]
            ],
        ),
    )   



#--------------------------------------------------------------------------
