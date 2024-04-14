from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

import re

#response = requests.get('https://liberalarts.mercer.edu/academic-programs/majors-and-minors/computer-science/faculty-and-staff/')
response = requests.get('https://liberalarts.mercer.edu/academic-programs/majors-and-minors/biology/faculty-and-staff/')
#esponse = requests.get('https://education.mercer.edu/faculty-and-staff/')


#typically a time command is input to not flood website
#time.sleep(1)
soup = BeautifulSoup(response.content, "html.parser")
directory = soup.get_text()
#print(directory)
parser = directory.split()
array = []
array = parser

#print(array)

#########FULL NAME
email = [x for x in array if x.endswith('@mercer.edu')]
matchingArray = []

for i in range(len(email)):
    parts = email[i].split("@")
    email[i] = parts[0]

for i in range(len(email)):
    parts = email[i].split("_")
    email[i] = parts[0]

for i in range(len(email)):
    parts = email[i].split(".")
    email[i] = parts[0]
#gives us array = ['zharo', 'yerby']

EMAIL = [word.capitalize() for word in email]

for i in range(len(array)):
    if array[i] in EMAIL:
        matchingArray.append(i)

minusMatching = [x - 1 for x in matchingArray]
minusMatching2 = [x - 2 for x in matchingArray]

index = [item for pair in zip(minusMatching2, minusMatching, matchingArray) for item in pair]

finalName = []
for i in index:
    if i < len(array):
        finalName.append(array[i])
    else:
        finalName.append(None)
combinedFinalName = [' '.join(finalName[i:i+3]) for i in range(0,len(finalName), 3)]
combinedFinalName = [re.sub(r'[\d-]', '', s).strip() for s in combinedFinalName]
#########FULL NAME

email2 = [x for x in array if x.endswith('@mercer.edu')]

array2 = []
array2 = parser
num = '(478)'

count = 0
for i in array2:
    count = array2.count(num)

numArray = []
for i in range(0,count):
    xval = array2.index(num)
    yval = xval + 1
    ffff = array2[xval]
    ffff2 = array2[yval]
    array2.pop(xval)
    array2.pop(yval)
    fullNum = str(ffff) + '-' + str(ffff2)
    numArray.append(fullNum)
    #print(fullNum)

#print(len(numArray))

pair = [item for pair in zip(combinedFinalName, email2, numArray) for item in pair]
#print(pair)

max_length = max(len(combinedFinalName), len(numArray), len(email2))
combinedFinalName = np.pad(combinedFinalName, (0, max_length - len(combinedFinalName)), constant_values=None)
numArray = np.pad(numArray, (0, max_length - len(numArray)), constant_values=None)
email2 = np.pad(email2, (0, max_length - len(email2)), constant_values=None)

data = {"Name": combinedFinalName,"Number": numArray,"Email": email2}
df = pd.DataFrame(data)
# print(df.to_string(index=False))
# df.to_csv('FullContacts.csv', header=False, index=False)
df1 = df
df1.fillna('Not Available', inplace=True)
print(df1)