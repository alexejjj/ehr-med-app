import requests
import json

def get_composition_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def extract_data(composition_data):
    date = composition_data['content'][0]['data']['events'][0]['data']['items'][0]['value']['value']
    weight = composition_data['content'][1]['data']['events'][0]['data']['items'][0]['value']['magnitude']
    height = composition_data['content'][2]['data']['events'][0]['data']['items'][0]['value']['magnitude']
    return date, weight, height


urls = [
    "http://localhost:8080/ehrbase/rest/openehr/v1/ehr/b60e53ff-2cdb-4d5f-9451-0eb972241ea3/composition/e0858855-c362-4a54-85dd-8af9eba7de2b::local.ehrbase.org::1",
    "http://localhost:8080/ehrbase/rest/openehr/v1/ehr/b60e53ff-2cdb-4d5f-9451-0eb972241ea3/composition/92c15787-207c-4df4-8342-4f3119710186::local.ehrbase.org::1",
    "http://localhost:8080/ehrbase/rest/openehr/v1/ehr/b60e53ff-2cdb-4d5f-9451-0eb972241ea3/composition/35ffb792-0285-486e-b863-ae80282588d1::local.ehrbase.org::1",
    "http://localhost:8080/ehrbase/rest/openehr/v1/ehr/b60e53ff-2cdb-4d5f-9451-0eb972241ea3/composition/2ed332c5-31c5-40ed-b222-406e5755f59c::local.ehrbase.org::1",
    "http://localhost:8080/ehrbase/rest/openehr/v1/ehr/b60e53ff-2cdb-4d5f-9451-0eb972241ea3/composition/15bb5987-79f5-4e7d-846b-515d46e90662::local.ehrbase.org::1",
    "http://localhost:8080/ehrbase/rest/openehr/v1/ehr/b60e53ff-2cdb-4d5f-9451-0eb972241ea3/composition/baca026c-8acf-45a4-a67f-84b7914f2106::local.ehrbase.org::1",
    "http://localhost:8080/ehrbase/rest/openehr/v1/ehr/b60e53ff-2cdb-4d5f-9451-0eb972241ea3/composition/9fb94895-bb64-4095-8a9e-6201fa25af2f::local.ehrbase.org::1"
]

for i, url in enumerate(urls):
    composition_data = get_composition_data(url)
    date, weight, height = extract_data(composition_data)
    print(f"Дата: {date}, Вес: {weight}, Рост: {height}")
