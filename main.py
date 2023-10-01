# Import any necessary modules or libraries
import sys
import user_list
import user
import todo
from PyQt5 import QtCore, QtGui, QtWidgets

# vars
main_dir = "./"


class Ui_MainWindow(object):
    def __init__(self):
        self.current_user = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 0, 681, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setObjectName("listWidget")

        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.listWidget.addItem(item)

        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setStrikeOut(True)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget.addItem(item)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName("menuBar")

        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")

        self.menuUsers = QtWidgets.QMenu(self.menuFile)
        self.menuUsers.setObjectName("menuUsers")

        MainWindow.setMenuBar(self.menuBar)

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.actionCreate_User = QtWidgets.QAction(MainWindow)
        self.actionCreate_User.setObjectName("actionCreate_User")

        self.actionUser_1 = QtWidgets.QAction(MainWindow)
        self.actionUser_1.setObjectName("actionUser_1")

        self.actionUser_2 = QtWidgets.QAction(MainWindow)
        self.actionUser_2.setObjectName("actionUser_2")

        self.actionCurrent_User = QtWidgets.QAction(MainWindow)
        self.actionCurrent_User.setEnabled(False)
        self.actionCurrent_User.setObjectName("actionCurrent_User")

        self.menuUsers.addAction(self.actionCreate_User)
        self.menuUsers.addSeparator()
        self.menuUsers.addAction(self.actionUser_1)
        self.menuUsers.addAction(self.actionUser_2)

        self.menuFile.addAction(self.menuUsers.menuAction())
        self.menuFile.addAction(self.actionCurrent_User)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "New Item1"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "New Item2"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuUsers.setTitle(_translate("MainWindow", "Users"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCreate_User.setText(_translate("MainWindow", "Create User"))
        self.actionUser_1.setText(_translate("MainWindow", "User 1"))
        self.actionUser_2.setText(_translate("MainWindow", "User 2"))
        self.actionCurrent_User.setText(_translate("MainWindow", "Current User:"))

    def set_current_user(self, user_id):
        self.current_user = user.select(user_id)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
