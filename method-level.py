import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

junit5_r5_12_2 = pd.read_csv('csv unfiltered/r5.12.2.csv')
junit5_r5_13_1 = pd.read_csv('csv unfiltered/r5.13.1.csv')
junit5_r5_14_0 = pd.read_csv('csv unfiltered/r5.14.0.csv')

extracted_methods_junit5_r5_12_2 = junit5_r5_12_2[
    (junit5_r5_12_2['Kind'].isin(["Private Method", "Public Method", "Protected Method"])) & 
    (junit5_r5_12_2['Name'].str.startswith('org.junit.'))
]

extracted_methods_junit5_r5_13_1 = junit5_r5_13_1[
    (junit5_r5_13_1['Kind'].isin(["Private Method", "Public Method", "Protected Method"])) & 
    (junit5_r5_13_1['Name'].str.startswith('org.junit.'))
]

extracted_methods_junit5_r5_14_0 = junit5_r5_14_0[
    (junit5_r5_14_0['Kind'].isin(["Private Method", "Public Method", "Protected Method"])) & 
    (junit5_r5_14_0['Name'].str.startswith('org.junit.'))
]

extracted_methods_junit5_r5_12_2.isna().sum()
extracted_methods_junit5_r5_13_1.isna().sum()
extracted_methods_junit5_r5_14_0.isna().sum()

# compute the number of methods for each release
print('\nThe number of methods for each type for r5_12_2 release: \n{} '.format(extracted_methods_junit5_r5_12_2.Kind.value_counts())) 
print('\nThe number of methods for each type for r5_13_1 release: \n{}'.format(extracted_methods_junit5_r5_13_1.Kind.value_counts()))
print('\nThe number of methods for each type for r5_14_0 release: \n{}'.format(extracted_methods_junit5_r5_14_0.Kind.value_counts()))

extracted_methods_junit5_r5_12_2.to_csv('methods/csv filtered/r5.12.2-filtered.csv', index=False)
extracted_methods_junit5_r5_13_1.to_csv('methods/csv filtered/r5.13.1-filtered.csv', index=False)
extracted_methods_junit5_r5_14_0.to_csv('methods/csv filtered/r5.14.0-filtered.csv', index=False)


def top_5_by_metric(dataframe, metric_column, metric_name, release_name):
    top_5 = dataframe.nlargest(5, metric_column)[['Name', 'Kind', 'CountLineCode', 'SumCyclomatic', 'Essential']]
    
    print(f"\n\nTop 5 methods with highest {metric_name} for {release_name}:")
    print(f"{'Rank':<6} {'SLOC':<8} {'Sum CC':<15} {'EC':<15} {'Kind':<20} {'Method Name'}")
    print(f"{'-'*150}")
    
    for idx, (i, row) in enumerate(top_5.iterrows(), 1):
        print(f"{idx:<6} {row['CountLineCode']:<8.0f} {row['SumCyclomatic']:<15.0f} "
              f"{row['Essential']:<15.1f} {row['Kind']:<20} {row['Name']}")
    
    return top_5

print("="*150)
print("TOP 5 BY SLOC (Source Lines of Code)")
print("="*150)
top_5_sloc_r5_12_2 = top_5_by_metric(extracted_methods_junit5_r5_12_2, 'CountLineCode', 'SLOC', 'r5.12.2')
top_5_sloc_r5_13_1 = top_5_by_metric(extracted_methods_junit5_r5_13_1, 'CountLineCode', 'SLOC', 'r5.13.1')
top_5_sloc_r5_14_0 = top_5_by_metric(extracted_methods_junit5_r5_14_0, 'CountLineCode', 'SLOC', 'r5.14.0')

print("\n" + "="*150)
print("TOP 5 BY EC (Essential Complexity)")
print("="*150)
top_5_ec_r5_12_2 = top_5_by_metric(extracted_methods_junit5_r5_12_2, 'Essential', 'EC', 'r5.12.2')
top_5_ec_r5_13_1 = top_5_by_metric(extracted_methods_junit5_r5_13_1, 'Essential', 'EC', 'r5.13.1')
top_5_ec_r5_14_0 = top_5_by_metric(extracted_methods_junit5_r5_14_0, 'Essential', 'EC', 'r5.14.0')

print("\n" + "="*150)
print("TOP 5 BY SUM CC (Sum Cyclomatic Complexity)")
print("="*150)
top_5_cc_r5_12_2 = top_5_by_metric(extracted_methods_junit5_r5_12_2, 'SumCyclomatic', 'Sum CC', 'r5.12.2')
top_5_cc_r5_13_1 = top_5_by_metric(extracted_methods_junit5_r5_13_1, 'SumCyclomatic', 'Sum CC', 'r5.13.1')
top_5_cc_r5_14_0 = top_5_by_metric(extracted_methods_junit5_r5_14_0, 'SumCyclomatic', 'Sum CC', 'r5.14.0')


OO_metrics = ['CountLineCode', 'SumCyclomatic', 'Essential']
x1 = extracted_methods_junit5_r5_12_2
x2 = extracted_methods_junit5_r5_13_1
x3 = extracted_methods_junit5_r5_14_0

os.makedirs('methods/boxplots', exist_ok=True)

outliers_count = np.zeros(len(OO_metrics))
for i in OO_metrics:
    metric = [x1[i], x2[i], x3[i]]
    plt.figure()
    plt.title('Notched Box Plot for ' + i)
    fig = plt.boxplot(metric, notch=True, tick_labels=['r5.12.2', 'r5.13.1', 'r5.14.0'])

    plt.ylabel('Variation')

    plt.tight_layout()
    plt.savefig(f'methods/boxplots/boxplot_{i}.png', dpi=300, bbox_inches='tight')
    plt.close()
