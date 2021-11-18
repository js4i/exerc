import os
import json
import csv


def _save_json(destination_path: str, idx: int, row_file: list):

    person_id, floor_access, floor_level, building = row_file
    data = {
        "title": "Floor Access Event",
        "type": "object",
        "properties": {
            "person_id": person_id,
            "datetime": floor_access,
            "floor_level": int(floor_level),
            "building": building
        },
        "required": ["person_id", "datetime", "floor_level", "building"]
    }

    with open(f'{destination_path}/{idx}_file.json', 'w') as outfile:
        json.dump(data, outfile)


def _csv_reader(file_name):
    for row in csv.reader(open(file_name, 'r')):
        yield row


def process_data(file_path, destination_path):

    for idx, row_file in enumerate(
        _csv_reader(file_name=file_path)
    ):
        if idx == 0:
            continue

        _save_json(
            destination_path, idx, row_file
        )

    return "All files processed."


if __name__ == '__main__':

    file_path = os.path.join(
        os.getcwd(), 'questao_02', 'questao_02.csv'
    )
    destination_path = os.path.join(
        os.getcwd(), 'questao_02', 'data'
    )

    process_data(
        file_path, destination_path
    )
