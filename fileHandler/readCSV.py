import csv 
file_path = '../csv/names.csv'

with open(file_path,'r') as csv_file:
    # if csv_file:
    #     print("file opend")
        csv_reader = csv.DictReader(csv_file,delimiter=',')
        for line in csv_reader:
            print(line)
            # print(line['first_name'])

