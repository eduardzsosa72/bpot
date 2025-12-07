
from srca.configs import addCommand,Client
from db.mongo_client import MongoDB
from random import randrange


@addCommand('antispam')
def bin(_,m):
    querY = MongoDB().query_user(int(m.from_user.id))
    if  querY == None: return m.reply('Usar el comando $register para el registro.')
    
    if MongoDB().admin(int(m.from_user.id)) == False: return ...
    
    data = m.text.split(' ')
    
    if len(data) < 3: return m.reply('ingrese datos correctos <code>$antispam id antispam</code>')

    idw = int(data[1])
    dias = int(data[2])
    
    MongoDB().add_antispam(idw,dias)
    m.reply('se ha editado el antidpam del usuraio✅')

    texto= f'''<b>Ha Usado el antispam

Name: {m.from_user.first_name}
id: {m.from_user.id}
Username: @{m.from_user.username}
━━━━━━━━
Ha aprovado Un chat.
• Id: <code>{idw}</code>
• <b>antispam :</b> <code>{dias}</code>
━━━━━━━━━━
</b>'''
    Client.send_message(_,chat_id=-1002639873144,text=texto)
        




    

