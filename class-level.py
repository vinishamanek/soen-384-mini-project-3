import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

junit5_r5_12_2 = pd.read_csv('csv unfiltered/r5.12.2.csv')
junit5_r5_13_1 = pd.read_csv('csv unfiltered/r5.13.1.csv')
junit5_r5_14_0 = pd.read_csv('csv unfiltered/r5.14.0.csv')

extracted_classes_junit5_r5_12_2 = junit5_r5_12_2[
    (junit5_r5_12_2['Kind'].isin(["Private Class", "Public Class"])) & 
    (junit5_r5_12_2['Name'].str.startswith('org.junit.'))
]

extracted_classes_junit5_r5_13_1 = junit5_r5_13_1[
    (junit5_r5_13_1['Kind'].isin(["Private Class", "Public Class"])) & 
    (junit5_r5_13_1['Name'].str.startswith('org.junit.'))
]

extracted_classes_junit5_r5_14_0 = junit5_r5_14_0[
    (junit5_r5_14_0['Kind'].isin(["Private Class", "Public Class"])) & 
    (junit5_r5_14_0['Name'].str.startswith('org.junit.'))
]

extracted_classes_junit5_r5_12_2.isna().sum()
extracted_classes_junit5_r5_13_1.isna().sum()
extracted_classes_junit5_r5_14_0.isna().sum()

# compute the number of classes for each release
print('\nThe number of classes for each type for 12_2 release: \n{}'.format(extracted_classes_junit5_r5_12_2.Kind.value_counts())) 
print('\nThe number of classes for each type for 13_1 release: \n{}'.format(extracted_classes_junit5_r5_13_1.Kind.value_counts()))
print('\nThe number of classes for each type for 14_0 release: \n{}'.format(extracted_classes_junit5_r5_14_0.Kind.value_counts()))

extracted_classes_junit5_r5_12_2.to_csv('classes/csv filtered/r5.12.2-filtered.csv', index=False)
extracted_classes_junit5_r5_13_1.to_csv('classes/csv filtered/r5.13.1-filtered.csv', index=False)
extracted_classes_junit5_r5_14_0.to_csv('classes/csv filtered/r5.14.0-filtered.csv', index=False)

#Plotting boxplots
OO_metrics = ['SumCyclomatic','AvgEssential','MaxInheritanceTree','PercentLackOfCohesion','CountClassDerived','CountClassCoupled','CountDeclMethod','CountLineCode']
x1=extracted_classes_junit5_r5_12_2
x2=extracted_classes_junit5_r5_13_1
x3=extracted_classes_junit5_r5_14_0

os.makedirs('classes/boxplots', exist_ok=True)


outliers_count= np.zeros(len(OO_metrics))
for i in OO_metrics:
    metric= [x1[i],x2[i],x3[i]]
    plt.figure()
    plt.title('Notched Box Plot for '+ i)
    fig = plt.boxplot(metric, notch=True,tick_labels=['r5.12.2','r5.13.1','r5.14.0'])
    plt.ylabel('Variation')
    

    plt.tight_layout()
    plt.savefig(f'classes/boxplots/boxplot_{i}.png', dpi=300, bbox_inches='tight')
    plt.close()