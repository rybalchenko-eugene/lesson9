from cgitb import text
from tkinter.tix import TEXT
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler
import random
import emoji



async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('/help - список комманд\n/hello - привет\n/game - игра\n/show - выбор\n/board - доска')


async def game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('\bОпределяем, кто ходит первый...')
    if random.random() > 0.5:
        player_token, comp_token = 'X', 'O'
    else:
        player_token, comp_token = 'O', 'X'

    if player_token == 'X':
        await update.message.reply_text('Ваши - ' + emoji.emojize(':crossed_swords:'))
    else:
        await update.message.reply_text('Ваши - ' + emoji.emojize(':egg:'))
    await update.message.reply_text('А теперь эхобот')
    return player_token
    


async def board(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for i in range(3):
        s = ''
        for j in range(3):
            if new_board[i*3+j] == 'X':
                s = str(s) + emoji.emojize(' :crossed_swords: |')
            elif new_board[i*3+j] == 'O':
                s = s + emoji.emojize(' :egg:|')
            else:    
                s = s + ' ' + str(new_board[i*3+j]) + ' |'
        await update.message.reply_text(s)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answ = update.message.text
    answ = 'Никогда больше не говори ' + answ
    await update.message.reply_text(answ)

async def show(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(player_token)

app = ApplicationBuilder().token("5516351397:AAEGHZDdpR4gi-p1eUxfZjwxO8KV6ScenOg").build()

app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("game", game))
app.add_handler(CommandHandler("show", show))
app.add_handler(CommandHandler("board", board))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# conv_handler = ConversationHandler(
#         entry_points=[CommandHandler("start", start)],
#         states={
#             GENDER: [MessageHandler(filters.Regex("^(Boy|Girl|Other)$"), gender)],
#             PHOTO: [MessageHandler(filters.PHOTO, photo), CommandHandler("skip", skip_photo)],
#             LOCATION: [
#                 MessageHandler(filters.LOCATION, location),
#                 CommandHandler("skip", skip_location),
#             ],
#             BIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, bio)],
#         },
#         fallbacks=[CommandHandler("cancel", cancel)],
#     )

## app.add_handler(conv_handler)
print('server started...')
app.run_polling()

# app = ApplicationBuilder().token("5516351397:AAEGHZDdpR4gi-p1eUxfZjwxO8KV6ScenOg").build()