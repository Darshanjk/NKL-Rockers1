import asyncio
from pyrogram import Client,filters
from pyrogram.types import Message



app_id = your api hash
app_key = 'your api id'
token = "api token"



app = Client("antiservicemessage", app_id, app_key, bot_token=token)

DONATESTARTTEXT = """
text  
"""




@app.on_message(filters.service)
async def service(client, Message):
    await Message.delete()



@app.on_message(filters.private)
async def start(client, Message):
   await Message.reply(DONATESTARTTEXT,
)

@app.on_message(filters.group & filters.command("command@botname"))
async def main(client, Message):
  await  Message.reply("""text""")

@app.on_message(filters.group & filters.command("command"))
async def main(client, Message):
   await Message.reply("""text""")


app.run()
