import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram.ext import filters, MessageHandler

from keycode import KeyCode
from encryption import Encryption

kc = KeyCode()
enc = Encryption()
cypher = True

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
# Lo basico
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global cypher
    kc.reset_key()
    enc.key_code = kc
    cypher = True
    texto_bienvenida = """
Este Bot esta hecho para el cifrado y descifrado de msjes sencillos.

Lo que puedes hacer:
/llaveNueva:            Resetea la llave, eliminando la anterior si hay una.
/generarLlave:          Genera una nueva llave
/introLlave k1 k2 k3:   Introduce una llave previamente generada
/mostrarLlave:          Mostrar la llave actual
/cifra                  En modo cifrando
/decifra                En modo descifrando
/metodoInfo:            ¿Esta cifrando?
/help                   Consulta esta info de nuevo
"""
    await context.bot.send_message(chat_id=update.effective_chat.id, text=texto_bienvenida)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto_help = """
Lo que puedes hacer:
/start                  Inicias de nuevo.
/llaveNueva:            Resetea la llave, eliminando la anterior si hay una.
/generarLlave:          Genera una nueva llave.
/introLlave k1 k2 k3:   Introduce una llave previamente generada.
/mostrarLlave:          Mostrar la llave actual.
/cifra                  En modo cifrando.
/decifra                En modo descifrando.
/metodoInfo:            ¿Esta cifrando?
"""
    await context.bot.send_message(chat_id=update.effective_chat.id, text=texto_help)

async def iniciando_llaves(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kc.reset_key()
    enc.key_code = kc
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Nueva llave")

async def generar_llaves(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kc()
    enc.key_code = kc
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{kc}")

async def introducir_llaves(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kc._k1, kc._k2, kc._k3 = int(context.args[0]) , int(context.args[1]) , int(context.args[2])
    enc.key_code = kc
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Se introdujeron las nuevas llaves")

async def mostrar_llaves(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{kc}")

async def cifra(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global cypher
    cypher = True
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Cifrando ...")

async def decifra(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global cypher
    cypher = False
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Descifrando ...")

async def metodo_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Cifrando: {cypher}")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    enc.message = update.message.text
    if cypher:
        enc.encrypt_message()
    else:
        enc.decipher_message()

    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{enc.message}")


# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


##

# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Lo siento, para las opciones consulta /help")
###

if __name__ == '__main__':

# Lo basico    
    application = ApplicationBuilder().token('TOKEN_BOT').build()

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    nueva_llave_handler = CommandHandler('llaveNueva', iniciando_llaves)
    generar_llaves_handler = CommandHandler('generarLlave', generar_llaves)
    introducir_llaves_handler = CommandHandler('introLlave', introducir_llaves)
    mostrar_llaves_handler = CommandHandler('mostrarLlave', mostrar_llaves)
    cifra_handler = CommandHandler('cifra', cifra)
    decifra_handler = CommandHandler('decifra', decifra)
    metodo_info_handler = CommandHandler('metodoInfo', metodo_info)

    caps_handler = CommandHandler('caps', caps)
##
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(nueva_llave_handler)
    application.add_handler(generar_llaves_handler)
    application.add_handler(introducir_llaves_handler)
    application.add_handler(mostrar_llaves_handler)
    application.add_handler(cifra_handler)
    application.add_handler(decifra_handler)
    application.add_handler(metodo_info_handler)

    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(unknown_handler)
###    
    application.run_polling()