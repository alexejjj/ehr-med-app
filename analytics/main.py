import matplotlib.pyplot as plt
import numpy as np
from visit_2018 import ehr_id_2018, visit_date_2018, element_size_x_2018, element_size_y_2018, element_area_2018, \
    height_2018, weight_2018
from visit_2019 import ehr_id_2019, visit_date_2019, element_size_x_2019, element_size_y_2019, element_area_2019, \
    height_2019, weight_2019
from visit_2021 import ehr_id_2021, visit_date_2021, element_size_x_2021, element_size_y_2021, element_area_2021, \
    height_2021, weight_2021
from visit_2022 import ehr_id_2022, visit_date_2022, element_size_x_2022, element_size_y_2022, element_area_2022, \
    height_2022, weight_2022
import os

# os.environ['LINES'] = "120"

print(f"Работа с ehr - {ehr_id_2018}")

variable_names = {
    "ehr_id": [ehr_id_2018, ehr_id_2019, ehr_id_2021, ehr_id_2022],
    "visit_date": [visit_date_2018, visit_date_2019, visit_date_2021, visit_date_2022],
    "element_size_x": [element_size_x_2018, element_size_x_2019, element_size_x_2021, element_size_x_2022],
    "element_size_y": [element_size_y_2018, element_size_y_2019, element_size_y_2021, element_size_y_2022],
    "element_area": [element_area_2018, element_area_2019, element_area_2021, element_area_2022],
    "height": [height_2018, height_2019, height_2021, height_2022],
    "weight": [weight_2018, weight_2019, weight_2021, weight_2022]
}

while True:
    var = input("Введите название переменной, которую вы хотите проанализировать: ")
    if var not in variable_names:
        print("Такой переменной нет.")
        continue
    y_data = variable_names[var]
    years = [2018, 2019, 2021, 2022]
    plt.plot(years, y_data)
    plt.xlabel("Год")
    plt.ylabel("Значение переменной")
    plt.title(f"График переменной {var} по годам")
    plt.xticks(years)
    plt.savefig(f"{var}.png")
    plt.show()
