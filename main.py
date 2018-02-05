import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(600, 800)
    w.setWindowTitle('Caves & Cheese')
    w.show()
    
    sys.exit(app.exec_())