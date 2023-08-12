# K Windfuhr, D While, N Kapur, D M Ashcroft, E Kontopantelis, M J Carr, J Shaw, L Applyby, R T Webb, 2023.

import sys, csv, re

codes = [{"code":"209021","system":"multilex"},{"code":"33610020","system":"multilex"},{"code":"35008020","system":"multilex"},{"code":"35010020","system":"multilex"},{"code":"3580020","system":"multilex"},{"code":"411021","system":"multilex"},{"code":"42176020","system":"multilex"},{"code":"447021","system":"multilex"},{"code":"72580020","system":"multilex"},{"code":"78753020","system":"multilex"},{"code":"81008020","system":"multilex"},{"code":"81014020","system":"multilex"},{"code":"85203020","system":"multilex"},{"code":"85212020","system":"multilex"},{"code":"86494020","system":"multilex"},{"code":"88167020","system":"multilex"},{"code":"89950020","system":"multilex"},{"code":"99745020","system":"multilex"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('atypical-apds-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["atypical-apds-125mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["atypical-apds-125mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["atypical-apds-125mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
