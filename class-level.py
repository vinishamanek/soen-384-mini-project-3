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
print('\nThe number of classes for each type for r5_12_2 release: \n{}'.format(extracted_classes_junit5_r5_12_2.Kind.value_counts()))
print('\nThe number of classes for each type for r5_13_1 release: \n{}'.format(extracted_classes_junit5_r5_13_1.Kind.value_counts()))
print('\nThe number of classes for each type for r5_14_0 release: \n{}'.format(extracted_classes_junit5_r5_14_0.Kind.value_counts()))

extracted_classes_junit5_r5_12_2.to_csv('classes/csv filtered/r5.12.2-filtered.csv', index=False)
extracted_classes_junit5_r5_13_1.to_csv('classes/csv filtered/r5.13.1-filtered.csv', index=False)
extracted_classes_junit5_r5_14_0.to_csv('classes/csv filtered/r5.14.0-filtered.csv', index=False)

# Plotting boxplots
OO_metrics = ['SumCyclomatic', 'AvgEssential', 'MaxInheritanceTree', 'PercentLackOfCohesion', 'CountClassDerived', 'CountClassCoupled', 'CountDeclMethod', 'CountLineCode']
x1 = extracted_classes_junit5_r5_12_2
x2 = extracted_classes_junit5_r5_13_1
x3 = extracted_classes_junit5_r5_14_0

os.makedirs('classes/boxplots', exist_ok=True)
os.makedirs('classes/stats', exist_ok=True)


outliers_count = np.zeros(len(OO_metrics))
for i in OO_metrics:
    metric = [x1[i], x2[i], x3[i]]
    plt.figure()
    plt.title('Notched Box Plot for ' + i)
    fig = plt.boxplot(metric, notch=True, tick_labels=['r5.12.2', 'r5.13.1', 'r5.14.0'])

    plt.ylabel('Variation')

    plt.tight_layout()
    plt.savefig(f'classes/boxplots/boxplot_{i}.png', dpi=300, bbox_inches='tight')
    plt.close()
    metric_df = pd.DataFrame({'r5.12.2': x1[i], 'r5.13.1': x2[i], 'r5.14.0': x3[i]})
    metrics = pd.DataFrame()
    metrics.index.name = 'Tags'
    metrics['Median'] = metric_df.median()
    metrics['Bottom Quantile'] = metric_df.quantile(0.25)
    metrics['Top Quantile'] = metric_df.quantile(0.75)
    metrics['Min'] = metric_df.min()
    metrics['Max'] = metric_df.max()
    metrics.to_csv(f"classes/stats/stats_{i}.csv", index=True)


# # Example for version extracted_classes_jsoup_1_14_3, metric SumEssential
# # metric = extracted_classes_jsoup_1_14_3.SumEssential

# q1 = np.quantile(metric, 0.25)
# # finding the 3rd quartile
# q3 = np.quantile(metric, 0.75)
# med = np.median(metric,0.50)
# # finding the iqr region
# iqr = q3-q1

# # finding upper and lower whiskers
# upper_bound = q3+(1.5*iqr)
# lower_bound = q1-(1.5*iqr)
# print(iqr, upper_bound, lower_bound)

# outliers = metric[(metric <= lower_bound) | (metric >= upper_bound)]
# print('The following are the outliers in the boxplot: \n{}'.format(outliers))
# print('The number of outliers for the variable EssentialSum in jsoup_1_14_3 is : \n{}'.format(outliers.values.size))


# plt.figure()
# plt.title('Notched Box Plot for SumEssential in jsoup_1_14_3')
# fig = plt.boxplot(metric, notch=True,labels=['1_14_3'])
# # outliers_count = fig.fliers
# plt.ylabel('Variation')
