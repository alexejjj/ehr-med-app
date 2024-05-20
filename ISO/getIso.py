import requests


def get_composition(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data from {url}")
        return None


def extract_static_info(data):
    equipment_name = data["content"][0]["data"]["events"][0]["data"]["items"][0]["value"]["value"]
    manufacturer_name = data["content"][2]["data"]["events"][0]["data"]["items"][0]["value"]["value"]
    power_mw = data["content"][3]["data"]["events"][0]["data"]["items"][0]["value"]["magnitude"]
    temp_min = data["content"][3]["data"]["events"][0]["data"]["items"][2]["value"]["magnitude"]
    temp_max = data["content"][3]["data"]["events"][0]["data"]["items"][3]["value"]["magnitude"]
    pressure_pa = data["content"][3]["data"]["events"][0]["data"]["items"][4]["value"]["magnitude"]
    voltage_v = data["content"][3]["data"]["events"][0]["data"]["items"][5]["value"]["magnitude"]

    print("Запись Static:")
    print(f"Название оборудования - {equipment_name}")
    print(f"Наименование производителя - {manufacturer_name}")
    print(f"Мощность в MW - {power_mw}")
    print(f"Рабочая температура min в градусах Цельсия - {temp_min}")
    print(f"Рабочая температура max в градусах Цельсия - {temp_max}")
    print(f"Давление в Па - {pressure_pa}")
    print(f"Напряжение в V - {voltage_v}")


def extract_dynamic_info(data):
    installation_date = data["content"][0]["data"]["events"][0]["data"]["items"][0]["value"]["value"]
    last_maintenance_date = data["content"][0]["data"]["events"][0]["data"]["items"][1]["value"]["value"]
    next_maintenance_date = data["content"][0]["data"]["events"][0]["data"]["items"][2]["value"]["value"]
    malfunction_records = data["content"][0]["data"]["events"][0]["data"]["items"][3]["value"]["value"]
    latitude = data["content"][0]["data"]["events"][0]["data"]["items"][4]["value"]["magnitude"]
    longitude = data["content"][0]["data"]["events"][0]["data"]["items"][5]["value"]["magnitude"]

    print("\nЗапись Dynamic:")
    print(f"Дата установки - {installation_date}")
    print(f"Дата последнего технического обслуживания - {last_maintenance_date}")
    print(f"Дата следующего планового обслуживания - {next_maintenance_date}")
    print(f"Записи о неисправностях и ремонте - {malfunction_records}")
    print(f"Координаты установленного оборудования широта - {latitude}")
    print(f"Координаты установленного оборудования долгота - {longitude}")



static_url = "http://localhost:8080/ehrbase/rest/openehr/v1/ehr/5e5c93b7-e8a9-401c-9111-b48f6ea11ecc/composition/d4728176-9529-4279-9ada-766ace4ec972::local.ehrbase.org::1"
dynamic_url = "http://localhost:8080/ehrbase/rest/openehr/v1/ehr/5e5c93b7-e8a9-401c-9111-b48f6ea11ecc/composition/5bd1c363-9ec3-4fca-81a8-4befccaff5eb::local.ehrbase.org::1"


static_data = get_composition(static_url)
dynamic_data = get_composition(dynamic_url)


if static_data:
    extract_static_info(static_data)

if dynamic_data:
    extract_dynamic_info(dynamic_data)
