import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
import os

files_exp = [
{'files': 'Svisc_exp_0.0mol.csv', 'mol': '0.0'},
{'files': 'Svisc_exp_1.0mol.csv', 'mol': '1.0'},
{'files': 'Svisc_exp_2.0mol.csv', 'mol': '2.0'},
{'files': 'Svisc_exp_3.0mol.csv', 'mol': '3.0'},
{'files': 'Svisc_exp_4.0mol.csv', 'mol': '4.0'},
{'files': 'Svisc_exp_5.0mol.csv', 'mol': '5.0'}
                ]

files_tip4p=[
{'files': 'Svisc_tip4p_0.0mol.csv', 'mol': '0.0'},
{'files': 'Svisc_tip4p_1.09mol.csv', 'mol': '1.09'},
{'files': 'Svisc_tip4p_2.17mol.csv', 'mol': '2.17'},
{'files': 'Svisc_tip4p_3.26mol.csv', 'mol': '3.26'},
{'files': 'Svisc_tip4p_4.34mol.csv', 'mol': '4.34'},
{'files': 'Svisc_tip4p_5.43mol.csv', 'mol': '5.43'},
            ]

Temp = [298, 323, 373]

y_exp =[]
x_exp=[]
all_exp =[]
all_tip4p =[]

for file_info in files_exp:
    path_exp =os.path.join('./Exp_Svisc',file_info['files'])
    '''
    put data by each file in df_exp(every time)
    put them in all_exp as a list
    after that combine them in a new df all data : exp_data
    '''
    df_exp = pd.read_csv(path_exp)
    all_exp.append(df_exp)
exp_data = pd.concat(all_exp, ignore_index = True)


for file_info in files_tip4p:
    path_tip4p =os.path.join('./Tip4p_Svisc_NVT',file_info['files'])
    df_tip4p = pd.read_csv(path_tip4p)
    all_tip4p.append(df_tip4p)

tip4p_data = pd.concat(all_tip4p, ignore_index = True)

#print(tip4p_data['Mol'])
#exit()
for temp in Temp:

#        for i in range(len(df_exp['T'])):
#            if df_exp['T'][i] == temp:
#                y_exp.append(df_exp['D'][i])
#                x_exp.append(df_exp['Mol'][i])
#
    temp_exp = exp_data[exp_data['T']==temp]
    temp_tip4p = tip4p_data[tip4p_data['T']==temp]
    plt.figure(figsize=(10, 6))

    # Plot experimental data
    plt.plot(temp_exp['Mol'], temp_exp['Svisc'],color='blue', marker='o', linestyle='-', label=f'Experimental (Temperature: {temp}K)')

    # Plot simulation data
    plt.plot(temp_tip4p['Mol'], temp_tip4p['Svisc'],color='red', marker='D', linestyle='--', label=f'Tip4p (Temperature: {temp}K)')

    fpng = 'Svisc_comparison_%sK.png'%(temp)

    plt.xlabel('Molality (mol/kg)',fontweight ='bold', fontsize = 8)
    plt.ylabel('Shear viscosity_nvt (10$^{-4}$Pa*s)',fontweight ='bold', fontsize = 8)
    plt.title(f'Shear viscosity_nvt vs. Molality at {temp}K',fontweight ='bold', fontsize = 10)
    plt.legend()
    plt.show()

    plt.savefig('./png/Svisc_Exp_vs_Tip4p_nvt/' + fpng)
    plt.close()

