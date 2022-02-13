import math


def metal_per_hour(
        mine_level,
        universe_speed,
        item,
        speed,
        merchant,
        collector,
        plasma_tech,
        main_income,
        geologist,
        recruit_officers,
        pallets,
        pallets_speed
):
    base_value = round(30 * mine_level * pow(1.1, mine_level) * universe_speed * speed / 100)
    if main_income > 240:
        base_value = round(30 * mine_level * pow(1.1, mine_level) * universe_speed * speed / 100) * (main_income / 240)
    collector_value = round(base_value * 0.25)
    merchant_value = round(base_value * 0.05)
    item_value = round(base_value * item / 100)
    plasma_tech_value = round(base_value * plasma_tech * 0.01)
    geologist_value = round(base_value * 0.1)
    pallets_value = base_value * 0.0002 * pallets * pallets_speed / 100

    if merchant:
        base_value += merchant_value
    if collector:
        base_value += collector_value
        pallets_value = pallets_value * 1.5
    if item > 0:
        base_value += item_value
    if plasma_tech > 0:
        base_value += plasma_tech_value
    if geologist or recruit_officers:
        base_value += geologist_value

    return base_value + main_income + pallets_value


def crystal_per_hour(
        mine_level,
        universe_speed,
        item,
        speed,
        merchant,
        collector,
        plasma_tech,
        main_income,
        geologist,
        recruit_officers,
        pallets,
        pallets_speed
):
    base_value = round(20 * mine_level * pow(1.1, mine_level) * universe_speed * speed / 100)
    if main_income > 120:
        base_value = round(20 * mine_level * pow(1.1, mine_level) * universe_speed * speed / 100) * (main_income / 120)
    collector_value = round(base_value * 0.25)
    merchant_value = round(base_value * 0.05)
    item_value = round(base_value * item / 100)
    plasma_tech_value = round(base_value * plasma_tech * 0.0066)
    geologist_value = round(base_value * 0.1)
    pallets_value = base_value * 0.0002 * pallets * pallets_speed / 100

    if merchant:
        base_value += merchant_value
    if collector:
        base_value += collector_value
        pallets_value = pallets_value * 1.5
    if item > 0:
        base_value += item_value
    if plasma_tech > 0:
        base_value += plasma_tech_value
    if geologist or recruit_officers:
        base_value += geologist_value

    return base_value + main_income + pallets_value


def deuterium_per_hour(
        mine_level,
        universe_speed,
        item,
        speed,
        merchant,
        collector,
        plasma_tech,
        temperature_min,
        temperature_max,
        fusion_plant_level,
        fusion_plant_speed,
        geologist,
        recruit_officers,
        pallets,
        pallets_speed
):
    base_value = round(
        10 * mine_level * pow(1.1, mine_level) * (-0.004 * avarage_temperature(temperature_min,
                                                                               temperature_max) + 1.36) * universe_speed * speed / 100)
    collector_value = round(base_value * 0.25)
    merchant_value = round(base_value * 0.05)
    item_value = round(base_value * item / 100)
    plasma_tech_value = round(base_value * plasma_tech * 0.0033)
    geologist_value = round(base_value * 0.1)
    pallets_value = base_value * 0.0002 * pallets * pallets_speed / 100

    if merchant:
        base_value += merchant_value
    if collector:
        base_value += collector_value
        pallets_value = pallets_value * 1.5
    if item > 0:
        base_value += item_value
    if plasma_tech > 0:
        base_value += plasma_tech_value
    if geologist or recruit_officers:
        base_value += geologist_value

    return base_value + fusionPlantDeuterium(fusion_plant_level, universe_speed, fusion_plant_speed) + pallets_value


def fusionPlantDeuterium(plant_level, universe_speed, speed):
    return math.ceil(-10 * plant_level * pow(1.1, plant_level) * universe_speed * speed / 100)


def avarage_temperature(min_temp, max_temp):
    return (min_temp + max_temp) / 2


def energy_per_hour(
        solar_plant_level,
        item,
        solar_speed,
        merchant,
        collector,
        energy_tech,
        temperature_min,
        temperature_max,
        fusion_plant_level,
        fusion_plant_speed,
        solar_sattelite,
        solar_sattelite_speed,
        engineer,
        recruit_officers,
        metal_mine_level,
        crystal_mine_level,
        deuterium_mine_level,
        metal_speed,
        crystal_speed,
        deuterium_speed,
        pallets,
        pallets_speed
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

    merchant_value = math.floor(solar_plant_base_value * 0.05) + math.ceil(fusion_plant_base_value * 0.05) + math.floor(
        solar_sattelite_base_value * 0.05)

    item_value = math.ceil(solar_plant_base_value * item / 100) + math.floor(
        fusion_plant_base_value * item / 100) + math.floor(solar_sattelite_base_value * item / 100)

    if merchant:
        total_energy += merchant_value
    if collector:
        total_energy += collector_value
    if item > 0:
        total_energy += item_value
    if engineer or recruit_officers:
        total_energy += engineer_value

    if pallets_speed > 100:
        pallets_energy = round((50 * pallets * (pallets_speed - 100) / 100) * 2) + round(50 * pallets)
    else:
        pallets_energy = round(50 * pallets * pallets_speed / 100)

    energy_consumption = metal_crystal_mine_power(metal_mine_level, metal_speed) + metal_crystal_mine_power(
        crystal_mine_level, crystal_speed) + deuterium_mine_power(deuterium_mine_level,
                                                                  deuterium_speed) + pallets_energy

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
