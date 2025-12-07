
from srca.configs import addCommand,Client
from db.mongo_client import MongoDB



@addCommand('panel')
def bin(_,m):

    if MongoDB().admin(int(m.from_user.id)) == False: return ...

    m.reply('Aqui va el texto del panes para los admins. de todo lo que pueden usar si son admins o seller, o co-funders')
    