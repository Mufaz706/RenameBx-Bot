class script(object):
    START_TEXT = """ A Simple File Renamer Bot With Permanent Thumbnail support!💯

<b>Send me any Telegram file and choose appropriate option! </b>
**👲 Maintained By** : [ᴍʜᴅ ᴍᴜꜰᴀᴢ](https://t.me/mufaz123)"""

    # Buttons
    buttons = [
        [
            InlineKeyboardButton('🤖 'Bot Updates, url=f"https://t.me/Bx_Botz")
        ]
    ]
    await m.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

    RENAME_403_ERR = "What Are You Doing? You are Banned"
    UPGRADE_TEXT = "CONTACT @mufaz123"
    DOWNLOAD_START = "Give Me Some Time..."
    UPLOAD_START = "Starting to upload..."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "**Thank you for Using Me > ©  @Bx_Botz **"
    SAVED_THUMB = "Thumbnail Saved ✅ This Is Permanent"
    DEL_THUMB = "Thumbnail cleared succesfully!"
    NO_THUMB = "No thumbnails found!"
    SAVED_RECVD_DOC_FILE = "File Downloaded Successfully 😎"
    CUSTOM_CAPTION_UL_FILE = " "
    HELP_USER = """It's not that complicated😅
    
1. Send me any Telegram File.
2. Choose appropriate option."""

