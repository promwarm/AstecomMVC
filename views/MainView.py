from PyQt5 import QtWidgets
from gen.ui_MainView import Ui_MainWindow


class MainView(QtWidgets.QMainWindow):

    #### properties for widget value ####

    @property
    def exit(self):
        return self.ui.pushButton_exit.isChecked()

    @exit.setter
    def exit(self, value):
        self.ui.pushButton_exit.setChecked(value)

    @property
    def settings(self):
        return self.ui.pushButton_settings.isChecked()

    @settings.setter
    def settings(self, value):
        self.ui.pushButton_settings.setChecked(value)

    #### properties for widget enabled state ####

    @property
    def exit_enabled(self):
        return self.ui.pushButton_exit.isEnabled()

    @exit_enabled.setter
    def exit_enabled(self, value):
        self.ui.pushButton_exit.setEnabled(value)

    @property
    def settings_enabled(self):
        return self.ui.pushButton_settings.isEnabled()

    @settings_enabled.setter
    def settings_enabled(self, value):
        self.ui.pushButton_settings.setEnabled(value)

    def __init__(self, model, main_ctrl):
        self.model = model
        self.main_ctrl = main_ctrl
        super(MainView, self).__init__()
        self.build_ui()
        # register func with model for model update announcements
        self.model.subscribe_update_func(self.update_ui_from_model)

    def build_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #### set Qt model for compatible widget types ####

        #### connect widget signals to event functions ####
        self.ui.pushButton_exit.clicked.connect(self.on_exit)
        self.ui.pushButton_settings.clicked.connect(self.on_settings)

    def update_ui_from_model(self):
        print('DEBUG: update_ui_from_model called')
        #### update widget values from model ####
        self.exit = self.model.exit
        self.settings = self.model.settings

    #### widget signal event functions ####
    def on_exit(self): self.main_ctrl.change_exit(self.exit)
    def on_settings(self): self.main_ctrl.change_settings(self.settings)

