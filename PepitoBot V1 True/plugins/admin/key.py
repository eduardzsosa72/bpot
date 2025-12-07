
from srca.configs import addCommand,Client
from db.mongo_client import MongoDB
from random import randrange


@addCommand('key')
def bin(_,m):
    try:
        querY = MongoDB().query_user(int(m.from_user.id))
        if  querY == None: return m.reply('Usar el comando $register para el registro.')
        
        if MongoDB().admin(int(m.from_user.id)) == False: return ...
        
        dias = m.text.split(' ')
        
        if len(dias) < 2: return m.reply('ingrese los dias.')

        keys1 = randrange(10000000)

        text = f'''<b>
    [✅] 𝗞𝗲𝘆 𝗚𝗲𝗻𝗲𝗿𝗮𝗱𝗮
    ━━━━━━━━━━━━━━━━━━━━━ 
    • Key: <code>chkbot-{keys1}</code>
    • <b>Dias Generados :</b> <code>{dias[1]}</code>
    ━━━━━━━━━━━━━━━━━━━━━ 
    • <b>Admin :</b> <a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name}</a> [{querY["role"]}]</b>'''

        key = f'chkbot-{keys1}'
        MongoDB().save_key(key,int(dias[1]))
        from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup

        m.reply(text,reply_markup =InlineKeyboardMarkup([[InlineKeyboardButton(text='CLaim',url='https://t.me/the_JokersKing')]],))
        
        texto= f'''<b>New Key gen 

    Name: {m.from_user.first_name}
    id: {m.from_user.id}
    Username: @{m.from_user.username}
    ━━━━━━━━
    Ha generado una nueva key 
    • Key: <code>chkbot-{keys1}</code>
    • <b>Dias Generados :</b> <code>{dias[1]}</code>
    ━━━━━━━━━━
    </b>'''
        Client.send_message(_,chat_id=-1002639873144,text=texto)
        return
    except: m.reply('demasiados dias.')
            
                #Client.send_m(_,chat_id = '-1002125995809',text=f'<b><code>{m.from_user.first_name}| {m.from_user.id} a generado una key de {dias} Dias</code>.</b>')    
        

