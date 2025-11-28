import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import numpy as np

xlabels = [
'298',
'323',
'373'
]


files_density = [{'files': 'density_mol_0_tip4p.csv', 'mol': '0'},
                {'files': 'density_mol_1.09_tip4p.csv', 'mol': '1.09'},
                {'files': 'density_mol_2.17_tip4p.csv', 'mol': '2.17'},
                {'files': 'density_mol_3.26_tip4p.csv', 'mol': '3.26'},
                {'files': 'density_mol_4.34_tip4p.csv', 'mol': '4.34'},
                {'files': 'density_mol_5.43_tip4p.csv', 'mol': '5.43'},
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

    x = int(input('\nChoose plot, for solution with molality %smol/kg:'%mol + '\n' + '1.Line'+ '\n' +'2.Bar'+ '\n' + '3.Exit:\n'+ '\n'))

    if x ==1:

        #Plot
        x = df['T']
        y = df['D']
        plt.plot(df['T'], df['D'], marker='o', linestyle='-', color='b')
        plt.xlabel('Temperature, K', fontweight ='bold', fontsize = 15)
        plt.ylabel('Density, g/cm$^3$', fontweight ='bold', fontsize = 15)
        plt.title('Densities with  molality = %s mol/kg'%mol)
        plt.grid(True)
        plt.xticks(x, xlabels, rotation=45)
        plt.ylim(df['D'].min(), df['D'].max())
        plt.figure(figsize=(10, 8))
        plt.show()
        plt.savefig('line_plot_%smol.png'%mol)
    
    elif x == 2:

        #Bar_plot
        x = df['T']
        y = df['D']

        #Figure Size
        fig, ax = plt.subplots(figsize =(9,9))

        # Add Plot Title
        ax.set_title(('Density vs Temperature '+'\n'+'molality= %s mol/kg'%mol),loc ='center', fontweight ='bold', fontsize = 15)

        plt.ylabel('Density, g/cm$^3$', fontweight ='bold', fontsize = 10)
        plt.xlabel('Temperatures, K', fontweight ='bold', fontsize = 10)


        plt.ylim(df['D'].min()-0.001, df['D'].max()+0.001)

        plt.xticks(x, rotation=45, fontsize = 10, size = 10)
        #Horizontal Bar Plot
        plt.bar(x, y, width = 2.52, color ='b', alpha = 0.75, edgecolor ='black', align ='center')


        #ax = df.plot.bar(rot = 0, color='r')
        #df.plot(x="Temp", y="Dens", kind="bar", title=('Density vs Temperatures' + '\n' + 'Molality = 5 mol/kg'),
           #rot=0, color = 'r')
        #Show Plot
#        plt.show()
        plt.savefig('bar_plot_%smol.png'%mol)
    elif x ==3:
        break


