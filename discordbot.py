import discord
import time
import asyncio
import sys
from discord import opus

client = discord.Client()
channeldict = {}
memberdict = {}
serverdict = {}

OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']



def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            pass

    raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))


class Player:
    def __init__(self, client, channel):
        self.client = client
        self.currentChannel = channel

    def getChannel(self):
        return self.currentChannel

    def setChannel(self, channel):
        self.currentChannel = channel


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    author = message.author
    load_opus_lib()
    if message.content.startswith('!hello'):
        msg = "%s How are you?" % author
        await client.send_message(message.channel, msg)
    elif message.content.startswith("!voice"):
        user_channel = message.author.voice_channel
        if user_channel is None:
            await client.send_message(message.channel, "%s, you are not in a voice channel" % author)
        else:
            await client.join_voice_channel(user_channel)
    elif message.content.startswith("!meme"):
        try:
            voice = await client.join_voice_channel(author.voice_channel)
            player = voice.create_ffmpeg_player("./audio/meme.mp3")
            player.volume = 0.5
            player.start()
            while(True):
                if(player.is_done()):
                    await voice.disconnect()
                    print("client disconnected")
                    break
        except Exception:
            pass
    elif message.content.startswith("!imissthegoodtimes"):
        try:
            voice = await client.join_voice_channel(author.voice_channel)
            player = voice.create_ffmpeg_player("./audio/lekick.wav")
            player.volume = 0.5
            player.start()
            while(True):
                if(player.is_done()):
                    await voice.disconnect()
                    print("client disconnected")
                    break
            await client.move_member(memberdict["Mattchew"], channeldict["Matt's Corner"])
        except Exception:
            traceback.print_exc()

    elif message.content.startswith("!kill"):
        sys.exit("Manual Kill")
    elif message.contentstartswith("!message"):
        try:
            user = message.content[7:]
        except Exception:
            await client.start_private_message(message.author)
            #await client.send_message()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print("Servers:")
    for i in client.servers:
        print(i.name, i.id)
        serverdict[i.name] = i
    print("Channels:")
    channels = client.get_all_channels()
    for i in channels:
        print(i.name, i.id, i.type)
        channeldict[i.name] = i
    #print(channeldict)
    members = client.get_all_members()
    for i in members:
        print(i.name, i.id)
        memberdict[i.name] = i
    #print(memberdict)
    print(serverdict)
            

client.run("MjIwMzQzMzcxNDkzOTMzMDU3.Cqe64A.GKJ63ESBuP6QTmQyOSYy9KpfV78")


