

import logging
from telegram import Update
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,CallbackContext



logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'

)
logger = logging.getLogger(__name__)
#print(logger.setLevel(logging.INFO))
#logger.setLevel(logging.DEBUG)




def start(update: Update, context:CallbackContext)-> None:
    update.message.reply_text('خب خب خب..ببین کی اینجاس...\nسلام جون دل...\nسر کیفی عزیز..\n.سر کیفی بدم سر کیفی...\nالکی ادا حال بدا رو در نیار')

def help_command(update: Update, context: CallbackContext)->None:
    print(update.message.text)
    update.message.reply_text('کمک میخوای جووون دل \n\n       1- میتونی به من سلام کنی تا جوابت رو بدم  \n 2_ میتونی منو ادد کنی به گروهایی که توشی تا به تازه وارد ها خوشامد بگم و جواب سلاما رو بدم جوون دل... ')

def echo(update:Update, context: CallbackContext) -> None:
    #print(update.message.new_chat_members)
    #print(update.message.MESSAGE_TYPES)
    #print(update.message.chat.type)
    #print(update.message.chat.all_members_are_administrators)
    #update.message.reply_text(str(update.message.date))
    #print(update.message.forward_from_chat)
    #update.message.reply_text(update.effective_user.mention_html(update.effective_user.username),parse_mode='HTML')
    #print(update.effective_user.username)
    #print(update.effective_user.full_name)
    for i in update.message.new_chat_members:
        reply_hi = '\nخوش اومدی جوووون دل\.\.\nسر کیفی عزیز\.\.\. \nسر کیفی بدم سر کیفی\.\.\.\n'
        update.message.reply_text(i.mention_markdown_v2(i.name) + reply_hi, parse_mode='MarkdownV2')

    if 'سلام' in update.message.text.split() :
        reply_hi = '\nسلام جوووون دل\.\.\nسر کیفی عزیز\.\.\. \nسر کیفی بدم سر کیفی\.\.\.\n'
        update.message.reply_text(update.effective_user.mention_markdown_v2(update.effective_user.name)+reply_hi,parse_mode='MarkdownV2')
    #update.message.reply_text(update.effective_user.mention_markdown(update.effective_user.username)+'\n\nسلام جون دل',parse_mode='Markdownٰ')

    #print(i)

    #update.message.reply_text(update.message.text)


if __name__ == '__main__':
    print('start')
    TOKEN = ''
    updater = Updater(TOKEN)
    print(type(updater))

    dispatcher = updater.dispatcher
    print(dispatcher)

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help_command))

    print('is correct ?')
    dispatcher.add_handler(MessageHandler(Filters.all, echo))
    updater.start_polling()


    updater.idle()
