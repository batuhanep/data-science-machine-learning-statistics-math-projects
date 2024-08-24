'''You are in charge of monitoring the number of defective products from a specific factory. You’ve been told that the number of defects on a given day follows the Poisson distribution with the rate parameter (lambda) equal to 7. You’re new here, so you want to get a feel for what it means to follow the Poisson(7) distribution. You remember that the Poisson distribution is special because the rate parameter represents the expected value of the distribution, so in this case, the expected value of the Poisson(7) distribution is 7 defects per day.'''

import scipy.stats as stats
import numpy as np

### Task Group 1 ###
## Task 1 Create a variable called lam that represents the rate parameter of our distribution.: 

lam = 7

## Task 2 Calculate and print the probability of observing exactly lam defects on a given day.:

print(stats.poisson.pmf(lam, lam))

## Task 3 Our boss said that having 4 or fewer defects on a given day is an exceptionally good day. You are curious about how often that might happen. Calculate and print the probability of having one of these days.:

print(stats.poisson.cdf(4, lam))

## Task 4 On the other hand, our boss said that having more than 9 defects on any given day is considered a bad day. Calculate and print the probability of having one of these bad days. :

print(1- stats.poisson.cdf(9, lam))

### Task Group 2 ###
## Task 5 Create a variable called year_defects that has 365 random values from the Poisson distribution.:

year_defects = stats.poisson.rvs(lam, size = 365)

## Task 6 Print the first 20 values in this data set.:
print(year_defects[0:20])

## Task 7 If we expect 7 defects on a given day, what is the total number of defects we would expect over 365 days?:

print(lam * 365)

## Task 8 Calculate and print the total sum of the data set year_defects. How does this compare to the total number of defects we expected over 365 days?:

print(sum(year_defects))

## Task 9 Calculate and print the average number of defects per day from our simulated dataset.:

print(np.mean(year_defects))

## Task 10 You’re worried about what the highest amount of defects in a single day might be because that would be a hectic day.:

print(year_defects.max())

## Task 11 Calculate and print the probability of observing that maximum value or more from the Poisson(7) distribution.:

print(1-stats.poisson.cdf(year_defects.max(), lam))

### Extra Bonus ###
# Task 12

print(stats.poisson.ppf(0.9, lam))

# 13:

print(sum(year_defects > stats.poisson.ppf(0.9,lam))/len(year_defects))