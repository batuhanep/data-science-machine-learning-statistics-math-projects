'''In this project, you’ll investigate some data from a sample patients who were evaluated for heart disease at the Cleveland Clinic Foundation.'''


# import libraries
import codecademylib3
import pandas as pd
import numpy as np

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

# patients with heart disease
chol_hd=yes_hd.chol

#Calculate the mean cholesterol level for patients who were diagnosed with heart disease 

print(np.mean(chol_hd))

#Do people with heart disease have high cholesterol levels (greater than or equal to 240 mg/dl) on average?

from scipy.stats import ttest_1samp
tstat,pval=ttest_1samp(chol_hd, 240)
print(pval/2)

# 0.0035 is less than 0.05

#Do patients without heart disease have average cholesterol levels significantly above 240 mg/dl?

chol_no_hd = no_hd.chol

#mean

print(np.mean(chol_no_hd))

# above 240?

from scipy.stats import ttest_1samp
tstat, pval = ttest_1samp(chol_no_hd, 240)
print(pval/2)

#How many patients are there in this dataset?

num_patients=len(heart)
print(num_patients)

# the number of patients with fasting blood sugar greater than 120
num_highfbs_patients=np.sum(heart.fbs)
print(num_highfbs_patients)

# 8% of the sample
print(0.08*num_patients)

#binomial test 

from scipy.stats import binom_test
pval=binom_test(num_highfbs_patients, num_patients, 0.08, alternative='greater')
print(pval)