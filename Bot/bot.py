
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ( CommandHandler, Filters, MessageHandler, Updater)
from message import Editmessage, Sendmessage, logger
from Checks.Altbalaji import altbalaji_helper
from Checks.hoichoi import hoichoi_helper
from Checks.voot import Voot_helper
from Checks.aha import aha_helper
from Checks.zee5 import zee_helper
from Checks.sun import Sun_helper
from Miscellaneous.Scraper import pastebin, text_scraper, throwbin, ghostbin
import os
import os
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
    text = "Hey, welcome to this Bot! Below I show you all available commands: \n Bin lookup: /bin xxxxxx \n SK-Key Check: /sk sk_live_xxxxxxxxxxxx  \n Card-Check:/chk xxxxxxxxxxxxxxxx|xx|xx|xxx"
    Sendmessage(chat_id, text)
def botinfo(update, context):
    chat_id = update.message.chat_id
    text = "Hey! I am a CC-Checker bot with a few extras. Send /ctr for a list of all commands!"
    Sendmessage(chat_id, text)

def duty(update, context):
    chat_id = update.message.chat_id
    text =  update.message.text.split(' ', 1)
    if (text[0] == "/"+"!start") :
        Sendmessage(chat_id, "Hey! I am a CC-Checker!");
    elif (text[0] == "/"+"cmds") :
        Sendmessage(chat_id, "'<b>Hey, welcome to this Bot! Below I show you all available commands:</b>\n Bin lookup:</u> <code>/bin xxxxxx</code><u> \n SK-Key Check:</u> <code>/sk sk_live_xxxxxxxxxxxx</code><u> \n Card-Check:</u> <code>/stm xxxxxxxxxxxxxxxx|xx|xx|xxx</code>");
    elif (text[0] == "/" +"info") :
        Sendmessage(chat_id, "Hey! I am a CC-Checker bot with a few extras. Send /cmds for a list of all commands!");
    elif (text[0] == "/"+"bin") :
        bin = text[5: ];
        ch = curl_init();
        curl_setopt(ch, CURLOPT_URL, str('https://lookup.binlist.net/' + str(bin)) + '');
        curl_setopt(ch, CURLOPT_USERAGENT, user_agent);
        curl_setopt(ch, CURLOPT_HTTPHEADER, OrderedDict([(0,'Host: lookup.binlist.net'),(1,'Cookie: _ga=GA1.2.549903363.1545240628; _gid=GA1.2.82939664.1545240628'),(2,'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')]));
        curl_setopt(ch, CURLOPT_FOLLOWLOCATION, 1);
        curl_setopt(ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt(ch, CURLOPT_POSTFIELDS, '');
        resul = curl_exec(ch);
        result = resul.upper();
        fim = json_decode(result, True);
        bank = fim['BANK']['NAME'];
        country = fim['COUNTRY']['NAME'];
        brand = fim['SCHEME'];
        type = fim['TYPE'];
        level = fim['BRAND'];
        flag = fim['COUNTRY']['EMOJI'];
        currency = fim['country']['currency'];
        type3 = fim['type'].upper();
        response = str(str(str(str(str(str(str(str(str(str(str('BinData:' + str(type1)) + '-') + str(type3)) + '-') + str(country)) + '-') + str(type)) + ' -') + str(bank)) + ' BANK ') + str(flag)) + '';
        response = str(str(str(str(str(str(str(str(str(str(str(str(str('✔️ Valid BIN <b>%0ABRAND: </b>' + str(brand)) + '<b>%0ATYPE: </b>') + str(type)) + '<b>%0ALEVEL: </b>') + str(level)) + '<b>%0ABANK: </b>') + str(bank)) + ' <b>%0ACOUNTRY: </b>') + str(country)) + ' ') + str(flag)) + '%0A<b>CHECKED BY:</b> ') + str(username)) + '<b>%0ABOT BY:</b> @teamxcode CyraX';


        
    else:
        logger.info('Unknown Command')


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
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, duty))
    dp.add_handler(CommandHandler("scrape", scraperdfnc))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("botinfo", botinfo))
    dp.add_handler(CommandHandler("botcmds", botcmds))
    #dp.add_handler(CommandHandler("bin", bin))
    dp.add_handler(CommandHandler("botstart", botstart))
    logger.info("Bot Started!!!")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
