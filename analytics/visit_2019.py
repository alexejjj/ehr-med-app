import requests
import json
import base64

# укажите URL эндпоинта и параметры запроса
url = "http://localhost:8080/ehrbase/rest/openehr/v1/query/aql"
params = {
    "q": "SELECT e/ehr_id/value, c/uid/value, c/archetype_details/template_id/value, o1/data[at1234]/events["
         "at1235]/data[at1236]/items[at1237]/value as patient_visit_date, o2/data[at1001]/events[at1002]/data["
         "at1003]/items[at1004]/value as patient_element_size_x, o3/data[at2001]/events[at2002]/data[at2003]/items["
         "at2004]/value as patient_element_size_y, o4/data[at0081]/events[at0082]/data[at0083]/items[at0084]/value as "
         "patient_element_area, o5/data[at0601]/events[at0602]/data[at0603]/items[at0604]/value as patient_height, "
         "o6/data[at4001]/events[at4002]/data[at4003]/items[at4004]/value as patient_weight FROM EHR e CONTAINS "
         "COMPOSITION c [openEHR-EHR-COMPOSITION.finalmainmonitoring.v0] CONTAINS OBSERVATION o1 ["
         "openEHR-EHR-OBSERVATION.visitdate.v0] OR OBSERVATION o2 [openEHR-EHR-OBSERVATION.sizex.v0] OR OBSERVATION "
         "o3 [openEHR-EHR-OBSERVATION.sizey.v0] OR OBSERVATION o4 [openEHR-EHR-OBSERVATION.elementarea.v0] OR "
         "OBSERVATION o5 [openEHR-EHR-OBSERVATION.height.v0] OR OBSERVATION o6 [openEHR-EHR-OBSERVATION.weight.v0] "
         "WHERE c/uid/value = '0a7a090e-55cd-48a9-acb4-911b38516611::local.ehrbase.org::1' LIMIT 1",
    "format": "json"}

# укажите свой логин и пароль
username = "ehrbase-user"
password = "SuperSecretPassword"

# кодируем логин и пароль в формат base64
auth_string = f"{username}:{password}"
auth_bytes = auth_string.encode("ascii")
base64_bytes = base64.b64encode(auth_bytes)
base64_auth = base64_bytes.decode("ascii")

# создаем заголовок Authorization
headers = {"Authorization": f"Basic {base64_auth}", "Content-Type": "application/json"}

# Отправляем запрос на сервер и получаем ответ
response = requests.get(url, params=params, headers=headers)

# распарсить ответ в формате JSON
response_json = json.loads(response.text)

# извлечь состояния пациента из результата запроса
patient_states = []
for result in response_json['rows']:
    ehr_id = result[0]
    visit_date = result[3]
    element_size_x = result[4]
    element_size_y = result[5]
    element_area = result[6]
    height = result[7]
    weight = result[8]

    # добавить состояние пациента в список
    patient_states.append({
        'ehr_id': ehr_id,
        'visit_date': visit_date,
        'element_size_x': element_size_x,
        'element_size_y': element_size_y,
        'element_area': element_area,
        'height': height,
        'weight': weight
    })

    patient_states_cleaned = []
    for state in patient_states:
        cleaned_state = {
            'ehr_id': state['ehr_id'],
            'visit_date': state['visit_date']['value'],
            'element_size_x': state['element_size_x'].get('magnitude', None),
            'element_size_y': state['element_size_y'].get('magnitude', None),
            'element_area': state['element_area'].get('magnitude', None),
            'height': state['height'].get('magnitude', None),
            'weight': state['weight'].get('magnitude', None),
        }
        patient_states_cleaned.append(cleaned_state)

for state in patient_states_cleaned:
    ehr_id_2019 = state['ehr_id']
    visit_date_2019 = state['visit_date']
    element_size_x_2019 = state['element_size_x']
    element_size_y_2019 = state['element_size_y']
    element_area_2019 = state['element_area']
    height_2019 = state['height']
    weight_2019 = state['weight']

    # print(ehr_id_2019, '\n', visit_date_2019, '\n', element_size_x_2019, '\n', element_size_y_2019, '\n',
    #       element_area_2019, '\n', height_2019, '\n', weight_2019)
