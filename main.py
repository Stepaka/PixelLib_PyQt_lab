# import pixellib
# from pixellib.tune_bg import alter_bg
# import os
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
#
# change_bg = alter_bg(model_type = "pb")
# change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
# change_bg.change_bg_img(f_image_path ="img/I.jpg", b_image_path ="img/background.jpg", output_image_name="new_img.jpg")
import shutil
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic.properties import QtWidgets
from PIL import Image, ImageDraw
from ai import object_detection_on_an_image, obj_change_background


from gui import *
import sys


def find():
    if ui.lineEdit.text():
        List = [ui.checkBox.isChecked(),ui.checkBox_2.isChecked(),ui.checkBox_3.isChecked()]
        print(List)
        ui.lineEdit_2.setText(object_detection_on_an_image(ui.lineEdit.text(), List))
        ui.label.setPixmap(QtGui.QPixmap('output.jpg'))

def change():
    if ui.lineEdit.text() and ui.lineEdit_3.text():
        List = [ ui.checkBox.isChecked() ,ui.checkBox_2.isChecked(),ui.checkBox_3.isChecked()]
        print(List)
        ui.lineEdit_2.setText(obj_change_background(ui.lineEdit.text(), ui.lineEdit_3.text(), List))
        ui.label.setPixmap(QtGui.QPixmap('output.jpg'))

def brows_file_main():
    try:
        fpath = QFileDialog.getOpenFileNames(caption='Open file')[0][0]
        ui.lineEdit.setText(fpath)
        ui.label.setPixmap(QtGui.QPixmap(fpath))
        print(fpath)
    except:
        print('ERROR brows_file_main')


def brows_file_background():
    try:
        fpath = QFileDialog.getOpenFileNames(caption='Open file')[0][0]
        ui.lineEdit_3.setText(fpath)
        # ui.label.setPixmap(QtGui.QPixmap(fpath))
        print(fpath)
    except:
        print('ERROR brows_file_background')

def save_file():
    try:
        fpath_save = QFileDialog.getSaveFileName(filter='Images (*.jpg)')[0]

        shutil.copy('output.jpg', fpath_save)
    except:
        print('ERROR save_file')


if __name__ == "__main__":
    List = {}
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.pushButton.clicked.connect(find)
    ui.pushButton_2.clicked.connect(brows_file_main)
    ui.pushButton_3.clicked.connect(brows_file_background)
    ui.pushButton_4.clicked.connect(save_file)
    ui.pushButton_5.clicked.connect(change)


    sys.exit(app.exec_())