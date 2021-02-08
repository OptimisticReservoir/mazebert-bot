#!/usr/bin/python3
import discord
import logging
import sys

# I guess this needs to be global.
client = discord.Client()

def main(args):
    if(len(args)>1):
        discord_token = args[1]
    else:
        f = open("token_file")
        discord_token = f.read(60).rstrip()
        f.close()
    discord_logger = set_up_log('discord');
    client.run(discord_token);

mazebert_test_server = "Guild id=630506925620068352"
mazebert_replay_url = 'https://mazebert.com/rest/game/get-submitted?combinedId=aa63425f-c55d-4700-aa0d-f4941a481ccb-21950'
mazebert_profile_url = "https://mazebert.com/player/"
mazebert_profile_rest = "https://mazebert.com/rest/player/profile?id=";
roles = [{"name" : "Apprentice",
        "min" : 1,
        "max" : 20},
        {"name" : "Scholar",
        "min" : 21,
        "max" : 40},
        {"name" : "Master",
        "min" : 41,
        "max" : 60},
        {"name" : "Master Defender",
        "min" : 61,
        "max" : 80},
        {"name" : "Master Commander",
        "min" : 81,
        "max" : 99},
        {"name" : "King's Hand",
        "min" : 100,
        "max" : 105},
        {"name" : "King",
        "min" : 106,
        "max" : 110},
        {"name" : "Emperor",
        "min" : 111,
        "max" : 115},
        {"name" : "Master of the Universe",
        "min" : 116,
        "max" : 129},
        {"name" : "Chuck Norris",
        "min" : 130,
        "max" : 999999}]

bot_channel = "general"
bot_unique_id = "<@630501373779116047>"
bot_name = "Ganesha_Mazebert#4057"
guild_list = []
'''
await add_roles(*roles, reason=None, atomic=True)
This function is a coroutine.

Gives the member a number of Roles.

You must have the manage_roles permission to use this.

Parameters
*roles (abc.Snowflake) – An argument list of abc.Snowflake representing a Role to give to the member.

reason (Optional[str]) – The reason for adding these roles.
Shows up on the audit log.

atomic (bool) – Whether to atomically add roles. This will ensure that multiple
operations will always be applied regardless of the current state of the cache.
'''

@client.event
async def on_guild_available(guild):
    guild_list.append(guild)
    print(guild_list)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(client.user)
    for c in client.get_all_channels():
        print(c)
    #await message.channel.send('Hello!')

@client.event
async def on_message(message):
    msg_text = message.content
    msg_author = message.author
    msg_guild = message.guild
    msg_channel = message.channel
    msg_mentions = message.mentions
    if msg_author == client.user:
        #print(f"It's me: author={msg_author}")
        return
    if str(msg_channel) != bot_channel:
        #print(f"Not my channel. It's {msg_channel}")
        return

    await msg_channel.send(msg_text)
    if len(msg_mentions):
        for x in msg_mentions:
            print(x)
    print(f"text={msg_text} author={msg_author} in {msg_channel}")

def set_up_log(log_type):
    format_str = '%(asctime)s:%(levelname)s:%(name)s: %(message)s'
    log_file = log_type + ".log"
    new_log = logging.getLogger(log_type)
    new_log.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename=log_file,
                                  encoding='utf-8',
                                  mode='w')
    handler.setFormatter(logging.Formatter(format_str))
    new_log.addHandler(handler)
    return new_log


main(sys.argv)
