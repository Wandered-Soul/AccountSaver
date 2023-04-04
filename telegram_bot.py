import telebot
from telebot import types

# Replace YOUR_API_TOKEN with the token you received from the BotFather
bot = telebot.TeleBot('Bot_Token')

# Replace GROUP_CHAT_ID with the ID of the group chat where you want to forward messages
group_chat_id = 'Chat_ID'

# Replace YOUR_ADMIN_IDS with the IDs of the bot's admins
admin_ids = ['Admin1', 'Admin2']

# Define the handler for the /start command
@bot.message_handler(content_types=["text", "audio", "document", "photo", "video"])
def forward_all_messages(message):
    if str(message.from_user.id) in admin_ids:
        # Forward the message to the group chat with the forward tag removed
        if message.text:
            bot.send_message(group_chat_id, message.text)
        elif message.audio:
            bot.send_audio(group_chat_id, message.audio.file_id, caption=message.caption, disable_notification=True)
        elif message.document:
            bot.send_document(group_chat_id, message.document.file_id, caption=message.caption, disable_notification=True)
        elif message.photo:
            bot.send_photo(group_chat_id, message.photo[-1].file_id, caption=message.caption, disable_notification=True)
        elif message.video:
            bot.send_video(group_chat_id, message.video.file_id, caption=message.caption, disable_notification=True)

bot.polling()
