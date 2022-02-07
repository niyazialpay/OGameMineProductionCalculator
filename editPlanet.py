from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QDialog
from db import empire
from main import Ui


class editPlanet(QDialog):

    def __init__(self, *args, **kwargs):
        super(editPlanet, self).__init__(*args, **kwargs)
        uic.loadUi("template/editPlanetName.ui", self)
        self.pushButtonSave.clicked.connect(self.savePlanet)

    def savePlanet(self):
        planet_name = self.lineEditPlanetName.text()
        if len(planet_name) > 0 and planet_name != "":
            empire_db = empire.EmpireDB()
            if empire_db.updatePlanet(self.lineEditPlanetName.text(), self.lineEditCoordinate.text(), self.lineEditID.text()):
                self.close()
            else:
                Ui().messageBox('Planet name already in use', 'Warning', 'Warning')
