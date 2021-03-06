from typing import List

from telegram import Bot, Update
from kaga.modules.helper_funcs.alternate import typing_action

from kaga import dispatcher
from kaga.modules.disable import DisableAbleCommandHandler

normiefont = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
weebyfont = ['🅐', '🅑', '🅒', '🅓', '🅔', '🅕', '🅖', '🅗', '🅘', '🅙', '🅚', '🅛', '🅜', '🅝', '🅞', '🅟', '🅠', '🅡', '🅢', '🅣', '🅤',
              '🅥', '🅦', '🅧', '🅨', '🅩']


@typing_action
def weebify(update, context):
    bot = context.bot
    args = context.args
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    message = update.effective_message
    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


WEEBIFY_HANDLER = DisableAbleCommandHandler("blackout", weebify, pass_args=True, run_async=True)

dispatcher.add_handler(WEEBIFY_HANDLER)

command_list = ["weebify"]
handlers = [WEEBIFY_HANDLER]
