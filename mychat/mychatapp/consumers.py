from channels import Group
from channels.sessions import channel_session
import json
from .models import Messages

@channel_session
def ws_connect(message):
       label="in"
       message.reply_channel.send({"accept": True})
       Group('main').add(message.reply_channel)

@channel_session
def ws_disconnect(message):
    label="out"   
    Group('main').discard(message.reply_channel) 

@channel_session
def ws_receive(message):
    data = json.loads(message['text'])
    log.debug('update message  author=%s text=%s', 
             data['author'], data['text'])
    m = Messages.create(**data)
    Group('main').send('main',{'text': json.dumps(m.as_dict())})

