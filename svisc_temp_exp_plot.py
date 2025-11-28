import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

#Directory paths

data_dir = 'Exp_Svisc'
output_dir = 'png/Svisc_exp_plots'

files_Svisc = [{'files': 'Svisc_exp_0.0mol.csv', 'mol': '0.0'},
                 {'files': 'Svisc_exp_1.0mol.csv', 'mol': '1.0'},
                 {'files': 'Svisc_exp_1.5mol.csv', 'mol': '1.5'},
                 {'files': 'Svisc_exp_2.0mol.csv', 'mol': '2.0'},
                {'files': 'Svisc_exp_2.5mol.csv', 'mol': '2.5'},
                {'files': 'Svisc_exp_3.0mol.csv', 'mol': '3.0'},
                {'files': 'Svisc_exp_3.5mol.csv', 'mol': '3.5'},
                {'files': 'Svisc_exp_4.0mol.csv', 'mol': '4.0'},
                {'files': 'Svisc_exp_4.5mol.csv', 'mol': '4.5'},
                {'files': 'Svisc_exp_5.0mol.csv', 'mol': '5.0'},
                {'files': 'Svisc_exp_5.5mol.csv', 'mol': '5.5'},
            ]


for file_info in files_Svisc:

    file_path = os.path.join(data_dir,file_info['files'])
    mol = file_info['mol']


    df = pd.read_csv(file_path)

        #get some information
        #print('Df: '+ '\n',df)
        #print('Describe: '+ '\n', df.describe())
        #print('Info '+ '\n',df.info())
        #print('Head: '+ '\n', df.head())
        #how to print all moles and densities with Temp 273K
        #print(df[df['T']== 273])

    #Bar_plot
    x = df['T']
    y = df['Svisc']

    #Figure Size
    fig, ax = plt.subplots(figsize =(9,9))

    #Add Plot Title
    ax.set_title(('Shear Viscosity vs Temperature '+'\n'+'molality= %s mol/kg'%mol),loc ='center', fontweight ='bold', fontsize = 15)

    #Label axes
    plt.ylabel('Shear Viscosity, cP', fontweight ='bold', fontsize = 10,rotation =90)
    plt.xlabel('Temperatures, K', fontweight ='bold', fontsize = 10 )

    #Limit y axis
    plt.ylim(df['Svisc'].min()-0.2, df['Svisc'].max()+0.2)
    plt.xticks(x, rotation=45, fontsize = 10, size = 10)

    #Horizontal Bar Plot
    plt.bar(x, y, width = 2.52, color ='b', alpha = 0.75, edgecolor ='black', align ='center')
    
    #Show plots
    plt.show()

    #Save plots
    plot_name = os.path.join(output_dir,f'Sviscplot_exp_{mol}mol.png')
    fig.savefig(plot_name)
    exit()

