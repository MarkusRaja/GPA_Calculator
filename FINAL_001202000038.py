from PyQt5.QtWidgets import (QApplication, QWidget, QTableWidget, QTableWidgetItem, QFormLayout, QPushButton, QLabel, QMessageBox, QLineEdit)

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(290, 458)
        self.setWindowTitle("GPA Calculator")
        self.flayout = QFormLayout()
        self.setLayout(self.flayout)
        self.add_button = QPushButton("Add Subject")
        self.calcgpa = QPushButton("Calculate GPA")
        self.rowrmv = QLineEdit()
        self.rowrmv.setPlaceholderText("Num of Row")
        self.rmv_row = QPushButton("Row Remove")
        
        self.cdtionbtn = 0
        self.labelst = QLabel("Result:")
        self.labelnd = QLabel("")

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Subject", "Score"])
        self.flayout.addRow(self.add_button)
        self.flayout.addRow(self.rowrmv, self.rmv_row)
        self.flayout.addRow(self.calcgpa)
        
        self.flayout.addRow(self.table)
        self.flayout.addRow(self.labelst, self.labelnd)
        self.gradeA = 0
        self.gradeAmin = 0
        self.gradeBplus = 0
        self.gradeB = 0
        self.gradeBmin = 0
        self.gradeCplus = 0
        self.gradeC = 0
        self.gradeD = 0
        self.gradeE = 0
        self.totalIndex = 0
        self.totalCredit = 0
        self.GPA = 0
        self.msgbox = QMessageBox()
        self.add_button.clicked.connect(self.addRow)
        self.rmv_row.clicked.connect(self.rmvRow)
        self.calcgpa.clicked.connect(self.func_gpa)
        
        self.table.itemChanged.connect(self.on_type)
    def addRow(self):
        rowCount = self.table.rowCount()
        self.table.insertRow(rowCount)
    def rmvRow(self):
        if self.rowrmv.text().isnumeric():
            if self.cdtionbtn == 1:
                self.labelst.setText("Result:")
                self.labelnd.setText("")
                self.flayout.removeRow(self.showltrgrd)
                self.cdtionbtn = 0
            rowidx = int(self.rowrmv.text())
            rowidx -= 1
            self.table.removeRow(rowidx)
    def showletter(self):
        self.windownd = LetterWin(self)
        self.windownd.show()
    def func_gpa(self):
        self.gradeA = 0
        self.gradeAmin = 0
        self.gradeBplus = 0
        self.gradeB = 0
        self.gradeBmin = 0
        self.gradeCplus = 0
        self.gradeC = 0
        self.gradeD = 0
        self.gradeE = 0
        self.totalIndex = 0
        self.totalCredit = 0
        self.GPA = 0
        for row in range(0, self.table.rowCount()):
            scoretemp = self.table.item(row, 1)
            if scoretemp and scoretemp.text() != "":
                fltscoretemp = float(scoretemp.text())
                if fltscoretemp >= 85:
                    self.calca(fltscoretemp)
                elif fltscoretemp >= 80 and fltscoretemp < 85:
                    self.calcamin(fltscoretemp)
                elif fltscoretemp >= 75 and fltscoretemp < 80:
                    self.calcbplus(fltscoretemp)
                elif fltscoretemp >= 70 and fltscoretemp < 75:
                    self.calcb(fltscoretemp)
                elif fltscoretemp >= 67 and fltscoretemp < 70:
                    self.calcbmin(fltscoretemp)
                elif fltscoretemp >= 64 and fltscoretemp < 67:
                    self.calccplus(fltscoretemp)
                elif fltscoretemp >= 60 and fltscoretemp < 64:
                    self.calcc(fltscoretemp)
                elif fltscoretemp >= 55 and fltscoretemp < 60:
                    self.calcd(fltscoretemp)
                elif fltscoretemp >= 0 and fltscoretemp < 55:
                    self.calce(fltscoretemp)
        self.GPA = self.totalIndex / self.totalCredit
        self.labelst.setText("Result:\nA\nA-\nB+\nB\nB-\nC+\nC\nD\nE\nTotal Index\nTotal Credit\nCumulative GPA")
        self.labelnd.setText("\n:%i\n:%i\n:%i\n:%i\n:%i\n:%i\n:%i\n:%i\n:%i\n:%.2f\n:%i\n:%.2f" %(self.gradeA, self.gradeAmin, self.gradeBplus, self.gradeB, self.gradeBmin, self.gradeCplus, self.gradeC, self.gradeD, self.gradeE, self.totalIndex, self.totalCredit, self.GPA))
        self.cdtionbtn = 1
        self.showltrgrd = QPushButton("Show Detail of Letter Grades")
        self.flayout.addRow(self.showltrgrd)
        self.showltrgrd.clicked.connect(self.showletter)
        
    def calca(self, fltscoretemp):
        self.gradeA += 1
        self.totalIndex += (float(4*3))
        self.totalCredit += 3
    def calcamin(self, fltscoretemp):
        self.gradeAmin += 1
        self.totalIndex += (3.67 * 3)
        self.totalCredit += 3
    def calcbplus(self, fltscoretemp):
        self.gradeBplus += 1
        self.totalIndex += (3.33 * 3)
        self.totalCredit += 3
    def calcb(self, fltscoretemp):
        self.gradeB += 1
        self.totalIndex += float((3 * 3))
        self.totalCredit += 3
    def calcbmin(self, fltscoretemp):
        self.gradeBmin += 1
        self.totalIndex += (2.67 * 3)
        self.totalCredit += 3
    def calccplus(self, fltscoretemp):
        self.gradeCplus += 1
        self.totalIndex += (2.33 * 3)
        self.totalCredit += 3
    def calcc(self, fltscoretemp):
        self.gradeC += 1
        self.totalIndex += float((2 * 3))
        self.totalCredit += 3
    def calcd(self, fltscoretemp):
        self.gradeD += 1
        self.totalIndex += float((1 * 3))
        self.totalCredit += 3
    def calce(self, fltscoretemp):
        self.gradeE += 1
        self.totalCredit += 3
    def on_type(self, item):
        row = item.row()
        col = item.column()
        if col == 1 and not item.text().isnumeric():
            item.setText("")
            self.labelst.setText("ERROR")
            self.labelnd.setText("")
            if self.cdtionbtn == 1:
                self.flayout.removeRow(self.showltrgrd)
                self.cdtionbtn = 0
            self.msgbox.setWindowTitle("Error 01")
            self.msgbox.setText("Hey Input in Numeric for This Column Please!! or the score Doesn't be Under 0 or the score doesn't be empty(but don't worry the system will skip empty score)")
            self.msgbox.show()
        elif col == 1 and item.text().isnumeric():
            if int(item.text()) > 100:
                item.setText("")
                if self.cdtionbtn == 1:
                    self.flayout.removeRow(self.showltrgrd)
                    self.cdtionbtn = 0
                self.labelst.setText("ERROR")
                self.labelnd.setText("")
                self.msgbox.setWindowTitle("Error 02")
                self.msgbox.setText("Hey the score just for 100 - 0")
                self.msgbox.show()
            elif self.cdtionbtn == 1:
                self.labelst.setText("Result:")
                self.labelnd.setText("")
                self.flayout.removeRow(self.showltrgrd)
                self.cdtionbtn = 0
            elif self.cdtionbtn == 0:
                self.labelst.setText("Result:")
                self.labelnd.setText("")
