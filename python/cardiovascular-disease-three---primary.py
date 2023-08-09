# Ellie Paige, Jessica Barret, David Stevens, Ruth H Keog, Michael J Sweeting, Irwin Nazareth, Irene Petersen, Angela M Wood, 2023.

import sys, csv, re

codes = [{"code":"7920200","system":"readv2"},{"code":"7921200","system":"readv2"},{"code":"7922200","system":"readv2"},{"code":"7923200","system":"readv2"},{"code":"7924200","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cardiovascular-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cardiovascular-disease-three---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cardiovascular-disease-three---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cardiovascular-disease-three---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
