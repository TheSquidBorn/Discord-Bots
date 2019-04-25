import discord
import json

def HasAdmin(author, server):
    adminRole = discord.utils.get(server.roles,name="Admin")
    for r in author.roles:
        if r == adminRole:
            return True
    return False

def GetMember(id, server): #.fetchUser(id)?
    for member in server.members:
        if member.id == id:
            return member

def changeCfg(key, value):
    with open("config.json", "r") as f:
        config = json.load(f)

    config[key] = value

    with open("config.json", "w") as f:
       json.dump(config, f, indent=4, sort_keys=True) 

def getCfg():
    with open("config.json", "r") as f:
        config = json.load(f)
        return config
