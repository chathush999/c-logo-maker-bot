from main import app
import pyrogram
from pyrogram import filters, idle
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from main.logo import generate_logo

START = """
**start masege danna**

➤ Click /help Or The Button Below To Know How To Use Me
"""

HELP = """
**🖼 How To Use Me ?**

**To Make Logo -** `/logo Your Name`
**To Make Square Logo - ** `/logosq Your Name`

**♻️ Example:** 
`/logo TechZBots`
`/logosq TechZBots`
"""

# Commands
@app.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://telegra.ph/file/7a98ead33e7b99fd82cc7.jpg",caption=START,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Help", callback_data="help_menu"), InlineKeyboardButton(text="Repo", url="https://github.com/TechShreyash/TechZ-Logo-Maker-Bot")]]))

@app.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://telegra.ph/file/7a98ead33e7b99fd82cc7.jpg",caption=HELP,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Back", callback_data="start_menu")]]))

@app.on_message(filters.command("logo") & filters.incoming & filters.text & ~filters.forwarded & (
  filters.group | filters.private))
async def logo(bot, message):
  try:
    text = message.text.replace("logo","").replace("/","").replace("@TechZLogoMakerBot","").strip().upper()
    
    if text == "":
      return await message.reply_text(HELP)

    x = await message.reply_text("`🔍 Generating Logo For You...`")  
    logo = await generate_logo(text)

    if "telegra.ph" not in logo:
      return await x.edit("`❌ Something Went Wrong...`\n\nReport This Error In @TechZBots_Support")
      
    if "error" in logo:
      return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In @TechZBots_Support \n\n`{logo}`")
      
    await x.edit("`🔄 Done Generated... Now Sending You`")

    logo_id = logo.replace("https://telegra.ph//file/","").replace(".jpg","").strip()
    await message.reply_photo(logo,caption="**🖼 Logo Generated By @TechZLogoMakerBot**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Upload As File 📁", callback_data=f"flogo {logo_id}")]]))
    await x.delete()
  except FloodWait:
    pass
  except Exception as e:
    try:
      await x.delete()
    except:
      pass
    return await message.reply_text("`❌ Something Went Wrong...`\n\nReport This Error In @TechZBots_Support")

# Square Logo
@app.on_message(filters.command("logosq") & filters.incoming & filters.text & ~filters.forwarded & (
  filters.group | filters.private))
async def logo(bot, message):
  try:
    text = message.text.replace("logosq","").replace("/","").replace("@TechZLogoMakerBot","").strip().upper()
      
    if text == "":
      return await message.reply_text(HELP)
  
    x = await message.reply_text("`🔍 Generating Logo For You...`")  
    logo = await generate_logo(text,True)
  
    if "telegra.ph" not in logo:
      return await x.edit("`❌ Something Went Wrong...`\n\nReport This Error In @TechZBots_Support")
        
    if "error" in logo:
      return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In @TechZBots_Support \n\n`{logo}`")
      
    await x.edit("`🔄 Done Generated... Now Sending You`")
    
    logo_id = logo.replace("https://telegra.ph//file/","").replace(".jpg","").strip()
    
    await message.reply_photo(logo,caption="**🖼 Logo Generated By @TechZLogoMakerBot**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Upload As File 📁", callback_data=f"flogo {logo_id}")]]))
    await x.delete()
  except FloodWait:
    pass
  except Exception as e:
    try:
      await x.delete()
    except:
      pass
    return await message.reply_text("`❌ Something Went Wrong...`\n\nReport This Error In @TechZBots_Support")

# Callbacks
@app.on_callback_query(filters.regex("start_menu"))
async def start_menu(_,query):
  await query.answer()
  await query.message.edit(START,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Help", callback_data="help_menu"),InlineKeyboardButton(text="Repo", url="https://github.com/TechShreyash/TechZ-Logo-Maker-Bot")]]))

@app.on_callback_query(filters.regex("help_menu"))
async def help_menu(_,query):
  await query.answer()
  await query.message.edit(HELP,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Back", callback_data="start_menu")]]))

@app.on_callback_query(filters.regex("flogo"))
async def logo_doc(_,query):
  await query.answer()
  try:
    x = await query.message.reply_text("`🔄 Sending You The Logo As File`")
    await query.message.edit_reply_markup(reply_markup=None)
    link = "https://telegra.ph//file/" + query.data.replace("flogo","").strip() + ".jpg"
    await query.message.reply_document(link,caption="**🖼 Logo Generated By @TechZLogoMakerBot**")
  except FloodWait:
    pass
  except Exception as e:
    try:
      return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In @TechZBots_Support \n\n`{str(e)}`")
    except:
      return
    
  return await x.delete()
  

if __name__ == "__main__":
  print("==================================")
  print("[INFO]: LOGO MAKER BOT STARTED BOT SUCCESSFULLY")
  print("==========JOIN @TECHZBOTS=========")

  idle()
  print("[INFO]: LOGO MAKER BOT STOPPED")
