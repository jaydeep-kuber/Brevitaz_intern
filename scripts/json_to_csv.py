import csv 
import  json

path_json= "../csv/names.json"
path_csv= "../csv/names_new.csv"

def json_to_csv(csvFilePath, jsonFilePath):

    with open(jsonFilePath, 'r') as jsonFile:
        data = json.load(jsonFile)

    with open(csvFilePath, 'w', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=data[0].keys(),delimiter=',')
        writer.writeheader()
        writer.writerows(data)

json_to_csv(path_csv, path_json)
print("csv file created")
