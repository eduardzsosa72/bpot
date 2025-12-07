
from srca.configs import find_cards, antispam
from plugins.gates.src.Braintree_avs import Braintree2
import time
from db.mongo_client import MongoDB
from srca.configs import addCommand


@addCommand('mass')
def mc(client, m):
    inicio = time.time()
    if MongoDB().query_group(m.chat.id) == None:
        return m.reply('Chat not Authorized.')
    querY = MongoDB().query_user(int(m.from_user.id))
    if querY == None:
        return m.reply('Usar el comando $register para el registro.')
    if querY['role'] == 'baneado':
        return m.reply('User baneado')
    # if  querY['plan'] == 'free': return m.reply('User Fre , adquiera el plan https://t.me/Deividjosh')
    inicio = time.time()

    if antispam(querY['antispam'], m):
        return

    final_msg = '<b>[⚡️] Mass Gate</b>\n\n'
    msg =  m.reply_text(final_msg)
 
    query = m.text.split(" ", 1)
    
    if not query[1]:
      return  msg.edit_text(
        '<b>Format: card|month|year|cvv...</b>'
        )
        
    inputData = query[1] 
    cards = inputData.split('\n')
    
    if len(cards) > 10:
      return  msg.edit_text(
        '<b>Error Max Limit: 10</b>'
        )
    
    for card in cards:
 
      try:
        cc, mes, ano, cvv = card.split('|')
        
        response, emoji = Braintree2().main(card)
        
        final_msg += f"<b>Card: <code>{card}</code>\nMessage: {response} {emoji}</b>\n\n"
        msg.edit_text(final_msg)
      except Exception as e:
       
        final_msg += f"<b>Card: <code>{card}</code>\nMessage: Invalid</b>\n"
     
        msg.edit_text(final_msg)
                    
    time.sleep(1)
    
    import requests
    req = requests.get(f'https://binlist.io/lookup/{cc[:6]}')
    print(req.url)
    fin = time.time()

    final_msg += f'''<b>• Bin: {req.json()['scheme']} {req.json()['type']} {req.json()['category']}
• Country:{req.json()['country']['name']} [{req.json()['country']['emoji']}]
• Bank: {req.json()['bank']['name']} 

• Pxs: Live ✅
• Time: <code>{fin-inicio:0.4f}'s</code>
• From: {m.from_user.first_name}</b>'''
    msg.edit_text(final_msg)