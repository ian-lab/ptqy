import sys
import os
import re
from word2pdf import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from win32com.client import constants, gencache

count = 0
num_file = 0
directory = ''


class trans(QMainWindow, Ui_MainWindow):  # 继承自父类QtWidgets.QMainWindow
    def __init__(self, parent=None):
        global directory, count, num_file
        count = 0
        num_file = 0
        super(trans, self).__init__()  # 因为继承关系，要对父类初始化
        # 通过super初始化父类，__init__()函数无self，若直接QtWidgets.QMainWindow).__init__(self)，括号里是有self的
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.progressBar.setValue(0)
        directory = os.getcwd()
        directory = directory.replace('\\', '/')
        self.FilePathText.setPlainText(directory)
        directory = directory.replace('/', '\\')

        self.word2pdfButton.clicked.connect(self.word2pdfButton_clicked)
        self.excel2pdfButton.clicked.connect(self.excel2pdfButton_clicked)
        self.openFileButton.clicked.connect(self.openFileButton_clicked)

    def openFileButton_clicked(self):
        global directory
        self.progressBar.setValue(0)
        last_directory = directory.replace('\\', '/')
        directory = QFileDialog.getExistingDirectory(self, '选择文件夹', './')
        if directory == "":
            directory = last_directory

        self.FilePathText.setPlainText(directory)
        directory = directory.replace('/', '\\')
        # self.FilePathText.append(directory)
    # word转pdf

    def word2pdf(self, wordPath, pdfPath):
        word = gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(wordPath, ReadOnly=1)
        doc.ExportAsFixedFormat(pdfPath,
                                constants.wdExportFormatPDF,
                                OptimizeFor=constants.wdExportOptimizeForPrint,
                                Item=constants.wdExportDocumentWithMarkup,
                                CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
        word.Quit(constants.wdDoNotSaveChanges)

    # excel转pdf
    def excel2pdf(self, excelPath, pdfPath):
        xlApp = gencache.EnsureDispatch('Excel.Application')
        xls = xlApp.Workbooks.Open(excelPath, ReadOnly=1)
        xls.ExportAsFixedFormat(
            0, pdfPath, Quality=constants.xlQualityStandard, IgnorePrintAreas=False)
        xlApp.Quit()

    # word转pdf按钮事件
    def word2pdfButton_clicked(self):
        self.word2pdfButton.setEnabled(False)
        self.excel2pdfButton.setEnabled(False)
        self.progressBar.setValue(0)
        QApplication.processEvents()
        for dirs, subdirs, files in os.walk(directory):
            for name in files:
                global num_file
                if re.search('\.(doc|docx)', name):
                    num_file += 1
        if num_file == 0:
            self.textBrowser.setPlainText('未找到Word文件，请确认文件路径')
        else:
            self.textBrowser.setPlainText(
                ("共找到 %d 个Word文件，开始转换" % (num_file)))
            for dirs, subdirs, files in os.walk(directory):
                for name in files:
                    if re.search('\.(doc|docx)', name):
                        global count
                        count = count + 1
                        self.textBrowser.append(
                            ("第 %d / %d 个文件转换中..." % (count, num_file)))
                        self.textBrowser.moveCursor(
                            self.textBrowser.textCursor().End)  # 文本框显示到底部
                        QApplication.processEvents()
                        self.word2pdf(dirs+'\\'+name, dirs+'\\' +
                                      re.subn('(docx|doc)', 'pdf', name)[0])
                        self.progressBar.setValue(count / num_file * 100)

            self.textBrowser.append('转换完成')
            self.progressBar.setValue(100)
        count = 0
        num_file = 0
        self.word2pdfButton.setEnabled(True)
        self.excel2pdfButton.setEnabled(True)

    # excel转pdf按钮
    def excel2pdfButton_clicked(self):
        self.word2pdfButton.setEnabled(False)
        self.excel2pdfButton.setEnabled(False)
        self.progressBar.setValue(0)
        QApplication.processEvents()
        for dirs, subdirs, files in os.walk(directory):
            for name in files:
                global num_file
                if re.search('\.(xlsx|xls)', name):
                    num_file += 1
        if num_file == 0:
            self.textBrowser.setPlainText('未找到Excel文件，请确认文件路径')
        else:
            self.textBrowser.setPlainText(
                ("共找到 %d 个Excel文件，开始转换" % (num_file)))
            for dirs, subdirs, files in os.walk(directory):
                for name in files:
                    if re.search('\.(xlsx|xls)', name):
                        global count
                        count = count + 1
                        self.textBrowser.append(
                            ("第 %d / %d 个文件转换中..." % (count, num_file)))
                        self.textBrowser.moveCursor(
                            self.textBrowser.textCursor().End)  # 文本框显示到底部
                        QApplication.processEvents()
                        self.excel2pdf(dirs+'\\'+name, dirs+'\\' +
                                       re.subn('(xlsx|xls)', 'pdf', name)[0])
                        self.progressBar.setValue(count/num_file*100)
            self.textBrowser.append('转换完成')
            self.progressBar.setValue(100)
        count = 0
        num_file = 0
        self.word2pdfButton.setEnabled(True)
        self.excel2pdfButton.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = trans()
    MainWindow.show()
    sys.exit(app.exec_())
