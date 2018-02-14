import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PlayerWidget import PlayerWidget

if __name__ == '__main__':

	app = QApplication(sys.argv)

	w = QWidget()
	w.setWindowTitle('Caves & Cheese')
	statfile = open("Paul.cnc")
	player = PlayerWidget(statfile)
	layout=QVBoxLayout()
	layout.addWidget(player)
	w.setLayout(layout)
	w.move(300,500)
	w.resize(0,w.height())
	w.show()
	sys.exit(app.exec_())