import requests
import json

def get_composition(url):
    response = requests.get(url)
    return response.json()

def post_composition(url, data):
    headers = {
        'Content-Type': 'application/json',
        'Prefer': 'return=representation'  # Указание предпочтений возвращаемого ответа
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print("Статус: ", response.status_code)
    print("Ответ сервера: ", response.text)
    return response.status_code, response.text

def convert_units(weight_kg, height_cm):
    weight_lb = round(weight_kg * 2.20462, 1)  # округляем до 1 знака после запятой
    height_ft = round(height_cm * 0.0328084, 1)  # округляем до 1 знака после запятой
    return weight_lb, height_ft

def modify_template(template_data, weight_lb, height_ft, visit_date):
    # Прямая замена значений магнитуды в строковом представлении JSON
    template_data = template_data.replace('xxx1', str(weight_lb))
    template_data = template_data.replace('xxx2', str(height_ft))
    template_data = template_data.replace('"xxx3"', f'"{visit_date}"')  # Заменяем xxx3 на дату в кавычках
    return template_data

# Загрузка шаблона
template_path = 'C:\\Users\\admin\\Desktop\\cw24\\тело запроса.txt'
with open(template_path, 'r', encoding='utf-8') as file:
    template_data = file.read()

# URL для получения и отправки данных
get_url = ("http://localhost:8080/ehrbase/rest/openehr/v1/ehr/b60e53ff-2cdb-4d5f-9451-0eb972241ea3/composition"
           "/35ffb792-0285-486e-b863-ae80282588d1::local.ehrbase.org::1")
post_url = "http://localhost:8080/ehrbase/rest/openehr/v1/ehr/b60e53ff-2cdb-4d5f-9451-0eb972241ea3/composition"

# Получение данных
composition_data = get_composition(get_url)
weight_kg = composition_data['content'][1]['data']['events'][0]['data']['items'][0]['value']['magnitude']
height_cm = composition_data['content'][2]['data']['events'][0]['data']['items'][0]['value']['magnitude']
visit_date = composition_data['content'][0]['data']['events'][0]['data']['items'][0]['value']['value']

# Конвертация единиц
weight_lb, height_ft = convert_units(weight_kg, height_cm)

# Модификация шаблона
modified_template = modify_template(template_data, weight_lb, height_ft, visit_date)

# Отправка данных
status, response = post_composition(post_url, json.loads(modified_template))

