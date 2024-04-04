import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from batch_renamer_ui import Ui_MainWindow
import batch_renamer_starter


class BatchRenamerWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.browseBtn.clicked.connect(self.get_filepath)
        self.runBtn.clicked.connect(self.run_renamer)
        # Initialize the batch renamer object
        self.batch_renamer = batch_renamer_starter.BatchRenamer()  # Assuming the class is named BatchRenamer
        self.showNormal()

    def get_filepath(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:  # Only update if a directory was selected
            self.filepath = directory
            self.set_filepath()

    def set_filepath(self):
        self.filepathEdit.setText(self.filepath)  # Display the selected directory in the UI
        self.update_list()

    def update_list(self):
        # Update the file list display based on the selected directory
        self.listWidget.clear()
        if os.path.exists(self.filepath):
            for filename in os.listdir(self.filepath):
                self.listWidget.addItem(filename)

    def gather_parameters(self):
        # Gather all renaming parameters from the UI
        self.batch_renamer.filepath = self.filepathEdit.text()
        self.batch_renamer.new_folder = self.newFolderEdit.text()
        self.batch_renamer.copy_files = self.copy.isChecked()
        self.batch_renamer.overwrite = self.forceoverwrite.isChecked()
        self.batch_renamer.filetypes = self.filetypes.text().split(',')
        self.batch_renamer.strings_to_find = self.stringstofind.text().split(',')
        self.batch_renamer.string_to_replace = self.stringstoreplace.text()
        self.batch_renamer.prefix = self.prefix.text()
        self.batch_renamer.suffix = self.suffix_2.text()

    def run_renamer(self):
        # This assumes that the correct name of the widget is `filepathEdit`, 
        # `newFolderEdit`, `filetypes`, `stringsToFindEdit`, and so on.
        filepath = self.filepathEdit.text()
        new_folder = self.newFolderEdit.text()
        copy_files = self.copyCheckBox.isChecked()  # Assuming you have a checkbox named copyCheckBox
        copy_files = self.copyFilesCheckBox.isChecked()  # Update to the correct name
        overwrite = self.overwriteCheckBox.isChecked()  # Assuming you have a checkbox named overwriteCheckBox
        filetypes = self.filetypesEdit.text().split(',')  # Split by comma for multiple filetypes
        strings_to_find = self.stringsToFindEdit.text().split(',')  # Assuming a naming pattern
        string_to_replace = self.stringToReplaceEdit.text()
        prefix = self.prefixEdit.text()
        suffix = self.suffixEdit.text()

        # Verbose can be set based on another UI element or hard-coded for now
        verbose = True  # or False, based on your application's needs

        # Assuming process_folder_with_params function is ready to be used with these parameters
        try:
            batch_renamer_starter.process_folder_with_params(
                filepath=filepath,
                new_folder=new_folder,
                copy_files=copy_files,
                overwrite=overwrite,
                filetypes=filetypes,
                strings_to_find=strings_to_find,
                string_to_replace=string_to_replace,
                prefix=prefix,
                suffix=suffix,
                verbose=verbose
            )
            print("Renaming completed successfully.")
        except Exception as e:
            print(f"Error during renaming: {e}")
        finally:
            self.update_list()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BatchRenamerWindow()
    sys.exit(app.exec())
