import pickle
import numpy as np
import matplotlib.pyplot as plt
import random
import bisect
import csv
import unicodedata

msaNames=[]
namesFile=csv.reader(open('MSA_COORDS.txt','r'),delimiter='\t')

for line in namesFile:
	msaNames.append(line[0])
#	msaNames.append(unicodedata.normalize('NFD',line[0]))

adjacency=pickle.load(open('ADJACENCY_ADJUSTED.dat'))

nCities=np.shape(adjacency)[0]
# Get number of cities

timeAtCity=np.zeros(shape=nCities)
# This is an array to store number of steps spent at each city

newPosition=-999
oldPosition=random.randint(0,nCities-1)
timeAtCity[oldPosition]+=1
# Choose a random city to start from

#for i in xrange(1):
for i in xrange(1000000):

	randSample=random.random()
	# This gives us a number between 0-1

	newPosition=bisect.bisect_left(np.cumsum(adjacency[oldPosition,:]),randSample)
	# This selects a node that is connected to the current node, 
	# with a probability according to the edge weight

#	print adjacency[oldPosition,:]
#	print randSample
#	print np.sum(adjacency[oldPosition,:])

	timeAtCity[newPosition]+=1

	oldPosition=newPosition

timeAtCity/=np.sum(timeAtCity)

plt.plot(timeAtCity)


maxIndex=np.argmax(timeAtCity)

#plt.axvline(maxIndex,color='k',linestyle='--')

tagIndices=[58,73,229,263,272]

for t in tagIndices:
	plt.axvline(t,color='k',linestyle='--')

plt.xticks(tagIndices,['DC','NY','LDN','BRA','SKM'])

#plt.xticks(range(nCities),msaNames,size=7)

labels=plt.gca().get_xticklabels()
for l in labels:
	l.set_rotation(-90)

plt.show()
