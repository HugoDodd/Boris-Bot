import random
import os
import discord
from keep_alive import keep_alive

messages = ["Lingling's on the flank again",
            "Zaknod's in the backline",
            "Truthrodian is dpsing on moira",
            "Brexit needs to unbind shift",
            "Gucci's locking the genji",
            "Frank on the flank",
            "META's playing a shit character",
            "Minty's looking for a boost again",
            "Wildrage is bubbling off cooldown"]

client = discord.Client()

@client.event
async def on_ready():
  print("Boris has been voted in to this server! The public loves Boris so much! Vote Tory!!!")
  
  setInterval(() => {
      var anouncements = client.channels.cache.get(485035231724699659);
      yourchannel.send('Vote on scrims this week');
    }, 604800000);

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith ('Prime Minister, '):
    await message.channel.send(random.choice(messages))

keep_alive()
client.run(os.getenv('Token'))