import pandas as pd
import csv
import pandas as pd

Temperatures = []
t = 293 
for i in range(20, 155, 5):

    Temperatures.append(str(t))
    t+=5
#print(Temperatures)

Molality = []
mol = 0.0
for i in range(0, 12):
    if not mol == 0.5:
        Molality.append(str(mol))
    mol+=0.5
#print(Molality)

#A number of entries were excluded from the list to ensure that only data relevant to the present analysis were retained. --> Svisc_initial

Svisc_initial = ['.....many values.....']
Svisc_final = []
for i in range(len(Svisc_initial)):
    Svisc_final.append('%.3f'%(Svisc_initial[i]/100))

data_files = [['Mol','T','Svisc', 'Data']]
i=0
for mol in Molality:
    if not mol == 0.5:
        for temp in Temperatures:
            data_files.append([mol,temp, Svisc_final[i], 'Exp'])
            i += 1

        #Open the file in write mode
        with open('Svisc_exp_%smol.csv'%mol, mode='w', newline='') as file:
        #Create a csv.writer object
            writer = csv.writer(file)
        #Write data to the CSV file
            writer.writerows(data_files)

        data_files = [['Mol','T', 'Svisc', 'Data']]

df =pd.read_csv('Svisc_exp_0.0mol.csv')
print(type(df['Svisc'][1]))


