import random
import os
import discord
from keep_alive import keep_alive
from discord.ext import tasks
from itertools import cycle

status = [
          "Rule Britannia!",
          "Go Conservatives!",
          "Eating a chocolate digestive",
          "I've had more children that you can count",
          "Busy running the greatest country in the world",
          "Making brexit deals",
          "Hide your wife, I'm here!",
          "Vote TORY!!!",
          "Boris Johnson is the most pro-gay option for the tories. Vote Boris!",
          "Reclaiming (India, Canada, Australia, New Zealand, South  Africa)",
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
          "setting fire to london",
          "holiday in Tienanmen square",
          "twitch.tv/ukgov_official",
          "As Stormzy once said, I love the government and I love Boris",
          "I'm a wet wipe",
          "I'm richer, better educated, more powerful and more sucessful than you",
          "Falklands 2.0",
          "Defeat? I do not recognise the meaning of the word",
          "Streaming fortnite now at twitch.tv/ukgov_official",
          "stay safe",
          "wear a mask",
          "U-Turn baby!",
          "Telling off hancock",
          "Bullying Raab",
          "Deporting immigrants",
          "Listening to You'll Never Walk Alone by Tom Moore",
          "Listening to Holy by Bieber and the NHS choir"]

vote_message = [
          "Weekly scrim vote (vote tory)",
          "When does everyone want to scrim this week? I think Wednesday is POG"
          "To quote the Margret Thatcher, 'Defeat? I do not recognise the meaning of the word'. I think that sums up team doublecross very well. On that note, when do you want to scrim this week?"
          "Scrim vote for this week"
          "Any scrimmers? If so what day?"
          "Boris reccommends at least 2 scrims this week! What days shall I put down for you"
          "META promised me if i get 7 votes for a scrim one one day today, it will be a POG scrim. VOTE!!!"
          "Remember everyone, vote! (for your scrim this week)"
          "This weeks scrims will be different to normal, you will be practicing brawl...oh wait. Vote for what days you want!!"
          "As the iron lady once said, 'I love argument. I love debate.' On that note, when do you want to scrim this week?"
          "I like a bourbon like I like my scrims - existent! When do you want to scrim this week?"
          "LingLing likes to flank, I like to run the country and Team Doublecross likes to scrim. When are you scrimming this week?"
          "Remember to vote kids! (on when you want to scrim this week)"
          "I like kids but I also like it when Team Doublecross scrims. When are you scrimming this week?",
          "If we get 7 votes on a scrim this week Truth will heal for the whole scrim",
          ]

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
    await message_channel.send(random.choice(vote_message).format(client.team.mention))

keep_alive()
client.run(os.getenv('Token'))