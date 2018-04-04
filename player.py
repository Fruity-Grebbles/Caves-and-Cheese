import sys, os

class Player():	

	def __init__(self, statFile):
		self.inventory = []
		self.stats = {}
		self.skills = []
		self.skill_num = 20
		self.health = 20
		self.traits = {"CHARACTER_NAME":'',"PLAYER_NAME":'',"STRENGTH":'',"CAPACITY":'',"HEALTH":'',"LEVEL":'',"SIZE":''}
		self.parseStats(statFile)

	def updateStat(self, key, value):
		self.stats[key]=value
		
	def updateInventory(self, item, index):
		self.inventory[index]=item
	
	def parseStats(self, filename):
		file = open(filename)
		for line in file:
			if line and not line.startswith('#') and not line.startswith("\n"):
				if line.startswith('@'):
					self.inventory.append(line[1:].strip())
				if line.startswith('^'):
					self.skills.append(line[1:])
				if line.startswith('?'):
					self.notes = line[1:]
				elif ("=" in line):
					split = line.split('=')
					self.stats[split[0]]=split[1].strip()
					
		for key, value in list(self.stats.items()):
			if (key in self.traits):
				self.traits[key] = value
				del self.stats[key]
				
		while len(self.inventory) < int(self.traits["CAPACITY"]):
			self.inventory.append("")
	
	def updateStat(self, key, value):
		self.stats[key]=value
		
	def updateInventory(self, item, index):
		self.inventory[index]=item
		
	def updateSkill(self, skill, index):
		self.skills[index]=skill
	
	def export(self, filename):
		file = open(filename,'w+')
		
		for key, value in self.stats.items():
			file.write(key+"="+str(value)+"\n")
		
		for item in self.inventory:
			if not item == "":
				file.write('@'+item+"\n")