from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import TELEGRAM_TOKEN

import logging
import quest


def start(update, context):
    response_message = """
Olá, eu sou o bot Cleber, seu ajudante do dia-a-dia.
Você tem as seguintes opções:

/wiki - para pesquisar algo no Wikipédia.
/defi - para pesquisar a definição de alguma palavra.
"""

    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text
    )


def wiki(update, context):
    query = str(" ".join(context.args))

    text = quest.search().wiki(query)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sugestão: " + text['sugestão'] + ".\n\nPesquisa: " + text['pesquisa']
    )


def defi(update, context):
    query = str(" ".join(context.args))

    text = quest.search().dicio(query)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text
    )


def unknown(update, context):
    response_message = "Não entendi o que você deseja"
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )

    dispatcher.add_handler(
        CommandHandler('start', start)
    )

    dispatcher.add_handler(
        CommandHandler('wiki', wiki)
    )

    dispatcher.add_handler(
        CommandHandler('defi', defi)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.text & (~Filters.command), echo)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()
