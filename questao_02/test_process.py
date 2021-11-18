import os
import csv
import tempfile
import json

from process import process_data


class TestProcess():

    def test_process__process_valid_csv_file__expected_all_file_processed(
        self
    ):
        # FIXTURE
        mock_header = ['Person Id', 'Floor Access DateTime',
                       'Floor Level', 'Building']
        mock_data = [
            ['1', '10/1/15 8:02', '6', 'B'],
            ['2', '10/1/15 8:02', '5', 'C'],
            ['3', '10/1/15 8:03', '1', 'C']
        ]

        with tempfile.TemporaryDirectory() as dirname:
            with open(f'{dirname}/data.csv', 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(mock_header)
                writer.writerows(mock_data)

            file_path = f'{dirname}/data.csv'
            destination_path = f'{dirname}/'

        # EXERCISE
            result = process_data(
                file_path, destination_path
            )

            all_files = os.listdir(dirname)

        # ASSERTS
        assert result == "All files processed."
        assert all_files == [
            '2_file.json', 'data.csv', '3_file.json', '1_file.json'
        ]

    def test_process__process_valid_csv_file__expected_schema_json(
        self
    ):
        # FIXTURE
        mock_header = ['Person Id', 'Floor Access DateTime',
                       'Floor Level', 'Building']
        mock_data = [
            ['1', '10/1/15 8:02', '7', 'C'],
        ]

        with tempfile.TemporaryDirectory() as dirname:
            with open(f'{dirname}/data.csv', 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(mock_header)
                writer.writerows(mock_data)

            file_path = f'{dirname}/data.csv'
            destination_path = f'{dirname}/'

        # EXERCISE
            result = process_data(
                file_path, destination_path
            )

            all_files = os.listdir(dirname)

            with open(f'{dirname}/1_file.json') as json_file:
                schema_json = json.load(json_file)

        # ASSERTS
        assert result == "All files processed."
        assert all_files == [
            'data.csv', '1_file.json'
        ]

        assert schema_json == {
            'title': 'Floor Access Event',
            'type': 'object',
            'properties': {
                'person_id': '1',
                'datetime': '10/1/15 8:02',
                'floor_level': 7,
                'building': 'C'
            },
            'required': [
                'person_id', 'datetime', 'floor_level', 'building'
            ]
        }

    def test_process__process_csv_file_with_only_header__expected_only_original_file(
        self
    ):
        # FIXTURE
        mock_header = ['Person Id', 'Floor Access DateTime',
                       'Floor Level', 'Building']

        with tempfile.TemporaryDirectory() as dirname:
            with open(f'{dirname}/data.csv', 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(mock_header)

            file_path = f'{dirname}/data.csv'
            destination_path = f'{dirname}/'

        # EXERCISE
            result = process_data(
                file_path, destination_path
            )

            all_files = os.listdir(dirname)

        # ASSERTS
        assert result == "All files processed."
        assert all_files == [
            'data.csv'
        ]
