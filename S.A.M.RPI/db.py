import discord
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def getGC():
	scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
	credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials/credentials.json', scope)
	gc = gspread.authorize(credentials)
	return gc

def AddUser(user):
	sheet = getGC().open("Members").sheet1
	if not sheet.findall(user.id):
		return False
	values = [user.id, user.name,0]
	sheet.append_row(values)
	return True

def AddPoints(userID, points):
	sheet = getSheet()
	if not sheet.findall(userID):
		AddUser(user)
	c = sheet.findall(userID)[0].col
	sheet.update_cell(c, 3, Integer.valueOf(sheet.cell(c, 3).value) + Integer.valueOf(points))

def MakePoll(name, alternatives):
	gc = getGC
	sh = gc.open("Polls")
	sh.share('erik.winnerstam@gmail.com', perm_type='user', role='writer')
	worksheet = sh.worksheet()