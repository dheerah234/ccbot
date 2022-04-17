
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ( CommandHandler, Filters, MessageHandler, Updater)
from message import Editmessage, Sendmessage, logger
from Miscellaneous.Scraper import pastebin, text_scraper, throwbin, ghostbin
import os
import requests
from bs4 import BeautifulSoup
import random
import string
import time
import json
import math
from collections import OrderedDict
sk_chg='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'
os.environ['TZ'] = 'America/Buenos_Aires'

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

#random str GEN FOR EMAIL
N = 10
rnd = ''.join(random.choices(string.ascii_lowercase +
                                string.digits, k = N))

def start(update, context):
    info = update.effective_user
    print(info)
    chat_id = info.id
    userid= info['username']
    text = f'Welcome @{userid}, to cc checker bot, to know more use /help  This bot is provided for educational use only, any misuse then you should be responsible.'
    Sendmessage(chat_id, text, reply_markup=InlineKeyboardMarkup(startmessage))
    return

    
####################################################################################################################################3
# help botstart botcmds botinfo bin

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
                  res["country"] = {"name": "Unavailable" , "emoji": " " , "currency": "--"}

             elif "type" not in res:
                  res["type"] = "Unavailable"
	
             bb=res["scheme"]
             dia='✅'
             
             
             
             dd=res["type"]
            
             true,false=True,False
             
             dd=res["type"]
             p=("Valid Bin! {} \n ━━━━━━━━━━━━━━━  \n • Bin: {} \n • Country: {} {} \n • Bank: {} \n • Scheme: {} \n • Type: {} \n • Currency: {} \n━━━━━━━━━━━━━━━ \n 👤 Checked By: @ASURCCWORLDBOT\n Used By @{}")
             text=p.format(dia ,ab[:6] ,res["country"]["name"],res["country"]["emoji"],res["bank"]["name"],bb,dd,res["country"]["currency"],userid)
             Sendmessage(chat_id, text)
        else:
             chat_id = update.message.chat_id
             info = update.effective_user
             chat_id = info.id
             userid= info['username']
             ab=text[-1]
             wdia='❌'
             p = "Not Valid Bin!{} \n ━━━━━━━━━━━━━━━  \n • Bin: {} \n ━━━━━━━━━━━━━━━ \n👤 Checked By: @ASURCCWORLDBOT\n  Used By @{}"
             text = p.format(wdia,ab[:6],userid)
             Sendmessage(chat_id, text)
             
    else:
        chat_id = update.message.chat_id
        info = update.effective_user
        chat_id = info.id
        userid= info['username']
        ab=text[-1]
        wdia='❌'
        p = "Not Valid Bin!{} \n ━━━━━━━━━━━━━━━  \n • Bin: {} \n 👤 Checked By: @ASURCCWORLDBOT\n Used By @{}"
        text = p.format(wdia,ab[:6],userid)
        Sendmessage(chat_id, text)
