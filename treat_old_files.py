import pandas as pd
import csv
 

#replacements
replacements = {
    ';': ',',    
    'dyn': 'svisc',  
    'Temp':'T',
    '\r':'',
    '0.1,': '',    
}
with open('Svisc_0.0mol_exp.csv','r') as file:
    reader = csv.reader(file)


    #every line in a list
    lines = list(reader)


#replacements and add new columns
updated_lines = []
header_processed = False
column_to_remove = 'press'
header_row = lines[0]

if column_to_remove in header_row:
    column_index_to_remove = header_row.index(column_to_remove)
else:
    column_index_to_remove = -1  # If column is not found, set to -1

#every element in list lines
for line in lines:
    # Remove characters if they exist 
    #item = element in each line
    for item in line:
        line = [item.replace('\r', '').replace('0.1,', '') for item in line]
    
    # Perform replacements
    for i in range(len(line)):
        #replacements.items() is each replacement
        for old, new in replacements.items():
            line[i] = line[i].replace(old, new)

    # Add new columns
    if not header_processed:
        # Process header line
        updated_line = ['Mol'] + line + ['Data']
        header_processed = True
    else:
        # Process data lines
        updated_line = ['0.0'] + line + ['exp']
    
    updated_lines.append(updated_line)

#new CSV file
with open('Svisc_0.0mol_exp.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(updated_lines)


