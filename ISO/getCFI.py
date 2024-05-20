import requests


def get_composition(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None


def extract_cfihos_info(data):
    try:
        project_name = data["content"][0]["data"]["events"][0]["data"]["items"][0]["value"]["value"]
        project_number = data["content"][0]["data"]["events"][0]["data"]["items"][1]["value"]["magnitude"]
        project_description = data["content"][0]["data"]["events"][0]["data"]["items"][2]["value"]["value"]
        client = data["content"][0]["data"]["events"][0]["data"]["items"][3]["value"]["value"]
        contractor = data["content"][0]["data"]["events"][0]["data"]["items"][4]["value"]["value"]
        start_date = data["content"][0]["data"]["events"][0]["data"]["items"][5]["value"]["value"]
        current_status = data["content"][0]["data"]["events"][0]["data"]["items"][6]["value"]["value"]
        full_address = data["content"][0]["data"]["events"][0]["data"]["items"][7]["value"]["value"]

        print("Запись CFIHOS:")
        print(f"Название проекта - {project_name}")
        print(f"Номер проекта - {project_number}")
        print(f"Описание проекта - {project_description}")
        print(f"Заказчик - {client}")
        print(f"Подрядчик - {contractor}")
        print(f"Дата начала проекта - {start_date}")
        print(f"Текущий статус проекта - {current_status}")
        print(f"Полный адрес объекта - {full_address}")
    except KeyError as e:
        print(f"Data extraction error: Missing key {e}")


# URL для запроса
url = "http://localhost:8080/ehrbase/rest/openehr/v1/ehr/5e5c93b7-e8a9-401c-9111-b48f6ea11ecc/composition/cf52c003-f73f-4541-92aa-b7d627c266e6::local.ehrbase.org::1"

# Получение данных
cfihos_data = get_composition(url)

# Извлечение и вывод информации
if cfihos_data:
    extract_cfihos_info(cfihos_data)
else:
    print("No data received or there was an error in the request.")