################################################################################################################################
def asetsk(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    chat_id = info.id
    global sk_chg
    userid= info['username']
    text =  update.message.text.split(' ', 1)
    tt=text[-1]
    if tt[:3]=="sk" or "pk":
        text=" ✅ Your Sk Key has been set!!"
        sk_chg = tt
        Sendmessage(chat_id, text)
    else:
        
        text ="Default is been continued as your sk key is invalid"
        Sendmessage(chat_id, text)
    
             

################################################################################################################################

def chk(update,context):
    chat_id = update.message.chat_id
    info = update.effective_user
    chat_id = info.id
    userid= info['username']
    tic = time.perf_counter()
    wdia ='❌'
    crs = '➟'
    text =  update.message.text.split(' ', 1)
    maintxt=text[-1]
    i=maintxt.split("|")
    cc=i[0]

    skq1=sk_chg[:16]
    skq2="x"*78
    skq3=sk_chg[-4:]
    skmains=(skq1+skq2+skq3)
    mes=i[1]
    ano=i[2]
    cvv=i[3]
    url = 'https://api.stripe.com/v1/payment_methods'
    headers = {
        'Authorization': 'Bearer {sk_chg}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'type': 'card',
        'card[number]': i[0],
        'card[exp_month]': i[1],
        'card[exp_year]': i[2],
        'card[cvc]': i[3]
    }
    response = requests.post(url, headers=headers, data=data)
    q=response.text
    w=json.loads(q)
    if "testmode_charges_only" in response.text:
        text = (f"""
{wdia} SK-key expired {crs} Change SK key \n Sk-key {crs} <code>{skmains}</code> \n RESPONSE {crs} Testmode Charges Only \n ━━━━━━━━━━━━━━━ \n CHECKED BY @ASURCCWORLDBOT \n Used by @{userid}
""")
        Sendmessage(chat_id , text)
    if 'card' not in w:
       w['card']['three_d_secure_usage']['supported'] == False
       vs ="False"
    if w['card']['three_d_secure_usage']['supported'] == False:
       vs ="False ✅"
    else:
       vs="True ❌"

    #second request
    url = 'https://api.stripe.com/v1/payment_intents'
    headers = {
        'Authorization': 'Bearer {sk_chg}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'amount': '60',
        'currency': 'usd',
        'payment_method_types[]': 'card',
        'description': 'Asur Donation',
        'payment_method': w["id"],
        'confirm': 'true',
        'off_session': 'true'
    }
    response = requests.post(url, headers=headers, data=data)
    b=response.text
    e=json.loads(b)
    if "error" not in e:
        msg = "CCN or CVV LIVE!"
    else:
        msg = e["error"]["message"]
    toc = time.perf_counter()
    if "invalid_cvc" or "incorrect_cvc" in response.text:
        text = (f"""
✅CC {crs} <code>{cc[:7]}xxxxxxxxxx|{mes}|{ano}|{cvv}</code> \n
STATUS {crs} #ApprovedCCN \n
MSG {crs} {msg} \n
VBV[3D] {crs} {vs} \n
TOOK: {toc - tic:0.4f}s\n
CHECKED BY @ASURCCWORLDBOT \n
Used by @{userid}
""")
        Sendmessage(chat_id , text)
    elif "Unrecognized request URL" in response.text:
        text = ("[UPDATE] PROXIES ERROR")
        Sendmessage(chat_id , text)
    elif response.status_code == 200:
        text = (f"""
✔️CC➟ <code>{cc[:7]}xxxxxxxxxx|{mes}|{ano}|{cvv}</code> \n
STATUS ➟ #ApprovedCVV \n
Response -» Successfully Charged 1$ ✅ \n
Gateway -» Stripe Charge 1$ \n
VBV[3D] {crs} {vs}  \n
TOOK: {toc - tic:0.4f}s\n
CHECKED BY @ASURCCWORLDBOT \n
Used by @{userid}
""")
        Sendmessage(chat_id , text)
    else:
        if msg ==  "Your card has insufficient funds.":
            msg = "Your card has insufficient funds ✅"
            text=(f"""
{wdia} CC {crs} <code>{cc[:7]}xxxxxxxxx|{mes}|{ano}|{cvv}</code> \n STATUS {crs} Declined \n MSG 
{crs} {msg} \n TOOK: {toc - tic:0.4f} \n CHECKED BY @ASURCCWORLDBOT \n
Used by @{userid}
""")
        else:
            text=(f"""
{wdia} CC {crs} <code>{cc[:7]}xxxxxxxxx|{mes}|{ano}|{cvv}</code> \n STATUS {crs} Declined \n MSG 
{crs} {msg} \n TOOK: {toc - tic:0.4f} \n CHECKED BY @ASURCCWORLDBOT \n
Used by @{userid}
""")
        Sendmessage(chat_id , text)
#########################################################################################################
	
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
    dp.add_handler(CommandHandler("asetsk", asetsk))
    dp.add_handler(CommandHandler("botcmds", botcmds))
    dp.add_handler(CommandHandler("chk", chk))
    dp.add_handler(CommandHandler("bin", bin))
    dp.add_handler(CommandHandler("botstart", botstart))
    logger.info("Bot Started!!!")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
