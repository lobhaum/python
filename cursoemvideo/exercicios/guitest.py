import sys

from PySide import QtGui

app = QtGui.Qapplication(sys.argv)
win = QtGui.QWidget()
win.resize(320, 240)
win.setWindowTitle('Olá! Mundo.')
win.show()
sys.exit(app.exec_())
