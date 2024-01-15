import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel, QLineEdit
from file_save_dialog import FileSaveDialog
from messages_counter import MessagesCounter
import time

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.waiting_for_input = True

        self.selected_folder_path = None
        self.selected_save_path = None
        self.selected_user_identity = None

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Facebook Message Counter ALPHA')

        self.label_title = QLabel('Count your Facebook messages', self)
        
        self.button_select_folder = QPushButton('Select folder', self)
        self.button_select_folder.clicked.connect(self.showFolderChooseDialog)
        self.label_selectedFolder = QLabel(f'Selected folder: None', self)

        self.button_save_place = QPushButton('Select where to save', self)
        self.button_save_place.clicked.connect(self.showSaveDialog)
        self.label_save_place = QLabel(f'Selected save path: None', self)

        self.label_identity = QLabel('Enter your name and surname', self)
        self.identity_textbox = QLineEdit(self)

        self.button_generate_raport = QPushButton('Generate raport', self)
        self.button_generate_raport.clicked.connect(self.generateRaport)

        self.label_status = QLabel('Status: Ready to generate', self)
        self.button_open_file = QPushButton('Open txt file', self)
        self.button_open_file.clicked.connect(self.openFile)
        self.button_open_file.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_title)
        vbox.addWidget(self.button_select_folder)
        vbox.addWidget(self.label_selectedFolder)
        vbox.addWidget(self.button_save_place)
        vbox.addWidget(self.label_save_place)
        vbox.addWidget(self.label_identity)
        vbox.addWidget(self.identity_textbox)          
        vbox.addWidget(self.button_generate_raport)
        vbox.addWidget(self.label_status)
        vbox.addWidget(self.button_open_file)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.show()


    def showFolderChooseDialog(self):
        self.resetStatus()

        dialog = QFileDialog.getExistingDirectory(self, 'Select a folder')

        if dialog:
            self.selected_folder_path = dialog
            self.label_selectedFolder.setText(f'Selected folder: {self.selected_folder_path}')


    def showSaveDialog(self):
        self.resetStatus()

        dialog = FileSaveDialog()

        if dialog.path_name:
            self.selected_save_path = dialog.path_name
            self.label_save_place.setText(f'Selected save path: {self.selected_save_path}')

    
    def validateUserIdentity(self):
        identity = self.identity_textbox.text().strip()

        if len(identity.split()) == 2:
            self.selected_user_identity = identity
        
    
    def generateRaport(self):
        self.label_status.setText(f'Status: Loading...')
        self.validateUserIdentity()

        if self.selected_user_identity and self.selected_folder_path and self.selected_save_path:           
            mc = MessagesCounter(self.selected_user_identity, self.selected_folder_path, self.selected_save_path)

            if mc.generate_data():
                self.waiting_for_input = False
                self.label_status.setText(f'Status: Success')
                self.button_open_file.setEnabled(True)
            else:
                self.label_status.setText(f'Status: Failure')
        else:
            self.label_status.setText(f'Status: Ivalid data')


    def openFile(self):
        try:
            os.system(f'notepad.exe {self.selected_save_path}.txt')
        except Exception as e:
            print(f"Error: {e}")


    def resetStatus(self):
        if not self.waiting_for_input:
            self.selected_folder_path = None
            self.selected_save_path = None
            self.selected_user_identity = None

            self.label_save_place.setText(f'Selected save path: None')
            self.label_selectedFolder.setText(f'Selected folder: None')
            self.identity_textbox.clear()

            self.label_status.setText(f'Status: ready to generate')
            self.button_open_file.setEnabled(False)

            self.waiting_for_input = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenu()
    sys.exit(app.exec_())