import psutil
import time
import os
import pandas as pd
import writeData
import plotting

UPDATE_DELAY = 1 # in seconds
WLP2S0 = "wlp2s0"

def get_size(bytes):
    """
    Returns size of bytes in a nice format
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            #return f"{bytes:.2f}{unit}B"
            return f"{bytes}"
        bytes /= 1024

def uploadThroughput(nicInterface):
    # get the network I/O stats from psutil on each network interface
    # by setting `pernic` to `True`
    io = psutil.net_io_counters(pernic=True)
    timeVal = 1
    while True:
        # sleep for `UPDATE_DELAY` seconds
        time.sleep(UPDATE_DELAY)
        # get the network I/O stats again per interface 
        io_2 = psutil.net_io_counters(pernic=True)
        # new - old stats gets us the speed
        upload_speed, download_speed = io_2[nicInterface].bytes_sent - io[nicInterface].bytes_sent, io_2[nicInterface].bytes_recv - io[nicInterface].bytes_recv

        #print(get_size(upload_speed / UPDATE_DELAY))
        print(upload_speed)
        # update the I/O stats for the next iteration
        io = io_2
        # clear the screen based on your OS
        #os.system("cls") if "nt" in os.name else os.system("clear")

        dictValue = {"throughput": upload_speed, "timeOf": timeVal}
        writeData.writeData(dictValue)
        # increment time
        timeVal = timeVal + 1



def start():
    writeData.writeHeader()
    plotting.startPlotting()
    uploadThroughput(WLP2S0)

if __name__ == "__main__":
    start()

