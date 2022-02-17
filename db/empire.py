import os
import sqlite3
from db import regex_data

regex = regex_data.regex_data()


class EmpireDB:

    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.__db_file = dir_path + "/empire.db"
        self.__connection = sqlite3.connect(self.__db_file, check_same_thread=False)
        self.__connection.row_factory = sqlite3.Row
        self.__db = self.__connection.cursor()

    def __del__(self):
        self.__db.close()
        self.__connection.close()

    def PlanetList(self):
        self.__db.execute("SELECT * FROM planets order by id asc")
        result = self.__db.fetchall()
        if result is not None:
            return result
        else:
            return None

    def Planet(self, planetID):
        self.__db.execute("select * from planets where id=" + str(regex.integer(planetID)))
        result = self.__db.fetchone()
        if result is not None:
            result.keys()
            return result
        else:
            return None

    def PlanetNameCheck(self, planet_name, planet_id=None):
        if planet_id is not None:
            sql = "select * from planets where planet_name='" + str(regex.string(planet_name)) + "' and id!=" + str(planet_id)
        else:
            sql = "select * from planets where planet_name='" + str(regex.string(planet_name)) + "'"
        self.__db.execute(sql)
        result = self.__db.fetchone()
        if result is not None:
            result.keys()
            return result
        else:
            return None

    def insertPlanet(self, planet_name):
        if self.PlanetNameCheck(planet_name) is None:
            self.__db.execute("insert into planets (planet_name) values('" + planet_name + "')")

            last_planet = self.PlanetNameCheck(planet_name)

            self.__db.execute("insert into planet_levels (planet_id) values(" + str(last_planet["id"]) + ")")
            self.__connection.commit()
            return True
        else:
            return False

    def deletePlanet(self, planet_id):
        self.__db.execute("delete from planets where id=" + str(regex.integer(planet_id)))
        self.__db.execute("delete from planet_levels where planet_id=" + str(regex.integer(planet_id)))
        self.__connection.commit()

    def updatePlanet(self, planet_name, coordinates, planet_id):
        if self.PlanetNameCheck(planet_name, planet_id) is None:
            self.__db.execute("update planets set planet_name='" + regex.string(planet_name) + "', coordinates='" + regex.string(coordinates) + "' where id=" + str(
                regex.integer(planet_id)))
            self.__connection.commit()
            return True
        else:
            return False

    def planetLevelsUpdate(self, values):
        self.__db.execute(
            "update planet_levels set metal_mine=" + str(
                regex.integer(values["metal_mine"])) + ", crystal_mine=" + str(
                regex.integer(values["crystal_mine"])) + ", deuterium_mine=" + str(
                regex.integer(values["deuterium_mine"])) + ", solar_sattelite=" + str(
                regex.integer(values["solar_sattelite"])) + ", fusion_reactor=" + str(
                regex.integer(values["fusion_reactor"])) + " , solar_plant=" + str(
                regex.integer(values["solar_plant"])) + ", planet_temperature_min=" + str(
                regex.integer(values["planet_temperature_min"])) +", planet_temperature_max=" + str(
                regex.integer(values["planet_temperature_max"])) + ", metal_item=" + str(
                regex.integer(values["metal_item"])) + ", crystal_item=" + str(
                regex.integer(values["crystal_item"])) + ", deuterium_item=" + str(
                regex.integer(values["deuterium_item"])) + ", energy_item=" + str(
                regex.integer(values["energy_item"])) + ", metal_main_income=" + str(
                regex.integer(values["metal_main_income"])) + ", crystal_main_income=" + str(
                regex.integer(values["crystal_main_income"])) + ", metal_speed=" + str(
                regex.integer(values["metal_speed"])) + ", crystal_speed=" + str(
                regex.integer(values["crystal_speed"])) + ", deuterium_speed=" + str(
                regex.integer(values["deuterium_speed"])) + ", solar_plant_speed=" + str(
                regex.integer(values["solar_plant_speed"])) + ", fusion_speed=" + str(
                regex.integer(values["fusion_speed"])) + ", solar_sattelite_speed=" + str(regex.integer(values["solar_sattelite_speed"])) + ", crawler=" + str(regex.integer(values["crawler"])) + ", crawler_speed=" + str(regex.integer(values["crawler_speed"])) + " where planet_id=" +
            str(regex.integer(values["planet_id"]))
        )
        self.__connection.commit()

    def planetLevels(self, planet_id):
        self.__db.execute("select * from planet_levels where planet_id=" + str(regex.integer(planet_id)))
        result = self.__db.fetchone()
        if result is not None:
            result.keys()
            return result
        else:
            return None

    def saveUniverseSettings(self, values):
        self.__db.execute("update research_and_officers set plasma_tech=" + str(regex.integer(values["plasma_tech"])) + ", energy_tech=" + str(regex.integer(values["energy_tech"])) + ", economy_speed=" + str(regex.integer(values["economy_speed"])) + ", geologist=" + str(regex.check_bool(values["geologist"])) + ", engineer=" + str(regex.check_bool(values["engineer"])) + ", commanding_staff=" + str(regex.check_bool(values["commanding_staff"])) + ", collector=" + str(regex.check_bool(values["collector"])) + ", trader=" + str(regex.check_bool(values["trader"])) + " where id=1")
        self.__connection.commit()

    def UniverseSettings(self):
        self.__db.execute("select * from research_and_officers where id=1")
        result = self.__db.fetchone()
        if result is not None:
            result.keys()
            return result
        else:
            return None