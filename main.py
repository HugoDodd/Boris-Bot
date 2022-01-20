import random
import os
import discord
from keep_alive import keep_alive
from discord.ext import tasks
from discord.utils import get

status = [
          "Rule Britannia!",
          "Eating a chocolate digestive",
          "Having more children",
          "Busy running the greatest country in the world",
          "Hide your wife, I'm here!",
          "Boris Johnson is the most pro-gay option for the tories. Vote Boris!",
          "Reclaiming India", 
          "Reclaiming Canada",
          "Reclaiming Australia", 
          "Reclaiming New Zealand", 
          "Reclaiming South Africa",
          "With my balls",
          "Funding the NHS",
          "Squatting on Jeremy Corbyn",
          "Punching europeans",
          "Punching immigrant babies",
          "Bombing syria",
          "Nuking iran",
          "Wondering why no-one likes me",
          "Unearthing lord Thatcher",
          "Dumping napalm in the Thames",
          "Making a time machine",
          "Setting fire to london",
          "Holiday in Tienanmen square",
          "I'm a wet wipe",
          "Streaming fortnite now at twitch.tv/ukgov_official",
          "Stay safe",
          "Wear a mask",
          "U-Turn baby!",
          "Cancelling hancock",
          "Bullying Raab",
          "Deporting immigrants",
          "Listening to You'll Never Walk Alone by Tom Moore",
          "Listening to Holy by Bieber and the NHS choir",
          "Hosting a party at number 10!",
          "Curing COVID",
          "Getting a vaccine",
          "God save our queen",
          "God save our NHS",
          "Eating a vegan sausage roll",
          "My policy on cake is pro having it and pro eating it",
          "Ping-pong was invented on the dining tables of England in the 19th century, and it was called Wiff-waff!",
          "Other nations, looked at a dining table and saw an opportunity to have dinner; we looked at it an saw an opportunity to play Wiff-waff!",
          "It is absolutely ridiculous that people should choose to go around looking like letter boxes",
          "Jamming out on Downing street",
          "I was NOT breaking any rules!",
          "Bring your own booze",
          "Enjoying a garden party",
          "Lockdown won't stop me enjoying the nice weather!"]

client = discord.Client()

@client.event
async def on_ready():
  print("Boris has been voted in to this server! The public loves Boris so much! Vote Tory!!!")
  change_status.start()
  send_weekly_message.start()
  
@tasks.loop(minutes=30)
async def change_status():
    await client.change_presence(activity=discord.Game(random.choice(status)))

@tasks.loop(hours=168)
async def send_weekly_message():
    message_channel = client.get_channel(485035231724699659)
    await message_channel.send("<@&745591167193841749>" + " /tts" + random.choice(vote_message))

keep_alive()
client.run(os.getenv('Token'))
