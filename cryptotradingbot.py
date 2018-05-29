import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from emoji import emojize

#Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
          
logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    update.message.reply_photo('http://i66.tinypic.com/24n34op.jpg')
    
def balance(bot, update):
    keyboard = [[InlineKeyboardButton("My investments", callback_data='1'),
                 InlineKeyboardButton("My withdrawals", callback_data='2')],

                [InlineKeyboardButton("My transactions", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Your Balance: \n *0.00000000* BTC \n Total Investments: *0.00000000* BTC \n 
Total Profits: *0.00000000* BTC \n Referral Gifts: *0.00000000* BTC \n *Investment List* \n More details about your account at My 
Investments', parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query

    query.edit_message_text(text="Selected option: {}".format(query.data))


def help(update, context):
    update.message.reply_text("Use /start to test this bot.")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("612354001:AAF_vXOY-bCXkv57Jif0K8U8mXy85mZawE0
", use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()


