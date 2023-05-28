import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram.ext import filters, MessageHandler

from keycode import KeyCode
from encryption import Encryption

enc = Encryption()
kc = KeyCode()
cypher = True

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
# Lo basico
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    enc.reset_message()
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Se inicio un nuevo cifrado")

async def iniciando_llaves(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kc.reset_key()
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Llave iniciada")

async def generar_llaves(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kc()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{kc}")

async def mostrar_llaves(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{kc}")

##

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")    
###

if __name__ == '__main__':

# Lo basico    
    application = ApplicationBuilder().token('6260522820:AAE5jiDvZRPGCGi17yr7u6Kg2NhIR0tOOqQ').build()

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    start_handler = CommandHandler('startt', start)
    nueva_llave_handler = CommandHandler('llaveNueva', iniciando_llaves)
    generar_llaves_handler = CommandHandler('generarLlave', generar_llaves)
    mostrar_llaves_handler = CommandHandler('mostrarLlave', mostrar_llaves)

    caps_handler = CommandHandler('caps', caps)
##
    application.add_handler(start_handler)
    application.add_handler(nueva_llave_handler)
    application.add_handler(generar_llaves_handler)
    application.add_handler(mostrar_llaves_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(unknown_handler)
###    
    application.run_polling()