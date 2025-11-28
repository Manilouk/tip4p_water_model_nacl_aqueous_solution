import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import numpy as np

files_density = [{'files': 'density_mol_0.1_exp.csv', 'mol': '0.1'},
                 {'files': 'density_mol_0.25_exp.csv', 'mol': '0.25'},
                 {'files': 'density_mol_0.5_exp.csv', 'mol': '0.5'},
                 {'files': 'density_mol_0.75_exp.csv', 'mol': '0.75'},
                {'files': 'density_mol_1_exp.csv', 'mol': '1'},
                {'files': 'density_mol_2_exp.csv', 'mol': '2'},
                {'files': 'density_mol_3_exp.csv', 'mol': '3'},
                {'files': 'density_mol_4_exp.csv', 'mol': '4'},
                {'files': 'density_mol_5_exp.csv', 'mol': '5'},
            ]

for i in range(0, len(files_density)):
    df = pd.read_csv(files_density[i]['files'])
    mol = files_density[i]['mol']

    #get some information
    #print('Df: '+ '\n',df)
    #print('Describe: '+ '\n', df.describe())
    #print('Info '+ '\n',df.info())
    #print('Head: '+ '\n', df.head())
    #how to print all moles and densities with Temp 273K
    #print(df[df['T']== 273])


    #Bar_plot
    x = df['T']
    y = df['D']

    #Figure Size
    fig, ax = plt.subplots(figsize =(9,9))

    #Add Plot Title
    ax.set_title(('Density vs Temperature '+'\n'+'molality= %s mol/kg'%mol),loc ='center', fontweight ='bold', fontsize = 15)

    #Label axes
    plt.ylabel('Density, g/cm$^3$', fontweight ='bold', fontsize = 10)
    plt.xlabel('Temperatures, K', fontweight ='bold', fontsize = 10)

    #Limit y axis
    plt.ylim(df['D'].min()-0.001, df['D'].max()+0.001)

    plt.xticks(x, rotation=45, fontsize = 10, size = 10)
    

    #Horizontal Bar Plot
    plt.bar(x, y, width = 2.52, color ='b', alpha = 0.75, edgecolor ='black', align ='center')
    
    #Show plots
    plt.show()
    
    #Save plots
    plt.savefig('plot_%smol.png'%mol)

