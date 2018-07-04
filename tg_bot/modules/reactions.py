
import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import CommandHandler

reactions = ["¯_(ツ)_/","(▼・ェ・▼)","(＞（●●）＜)","◕‿↼",""͡ ͜ʖ ͡","≧◔◡◔≦","O_o","◎_◎",ʕ•̫͡•ʕ*̫͡*ʕ•͓͡•ʔ-̫͡-ʕ•̫͡•ʔ*̫͡*ʔ-̫͡-ʔ","(❁´◡`❁)✲"]

@run_async
def react(bot: Bot, update: Update):
    message = update.effective_message
    react = random.choice(reactions)
    if message.reply_to_message:
      message.reply_to_message.reply_text(react)
    else:
      message.reply_text(react)
    

REACT_HANDLER = CommandHandler("react", react)

dispatcher.add_handler(REACT_HANDLER)