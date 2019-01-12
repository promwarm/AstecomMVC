from PyQt5 import QtWidgets


class MainController(object):

    def __init__(self, model):
        self.model = model

    #### widget event functions ####

    def change_exit(self, checked):
        self.model.exit = checked
        print(f'DEBUG: change_exit called with arg value: {checked}')

    def change_settings(self, checked):
        self.model.settings = checked
        print(f'DEBUG: change_settings called with arg value: {checked}')

    def change_startjaar(self, index):
        self.model.startjaar = index
        print('DEBUG: change_startjaar called with arg value:', index)

    def change_startmaand(self, index):
        self.model.startmaand = index
        print('DEBUG: change_startmaand called with arg value:', index)

    def change_uurtarief(self, text):
        self.model.uurtarief = text
        print('DEBUG: change_uurtarief called with arg value:', text)

    def change_huur(self, text):
        self.model.huur = text
        print('DEBUG: change_huur called with arg value:', text)

    def change_OK(self, checked):
        self.model.OK = checked
        print('DEBUG: change_OK called with arg value:', checked)

    def change_cancel(self, checked):
        self.model.cancel = checked
        print('DEBUG: change_cancel called with arg value:', checked)