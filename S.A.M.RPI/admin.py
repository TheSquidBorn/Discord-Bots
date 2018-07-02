import discord

def HasAdmin(author, server): #Very crude, try to streamline
	adminRole = discord.utils.get(server.roles,name="Admin")
	for r in author.roles: 
			if r == adminRole:
				return True
	return False

def GetMember(id, server):
	for member in server.members:
		if member.id == id:
			return member