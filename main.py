import telebot
from telebot import types
from spellchecker import SpellChecker
from textblob import TextBlob
import re
from string import digits
from telebot import util

bot = telebot.TeleBot("5919000419:AAEvJ9Lo1CuYNmk8tcdtUdvnySJwJW_lgN8")
spell = SpellChecker("en")
# a = []
# def reversed_text(message):
#   a.append(message.text)
#   print(a)
#   txt = message.text[::-1]
#   return txt

# @bot.message_handler(commands=['help'])

# def start(message):
#   bot.send_message(message.chat.id, message.from_user.first_name)
def remove_d(sen):
  remove_digits = str.maketrans('', '', digits)
  res = sen.text.translate(remove_digits)
  return res

def misspelled_words(words):
    all_words = remove_d(words)
    misspelled = spell.unknown(all_words.split())
    number_of_mistakes = str(len(misspelled))
    display = "Number of spelling mistakes: "+f"<u><b>{number_of_mistakes}</b></u>"
    if len(misspelled) > 0:      
          miss_str = str(misspelled)   
          bot.send_message(words.chat.id, display , parse_mode="HTML")
          clear_w = miss_str[1:len(miss_str)-1]
          return clear_w
    else:
          bot.send_message(words.chat.id,text="No mistake!")
          
    

def correction_senten(text):
      all_words = remove_d(text)
      new_doc = TextBlob(all_words)
      result = new_doc.correct()
      final_result = str(result)
      return final_result
@bot.message_handler(commands=["start"])
def intro(message):
      bot.send_message(message.chat.id,text=f"Wassup! {message.from_user.first_name} 😉")
      bot.send_message(message.chat.id,text="Welcome to SupText <u><b>version 1.0</b></u> \n\nHere you may send text or file and check for grammar and spelling mistakes!", parse_mode="HTML")
      # bot.send_message(message.chat.id,text="Here you may send text or file and check for grammar and spelling mistakes!")
@bot.message_handler(content_types=['text']) #func= lambda message: True 
def start(message):
      try:
        answer = str(correction_senten(message))
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn = types.InlineKeyboardButton(text="correct it",callback_data="correct_btn")
        kb.add(btn)
        bot.send_message(message.chat.id, misspelled_words(message))
        print(message.text)
        bot.send_message(message.chat.id, message.text,reply_markup=kb)
        
      #   bot.send_message(message.chat.id, text=answer)

      except:
        pass
  
@bot.callback_query_handler(func=lambda callback:callback.data) 
def reply_btn(callback):
      #correction_senten(callback)
      if callback.data == "correct_btn":
            data = callback.message
            
            # bot.send_message(callback.message.chat.id,text=correction_senten(callback.message))
            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,text=correction_senten(data))
            



  # kb = types.ReplyKeyboardMarkup()
  # btn1 = types.KeyboardButton(text='Button 1')
  # btn2 = types.KeyboardButton(text='Button 2')
  # kb.add(btn1,btn2)
  
  # if message.text == 'yes':
  #   bot.delete_message(message.chat.id , message.id)

  # else:
  #   bot.send_message(message.chat.id, reversed_text(message))
  #   bot.send_message(message.chat.id,'1', reply_markup=kb)
  
      
      

  
  
  # file = open('rO1Udvo.jpg','rb')
  # bot.send_photo(message.chat.id,file, message.text)


bot.polling()