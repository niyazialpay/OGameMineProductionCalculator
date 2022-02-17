from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from db import empire
import empire as calculate
from db import regex_data
regex = regex_data.regex_data()


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('template/main.ui', self)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("template/img/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.lineEditPlanetName = self.findChild(QtWidgets.QLineEdit, 'lineEditPlanetName')
        self.pushButtonPlanetAdd = self.findChild(QtWidgets.QPushButton, 'pushButtonPlanetAdd')
        self.tableWidgetPlanetList = self.findChild(QtWidgets.QTableWidget, 'tableWidgetPlanetList')

        self.delete_icon = QtGui.QIcon('template/img/delete.png')
        self.edit_icon = QtGui.QIcon('template/img/edit.png')
        self.copy_icon = QtGui.QIcon('template/img/copy.png')

        self.menu = QtWidgets.QMenu()

        self.copy_column_action = self.menu.addAction("Copy")
        self.copy_column_action.setIcon(self.copy_icon)

        self.edit_column_action = self.menu.addAction("Edit Planet")
        self.edit_column_action.setIcon(self.edit_icon)

        self.delete_column_action = self.menu.addAction("Delete Planet")
        self.delete_column_action.setIcon(self.delete_icon)

        self.groupBoxPlanet = self.findChild(QtWidgets.QGroupBox, 'groupBoxPlanet')
        self.groupBoxCurrentPlanet = self.findChild(QtWidgets.QGroupBox, 'groupBoxCurrentPlanet')

        self.lineEditPlanetID = self.findChild(QtWidgets.QLineEdit, 'lineEditPlanetID')

        self.pushButtonSaveResources = self.findChild(QtWidgets.QPushButton, 'pushButtonSaveResources')
        self.pushButtonSaveResources.clicked.connect(self.saveLevels)

        self.comboBoxMetal = self.findChild(QtWidgets.QComboBox, 'comboBoxMetal')
        self.comboBoxCrystal = self.findChild(QtWidgets.QComboBox, 'comboBoxCrystal')
        self.comboBoxDeuterium = self.findChild(QtWidgets.QComboBox, 'comboBoxDeuterium')
        self.comboBoxSolarPlant = self.findChild(QtWidgets.QComboBox, 'comboBoxSolarPlant')
        self.comboBoxFusionReactor = self.findChild(QtWidgets.QComboBox, 'comboBoxFusionReactor')
        self.comboBoxSolarSattelite = self.findChild(QtWidgets.QComboBox, 'comboBoxSolarSattelite')

        self.lineEditMetal = self.findChild(QtWidgets.QLineEdit, 'lineEditMetal')
        self.lineEditCrystal = self.findChild(QtWidgets.QLineEdit, 'lineEditCrystal')
        self.lineEditDeuterium = self.findChild(QtWidgets.QLineEdit, 'lineEditDeuterium')
        self.lineEditSolarPlant = self.findChild(QtWidgets.QLineEdit, 'lineEditSolarPlant')
        self.lineEditFusionReactor = self.findChild(QtWidgets.QLineEdit, 'lineEditFusionReactor')
        self.lineEditSolarSattelite = self.findChild(QtWidgets.QLineEdit, 'lineEditSolarSattelite')
        self.lineEditTemperatureMin = self.findChild(QtWidgets.QLineEdit, 'lineEditTemperatureMin')
        self.lineEditTemperatureMax = self.findChild(QtWidgets.QLineEdit, 'lineEditTemperatureMax')

        self.lineEditMetalItem = self.findChild(QtWidgets.QLineEdit, 'lineEditMetalItem')
        self.lineEditCrystalItem = self.findChild(QtWidgets.QLineEdit, 'lineEditCrystalItem')
        self.lineEditDeuteriumItem = self.findChild(QtWidgets.QLineEdit, 'lineEditDeuteriumItem')
        self.lineEditEnergyItem = self.findChild(QtWidgets.QLineEdit, 'lineEditEnergyItem')
        self.lineEditMetalIncome = self.findChild(QtWidgets.QLineEdit, 'lineEditMetalIncome')
        self.lineEditCrystalIncome = self.findChild(QtWidgets.QLineEdit, 'lineEditCrystalIncome')

        self.lineEditUniverseSpeed = self.findChild(QtWidgets.QLineEdit, 'lineEditUniverseSpeed')
        self.lineEditPlasmaTech = self.findChild(QtWidgets.QLineEdit, 'lineEditPlasmaTech')
        self.lineEditEnergyTech = self.findChild(QtWidgets.QLineEdit, 'lineEditEnergyTech')

        self.checkBoxEngineer = self.findChild(QtWidgets.QCheckBox, 'checkBoxEngineer')
        self.checkBoxGeologist = self.findChild(QtWidgets.QCheckBox, 'checkBoxGeologist')
        self.checkBoxCommandingStaff = self.findChild(QtWidgets.QCheckBox, 'checkBoxCommandingStaff')
        self.checkBoxCollector = self.findChild(QtWidgets.QCheckBox, 'checkBoxCollector')
        self.checkBoxTrader = self.findChild(QtWidgets.QCheckBox, 'checkBoxTrader')
        self.pushButtonSaveGlobalSettings = self.findChild(QtWidgets.QPushButton, 'pushButtonSaveGlobalSettings')
        self.pushButtonSaveGlobalSettings.clicked.connect(self.saveUniverseSettings)

        self.tableWidgetPlanetTotal = self.findChild(QtWidgets.QTableWidget, 'tableWidgetPlanetTotal')

        self.comboBoxCrawlerSpeed = self.findChild(QtWidgets.QComboBox, 'comboBoxCrawlerSpeed')
        self.lineEditCrawler = self.findChild(QtWidgets.QLineEdit, 'lineEditCrawler')
        self.label_crawler = self.findChild(QtWidgets.QLabel, 'label_crawler')
        self.comboBoxCrawlerSpeed.setCurrentIndex(5)

    def setupUi(self):
        self.pushButtonPlanetAdd.clicked.connect(self.addPlanet)
        self.planetList()
        self.tableWidgetPlanetList.customContextMenuRequested.connect(self.customContextPlanetList)
        self.tableWidgetPlanetList.setColumnHidden(2, True)
        self.tableWidgetPlanetList.verticalHeader().setVisible(False)
        self.lineEditPlanetName.returnPressed.connect(self.addPlanet)

        self.tableWidgetPlanetList.doubleClicked.connect(self.copyPlanetName)
        self.tableWidgetPlanetList.clicked.connect(self.PlanetLevels)

        self.lineEditPlanetID.setVisible(False)
        self.universeResources()

        self.comboBoxSolarSattelite.currentIndexChanged.connect(self.PlanetResources)
        self.comboBoxSolarPlant.currentIndexChanged.connect(self.PlanetResources)
        self.comboBoxCrystal.currentIndexChanged.connect(self.PlanetResources)
        self.comboBoxDeuterium.currentIndexChanged.connect(self.PlanetResources)
        self.comboBoxFusionReactor.currentIndexChanged.connect(self.PlanetResources)
        self.comboBoxMetal.currentIndexChanged.connect(self.PlanetResources)

        self.lineEditEnergyTech.textChanged.connect(self.PlanetResources)
        self.lineEditSolarSattelite.textChanged.connect(self.PlanetResources)
        self.lineEditSolarPlant.textChanged.connect(self.PlanetResources)
        self.lineEditEnergyItem.textChanged.connect(self.PlanetResources)
        self.lineEditFusionReactor.textChanged.connect(self.PlanetResources)

        self.lineEditMetal.textChanged.connect(self.PlanetResources)
        self.lineEditCrystal.textChanged.connect(self.PlanetResources)
        self.lineEditDeuterium.textChanged.connect(self.PlanetResources)
        self.lineEditTemperatureMin.textChanged.connect(self.PlanetResources)
        self.lineEditTemperatureMax.textChanged.connect(self.PlanetResources)
        self.lineEditMetalIncome.textChanged.connect(self.PlanetResources)
        self.lineEditCrystalIncome.textChanged.connect(self.PlanetResources)
        self.lineEditMetalItem.textChanged.connect(self.PlanetResources)
        self.lineEditCrystalItem.textChanged.connect(self.PlanetResources)
        self.lineEditDeuteriumItem.textChanged.connect(self.PlanetResources)

        self.lineEditUniverseSpeed.textChanged.connect(self.PlanetResources)
        self.lineEditPlasmaTech.textChanged.connect(self.PlanetResources)

        self.checkBoxEngineer.stateChanged.connect(self.PlanetResources)
        self.checkBoxGeologist.stateChanged.connect(self.PlanetResources)
        self.checkBoxCommandingStaff.stateChanged.connect(self.PlanetResources)
        self.checkBoxCollector.stateChanged.connect(self.PlanetResources)
        self.checkBoxTrader.stateChanged.connect(self.PlanetResources)

        self.lineEditCrawler.textChanged.connect(self.PlanetResources)
        self.comboBoxCrawlerSpeed.currentIndexChanged.connect(self.PlanetResources)

        self.allPlanetsTotal()

        if self.tableWidgetPlanetList.rowCount() > 0:
            self.tableWidgetPlanetList.selectRow(0)
            self.PlanetLevels()

        self.show()

    def addPlanet(self):
        planet_name = str(self.lineEditPlanetName.text()).strip()
        if len(planet_name) > 0 and planet_name != "":
            empire_db = empire.EmpireDB()
            insert = empire_db.insertPlanet(planet_name)
            if insert is False:
                self.messageBox('Planet name already in use', 'Warning', 'Warning')
            else:
                self.planetList()
                self.lineEditPlanetName.clear()
        else:
            self.messageBox('Planet name must be required', 'Warning', 'Warning')

    def planetList(self):
        empire_db = empire.EmpireDB()
        planets = empire_db.PlanetList()
        self.tableWidgetPlanetList.setRowCount(0)
        for row_number, row_data in enumerate(planets):
            self.tableWidgetPlanetList.insertRow(row_number)
            self.tableWidgetPlanetList.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(row_data["planet_name"])))
            if row_data["coordinates"] is not None:
                coordinates = str(row_data["coordinates"])
            else:
                coordinates = ""
            self.tableWidgetPlanetList.setItem(row_number, 1, QtWidgets.QTableWidgetItem(coordinates))
            self.tableWidgetPlanetList.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(row_data["id"])))

    def customContextPlanetList(self, pos):
        try:
            empire_db = empire.EmpireDB()
            action = self.menu.exec_(self.tableWidgetPlanetList.viewport().mapToGlobal(pos))
            if action == self.delete_column_action:
                reply = QMessageBox().question(self, 'Delete',
                                               "Bu gezegeni silmek istediğinizden emin misiniz?\n\n" + self.tableWidgetPlanetList.item(
                                                   self.tableWidgetPlanetList.currentRow(), 0).text(),
                                               QMessageBox().Yes,
                                               QMessageBox().No)

                if reply == QMessageBox().Yes:
                    empire_db.deletePlanet(
                        self.tableWidgetPlanetList.item(self.tableWidgetPlanetList.currentRow(), 2).text())
                self.planetList()

            if action == self.edit_column_action:
                self.editPlanetName()
                self.planetList()

            if action == self.copy_column_action:
                self.copyPlanetName()
        except:
            self.messageBox('You must select a valid row!', 'Warning', 'Warning')

    def editPlanetName(self):
        from editPlanet import editPlanet
        empire_db = empire.EmpireDB()
        planet = empire_db.Planet(self.tableWidgetPlanetList.item(self.tableWidgetPlanetList.currentRow(), 2).text())
        w = editPlanet()
        w.lineEditPlanetName.setText(planet["planet_name"])
        if planet["coordinates"] is not None:
            coordinates = str(planet["coordinates"])
        else:
            coordinates = ""
        w.lineEditCoordinate.setText(coordinates)
        w.lineEditID.setText(str(planet["id"]))
        w.lineEditID.setVisible(False)
        w.exec_()

    def copyPlanetName(self):
        import clipboard
        clipboard.copy(self.tableWidgetPlanetList.item(self.tableWidgetPlanetList.currentRow(),
                                                       0).text() + " - " + self.tableWidgetPlanetList.item(
            self.tableWidgetPlanetList.currentRow(), 1).text())
        self.messageBox("Planet name has been copied to clipboard.", "Informatin", "Information")

    def PlanetLevels(self):
        empire_db = empire.EmpireDB()
        planet = empire_db.Planet(self.tableWidgetPlanetList.item(self.tableWidgetPlanetList.currentRow(), 2).text())
        self.groupBoxPlanet.setTitle(planet["planet_name"])
        self.groupBoxCurrentPlanet.setTitle(planet["planet_name"])
        self.lineEditPlanetID.setText(str(planet["id"]))

        levels = empire_db.planetLevels(str(planet["id"]))

        if levels is not None:
            self.lineEditMetal.setText(str(levels["metal_mine"]))
            self.lineEditCrystal.setText(str(levels["crystal_mine"]))
            self.lineEditDeuterium.setText(str(levels["deuterium_mine"]))
            self.lineEditSolarSattelite.setText(str(levels["solar_sattelite"]))
            self.lineEditSolarPlant.setText(str(levels["solar_plant"]))
            self.lineEditFusionReactor.setText(str(levels["fusion_reactor"]))
            self.lineEditTemperatureMin.setText(str(levels["planet_temperature_min"]))
            self.lineEditTemperatureMax.setText(str(levels["planet_temperature_max"]))
            self.lineEditMetalItem.setText(str(levels["metal_item"]))
            self.lineEditCrystalItem.setText(str(levels["crystal_item"]))
            self.lineEditDeuteriumItem.setText(str(levels["deuterium_item"]))
            self.lineEditEnergyItem.setText(str(levels["energy_item"]))
            self.lineEditMetalIncome.setText(str(levels["metal_main_income"]))
            self.lineEditCrystalIncome.setText(str(levels["crystal_main_income"]))
            self.lineEditCrawler.setText(str(levels["crawler"]))
            self.label_crawler.setText("Crawler (" + str(
                (int(levels["metal_mine"]) + int(levels["crystal_mine"]) + int(levels["deuterium_mine"])) * 8) + ")")

            # production speeds
            if levels["metal_speed"] == 100:
                metal_index = 0
            elif levels["metal_speed"] == 90:
                metal_index = 1
            elif levels["metal_speed"] == 80:
                metal_index = 2
            elif levels["metal_speed"] == 70:
                metal_index = 3
            elif levels["metal_speed"] == 60:
                metal_index = 4
            elif levels["metal_speed"] == 50:
                metal_index = 5
            elif levels["metal_speed"] == 40:
                metal_index = 6
            elif levels["metal_speed"] == 30:
                metal_index = 7
            elif levels["metal_speed"] == 20:
                metal_index = 8
            elif levels["metal_speed"] == 10:
                metal_index = 9
            elif levels["metal_speed"] == 0:
                metal_index = 10
            else:
                metal_index = 0
            self.comboBoxMetal.setCurrentIndex(metal_index)

            if levels["crystal_speed"] == 100:
                crystal_index = 0
            elif levels["crystal_speed"] == 90:
                crystal_index = 1
            elif levels["crystal_speed"] == 80:
                crystal_index = 2
            elif levels["crystal_speed"] == 70:
                crystal_index = 3
            elif levels["crystal_speed"] == 60:
                crystal_index = 4
            elif levels["crystal_speed"] == 50:
                crystal_index = 5
            elif levels["crystal_speed"] == 40:
                crystal_index = 6
            elif levels["crystal_speed"] == 30:
                crystal_index = 7
            elif levels["crystal_speed"] == 20:
                crystal_index = 8
            elif levels["crystal_speed"] == 10:
                crystal_index = 9
            elif levels["crystal_speed"] == 0:
                crystal_index = 10
            else:
                crystal_index = 0
            self.comboBoxCrystal.setCurrentIndex(crystal_index)

            if levels["deuterium_speed"] == 100:
                deuterium_index = 0
            elif levels["deuterium_speed"] == 90:
                deuterium_index = 1
            elif levels["deuterium_speed"] == 80:
                deuterium_index = 2
            elif levels["deuterium_speed"] == 70:
                deuterium_index = 3
            elif levels["deuterium_speed"] == 60:
                deuterium_index = 4
            elif levels["deuterium_speed"] == 50:
                deuterium_index = 5
            elif levels["deuterium_speed"] == 40:
                deuterium_index = 6
            elif levels["deuterium_speed"] == 30:
                deuterium_index = 7
            elif levels["deuterium_speed"] == 20:
                deuterium_index = 8
            elif levels["deuterium_speed"] == 10:
                deuterium_index = 9
            elif levels["deuterium_speed"] == 0:
                deuterium_index = 10
            else:
                deuterium_index = 0
            self.comboBoxDeuterium.setCurrentIndex(deuterium_index)

            if levels["solar_plant_speed"] == 100:
                solar_plant_index = 0
            elif levels["solar_plant_speed"] == 90:
                solar_plant_index = 1
            elif levels["solar_plant_speed"] == 80:
                solar_plant_index = 2
            elif levels["solar_plant_speed"] == 70:
                solar_plant_index = 3
            elif levels["solar_plant_speed"] == 60:
                solar_plant_index = 4
            elif levels["solar_plant_speed"] == 50:
                solar_plant_index = 5
            elif levels["solar_plant_speed"] == 40:
                solar_plant_index = 6
            elif levels["solar_plant_speed"] == 30:
                solar_plant_index = 7
            elif levels["solar_plant_speed"] == 20:
                solar_plant_index = 8
            elif levels["solar_plant_speed"] == 10:
                solar_plant_index = 9
            elif levels["solar_plant_speed"] == 0:
                solar_plant_index = 10
            else:
                solar_plant_index = 0
            self.comboBoxSolarPlant.setCurrentIndex(solar_plant_index)

            if levels["fusion_speed"] == 100:
                fusion_index = 0
            elif levels["fusion_speed"] == 90:
                fusion_index = 1
            elif levels["fusion_speed"] == 80:
                fusion_index = 2
            elif levels["fusion_speed"] == 70:
                fusion_index = 3
            elif levels["fusion_speed"] == 60:
                fusion_index = 4
            elif levels["fusion_speed"] == 50:
                fusion_index = 5
            elif levels["fusion_speed"] == 40:
                fusion_index = 6
            elif levels["fusion_speed"] == 30:
                fusion_index = 7
            elif levels["fusion_speed"] == 20:
                fusion_index = 8
            elif levels["fusion_speed"] == 10:
                fusion_index = 9
            elif levels["fusion_speed"] == 0:
                fusion_index = 10
            else:
                fusion_index = 0
            self.comboBoxFusionReactor.setCurrentIndex(fusion_index)

            if levels["solar_sattelite_speed"] == 100:
                solar_sattelite_index = 0
            elif levels["solar_sattelite_speed"] == 90:
                solar_sattelite_index = 1
            elif levels["solar_sattelite_speed"] == 80:
                solar_sattelite_index = 2
            elif levels["solar_sattelite_speed"] == 70:
                solar_sattelite_index = 3
            elif levels["solar_sattelite_speed"] == 60:
                solar_sattelite_index = 4
            elif levels["solar_sattelite_speed"] == 50:
                solar_sattelite_index = 5
            elif levels["solar_sattelite_speed"] == 40:
                solar_sattelite_index = 6
            elif levels["solar_sattelite_speed"] == 30:
                solar_sattelite_index = 7
            elif levels["solar_sattelite_speed"] == 20:
                solar_sattelite_index = 8
            elif levels["solar_sattelite_speed"] == 10:
                solar_sattelite_index = 9
            elif levels["solar_sattelite_speed"] == 0:
                solar_sattelite_index = 10
            else:
                solar_sattelite_index = 0
            self.comboBoxSolarSattelite.setCurrentIndex(solar_sattelite_index)

            if levels["crawler_speed"] == 150:
                crawler_index = 0
            elif levels["crawler_speed"] == 140:
                crawler_index = 1
            elif levels["crawler_speed"] == 130:
                crawler_index = 2
            elif levels["crawler_speed"] == 120:
                crawler_index = 3
            elif levels["crawler_speed"] == 110:
                crawler_index = 4
            elif levels["crawler_speed"] == 100:
                crawler_index = 5
            elif levels["crawler_speed"] == 90:
                crawler_index = 6
            elif levels["crawler_speed"] == 80:
                crawler_index = 7
            elif levels["crawler_speed"] == 70:
                crawler_index = 8
            elif levels["crawler_speed"] == 60:
                crawler_index = 9
            elif levels["crawler_speed"] == 50:
                crawler_index = 10
            elif levels["crawler_speed"] == 40:
                crawler_index = 11
            elif levels["crawler_speed"] == 30:
                crawler_index = 12
            elif levels["crawler_speed"] == 20:
                crawler_index = 13
            elif levels["crawler_speed"] == 10:
                crawler_index = 14
            else:
                crawler_index = 0
            self.comboBoxCrawlerSpeed.setCurrentIndex(crawler_index)

            # production speeds

        self.PlanetResources()
        self.allPlanetsTotal()

    def ResourceCheck(self):
        if len(str(self.lineEditMetal.text()).strip()) == 0:
            metal_mine_level = 0
        else:
            if regex.integer(str(self.lineEditMetal.text()).strip()) == "-":
                metal_mine_level = 0
            else:
                metal_mine_level = int(regex.integer(str(self.lineEditMetal.text()).strip()))

        if len(str(self.lineEditPlasmaTech.text()).strip()) == 0:
            plasma_tech = 0
        else:
            if regex.integer(str(self.lineEditPlasmaTech.text()).strip()) == "-":
                plasma_tech = 0
            else:
                plasma_tech = int(regex.integer(str(self.lineEditPlasmaTech.text()).strip()))

        if len(str(self.lineEditUniverseSpeed.text()).strip()) == 0:
            universe_speed = 1
        else:
            if regex.integer(str(self.lineEditUniverseSpeed.text()).strip()) == "-":
                universe_speed = 1
            else:
                universe_speed = int(regex.integer(str(self.lineEditUniverseSpeed.text()).replace("-", "").strip()))

        if len(str(self.lineEditMetalIncome.text()).strip()) == 0:
            metal_income = 0
        else:
            if regex.integer(str(self.lineEditMetalIncome.text()).strip()) == "-":
                metal_income = 0
            else:
                metal_income = int(regex.integer(str(self.lineEditMetalIncome.text()).strip()))

        if len(str(self.lineEditMetalItem.text()).strip()) == 0:
            metal_item = 0
        else:
            if regex.integer(str(self.lineEditMetalItem.text()).strip()) == "-":
                metal_item = 0
            else:
                metal_item = int(regex.integer(str(self.lineEditMetalItem.text()).strip()))

        metal_speed = int(regex.integer(str(self.comboBoxMetal.currentText()).strip()))

        if len(str(self.lineEditCrystal.text()).strip()) == 0:
            crystal_mine_level = 0
        else:
            if regex.integer(str(self.lineEditCrystal.text()).strip()) == "-":
                crystal_mine_level = 0
            else:
                crystal_mine_level = int(regex.integer(str(self.lineEditCrystal.text()).strip()))

        if len(str(self.lineEditCrystalIncome.text()).strip()) == 0:
            crystal_income = 0
        else:
            if regex.integer(str(self.lineEditCrystalIncome.text()).strip()) == "-":
                crystal_income = 0
            else:
                crystal_income = int(regex.integer(str(self.lineEditCrystalIncome.text()).strip()))

        if len(str(self.lineEditCrystalItem.text()).strip()) == 0:
            crystal_item = 0
        else:
            if regex.integer(str(self.lineEditCrystalItem.text()).strip()) == "-":
                crystal_item = 0
            else:
                crystal_item = int(regex.integer(str(self.lineEditCrystalItem.text()).strip()))

        crystal_speed = int(regex.integer(str(self.comboBoxCrystal.currentText()).strip()))

        if len(str(self.lineEditDeuterium.text()).strip()) == 0:
            deuterium_mine_level = 0
        else:
            if regex.integer(str(self.lineEditDeuterium.text()).strip()) == "-":
                deuterium_mine_level = 0
            else:
                deuterium_mine_level = int(regex.integer(str(self.lineEditDeuterium.text()).strip()))

        deuterium_speed = int(regex.integer(str(self.comboBoxDeuterium.currentText()).strip()))

        if len(str(self.lineEditDeuteriumItem.text()).strip()) == 0:
            deuterium_item = 0
        else:
            if regex.integer(str(self.lineEditDeuteriumItem.text()).strip()) == "-":
                deuterium_item = 0
            else:
                deuterium_item = int(regex.integer(str(self.lineEditDeuteriumItem.text()).strip()))

        fusion_plant_speed = int(regex.integer(str(self.comboBoxFusionReactor.currentText()).strip()))

        if len(str(self.lineEditFusionReactor.text()).strip()) == 0:
            fusion_plant_level = 0
        else:
            if regex.integer(str(self.lineEditFusionReactor.text()).strip()) == "-":
                fusion_plant_level = 0
            else:
                fusion_plant_level = int(regex.integer(str(self.lineEditFusionReactor.text()).strip()))

        if len(str(self.lineEditTemperatureMax.text()).strip()) == 0:
            max_temperature = 0
        else:
            if regex.integer(str(self.lineEditTemperatureMax.text()).strip()) == "-":
                max_temperature = 0
            else:
                max_temperature = int(regex.integer(str(self.lineEditTemperatureMax.text()).strip()))

        if len(str(self.lineEditTemperatureMin.text()).strip()) == 0:
            min_temperature = 0
        else:
            if regex.integer(str(self.lineEditTemperatureMin.text()).strip()) == "-":
                min_temperature = 0
            else:
                min_temperature = int(regex.integer(str(self.lineEditTemperatureMin.text()).strip()))

        if len(str(self.lineEditEnergyItem.text()).strip()) == 0:
            energy_item = 0
        else:
            if regex.integer(str(self.lineEditEnergyItem.text()).strip()) == "-":
                energy_item = 0
            else:
                energy_item = int(regex.integer(str(self.lineEditEnergyItem.text()).strip()))

        if len(str(self.lineEditEnergyTech.text()).strip()) == 0:
            energy_tech = 0
        else:
            if regex.integer(str(self.lineEditEnergyTech.text()).strip()) == "-":
                energy_tech = 0
            else:
                energy_tech = int(regex.integer(str(self.lineEditEnergyTech.text()).strip()))

        if len(str(self.lineEditSolarPlant.text()).strip()) == 0:
            solar_plant_level = 0
        else:
            if regex.integer(str(self.lineEditSolarPlant.text()).strip()) == "-":
                solar_plant_level = 0
            else:
                solar_plant_level = int(regex.integer(str(self.lineEditSolarPlant.text()).strip()))

        if len(str(self.lineEditSolarSattelite.text()).strip()) == 0:
            solar_sattelites = 0
        else:
            if regex.integer(str(self.lineEditSolarSattelite.text()).strip()) == "-":
                solar_sattelites = 0
            else:
                solar_sattelites = int(regex.integer(str(self.lineEditSolarSattelite.text()).strip()))

        if len(str(self.lineEditCrawler.text()).strip()) == 0:
            crawler = 0
        else:
            if regex.integer(str(self.lineEditCrawler.text()).strip()) == "-":
                crawler = 0
            else:
                crawler = int(regex.integer(str(self.lineEditCrawler.text()).strip()))
        crawler_speed = int(regex.integer(str(self.comboBoxCrawlerSpeed.currentText()).strip()))

        return {
            "metal_mine_level": metal_mine_level,
            "crystal_mine_level": crystal_mine_level,
            "deuterium_mine_level": deuterium_mine_level,
            "fusion_plant_level": fusion_plant_level,
            "solar_plant_level": solar_plant_level,
            "universe_speed": universe_speed,
            "plasma_tech": plasma_tech,
            "metal_income": metal_income,
            "metal_speed": metal_speed,
            "metal_item": metal_item,
            "crystal_income": crystal_income,
            "crystal_speed": crystal_speed,
            "crystal_item": crystal_item,
            "deuterium_speed": deuterium_speed,
            "deuterium_item": deuterium_item,
            "fusion_plant_speed": fusion_plant_speed,
            "max_temperature": max_temperature,
            "min_temperature": min_temperature,
            "energy_item": energy_item,
            "energy_tech": energy_tech,
            "solar_sattelites": solar_sattelites,
            "crawler": crawler,
            "crawler_speed": crawler_speed
        }

    def PlanetResources(self):
        try:
            levels = self.ResourceCheck()
            metal_mine_per_hour = calculate.metal_per_hour(
                mine_level=levels["metal_mine_level"],
                commanding_staff=self.checkBoxCommandingStaff.isChecked(),
                plasma_tech=levels["plasma_tech"],
                collector=self.checkBoxCollector.isChecked(),
                trader=self.checkBoxTrader.isChecked(),
                universe_speed=levels["universe_speed"],
                main_income=levels["metal_income"],
                speed=levels["metal_speed"],
                item=levels["metal_item"],
                geologist=self.checkBoxGeologist.isChecked(),
                crawler=levels["crawler"],
                crawler_speed=levels["crawler_speed"]
            )

            crystal_mine_per_hour = calculate.crystal_per_hour(
                mine_level=levels["crystal_mine_level"],
                commanding_staff=self.checkBoxCommandingStaff.isChecked(),
                plasma_tech=levels["plasma_tech"],
                collector=self.checkBoxCollector.isChecked(),
                trader=self.checkBoxTrader.isChecked(),
                universe_speed=levels["universe_speed"],
                main_income=levels["crystal_income"],
                speed=levels["crystal_speed"],
                item=levels["crystal_item"],
                geologist=self.checkBoxGeologist.isChecked(),
                crawler=levels["crawler"],
                crawler_speed=levels["crawler_speed"]
            )

            deuterium_mine_per_hour = calculate.deuterium_per_hour(
                mine_level=levels["deuterium_mine_level"],
                commanding_staff=self.checkBoxCommandingStaff.isChecked(),
                plasma_tech=levels["plasma_tech"],
                collector=self.checkBoxCollector.isChecked(),
                trader=self.checkBoxTrader.isChecked(),
                universe_speed=levels["universe_speed"],
                speed=levels["deuterium_speed"],
                item=levels["deuterium_item"],
                geologist=self.checkBoxGeologist.isChecked(),
                fusion_plant_speed=levels["fusion_plant_speed"],
                fusion_plant_level=levels["fusion_plant_level"],
                temperature_max=levels["max_temperature"],
                temperature_min=levels["min_temperature"],
                crawler=levels["crawler"],
                crawler_speed=levels["crawler_speed"]
            )

            energy_per_hour = calculate.energy_per_hour(
                fusion_plant_level=levels["fusion_plant_level"],
                trader=self.checkBoxTrader.isChecked(),
                collector=self.checkBoxCollector.isChecked(),
                temperature_min=levels["min_temperature"],
                temperature_max=levels["max_temperature"],
                fusion_plant_speed=levels["fusion_plant_speed"],
                crystal_speed=levels["crystal_speed"],
                metal_speed=levels["metal_speed"],
                deuterium_speed=levels["deuterium_speed"],
                metal_mine_level=levels["metal_mine_level"],
                crystal_mine_level=levels["crystal_mine_level"],
                deuterium_mine_level=levels["deuterium_mine_level"],
                commanding_staff=self.checkBoxCommandingStaff.isChecked(),
                engineer=self.checkBoxEngineer.isChecked(),
                item=levels["energy_item"],
                energy_tech=levels["energy_tech"],
                solar_plant_level=levels["solar_plant_level"],
                solar_speed=int(regex.integer(str(self.comboBoxSolarPlant.currentText()).strip())),
                solar_sattelite=levels["solar_sattelites"],
                solar_sattelite_speed=int(regex.integer(str(self.comboBoxSolarSattelite.currentText()).strip())),
                crawler=levels["crawler"],
                crawler_speed=levels["crawler_speed"]
            )

            self.label_crawler.setText("Crawler (" + str(
                (int(levels["metal_mine_level"]) + int(levels["crystal_mine_level"]) + int(levels["deuterium_mine_level"])) * 8) + ")")

            self.tableWidgetPlanetTotal.setItem(0, 0, QtWidgets.QTableWidgetItem(
                str(calculate.format_number(metal_mine_per_hour))))
            self.tableWidgetPlanetTotal.setItem(0, 1, QtWidgets.QTableWidgetItem(
                str(calculate.format_number(crystal_mine_per_hour))))
            self.tableWidgetPlanetTotal.setItem(0, 2, QtWidgets.QTableWidgetItem(
                str(calculate.format_number(deuterium_mine_per_hour))))
            self.tableWidgetPlanetTotal.setItem(0, 3,
                                                QtWidgets.QTableWidgetItem(str(calculate.format_number(energy_per_hour))))

            self.tableWidgetPlanetTotal.setItem(1, 0, QtWidgets.QTableWidgetItem(
                str(calculate.format_number(metal_mine_per_hour * 24))))
            self.tableWidgetPlanetTotal.setItem(1, 1, QtWidgets.QTableWidgetItem(
                str(calculate.format_number(crystal_mine_per_hour * 24))))
            self.tableWidgetPlanetTotal.setItem(1, 2, QtWidgets.QTableWidgetItem(
                str(calculate.format_number(deuterium_mine_per_hour * 24))))
            self.tableWidgetPlanetTotal.setItem(1, 3,
                                                QtWidgets.QTableWidgetItem(str(calculate.format_number(energy_per_hour))))

            self.tableWidgetPlanetTotal.setItem(2, 0, QtWidgets.QTableWidgetItem(
                str(calculate.format_number(metal_mine_per_hour * 24 * 7))))
            self.tableWidgetPlanetTotal.setItem(2, 1, QtWidgets.QTableWidgetItem(
                str(calculate.format_number(crystal_mine_per_hour * 24 * 7))))
            self.tableWidgetPlanetTotal.setItem(2, 2, QtWidgets.QTableWidgetItem(
                str(calculate.format_number(deuterium_mine_per_hour * 24 * 7))))
            self.tableWidgetPlanetTotal.setItem(2, 3,
                                                QtWidgets.QTableWidgetItem(str(calculate.format_number(energy_per_hour))))
        except:
            self.messageBox("You must enter a valid number", "Warning", "Warning")

    def universeResources(self):
        empire_db = empire.EmpireDB()
        universe = empire_db.UniverseSettings()
        if universe is not None:
            self.lineEditEnergyTech.setText(str(universe["energy_tech"]))
            self.lineEditUniverseSpeed.setText(str(universe["economy_speed"]))
            self.lineEditPlasmaTech.setText(str(universe["plasma_tech"]))
            self.checkBoxEngineer.setChecked(universe["engineer"])
            self.checkBoxGeologist.setChecked(universe["geologist"])
            self.checkBoxCommandingStaff.setChecked(universe["commanding_staff"])
            self.checkBoxCollector.setChecked(universe["collector"])
            self.checkBoxTrader.setChecked(universe["trader"])

    def saveUniverseSettings(self):
        universe_speed = self.lineEditUniverseSpeed.text()
        if len(universe_speed) > 0 and universe_speed != "" and int(universe_speed) > 0:
            speed = universe_speed
        else:
            speed = 1
        empire_db = empire.EmpireDB()
        empire_db.saveUniverseSettings({
            "plasma_tech": self.lineEditPlasmaTech.text(),
            "energy_tech": self.lineEditEnergyTech.text(),
            "economy_speed": speed,
            "geologist": self.checkBoxGeologist.isChecked(),
            "engineer": self.checkBoxEngineer.isChecked(),
            "commanding_staff": self.checkBoxCommandingStaff.isChecked(),
            "collector": self.checkBoxCollector.isChecked(),
            "trader": self.checkBoxTrader.isChecked()
        })
        self.allPlanetsTotal()
        self.messageBox("Changes saved!", "Information", "Information")

    def allPlanetsTotal(self):
        empire_db = empire.EmpireDB()
        planets = empire_db.PlanetList()
        settings = empire_db.UniverseSettings()
        metal_mine_per_hour_total = 0
        crystal_mine_per_hour_total = 0
        deuterium_mine_per_hour_total = 0
        energy_per_hour_total = 0
        for planet in planets:
            planet_levels = empire_db.planetLevels(str(planet["id"]))
            metal_mine_per_hour_total += calculate.metal_per_hour(
                mine_level=planet_levels["metal_mine"],
                trader=settings["trader"],
                collector=settings["collector"],
                commanding_staff=settings["commanding_staff"],
                plasma_tech=settings["plasma_tech"],
                geologist=settings["geologist"],
                universe_speed=settings["economy_speed"],
                main_income=planet_levels["metal_main_income"],
                item=planet_levels["metal_item"],
                speed=planet_levels["metal_speed"],
                crawler=planet_levels["crawler"],
                crawler_speed=planet_levels["crawler_speed"]
            )
            crystal_mine_per_hour_total += calculate.crystal_per_hour(
                trader=settings["trader"],
                collector=settings["collector"],
                commanding_staff=settings["commanding_staff"],
                plasma_tech=settings["plasma_tech"],
                geologist=settings["geologist"],
                universe_speed=settings["economy_speed"],
                main_income=planet_levels["crystal_main_income"],
                mine_level=planet_levels["crystal_mine"],
                speed=planet_levels["crystal_speed"],
                item=planet_levels["crystal_item"],
                crawler=planet_levels["crawler"],
                crawler_speed=planet_levels["crawler_speed"]
            )
            deuterium_mine_per_hour_total += calculate.deuterium_per_hour(
                trader=settings["trader"],
                collector=settings["collector"],
                commanding_staff=settings["commanding_staff"],
                plasma_tech=settings["plasma_tech"],
                geologist=settings["geologist"],
                universe_speed=settings["economy_speed"],
                mine_level=planet_levels["deuterium_mine"],
                speed=planet_levels["deuterium_speed"],
                item=planet_levels["deuterium_item"],
                fusion_plant_level=planet_levels["fusion_reactor"],
                fusion_plant_speed=planet_levels["fusion_speed"],
                temperature_min=planet_levels["planet_temperature_min"],
                temperature_max=planet_levels["planet_temperature_max"],
                crawler=planet_levels["crawler"],
                crawler_speed=planet_levels["crawler_speed"]
            )
            energy_per_hour_total += calculate.energy_per_hour(
                trader=settings["trader"],
                collector=settings["collector"],
                commanding_staff=settings["commanding_staff"],
                fusion_plant_level=planet_levels["fusion_reactor"],
                fusion_plant_speed=planet_levels["fusion_speed"],
                temperature_min=planet_levels["planet_temperature_min"],
                temperature_max=planet_levels["planet_temperature_max"],
                item=planet_levels["energy_item"],
                solar_plant_level=planet_levels["solar_plant"],
                solar_sattelite=planet_levels["solar_sattelite"],
                deuterium_speed=planet_levels["deuterium_speed"],
                metal_speed=planet_levels["metal_speed"],
                solar_sattelite_speed=planet_levels["solar_sattelite_speed"],
                solar_speed=planet_levels["solar_plant_speed"],
                crystal_mine_level=planet_levels["crystal_mine"],
                energy_tech=settings["energy_tech"],
                crystal_speed=planet_levels["crystal_speed"],
                metal_mine_level=planet_levels["metal_mine"],
                deuterium_mine_level=planet_levels["deuterium_mine"],
                engineer=settings["engineer"],
                crawler=planet_levels["crawler"],
                crawler_speed=planet_levels["crawler_speed"]
            )

            self.tableWidgetAllPlanetTotal.setItem(0, 0, QtWidgets.QTableWidgetItem(
                str(calculate.format_number(metal_mine_per_hour_total))))
            self.tableWidgetAllPlanetTotal.setItem(0, 1, QtWidgets.QTableWidgetItem(
                str(calculate.format_number(crystal_mine_per_hour_total))))
            self.tableWidgetAllPlanetTotal.setItem(0, 2, QtWidgets.QTableWidgetItem(
                str(calculate.format_number(deuterium_mine_per_hour_total))))
            self.tableWidgetAllPlanetTotal.setItem(0, 3,
                                                   QtWidgets.QTableWidgetItem(
                                                       str(calculate.format_number(energy_per_hour_total))))

            self.tableWidgetAllPlanetTotal.setItem(1, 0, QtWidgets.QTableWidgetItem(
                str(calculate.format_number(metal_mine_per_hour_total * 24))))
            self.tableWidgetAllPlanetTotal.setItem(1, 1, QtWidgets.QTableWidgetItem(
                str(calculate.format_number(crystal_mine_per_hour_total * 24))))
            self.tableWidgetAllPlanetTotal.setItem(1, 2, QtWidgets.QTableWidgetItem(
                str(calculate.format_number(deuterium_mine_per_hour_total * 24))))
            self.tableWidgetAllPlanetTotal.setItem(1, 3,
                                                   QtWidgets.QTableWidgetItem(
                                                       str(calculate.format_number(energy_per_hour_total))))

            self.tableWidgetAllPlanetTotal.setItem(2, 0, QtWidgets.QTableWidgetItem(
                str(calculate.format_number(metal_mine_per_hour_total * 24 * 7))))
            self.tableWidgetAllPlanetTotal.setItem(2, 1, QtWidgets.QTableWidgetItem(
                str(calculate.format_number(crystal_mine_per_hour_total * 24 * 7))))
            self.tableWidgetAllPlanetTotal.setItem(2, 2, QtWidgets.QTableWidgetItem(
                str(calculate.format_number(deuterium_mine_per_hour_total * 24 * 7))))
            self.tableWidgetAllPlanetTotal.setItem(2, 3,
                                                   QtWidgets.QTableWidgetItem(
                                                       str(calculate.format_number(energy_per_hour_total))))

    def saveLevels(self):
        levels = self.ResourceCheck()
        planet_id = self.lineEditPlanetID.text()
        if len(planet_id) > 0 and planet_id != "":
            empire_db = empire.EmpireDB()
            empire_db.planetLevelsUpdate({
                "metal_mine": str(levels["metal_mine_level"]).strip(),
                "crystal_mine": str(levels["metal_mine_level"]).strip(),
                "deuterium_mine": str(levels["deuterium_mine_level"]).strip(),
                "solar_sattelite": str(levels["solar_sattelites"]).strip(),
                "fusion_reactor": str(levels["fusion_plant_level"]).strip(),
                "solar_plant": str(levels["solar_plant_level"]).strip(),
                "planet_temperature_min": str(levels["min_temperature"]).strip(),
                "planet_temperature_max": str(levels["max_temperature"]).strip(),
                "metal_item": str(levels["metal_item"]).strip(),
                "crystal_item": str(levels["crystal_item"]).strip(),
                "deuterium_item": str(levels["deuterium_item"]).strip(),
                "energy_item": str(levels["energy_item"]).strip(),
                "metal_main_income": str(levels["metal_income"]).strip(),
                "crystal_main_income": str(levels["crystal_income"]).strip(),
                "metal_speed": self.comboBoxMetal.currentText().replace("%", ""),
                "crystal_speed": self.comboBoxCrystal.currentText().replace("%", ""),
                "deuterium_speed": self.comboBoxDeuterium.currentText().replace("%", ""),
                "solar_plant_speed": self.comboBoxSolarPlant.currentText().replace("%", ""),
                "fusion_speed": self.comboBoxFusionReactor.currentText().replace("%", ""),
                "solar_sattelite_speed": self.comboBoxSolarSattelite.currentText().replace("%", ""),
                "crawler": str(levels["crawler"]).strip(),
                "crawler_speed": self.comboBoxCrawlerSpeed.currentText().replace("%", ""),
                "planet_id": str(self.lineEditPlanetID.text()).strip()
            })
            self.messageBox("Changes saved!", "Information", "Information")
            self.allPlanetsTotal()
        else:
            self.messageBox("You must select a planet!", "Warning", "Warning")

    def messageBox(self, alert_message, alert_title, alert_icon):
        message = QMessageBox()
        if alert_icon == "Critical":
            message_icon = QMessageBox.Critical
        elif alert_icon == "Warning":
            message_icon = QMessageBox.Warning

        elif alert_icon == "Information":
            message_icon = QMessageBox.Information
        else:
            message_icon = QMessageBox.Critical
        message.setIcon(message_icon)
        message.setText(alert_message)
        message.setWindowTitle(alert_title)
        message.setWindowIcon(self.icon)
        message.exec()


    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit the program?"
        reply = QMessageBox().question(self, 'Exit',
                                       quit_msg, QMessageBox().Yes, QMessageBox().No)

        if reply == QMessageBox().Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui()
    ui.setupUi()
    sys.exit(app.exec_())
