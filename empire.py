import math


def metal_per_hour(
        mine_level,
        universe_speed,
        item,
        speed,
        trader,
        collector,
        plasma_tech,
        main_income,
        geologist,
        commanding_staff,
        crawler,
        crawler_speed
):
    base_value = round(30 * mine_level * pow(1.1, mine_level) * universe_speed * speed / 100)
    if main_income > 240:
        base_value = round(30 * mine_level * pow(1.1, mine_level) * universe_speed * speed / 100) * (main_income / 240)
    collector_value = round(base_value * 0.25)
    trader_value = round(base_value * 0.05)
    item_value = round(base_value * item / 100)
    plasma_tech_value = round(base_value * plasma_tech * 0.01)
    geologist_value = round(base_value * 0.1)
    crawler_value = base_value * 0.0002 * crawler * crawler_speed / 100
    commanding_staff_value = base_value * 0.02

    if trader:
        base_value += trader_value
    if collector:
        base_value += collector_value
        crawler_value = crawler_value * 1.5
    if item > 0:
        base_value += item_value
    if plasma_tech > 0:
        base_value += plasma_tech_value
    if geologist and commanding_staff is False:
        base_value += geologist_value
    if (geologist and commanding_staff) or (geologist is False and commanding_staff):
        base_value += geologist_value + commanding_staff_value

    return base_value + main_income + crawler_value


def crystal_per_hour(
        mine_level,
        universe_speed,
        item,
        speed,
        trader,
        collector,
        plasma_tech,
        main_income,
        geologist,
        commanding_staff,
        crawler,
        crawler_speed
):
    base_value = round(20 * mine_level * pow(1.1, mine_level) * universe_speed * speed / 100)
    if main_income > 120:
        base_value = round(20 * mine_level * pow(1.1, mine_level) * universe_speed * speed / 100) * (main_income / 120)
    collector_value = round(base_value * 0.25)
    trader_value = round(base_value * 0.05)
    item_value = round(base_value * item / 100)
    plasma_tech_value = round(base_value * plasma_tech * 0.0066)
    geologist_value = round(base_value * 0.1)
    crawler_value = base_value * 0.0002 * crawler * crawler_speed / 100
    commanding_staff_value = base_value * 0.02

    if trader:
        base_value += trader_value
    if collector:
        base_value += collector_value
        crawler_value = crawler_value * 1.5
    if item > 0:
        base_value += item_value
    if plasma_tech > 0:
        base_value += plasma_tech_value
    if geologist and commanding_staff is False:
        base_value += geologist_value
    if (geologist and commanding_staff) or (geologist is False and commanding_staff):
        base_value += geologist_value + commanding_staff_value

    return base_value + main_income + crawler_value


def deuterium_per_hour(
        mine_level,
        universe_speed,
        item,
        speed,
        trader,
        collector,
        plasma_tech,
        temperature_min,
        temperature_max,
        fusion_plant_level,
        fusion_plant_speed,
        geologist,
        commanding_staff,
        crawler,
        crawler_speed
):
    base_value = round(
        10 * mine_level * pow(1.1, mine_level) * (-0.004 * avarage_temperature(temperature_min,
                                                                               temperature_max) + 1.36) * universe_speed * speed / 100)
    collector_value = round(base_value * 0.25)
    trader_value = round(base_value * 0.05)
    item_value = round(base_value * item / 100)
    plasma_tech_value = round(base_value * plasma_tech * 0.0033)
    geologist_value = round(base_value * 0.1)
    crawler_value = base_value * 0.0002 * crawler * crawler_speed / 100
    commanding_staff_value = base_value * 0.02

    if trader:
        base_value += trader_value
    if collector:
        base_value += collector_value
        crawler_value = crawler_value * 1.5
    if item > 0:
        base_value += item_value
    if plasma_tech > 0:
        base_value += plasma_tech_value
    if geologist and commanding_staff is False:
        base_value += geologist_value
    if (geologist and commanding_staff) or (geologist is False and commanding_staff):
        base_value += geologist_value + commanding_staff_value

    return base_value + fusionPlantDeuterium(fusion_plant_level, universe_speed, fusion_plant_speed) + crawler_value


