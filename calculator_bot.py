from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Start command to greet the user
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I am a simple calculator bot. Send me any math expression like '2+2'.")

# Function to evaluate the expression
def calculate(update: Update, context: CallbackContext) -> None:
    try:
        # Get the message text and evaluate it
        expression = update.message.text
        result = eval(expression)  # This evaluates the mathematical expression
        update.message.reply_text(f"The result is: {result}")
    except Exception as e:
        update.message.reply_text("Sorry, I couldn't calculate that. Please make sure you are sending a valid expression.")

def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    updater = Updater("7791223065:AAFaZ9A1PphHJ-BhIzXLe0J9B94NXTcQ-qQ", use_context=True)
    
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    
    # Command handler for '/start'
    dispatcher.add_handler(CommandHandler("start", start))
    
    # Message handler to capture any text messages and calculate the result
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, calculate))
    
    # Start the Bot
    updater.start_polling()
    
    # Run the bot until you send a signal to stop it
    updater.idle()

if __name__ == '__main__':
    main()
