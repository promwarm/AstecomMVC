from PyQt5 import QtWidgets
# from gen.ui_MainView import Ui_MainWindow # OLD
from gen.ui_SettingsView import Ui_Dialog


class SettingsView(QtWidgets.QMainWindow):

    #### properties for widget value ####
    @property
    def startjaar(self):
        return self.ui.comboBox_startjaar.currentIndex()

    @startjaar.setter
    def startjaar(self, value):
        self.ui.comboBox_startjaar.setCurrentIndex(value)

    @property
    def startmaand(self):
        return self.ui.comboBox_startmaand.currentIndex()
    @startmaand.setter
    def startmaand(self, value):
        self.ui.comboBox_startmaand.setCurrentIndex(value)
    @property
    def uurtarief(self):
        return self.ui.lineEdit_uurtarief.text()
    @uurtarief.setter
    def uurtarief(self, value):
        self.ui.lineEdit_uurtarief.setText(value)
    @property
    def huur(self):
        return self.ui.lineEdit_huur.text()
    @huur.setter
    def huur(self, value):
        self.ui.lineEdit_huur.setText(value)
    @property
    def OK(self):
        return self.ui.pushButton_OK.isChecked()
    @OK.setter
    def OK(self, value):
        self.ui.pushButton_OK.setChecked(value)
    @property
    def cancel(self):
        return self.ui.pushButton_cancel.isChecked()
    @cancel.setter
    def cancel(self, value):
        self.ui.pushButton_cancel.setChecked(value)

    #### properties for widget enabled state ####
    @property
    def startjaar_enabled(self):
        return self.ui.comboBox_startjaar.isEnabled()
    @startjaar_enabled.setter
    def startjaar_enabled(self, value):
        self.ui.comboBox_startjaar.setEnabled(value)
    @property
    def startmaand_enabled(self):
        return self.ui.comboBox_startmaand.isEnabled()
    @startmaand_enabled.setter
    def startmaand_enabled(self, value):
        self.ui.comboBox_startmaand.setEnabled(value)
    @property
    def uurtarief_enabled(self):
        return self.ui.lineEdit_uurtarief.isEnabled()
    @uurtarief_enabled.setter
    def uurtarief_enabled(self, value):
        self.ui.lineEdit_uurtarief.setEnabled(value)
    @property
    def huur_enabled(self):
        return self.ui.lineEdit_huur.isEnabled()
    @huur_enabled.setter
    def huur_enabled(self, value):
        self.ui.lineEdit_huur.setEnabled(value)
    @property
    def OK_enabled(self):
        return self.ui.pushButton_OK.isEnabled()
    @OK_enabled.setter
    def OK_enabled(self, value):
        self.ui.pushButton_OK.setEnabled(value)
    @property
    def cancel_enabled(self):
        return self.ui.pushButton_cancel.isEnabled()
    @cancel_enabled.setter
    def cancel_enabled(self, value):
        self.ui.pushButton_cancel.setEnabled(value)

    def __init__(self, model, main_ctrl):
        self.model = model
        self.main_ctrl = main_ctrl
        super(SettingsView, self).__init__()
        self.build_ui()

        # register func with model for model update announcements
        self.model.subscribe_update_func(self.update_ui_from_model)

        # Set defauls
        self.setDefaults(main_ctrl)
        self.update_ui_from_model()

    def setDefaults(self, controller):
        controller.change_startjaar(1)
        controller.change_startmaand(1)
        controller.change_uurtarief('86.40')
        controller.change_huur('3000' )
        controller.change_OK(True)
        controller.change_cancel(False)

    def build_ui(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #### set Qt model for compatible widget types ####
        self.ui.comboBox_startjaar.setModel(self.model.startjaar_model)
        self.ui.comboBox_startmaand.setModel(self.model.startmaand_model)

        #### connect widget signals to event functions ####
        self.ui.comboBox_startjaar.currentIndexChanged.connect(self.on_startjaar)
        self.ui.comboBox_startmaand.currentIndexChanged.connect(self.on_startmaand)
        self.ui.lineEdit_uurtarief.textEdited.connect(self.on_uurtarief)
        self.ui.lineEdit_huur.textEdited.connect(self.on_huur)
        self.ui.pushButton_OK.clicked.connect(self.on_OK)
        self.ui.pushButton_cancel.clicked.connect(self.on_cancel)

    def update_ui_from_model(self):
        print(f'DEBUG: update_ui_from_model called')
        #### update widget values from model ####
        self.startjaar = self.model.startjaar
        self.startmaand = self.model.startmaand
        self.uurtarief = self.model.uurtarief
        self.huur = self.model.huur
        self.OK = self.model.OK
        self.cancel = self.model.cancel

    #### widget signal event functions ####
    def on_startjaar(self, index): self.main_ctrl.change_startjaar(index)
    def on_startmaand(self, index): self.main_ctrl.change_startmaand(index)
    def on_uurtarief(self, text): self.main_ctrl.change_uurtarief(text)
    def on_huur(self, text): self.main_ctrl.change_huur(text)
    def on_OK(self): self.main_ctrl.change_OK(self.OK)
    def on_cancel(self): self.main_ctrl.change_cancel(self.cancel)