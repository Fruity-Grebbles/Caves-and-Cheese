from PyQt5.QtWidgets import QWidget, QFileDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QMessageBox, QGroupBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal
import PyQt5
from PyQt5.Qt import QSizePolicy
import sys, os
from main_tab_widgets import LabelBoxWidget
from player import Player
import pickle
				
class SplashWidget(QWidget):
	
	start=pyqtSignal(Player)

	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		hbox = QHBoxLayout(self)
		
		logo = QLabel(self)
		logo.setPixmap(QPixmap(resource_path("Images/logo-text.png")))
		hbox.addWidget(logo)

		newCharacterLayout = QVBoxLayout()
		stack = QVBoxLayout()
		
		newCharacterBox = QGroupBox("New Character")
		hbox.addLayout(stack)
		
		self.character_name = LabelBoxWidget("Character Name","",valType = None, width = None, placeholder = "Enter Character Name")
		self.player_name = LabelBoxWidget("Player Name","",valType = None, width = None, placeholder = "Enter Your Name")
		self.size = LabelBoxWidget("Character Size","",valType = None, width = None, placeholder = "Enter Character Size")
		newCharacterLayout.addWidget(self.character_name)
		newCharacterLayout.addWidget(self.size)
		newCharacterLayout.addWidget(self.player_name)
		newCharacterBox.setLayout(newCharacterLayout)
		stack.addWidget(newCharacterBox)
		
		self.open_button = QPushButton("Open Character")
		self.new_button = QPushButton("Create Character")
		
		self.open_button.clicked.connect(self.openDialog)
		self.new_button.clicked.connect(self.newCharacter)
		
		button_hbox = QHBoxLayout()
		button_hbox.addWidget(self.open_button)
		button_hbox.addWidget(self.new_button)
		stack.addLayout(button_hbox)		
			
	def openDialog(self):    
		options = QFileDialog.Options()
		filename, _ = QFileDialog.getOpenFileName(None,"Open Character", "","Caves and Cheese Files (*.cheese)", options=options)
		if filename:
			try:
				self.start.emit(pickle.load(open(filename, "rb" )))
			except pickle.UnpicklingError as e:
				msg = QMessageBox(self)
				msg.setIcon(QMessageBox.Critical)
				msg.setText("Error: Could not open file")
				msg.setDetailedText(str(e))
				msg.setInformativeText("File may be incompatible with this C&C version		")
				msg.setStandardButtons(QMessageBox.Close)
				msg.setWindowTitle("File Open Error")
				msg.show()
				
	def newCharacter(self):
		player = Player()
		player.init_new(self.character_name.value,self.player_name.value,self.size.value)
		self.start.emit(player)

def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath("."), relative_path)