def fusionPlantDeuterium(plant_level, universe_speed, speed):
    return math.ceil(-10 * plant_level * pow(1.1, plant_level) * universe_speed * speed / 100)


def avarage_temperature(min_temp, max_temp):
    return (min_temp + max_temp) / 2


def energy_per_hour(
        solar_plant_level,
        item,
        solar_speed,
        trader,
        collector,
        energy_tech,
        temperature_min,
        temperature_max,
        fusion_plant_level,
        fusion_plant_speed,
        solar_sattelite,
        solar_sattelite_speed,
        engineer,
        commanding_staff,
        metal_mine_level,
        crystal_mine_level,
        deuterium_mine_level,
        metal_speed,
        crystal_speed,
        deuterium_speed,
        crawler,
        crawler_speed
):
    solar_plant_base_value = math.floor(20 * solar_plant_level * pow(1.1, solar_plant_level) * solar_speed / 100)

    fusion_plant_base_value = math.floor(
        30 * fusion_plant_level * pow((1.05 + energy_tech * 0.01), fusion_plant_level) * fusion_plant_speed / 100)

    solar_sattelite_base_value = round(
        (math.floor((avarage_temperature(temperature_min,
                                         temperature_max) + 160) / 6) * solar_sattelite_speed / 100) * solar_sattelite)

    total_energy = solar_sattelite_base_value + fusion_plant_base_value + solar_plant_base_value

    engineer_value = math.floor(solar_plant_base_value * 0.1) + math.floor(fusion_plant_base_value * 0.1) + math.floor(
        solar_sattelite_base_value * 0.1)

    collector_value = math.floor(solar_plant_base_value * 0.1) + math.floor(fusion_plant_base_value * 0.1) + math.floor(
        solar_sattelite_base_value * 0.1)

    trader_value = math.floor(solar_plant_base_value * 0.05) + math.ceil(fusion_plant_base_value * 0.05) + math.floor(
        solar_sattelite_base_value * 0.05)

    item_value = math.ceil(solar_plant_base_value * item / 100) + math.floor(
        fusion_plant_base_value * item / 100) + math.floor(solar_sattelite_base_value * item / 100)

    commanding_staff_value = (solar_plant_base_value * 0.02) + (fusion_plant_base_value * 0.02) + (
                solar_sattelite_base_value * 0.02)

    if trader:
        total_energy += trader_value
    if collector:
        total_energy += collector_value
    if item > 0:
        total_energy += item_value
    if engineer and commanding_staff is False:
        total_energy += engineer_value
    if (engineer and commanding_staff) or (engineer is False and commanding_staff):
        total_energy += engineer_value + commanding_staff_value

    if crawler_speed > 100:
        crawler_energy = round((50 * crawler * (crawler_speed - 100) / 100) * 2) + round(50 * crawler)
    else:
        crawler_energy = round(50 * crawler * crawler_speed / 100)

    energy_consumption = metal_crystal_mine_power(metal_mine_level, metal_speed) + metal_crystal_mine_power(
        crystal_mine_level, crystal_speed) + deuterium_mine_power(deuterium_mine_level,
                                                                  deuterium_speed) + crawler_energy

    return total_energy - energy_consumption


def metal_crystal_mine_power(mine_level, speed):
    return math.floor(10 * mine_level * pow(1.1, mine_level) * speed / 100)


def deuterium_mine_power(mine_level, speed):
    base_value = math.floor(20 * mine_level * pow(1.1, mine_level) * speed / 100)
    return base_value


def format_number(number):
    import locale
    locale.setlocale(locale.LC_ALL, 'tr_TR')
    return str(locale.format_string('%10.2f', number, True))
