import csv
import json

path_csv= "../csv/names.csv"
path_json= "../csv/names.json"

def csv_to_json(csvFilePath, jsonFilePath):
    
    tmp_data = []
    with open(csvFilePath, mode='r') as csvFile:
        csvReader = csv.DictReader(csvFile)

        for csvRow in csvReader:
            tmp_data.append(csvRow)

    with open(jsonFilePath, 'w') as jsonFile:
        json.dump(tmp_data, jsonFile , indent=1 )
        print(f"CSV file {csvFilePath} successfully converted to JSON file {jsonFilePath}")

csv_to_json(path_csv, path_json)
