from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QHBoxLayout, QLineEdit, QPushButton, QLCDNumber, QListWidget, QListWidgetItem, QLabel, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSignal

class PlayerWidget(QGroupBox):	

	def __init__(self, statFile):
		self.inventory = []
		self.stats = {}
		self.parseStats(statFile)
		self.initUI()
		
	def initUI(self):
		
		top_line = QHBoxLayout()
		bottom_line = QHBoxLayout()
		
		for key, value in self.stats.items():
			if(key=="CHARACTER_NAME"):
				self.character=self.stats[key]
			elif(key=="PLAYER_NAME"):
				self.player=self.stats[key]
			elif(key=="STRENGTH"):
				self.strength=self.stats[key]
			elif (key=="SIZE"):
				self.size=self.stats[key]
			elif (key=="CAPACITY"):
				self.capacity=self.stats[key]
			elif (key=="HEALTH"):
				self.health=self.stats[key]
			elif (key=="EXTRA_HEALTH"):
				self.health = int(self.health) + int(self.stats[key])
				self.stats[key] = 0
			else:
				swidget = StatWidget(key,value)
				bottom_line.addWidget(swidget)
				swidget.widgetUpdate.connect(self.updateStat)
				
		super().__init__(self.character + " - " + self.player)
		stat_stack = QVBoxLayout()
		
		self.healthbox = LabelBoxWidget("Health",self.health)
		self.strengthbox = LabelBoxWidget("Strength",self.strength)
		self.sizebox = LabelBoxWidget("Size",self.size)
		
		self.healthbox.widgetUpdate.connect(self.updateStat)
		self.strengthbox.widgetUpdate.connect(self.updateStat)
		self.sizebox.widgetUpdate.connect(self.updateStat)
		
		stat_stack.addWidget(self.healthbox)
		stat_stack.addWidget(self.strengthbox)
		stat_stack.addWidget(self.sizebox)
		
		save_stack = QVBoxLayout()
		top_line.addLayout(stat_stack)
		
		self.save_button = QPushButton("Save Character")
		self.save_button.setFixedWidth(200)
		self.save_button.clicked.connect(self.saveDialog)
		self.save_button_layout = QHBoxLayout()
		self.save_button_layout.addWidget(self.save_button)
		
		save_stack.addLayout(self.save_button_layout)
		
		inventory = InventoryWidget(self.capacity)
		
		top_line.addWidget(inventory)
		logo = QLabel(self)
		logo.setPixmap(QPixmap("logo-text.png"))
		save_stack.addWidget(logo)

		
		top_line.addLayout(save_stack)
		
		vbox = QVBoxLayout()
		vbox.addLayout(top_line)
		vbox.addLayout(bottom_line)
		self.setLayout(vbox)
		
	def updateStat(self, key, value):
		self.stats[key]=value
	
	def parseStats(self, filename):
		file = open(filename)
		for line in file:
			if line and not line.startswith('#') and not line.startswith("\n"):
				if line.startswith('@'):
					self.inventory.append(line)
				else:
					split = line.split('=')
					self.stats[split[0]]=split[1].strip()
	
	def saveDialog(self):
		options = QFileDialog.Options()
		filename, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","Caves and Cheese Files (*.cnc)", options=options)
		if filename:
			self.export(filename)
	
	def export(self, filename):
		file = open(filename,'w+')
		
		for key, value in self.stats.items():
			file.write(key+"="+str(value)+"\n")
		
		for item in self.inventory:
			file.write('@'+item)
			
class StatWidget(QGroupBox):
	
	widgetUpdate=pyqtSignal(str,str)
	
	def __init__(self, name, buff):
		self.name = name
		self.buff = buff
		super().__init__(name)
		self.initUI()
		
	def initUI(self):
		self.statLine = QLineEdit(self.buff, self)
		rollButton = QPushButton("Roll", self)
		display = QLCDNumber(self)
		
		vbox = QVBoxLayout(self)
		vbox.addWidget(self.statLine)
		vbox.addWidget(rollButton)
		vbox.addWidget(display)
		self.setLayout(vbox)
		self.setFixedHeight(200)
		self.statLine.textChanged.connect(self.valUpdate)
	
	def valUpdate(self):
		self.widgetUpdate.emit(self.name,self.statLine.text())

class LabelBoxWidget(QGroupBox):
	
	widgetUpdate=pyqtSignal(str,str)
	
	def __init__(self, name, value):
		self.name = name
		self.value = value
		super().__init__(name)
		self.initUI()
		
	def initUI(self):
		self.statLine = QLineEdit(str(self.value), self)
		vbox = QVBoxLayout()
		vbox.addWidget(self.statLine)
		self.setLayout(vbox)
		self.setFixedWidth(150)
		self.statLine.textChanged.connect(self.valUpdate)
	
	def valUpdate(self):
		self.widgetUpdate.emit(self.name,self.statLine.text())
		
class InventoryWidget(QGroupBox):

	def __init__(self, capacity):
		self.capacity = int(capacity)
		super().__init__("Inventory")
		self.initUI()
	def initUI(self):
		list = QListWidget()
		vbox = QVBoxLayout()
		for i in range(self.capacity):
			item = QLineEdit()
			listWidgetItem = QListWidgetItem(list)
			list.addItem(listWidgetItem)
			list.setItemWidget(listWidgetItem, item)
		vbox.addWidget(list)
		self.setLayout(vbox)