from PyQt5.QtWidgets import QWidget QVBoxLayout

class PlayerWidget(QWidget):

	def __init__(self,stats):
		self.stats = stats
		super().__init__()
		self.initUI()
		
	def initUI(self):
	
		for stat in stats:
		
class StatWidget(QWidget):
	
	def __init__(self, name, buff):
		self.name = name
		self.buff = buff
		super().__init__()
		self.initUI()
		
	def initUI(self):
		statText = QLineEdit(self.buff, self)
		rollButton = QPushButton("Roll", self)
		display = QLCDNumber(self)
		
		vbox = QVBoxLayout(self)
		vbox.addWidget(statText)
		vbox.addWidget(rollButton)
		vbox.addWidget(display)
		
		groupBox = QGroupBox(self.name,self)
		groupBox.addLayout(vbox)
		
		layout = QHBoxLayout(self)
		layout.addWidget(groupBox)
		
		self.setLayout(layout)