class LetterWin(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.resize(300, 250)
        self.setWindowTitle("Letter Grades per-Subject")
        self.flayoutnd = QFormLayout()
        self.setLayout(self.flayoutnd)
        self.windowst = parent
        self.sublabel = QLabel("")
        self.grdlabel = QLabel("")
        self.flayoutnd.addRow(self.sublabel, self.grdlabel)
        self.showletterfunc()
    def showletterfunc(self):
        strsub = ""
        lettergrd = ""
        for row in range(0, self.windowst.table.rowCount()):
            subname = self.windowst.table.item(row, 0)
            scoretemp = self.windowst.table.item(row, 1)
            if scoretemp and scoretemp.text() != "":
                strsub += "%s\n" % (subname.text())
                fltscoretemp = float(scoretemp.text())
                if fltscoretemp >= 85:
                    lettergrd += ":A\n"
                elif fltscoretemp >= 80 and fltscoretemp < 85:
                    lettergrd += ":A-\n"
                elif fltscoretemp >= 75 and fltscoretemp < 80:
                    lettergrd += ":B+\n"
                elif fltscoretemp >= 70 and fltscoretemp < 75:
                    lettergrd += ":B\n"
                elif fltscoretemp >= 67 and fltscoretemp < 70:
                    lettergrd += ":B-\n"
                elif fltscoretemp >= 64 and fltscoretemp < 67:
                    lettergrd += ":C+\n"
                elif fltscoretemp >= 60 and fltscoretemp < 64:
                    lettergrd += ":C\n"
                elif fltscoretemp >= 55 and fltscoretemp < 60:
                    lettergrd += ":D\n"
                elif fltscoretemp >= 0 and fltscoretemp < 55:
                    lettergrd += ":E\n"
        strsub += "Cumulative GPA"
        if self.windowst.GPA >= 4:
            lettergrd += ":A"
        elif self.windowst.GPA >= 3.67 and self.windowst.GPA < 4:
            lettergrd += ":A-"
        elif self.windowst.GPA >= 3.33 and self.windowst.GPA < 3.67:
            lettergrd += ":B+"
        elif self.windowst.GPA >= 3 and self.windowst.GPA < 3.33:
            lettergrd += ":B"
        elif self.windowst.GPA >= 2.67 and self.windowst.GPA < 3:
            lettergrd += ":B-"
        elif self.windowst.GPA >= 2.33 and self.windowst.GPA < 2.67:
            lettergrd += ":C+"
        elif self.windowst.GPA >= 2 and self.windowst.GPA < 2.33:
            lettergrd += ":C"
        elif self.windowst.GPA >= 1 and self.windowst.GPA < 2:
            lettergrd += ":D"
        elif self.windowst.GPA >= 0 and self.windowst.GPA < 1:
            lettergrd += ":E"
        self.sublabel.setText(strsub)
        self.grdlabel.setText(lettergrd)

app = QApplication([])
window = Window()
window.show()
app.exec_()