from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from ui_BrowserUI import Ui_Form
import sys


class moWidget(QtWidgets.QWidget):
    def __init__(self):
        super(moWidget, self).__init__()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()


class browserUI(moWidget, Ui_Form):
    def __init__(self):
        super(browserUI, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showMinimized)
        self.pushButton_2.clicked.connect(self.winShowMaximized)
        self.pushButton_3.clicked.connect(sys.exit)
        self.lineEdit.returnPressed.connect(self.load)
        self.pushButton_4.clicked.connect(self.reload)
        self.pushButton_5.clicked.connect(self.forward)
        self.pushButton_6.clicked.connect(self.backward)

    def load(self):
        url = QtCore.QUrl.fromUserInput(self.lineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)

    def backward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)

    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)

    def reload(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Reload)

    def winShowMaximized(self):
        if self.pushButton_2.isChecked():
            self.widget.setStyleSheet(
                "QWidget#widget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(20, 20, 20, 255), stop:0 rgba(20, 20, 20, 255), stop:0.711864 rgba(46, 46, 46, 255), stop:1 rgba(45, 45, 45, 255));border:0px solid rgb(45,45,45);border-radius:0px;}")
            self.showMaximized()
        else:
            self.widget.setStyleSheet(
                "QWidget#widget{border:4px solid rgb(45,45,45);border-radius:20px;}")
            self.showNormal()

# Este codigo  funciona para mostrar el browser


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = browserUI()
    # ui = Ui_Form()
    # ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
