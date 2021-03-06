# morteggs.py
# quick normal draw write to file script
# --------------------------------------
import numpy as np
import pdb
from scipy.stats import truncnorm
from scipy.stats import norm

datadir = "D:/projects/CDmetaPOP/Seattle/temp.txt"
mu = 62
sigma = 18
samp = 1378
lower = 0.
upper = 100.
intorfloat = 'float'


# Try #1 - baised
s1 = np.random.normal(mu,sigma,samp)
s1[np.where(s1>100)] = 100.
s1[np.where(s1<0)] = 0.

# Try #2 - biased?
s2 = []
for i in range(samp):
	temp = np.random.normal(mu,sigma,1)[0]
	while temp < 0 or temp > 100:
		temp = np.random.normal(mu,sigma,1)[0]
	s2.append(temp)

# Try #3 - truncnorm
s3 = truncnorm.rvs((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma,size=samp)

outfile = open(datadir,'w')
for i in xrange(len(s3)):
	if intorfloat == 'int':
		outfile.write(str(int(s3[i]))+'\n')
	else:
		outfile.write(str(round(s3[i],2))+'\n')

outfile.close()

# Apply the Todd and Ng method.
datadir = "D:/projects/CDmetaPOP/Seattle/GD182.txt"

# First apply a transformation to mu and sigma
#exp(x) / 1 + exp(x)