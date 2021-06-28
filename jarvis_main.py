import json
import random
from datetime import datetime
import requests as req
jet = req.get('https://raw.githubusercontent.com/sayampy/jarvis_ai/main/code/chat_data.json').text.strip()
import nltk
from nltk.tokenize import PunktSentenceTokenizer as sent_token
from googletrans import Translator
translator=Translator()
temp = []
'''
# for ai ml session chats
def sessions(text):
   global temp
   with open('chat_session.json') as cs:
       chat = json.load(cs)
       for topic in chat:
          temp.append(chat[topic])
sessions('hello')
'''
import os
app_id = os.environ.get(random.choice(('App_Id','App_Id1')))
def update_user(name,id):
    data = json.load(open('user_data.json'))
    if not str(id) in data:
        data[str(id)]={}
        data[str(id)]['gen'] = 'sir'
    data[str(id)]['name'] = name
    with open('user_data.json','w') as d:
        json.dump(data,d)

data = json.loads(jet)['bot']
def clear(msg):
   sign = [ ".",",","-","!","'","%","*","?","/"]
   o=[]
   out = msg
   for i in sign:
      out = out.replace(i,"")
      o.append(out)
   return o[-1]

#print()
import wolframalpha
client = wolframalpha.Client(app_id)
#print(client)
from difflib import SequenceMatcher as sm
def remove(text:str,obj:list):
  for s in obj:
    text = text.replace(s,'')
  return text
def __reply__(msg,id):
   usr_data = json.load(open('user_data.json','r'))
   _gen = ['call me ','i am your ']
   global data
   tmp_list = []
   tmp_dict = {}
   v = 0
   bot_age = datetime.now() - datetime(2021,5,2)
   msg = clear(msg).lower()
   for tyoe in _gen:
      if tyoe in msg:
         new = msg.replace(tyoe,'')
         user_data = json.load(open('user_data.json'))
         user_data[str(id)]['gen'] = new
         json.dump(user_data,open('user_data.json','w'))
         return f'ok,{new}'
         return
   try:
       res = client.query(msg)
       answer = next(res.results).text
       #print(answer)
   except StopIteration:
       answer = random.choice(('idk','i don\'t know'))
   for response in data:
     for alias in response['alias']:
        amount = sm(None,msg,alias).ratio()
        tmp_list.append(amount)
        tmp_dict[amount] = response['reply']
        if (alias in msg) and ('G.K.'in response['tag'] and 'owner' in response.get('context')):
#            print(alias)
            stat = '0'
            for itm in response.get('context'):
#                 print(stat, itm)
                 if (itm not in msg) | (not 'wolfram' in answer.lower()):
                    stat = 'safe'
                 else:
                    stat='unsafe'
                    break
            if stat=='safe':
              return random.choice(response['reply']).format(usr_name = usr_data[str(id)]['name'], gen = usr_data[str(id)]['gen'],age = bot_age,ans = answer).replace('J.A.R.V.I.S.','Mr. Clever')
              
              v=20
              break
   tmp_list = sorted(tmp_list)
#   print(tmp_list)
   if v==0:
      return random.choice(tmp_dict[tmp_list[-1]]).format(usr_name = usr_data[str(id)]['name'], gen = usr_data[str(id)]['gen'],ans='** **',age = bot_age).replace('J.A.R.V.I.S','Mr. Clever')

sent_analize = sent_token().sentences_from_text
def reply(msg,id):
      #try:
      en_msg = translator.translate(text=msg).text
      s = sent_analize(text = en_msg)
      tmp =[]
      for i in s:
         tmp.append(__reply__(i,id))
      lang_id = translator.detect(text=msg).lang
      #print(en_msg)
      return translator.translate(dest=lang_id, text = '. '.join(tmp)).text
      
      '''except Exception as e:
      return 'sorry, I recieve error.'
      print(f'{e}')'''
# for testing
'''
while True:
   print('bot: '+reply(input('you: '),805081101247709236))
'''
