import csv
import random
import time

fieldNames = ["throughput","timeOf"]

def writeHeader():
        
    with open('data.csv','w') as csvFile:
        csvWriter = csv.DictWriter(csvFile,fieldnames=fieldNames)
        csvWriter.writeheader()

def writeData(data):

    with open('data.csv','a') as csvFile:
        csvWriter = csv.DictWriter(csvFile, fieldnames=fieldNames)
    
        info = {
            "throughput": data['throughput'],
            "timeOf": data['timeOf']
        }

        csvWriter.writerow(info)
    