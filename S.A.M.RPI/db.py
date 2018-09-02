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

def saidVore(user):
	sheet = getGC().open("Vore").sheet1
	

def MakePoll(name, alternatives):
	gc = getGC()
	sh = gc.open("Polls")
	worksheet = sh.add_worksheet(title=name, rows="1", cols="1")
	for a in alternatives:
		worksheet.append_row([a.strip(" "),0])
	worksheet = sh.worksheet("Votes")
	worksheet.append_row([name])

def AddVote(id, poll, alternative):
	gc = getGC()
	#check if alternative is valid
	sh = gc.open("Polls")
	worksheet = sh.worksheet("Votes")
	cell = worksheet.findall(poll)[0]
	r = cell.row
	rCells = worksheet.row_values(r)
	for rc in rCells:
		if rc == id:
			return False
	values_list = worksheet.row_values(r)
	values_list.append(id)
	worksheet.delete_row(r) #put id as votes?
	worksheet.append_row(values_list)
	worksheet = sh.worksheet(poll)
	cell = worksheet.findall(alternative)[0]
	worksheet.update_cell(cell.row, 2, int(worksheet.cell(cell.row, 2).value) + 1)

def getPolls():
	gc = getGC()
	sh = gc.open("Polls")
	return sh.sheet1.col_values(1)

def getPoll(poll):
	gc = getGC()
	return gc.open("Polls").worksheet(poll)