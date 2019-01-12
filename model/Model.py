from PyQt5 import QtCore as Qt


class Model(object):

    #### properties for value of Qt model contents ####

    def __init__(self):
        self._update_funcs = []
        self.config_section = 'settings'
        self.config_options = (
            ('exit', 'getboolean'),
            ('settings', 'getboolean'),
            ('startjaar', 'getint'),
            ('startmaand', 'getint'),
            ('uurtarief', 'get'),
            ('huur', 'get'),
            ('OK', 'getboolean'),
            ('cancel', 'getboolean'),
        )

        #### create Qt models for compatible widget types ####
        self.startjaar_model = Qt.QStringListModel()
        self.startmaand_model = Qt.QStringListModel()

        #### model variables ####
        self.startjaar = None
        self.startmaand = None
        self.uurtarief = None
        self.huur = None
        self.OK = None
        self.cancel = None

        self.exit = None
        self.settings = None

    def subscribe_update_func(self, func):
        if func not in self._update_funcs:
            self._update_funcs.append(func)

    def unsubscribe_update_func(self, func):
        if func in self._update_funcs:
            self._update_funcs.remove(func)

    def announce_update(self):
        for func in self._update_funcs:
            func()



 #### properties for value of Qt model contents ####
    @property
    def startjaar_items(self):
        return self.startjaar_model.stringList()
    @startjaar_items.setter
    def startjaar_items(self, value):
        self.startjaar_model.setStringList(value)
    @property
    def startmaand_items(self):
        return self.startmaand_model.stringList()
    @startmaand_items.setter
    def startmaand_items(self, value):
        self.startmaand_model.setStringList(value)