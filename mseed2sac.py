# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:09:46 2019

@author: AFC
"""

import obspy
import os
import pandas as pd

mainPath = "."

listOfFiles = pd.DataFrame(columns = ['file', 'fileName', 'day'])
temp = list()
temp1 = list()
temp2 = list()
for (dirpath, dirnames, filenames) in os.walk(mainPath):
    temp += [os.path.join(dirpath, file) for file in filenames if file.split('.')[-1].isdigit()]

listOfFiles['file'] = temp
listOfFiles['fileName'] = [name[-1] for name in listOfFiles['file'].str.split('\\')]
listOfFiles['day'] = [name[-1] for name in listOfFiles['fileName'].str.split('.')]
listOfFiles['E'] = ['EHE' in name for name in listOfFiles['fileName']]
listOfFiles['N'] = ['EHN' in name for name in listOfFiles['fileName']]
listOfFiles['Z'] = ['EHZ' in name for name in listOfFiles['fileName']]

ehe = listOfFiles[listOfFiles['E'] == True][['file', 'fileName', 'day']]
ehn = listOfFiles[listOfFiles['N'] == True][['file', 'fileName', 'day']]
ehz = listOfFiles[listOfFiles['Z'] == True][['file', 'fileName', 'day']]

ehe['day'] = pd.to_numeric(ehe['day'])
ehn['day'] = pd.to_numeric(ehn['day'])
ehz['day'] = pd.to_numeric(ehz['day'])

firstDay = ehe['day'].min()
lastDay = ehe['day'].max()

for index, file in ehe.iterrows():
    if firstDay < file['day'] < lastDay:
        temp = ehe[ehe['day'] == (file['day'] - 1)].values.tolist()
        st = obspy.read(temp[0][0], format='MSEED')
        st += obspy.read(file['file'], format='MSEED')
        temp = ehe[ehe['day'] == (file['day'] + 1)].values.tolist()
        st += obspy.read(temp[0][0], format='MSEED')
        tr = st[0]
        st.merge(method=1, fill_value=0)
        starttime = obspy.UTCDateTime(tr.stats.starttime.year,tr.stats.starttime.month,(tr.stats.starttime.day),0,0)
        starttime += 86400
        endtime = starttime + 86400
        st.trim(starttime= starttime, endtime=endtime)
        tr = st[0]
        name = "{:02d}".format(tr.stats.starttime.year - 2000) + "{:02d}".format(tr.stats.starttime.month)
        name += "{:02d}".format(tr.stats.starttime.day) + "00"
        folder = "./" + str(tr.stats.starttime.year) + "_" + str(tr.stats.starttime.month)
        print(name)
        if not os.path.exists(folder + '/EHE'):
            os.makedirs(folder + '/EHE')
        if not os.path.exists(folder + '/EHN'):
            os.makedirs(folder + '/EHN')
        if not os.path.exists(folder + '/EHZ'):
            os.makedirs(folder + '/EHZ')
        if 'EHE' in file['file']:
            st.write(folder + '/EHE/' + name + 'E.sac', format='SAC')
        if 'EHN' in file['file']:
            st.write(folder + '/EHN/' + name + 'N.sac', format='SAC')
        if 'EHZ' in file['file']:
            st.write(folder + '/EHZ/' + name + 'Z.sac', format='SAC')

firstDay = ehn['day'].min()
lastDay = ehn['day'].max()

for index, file in ehn.iterrows():
    if firstDay < file['day'] < lastDay:
        temp = ehn[ehn['day'] == (file['day'] - 1)].values.tolist()
        st = obspy.read(temp[0][0], format='MSEED')
        st += obspy.read(file['file'], format='MSEED')
        temp = ehn[ehn['day'] == (file['day'] + 1)].values.tolist()
        st += obspy.read(temp[0][0], format='MSEED')
        tr = st[0]
        st.merge(method=1, fill_value=0)
        starttime = obspy.UTCDateTime(tr.stats.starttime.year,tr.stats.starttime.month,(tr.stats.starttime.day),0,0)
        starttime += 86400
        endtime = starttime + 86400
        st.trim(starttime= starttime, endtime=endtime)
        tr = st[0]
        name = "{:02d}".format(tr.stats.starttime.year - 2000) + "{:02d}".format(tr.stats.starttime.month)
        name += "{:02d}".format(tr.stats.starttime.day) + "00"
        folder = "./" + str(tr.stats.starttime.year) + "_" + str(tr.stats.starttime.month)
        print(name)
        if not os.path.exists(folder + '/EHE'):
            os.makedirs(folder + '/EHE')
        if not os.path.exists(folder + '/EHN'):
            os.makedirs(folder + '/EHN')
        if not os.path.exists(folder + '/EHZ'):
            os.makedirs(folder + '/EHZ')
        if 'EHE' in file['file']:
            st.write(folder + '/EHE/' + name + '.sac', format='SAC')
        if 'EHN' in file['file']:
            st.write(folder + '/EHN/' + name + '.sac', format='SAC')
        if 'EHZ' in file['file']:
            st.write(folder + '/EHZ/' + name + '.sac', format='SAC')
            
firstDay = ehz['day'].min()
lastDay = ehz['day'].max()
            
for index, file in ehz.iterrows():
    if firstDay < file['day'] < lastDay:
        temp = ehz[ehz['day'] == (file['day'] - 1)].values.tolist()
        st = obspy.read(temp[0][0], format='MSEED')
        st += obspy.read(file['file'], format='MSEED')
        temp = ehz[ehz['day'] == (file['day'] + 1)].values.tolist()
        st += obspy.read(temp[0][0], format='MSEED')
        tr = st[0]
        st.merge(method=1, fill_value=0)
        starttime = obspy.UTCDateTime(tr.stats.starttime.year,tr.stats.starttime.month,(tr.stats.starttime.day),0,0)
        starttime += 86400
        endtime = starttime + 86400
        st.trim(starttime= starttime, endtime=endtime)
        tr = st[0]
        name = "{:02d}".format(tr.stats.starttime.year - 2000) + "{:02d}".format(tr.stats.starttime.month)
        name += "{:02d}".format(tr.stats.starttime.day) + "00"
        folder = "./" + str(tr.stats.starttime.year) + "_" + str(tr.stats.starttime.month)
        print(name)
        if not os.path.exists(folder + '/EHE'):
            os.makedirs(folder + '/EHE')
        if not os.path.exists(folder + '/EHN'):
            os.makedirs(folder + '/EHN')
        if not os.path.exists(folder + '/EHZ'):
            os.makedirs(folder + '/EHZ')
        if 'EHE' in file['file']:
            st.write(folder + '/EHE/' + name + 'E.sac', format='SAC')
        if 'EHN' in file['file']:
            st.write(folder + '/EHN/' + name + 'N.sac', format='SAC')
        if 'EHZ' in file['file']:
            st.write(folder + '/EHZ/' + name + 'Z.sac', format='SAC')
        
#    print(file)
#    st = obspy.read(file, format='MSEED')
#    st.merge(method=1, fill_value=0)
#    tr = st[0]
#    name = "{:02d}".format(tr.stats.starttime.year - 2000) + "{:02d}".format(tr.stats.starttime.month)
#    name += "{:02d}".format(tr.stats.starttime.day) + "00"
#    folder = "./" + str(tr.stats.starttime.year) + "_" + str(tr.stats.starttime.month)
#    print(name)
#    if not os.path.exists(folder + '/EHE'):
#        os.makedirs(folder + '/EHE')
#    if not os.path.exists(folder + '/EHN'):
#        os.makedirs(folder + '/EHN')
#    if not os.path.exists(folder + '/EHZ'):
#        os.makedirs(folder + '/EHZ')
#    if 'EHE' in file:
#        st.write(folder + '/EHE/' + name + 'E.sac', format='SAC')
#    if 'EHN' in file:
#        st.write(folder + '/EHN/' + name + 'N.sac', format='SAC')
#    if 'EHZ' in file:
#        st.write(folder + '/EHZ/' + name + 'Z.sac', format='SAC')