import csv
import json


def csv_to_json(csv_file_path, json_file_path) -> None:
    """
    Receives .csv format file and converts it to .json file
    Before running change "model" value according to app name and model name
    """
    data_list = []

    with open(csv_file_path, encoding='utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)

        for rows in csv_reader:
            # change "model" value according to app name and model name
            data_dict = {"model": "users.location", "pk": rows["id"], "fields": rows}
            data_list.append(data_dict)

    with open(json_file_path, 'w', encoding='utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(data_list, indent=4, ensure_ascii=False))


csv_file_path = input('Enter the absolute path of the CSV file: ')
json_file_path = input('Enter the absolute path of the JSON file: ')

csv_to_json(csv_file_path, json_file_path)
