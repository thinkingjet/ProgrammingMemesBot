#ADD async later if needed

import os,discord,random,time
from keep_alive import keep_alive

client = discord.Client()
import praw

client_secret = os.getenv("CLIENT_SECRET")
client_pass = os.getenv("CLIENT_PASS")
client_id = os.getenv("CLIENT_ID")
username = os.getenv("USERNAME")
user_agent = os.getenv("USER_AGENT")

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, username=username, password=client_pass, user_agent=user_agent)
"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
@client.event
async def on_ready():
  print(f"Logged in as user {client.user}")

ls = []

subreddit = reddit.subreddit("ProgrammerHumour")

top = subreddit.top(limit=50000)

for x in top:
    ls.append(x)

@client.event
async def on_message(message):
  if message.author == client.user:
    pass
  if message.content.startswith("%hi"):
    await message.channel.send("Hi There!")
  if message.content.startswith("%m"):
      rand_meme = random.choice(ls)
      name = rand_meme.title
      url = rand_meme.url
      emb = discord.Embed(title=name)
      emb.set_image(url=url)
      await message.channel.send(embed=emb)

  if message.content.startswith("%ping"):
    await message.channel.send(f"My Ping Is {client.latency}")

keep_alive()
client.run(os.getenv("TOKEN"))