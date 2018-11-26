#! /usr/bin/python3

from array import array 
from subprocess import call 
import os 

metrics = ["SentPackets",
		"ReceivedUnicastPackets",
		"ReceivedBroadcasts", 
		"SNIRLostPackets", 
		"RXTXLostPackets",
		"TotalLostPackets",
		"DroppedPacketsInMac",
		"receivedFramesLowerMsg",
		"receivedBitsLowerPackets",
		"receivedBits",
		"packetsNotForMe"
                "chUtilizationCCH",
		"chUtilizationSCH1",
		"chUtilizationSCH2",
		"chUtilizationSCH3",
		"chUtilizationSCH4",
		"chUtilizationHPPS",
                "chUtilizationCRIT_SOL",
                "previousSignalQualityCCH",
                "previousSignalQualitySCH1",
                "previousSignalQualitySCH2",
                "previousSignalQualitySCH3",
                "previousSignalQualitySCH4",
                "chPacketsCCH",
                "chPacketsSCH1",
                "chPacketsSCH2",
                "chPacketsSCH3",
                "chPacketsSCH4",
                "numberOfNeighbors",
                "totalBusyTime",
                "ncollisions",
                "generatedWSMs",
                "receivedWSMs",
                "generatedBSMs",
                "receivedBSMs",
                "generatedWSAs",
                "receivedWSAs"]

for metric in metrics:
		
	command = "grep -r " + metric + " -H *.sca | awk -F '-' '{print $1}' | sort -u "
	fileNamesWithMetric = []
	fileNamesWithMetric=os.popen(command).read().splitlines()

	for fileName in fileNamesWithMetric:
		metricFile = metric + "_" + fileName + ".txt"
		scalarFile = fileName + "*"

		print(metricFile)

		if(not os.path.isdir("../../../results_per_metric/")):
			os.popen("mkdir ../../../results_per_metric/")
		createResultsCommand = "grep -r " + metric + " " +scalarFile + " > ../../../results_per_metric/" + metricFile
		print(createResultsCommand)
		os.popen(createResultsCommand)
