#! /usr/bin/python3

import re
import csv
import os

class DataParser():
	
    def parseValue(self, fileNames, metric, headers):
        outputLines=[]
        outputLines.insert(0,headers)

        for fileName in fileNames:
            print(fileName)
            isFileEmpty = os.stat(fileName).st_size 
            if isFileEmpty<=0:
                print ("Empty File")
            file = open(fileName, 'r')
            for index, line in enumerate(file):
                index = index + 1
                value = line.split(metric, 1)[1]
                value = value.strip()
                if fileName == 'DroppedPacketsInMac_B_100_Q_1.txt':
                    print (fileName + value)

                if isFileEmpty<=0 :
                    value = "None"

                if index<=len(outputLines):		
                    outputLines.insert(index, [str(index), value])
                else:
                    someVal = outputLines[index]
                    outputLines[index].append(value)

        return outputLines		

    def printData(self, data):
        fileName = "data.csv"
        with open(fileName, 'w') as file:
            writer = csv.writer(file)
			
            for dataByType in data: 
                for index, line in enumerate(dataByType):
                    row = dataByType[index]

                    writer.writerow(row)
                    print( " ".join(row))
	
    def printDataSet(self, dataByType, fileName):
        with open(fileName, 'wb') as file:
            writer = csv.writer(file)
            for index, line in enumerate(dataByType):
                row = dataByType[index]

                writer.writerow(row)
                print( " ".join(row))

dataParser = DataParser()
metrics = ['SentPackets',
	'ReceivedUnicastPackets',
	'ReceivedBroadcasts',
        'SNIRLostPackets',
	'RXTXLostPackets',
	'TotalLostPackets',
	'DroppedPacketsInMac',
	'receivedFramesLowerMsg',
	'receivedBitsLowerPackets',
	'receivedBits',
	'packetsNotForMe',
        'chUtilizationCCH',
	'chUtilizationSCH1',
	'chUtilizationSCH2',
	'chUtilizationSCH3',
	'chUtilizationSCH4',
	'chUtilizationHPPS',
	'chUtilizationCRIT_SOL',
        'previousSignalQualityCCH',
        'previousSignalQualitySCH1',
        'previousSignalQualitySCH2',
        'previousSignalQualitySCH3',
        'previousSignalQualitySCH4',
        'chPacketsCCH',
        'chPacketsSCH1',
        'chPacketsSCH2',
        'chPacketsSCH3',
        'chPacketsSCH4',
        'numberOfNeighbors',
        'totalBusyTime',
        'ncollisions',
        'generatedWSMs',
        'receivedWSMs',
        'generatedBSMs',
        'receivedBSMs',
        'generatedWSAs',
        'receivedWSAs',
 
        ]

#Per metric 
#Recreate file names to store into data csv file 
#The csv file is created with metrics with header name 
metricsParsed = []

fileName = "data.csv"

for index, metric in enumerate(metrics): 
  
    getfilesWithMetric = "ls | grep " + metric
    fileWithMetrics = []
    fileWithMetrics = os.popen(getfilesWithMetric).read().splitlines()
    headersSentPackets = [metric]
    for index, file in enumerate(fileWithMetrics):
        headersSentPackets.append(file)

	
    dataByMetric = dataParser.parseValue(fileWithMetrics, metric, headersSentPackets)  
    metricsParsed.insert(index, dataByMetric)
	
dataParser.printData(metricsParsed)

filesDroppedPackets = ['DroppedPacketsInMac_B_100_Q_5.txt', 'DroppedPacketsInMac_B_100_Q_2.txt', 'DroppedPacketsInMac_B_100_Q_1.txt' ]
