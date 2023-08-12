# K Windfuhr, D While, N Kapur, D M Ashcroft, E Kontopantelis, M J Carr, J Shaw, L Applyby, R T Webb, 2023.

import sys, csv, re

codes = [{"code":"49489020","system":"multilex"},{"code":"49491020","system":"multilex"},{"code":"53727020","system":"multilex"},{"code":"53728020","system":"multilex"},{"code":"53729020","system":"multilex"},{"code":"74841020","system":"multilex"},{"code":"79476020","system":"multilex"},{"code":"81543020","system":"multilex"},{"code":"92717020","system":"multilex"},{"code":"92721020","system":"multilex"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('atypical-apds-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["atypical-apds-risperidone---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["atypical-apds-risperidone---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["atypical-apds-risperidone---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
