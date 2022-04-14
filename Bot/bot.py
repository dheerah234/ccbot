
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ( CommandHandler, Filters, MessageHandler, Updater)
from message import Editmessage, Sendmessage, logger
from Checks.Altbalaji import altbalaji_helper
from Miscellaneous.Scraper import pastebin, text_scraper, throwbin, ghostbin
import os
import requests
import json
import math
from collections import OrderedDict


bot_token = os.environ.get('TG_BOT_TOKEN')
startmessage = [[
		InlineKeyboardButton(
			"Dev",
			url='https://t.me/asur_sinchan'
		),
        InlineKeyboardButton(
			"Channel",
			url='https://t.me/asurccworld'
		)
        ]]


def start(update, context):
    info = update.effective_user
    print(info)
    chat_id = info.id
    userid= info['username']
    text = f'Welcome @{userid}, to cc checker bot, to know more use /help  This bot is provided for educational use only, any misuse then you should be responsible.'
    Sendmessage(chat_id, text, reply_markup=InlineKeyboardMarkup(startmessage))
    return

    

#def combos_spilt(combos):
 ##   split = combos.split('\n')
#return split


def help(update, context):
    chat_id = update.message.chat_id
    text = "Available cmds available:\n /botinfo \n /bin \n /botcmds \n /help \n /botstart \n MORE WILL BE UPDATED SOON"
    Sendmessage(chat_id, text, reply_markup= InlineKeyboardMarkup(startmessage))
def botstart(update, context):
    chat_id = update.message.chat_id
    text = "Hey! I am a CC-Checker!"
    Sendmessage(chat_id, text)
def botcmds(update, context):
    chat_id = update.message.chat_id
    text = "Hey, welcome to this Bot! Below I show you all available commands: \n Bin lookup: /bin xxxxxx \n SK-Chck: /sk sk_live_xxxxxxxxxxx \n CC-Check:/chk xxxxxxxxxxxx|xx|xx|xxx"
    Sendmessage(chat_id, text)
def botinfo(update, context):
    chat_id = update.message.chat_id
    text = "Hey! I am a CC-Checker bot with a few extras. Send /botcmds for a list of all commands!"
    Sendmessage(chat_id, text)

def bin(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    chat_id = info.id
    userid= info['username']
    text =  update.message.text.split(' ', 1)
    if text[-1].isdigit():
        r = requests.get("https://lookup.binlist.net/" + str(text[1][:6]))
        url=r.text
        if len(url)>5:
             res=json.loads(url)
             ab=text[-1]

             if "bank" not in res:
                  res["bank"] = {'name': 'Unavailable'}

             if "country" not in res:
                  res["country"] = {'name': 'Unavailable' , "emoji": " " , "currency": "--"}

             elif "type" not in res:
                  res["type"] = "Unavailable"
	
             bb=res["scheme"]
             dia='✅'
             
             
             
             dd=res["type"]
            
             true,false=True,False
             
             dd=res["type"]
             p=("Valid Bin! {} \n ━━━━━━━━━━━━━━━  \n • Bin: {} \n • Country: {} {} \n • Bank: {} \n • Scheme: {} \n • Type: {} \n • Currency: {} \n━━━━━━━━━━━━━━━ \n 👤 Checked By: @ASURCCWORLDBOT\n Used By @{}")
             text=p.format(dia ,ab ,res["country"]["name"],res["country"]["emoji"],res["bank"]["name"],bb,dd,res["country"]["currency"],userid)
             Sendmessage(chat_id, text)
        else:
             wdia='❌'
             p = "Not Valid Bin!{} \n ━━━━━━━━━━━━━━━  \n • Bin: {} \n 👤 Checked By: @ASURCCWORLDBOT\n Used By @{}"
             text = p.format(wdia,ab,userid)
             Sendmessage(chat_id, text)
             
    else:
        wdia='❌'
        p = "Not Valid Bin!{} \n ━━━━━━━━━━━━━━━  \n • Bin: {} \n 👤 Checked By: @ASURCCWORLDBOT\n Used By @{}"
        text = p.format(wdia,ab,userid)
        Sendmessage(chat_id, text)

	
def scraperdfnc(update, context):
    msg = update.message.text
    status_msg = update.message
    chat_id = status_msg.chat_id
    try:
        if 'pastebin' in msg:
            link = msg.split(' ')[1]
            pastebin(chat_id,link)
        elif 'ghostbin' in msg:
            link = msg.split(' ')[1]
            ghostbin(chat_id,link)
        else:
            scrape_text = status_msg['reply_to_message']['text']
            text_scraper(chat_id, scrape_text)
    except:
        Sendmessage(chat_id, 'Only Supports pastebin, please check if you send paste bin link')

def main():
    updater = Updater(
        bot_token,
        use_context=True
    )
    dp = updater.dispatcher
    #dp.add_handler(MessageHandler(Filters.text & ~Filters.command, duty))
    dp.add_handler(CommandHandler("scrape", scraperdfnc))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("botinfo", botinfo))
    dp.add_handler(CommandHandler("botcmds", botcmds))
    dp.add_handler(CommandHandler("bin", bin))
    dp.add_handler(CommandHandler("botstart", botstart))
    logger.info("Bot Started!!!")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
