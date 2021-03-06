from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPlainTextEdit
from PyQt5.QtCore import pyqtSignal

class NotesWidget(QWidget):

	def __init__(self,player):
		super().__init__()
		self.initUI(player)
		
	def initUI(self, player):
		layout = QVBoxLayout()
		self.textedit = QPlainTextEdit()
		self.textedit.setPlainText(player.notes)
		self.textedit.textChanged.connect(lambda: self.valUpdate(self.textedit.document().toPlainText(), player))
		layout.addWidget(self.textedit)
		self.setLayout(layout)
		
	def valUpdate(self, text, player):
		player.updateNotes(text)