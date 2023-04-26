import sys
import os
import re
import datetime
import requests
import time
import docx
from word2pdf import Ui_MainWindow
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from win32com.client import constants, gencache, DispatchEx
from aip import AipOcr

# 全局变量
count = 0        # 已转换完成的文件计数器
num_file = 0     # 文件计数器
directory = ''   # 输入文件夹路径
Output_directory = ''  # 输出文件夹路径

# 百度API接口
APP_ID = '23967925'
API_KEY = 'wlZOiK8U3xuumf7xaS8z3XPG'
SECRET_KEY = 'XEYonAZ9Ze7ySVOMvITKhouLICWPQomM'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

class trans(QMainWindow, Ui_MainWindow):  
    def __init__(self, parent=None):
        global directory, count, num_file
        count = 0
        num_file = 0
        super(trans, self).__init__()  
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.progressBar.setValue(0)
        directory = os.getcwd()
        directory = directory.replace('\\', '/')
        self.FilePathText.setPlainText(directory)
        self.OutputFilePathText.setPlainText(directory)
        directory = directory.replace('/', '\\')

        self.word2pdfButton.clicked.connect(self.word2pdfButton_clicked)
        self.excel2pdfButton.clicked.connect(self.excel2pdfButton_clicked)
        self.img2wordButton.clicked.connect(self.img2wordButton_clicked)
        self.img2tableButton.clicked.connect(self.img2tableButton_clicked)
        self.openFileButton.clicked.connect(
            self.openFileButton_clicked)  # 输入文件夹
        self.openOutputFileButton.clicked.connect(
            self.openOutputFileButton_clicked)  # 输出文件夹

    # 选择输入文件夹
    def openFileButton_clicked(self):
        global directory
        global Output_directory

        self.progressBar.setValue(0)
        last_directory = directory.replace('\\', '/')
        directory = QFileDialog.getExistingDirectory(self, '选择输入文件夹', './')
        if directory == "":
            directory = last_directory

        self.FilePathText.setPlainText(directory)
        self.OutputFilePathText.setPlainText(directory)
        directory = directory.replace('/', '\\')
        Output_directory = directory

    # 选择输出文件夹
    def openOutputFileButton_clicked(self):
        global Output_directory

        self.progressBar.setValue(0)
        last_directory = Output_directory.replace('\\', '/')

        Output_directory = QFileDialog.getExistingDirectory(
            self, '选择输出文件夹', './')
        if Output_directory == "":
            Output_directory = last_directory

        self.OutputFilePathText.setPlainText(Output_directory)
        Output_directory = Output_directory.replace('/', '\\')

    # word转pdf
    def word2pdf(self, wordPath, pdfPath):
        word = gencache.EnsureDispatch('Word.Application')
        word.DisplayAlerts = False
        doc = word.Documents.Open(wordPath, ReadOnly=1)
        doc.ExportAsFixedFormat(pdfPath,
                                constants.wdExportFormatPDF,
                                OptimizeFor=constants.wdExportOptimizeForPrint,
                                Item=constants.wdExportDocumentWithMarkup,
                                CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
        doc.Close(False)
        word.Quit(constants.wdDoNotSaveChanges)

    # excel转pdf
    def excel2pdf(self, excelPath, pdfPath):
        xlApp = gencache.EnsureDispatch('Excel.Application')
        xlApp.DisplayAlerts = False
        # xlApp = DispatchEx('Excel.Application')
        xls = xlApp.Workbooks.Open(excelPath, ReadOnly=1)
        xls.ExportAsFixedFormat(
            0, pdfPath, Quality=constants.xlQualityStandard, IgnorePrintAreas=False)
        xls.Close(False)
        xlApp.Quit()

    # word转pdf按钮事件
    def word2pdfButton_clicked(self):
        self.word2pdfButton.setEnabled(False)
        self.excel2pdfButton.setEnabled(False)
        self.img2wordButton.setEnabled(False)
        self.img2tableButton.setEnabled(False)

        self.progressBar.setValue(0)
        QApplication.processEvents()
        for dirs, subdirs, files in os.walk(directory):
            for name in files:
                if re.search(r'\.(doc|docx)', name):
                    if re.search(r'\~\$', name):
                        pass
                    else:
                        global num_file
                        num_file += 1
        if num_file == 0:
            self.textBrowser.setPlainText('未找到Word文件，请确认文件路径')
        else:
            self.textBrowser.setPlainText(
                ("共找到 %d 个Word文件，开始转换" % (num_file)))
            for dirs, subdirs, files in os.walk(directory):
                for name in files:
                    if re.search(r'\.(doc|docx)', name):
                        if re.search(r'\~\$', name):
                            pass
                        else:
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
        self.img2wordButton.setEnabled(True)
        self.img2tableButton.setEnabled(True)

    # excel转pdf按钮
    def excel2pdfButton_clicked(self):
        self.word2pdfButton.setEnabled(False)
        self.excel2pdfButton.setEnabled(False)
        self.img2wordButton.setEnabled(False)
        self.img2tableButton.setEnabled(False)

        self.progressBar.setValue(0)
        QApplication.processEvents()
        for dirs, subdirs, files in os.walk(directory):
            for name in files:
                if re.search(r'\.(xlsx|xls)', name):
                    if re.search(r'\~\$', name):
                        pass
                    else:
                        global num_file
                        num_file += 1
        if num_file == 0:
            self.textBrowser.setPlainText('未找到Excel文件，请确认文件路径')
        else:
            self.textBrowser.setPlainText(
                ("共找到 %d 个Excel文件，开始转换" % (num_file)))
            for dirs, subdirs, files in os.walk(directory):
                for name in files:
                    if re.search(r'\.(xlsx|xls)', name):
                        if re.search(r'\~\$', name):
                            pass
                        else:
                            global count
                            count = count + 1
                            time1 = datetime.datetime.now()  # 获取当前时间
                            self.textBrowser.append(
                                ("第 %d / %d 个文件转换中..." % (count, num_file)))
                            self.textBrowser.moveCursor(
                                self.textBrowser.textCursor().End)  # 文本框显示到底部
                            QApplication.processEvents()
                            self.excel2pdf(dirs+'\\'+name, dirs+'\\' +
                                           re.subn('(xlsx|xls)', 'pdf', name)[0])
                            self.progressBar.setValue(count / num_file * 100)
                            time2 = datetime.datetime.now()  # 获取当前时间
                            time = time2 - time1 + \
                                datetime.timedelta(seconds=10)
                            self.textBrowser.append(
                                "转换完成,耗时%d秒" % time.seconds)
            self.textBrowser.append('所有文件转换完成')
            self.progressBar.setValue(100)
        count = 0
        num_file = 0
        self.word2pdfButton.setEnabled(True)
        self.excel2pdfButton.setEnabled(True)
        self.img2wordButton.setEnabled(True)
        self.img2tableButton.setEnabled(True)

    # 图片文字识别按钮
    def img2wordButton_clicked(self):
        self.word2pdfButton.setEnabled(False)
        self.excel2pdfButton.setEnabled(False)
        self.img2wordButton.setEnabled(False)
        self.img2tableButton.setEnabled(False)
        self.progressBar.setValue(0)
        self.textBrowser.setPlainText("识别图片文字")
        QApplication.processEvents()

        for dirs, subdirs, files in os.walk(directory):
            for name in files:
                if re.search(r'\.(jpg|png)', name):
                    global num_file
                    num_file += 1

        if num_file == 0:
            self.textBrowser.append('未找到图片，请确认输入文件路径')
            QApplication.processEvents()
        else:
            self.textBrowser.append(
                ("共找到 %d 个图片，开始识别" % (num_file)))
            QApplication.processEvents()
            for dirs, subdirs, files in os.walk(directory):
                for name in files:
                    if re.search(r'\.(jpg|png)', name):
                        global count
                        count += 1
                        file_path = dirs+'\\'+name
                        fp = open(file_path, 'rb')
                        result = client.basicGeneral(fp.read())
                        str = ''
                        try:
                            for w in result['words_result']:
                                str = str.__add__(w['words'])
                        except KeyError:
                            self.textBrowser.append('接口出错，请重试')
                        else:
                            pass
                        str = str.__add__('\n')
                        self.textBrowser.append('第 %d 张图片 %s 识别结果' % (count, name))
                        self.textBrowser.append(str)
                        QApplication.processEvents()
                        # 写入word文件
                        file = docx.Document()
                        file.add_paragraph(str)
                        file_path = ''
                        file_path = dirs+'\\'+name
                        file_path = file_path.replace('jpg', 'docx')
                        file_path = file_path.replace('png', 'docx')
                        file.save(file_path)
                        self.progressBar.setValue(count / num_file * 100)
            self.textBrowser.append('所有图片识别完成')
            self.progressBar.setValue(100)
        count = 0
        num_file = 0
        
        self.word2pdfButton.setEnabled(True)
        self.excel2pdfButton.setEnabled(True)
        self.img2wordButton.setEnabled(True)
        self.img2tableButton.setEnabled(True)

    # 图片文字表格按钮
    def img2tableButton_clicked(self):
        self.word2pdfButton.setEnabled(False)
        self.excel2pdfButton.setEnabled(False)
        self.img2wordButton.setEnabled(False)
        self.img2tableButton.setEnabled(False)
        self.progressBar.setValue(0)
        self.textBrowser.setPlainText("识别图片表格")
        QApplication.processEvents()

        for dirs, subdirs, files in os.walk(directory):
            for name in files:
                if re.search(r'\.(jpg|png)', name):
                    global num_file
                    num_file += 1

        if num_file == 0:
            self.textBrowser.append('未找到图片，请确认输入文件路径')
            QApplication.processEvents()
        else:
            self.textBrowser.append(
                ("共找到 %d 个图片，开始识别" % (num_file)))
            QApplication.processEvents()
            for dirs, subdirs, files in os.walk(directory):
                for name in files:
                    if re.search(r'\.(jpg|png)', name):
                        global count
                        count += 1
                        file_path = dirs+'\\'+name
                        fp = open(file_path, 'rb')
                        result = client.tableRecognitionAsync(fp.read())
                        req_id = result['result'][0]['request_id']  # 获取识别ID号
                        # OCR识别也需要一定时间，设定10秒内每隔1秒查询一次
                        for time_count in range(1, 20):
                            result = client.getTableRecognitionResult(
                                req_id)  # 通过ID获取表格文件XLS地址
                            try:
                                if result['result']['ret_msg'] == '已完成':
                                    break  # 云端处理完毕，成功获取表格文件下载地址，跳出循环
                                else:
                                    time.sleep(1)
                            except  KeyError:
                                self.textBrowser.append('接口出错，请重试')
                                break
                        url = result['result']['result_data']
                        file_path = ''
                        file_path = dirs+'\\'+name
                        file_path = file_path.replace('jpg', 'xls')
                        file_path = file_path.replace('png', 'xls')
                        r = requests.get(url)
                        with open(file_path, 'wb') as f:
                            f.write(r.content)

                        self.textBrowser.append('第 %d 张图片 %s 识别完成' % (count, name))
                        QApplication.processEvents()
                        self.progressBar.setValue(count / num_file * 100)
            self.textBrowser.append('所有图片识别完成')
            self.progressBar.setValue(100)
        count = 0
        num_file = 0
        
        self.word2pdfButton.setEnabled(True)
        self.excel2pdfButton.setEnabled(True)
        self.img2wordButton.setEnabled(True)
        self.img2tableButton.setEnabled(True)


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    MainWindow = trans()
    MainWindow.show()
    sys.exit(app.exec_())
