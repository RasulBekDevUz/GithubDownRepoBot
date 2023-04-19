#Importation librariy


import requests
from telebot.types import *
from courlan import validate_url

import  telebot

bot=telebot.TeleBot("6114463526:AAHdwGyFWb96hcpk9i4zrOmfuT0B_eXf6f0")




#starta message answer 

def start1(name):
    start_text  = f"""
<b>

✋ Assalomu alaykum {name} 

@{bot.get_me().username} ga Xush kelibsiz !

📥 Github.com dan yuklash uchun \nRepository havolasini  yuboring!
</b>
"""

    return start_text





#Custom keyboard 

docs = InlineKeyboardButton("📋Qollanma",callback_data='docs')
admin = InlineKeyboardButton("💻 Dasturchi",url='t.me/KgzNet')
btn = InlineKeyboardMarkup().add(docs,admin)

#



@bot.message_handler(commands=["start"])



#start handler
def start(msg):
    bot.send_message(msg.chat.id,start1(msg.from_user.first_name),parse_mode='html',reply_markup=btn)




@bot.message_handler(func=lambda m:True)

#Custom handler 

def custom(message):
    try:
        if(validate_url(message.text)[1].netloc=='github.com'):
            a  = bot.send_message(message.chat.id,'📥').message_id
            bot.delete_message(chat_id=message.chat.id,message_id=a)
            _ = bot.send_document(message.chat.id,document=f"{message.text}/archive/refs/heads/master.zip",caption=f"💻 Dasturchi : @Ulugbek_auf & @KgzNet").content_type
            _ = bot.send_document('@GithubProjekt',document=f"{message.text}/archive/refs/heads/master.zip",caption=f"{message.text} \n\n @{message.from_user.username}").content_type
            if _ =='document':
                pass
            else:
                bot.send_message(message.chat.id,"Bu hato link !")
    except :
        pass

#callback handler

@bot.callback_query_handler(func=lambda call:True)
def learn(call):
    if call.data =='docs':
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,text="<i>Qollanma bo'limiga xush kelibsiz !\n\nTelefon da github da repostoryni yuklashga qiynalayabsiz mi ? \nUnda bu bot aynan siz uchun ! \nFoydalanish uchun Repository havolani yuboring!</I>",parse_mode='HTML',reply_markup=InlineKeyboardMarkup().add(admin))


#Console logs bot info answer 

print("[INFO] Bot Ishga tushdi...  @",bot.get_me().username,sep='')



#Infinity polling 

bot.infinity_polling()