import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
