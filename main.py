from multiprocessing import Process, Queue
from client import ClientWlp

def runWlpProc(queue,host,port):
    runClient = ClientWlp(host,port)
    while True: 
       msg = queue.get()
       if msg == "DONE":
            break
       runClient.sendMsg(msg)
    #runClient.sendMsg(b"butter")

#this function is where the file will be read from
#and determine where to send bytes and sends the bytes
#to the specific queue for a wlps20 or wlps40
def sendToWlp(file,que1,que2):
    que1.put(b"from Queue")
    

def main():
    #two queues that will go to wlp2s0 and wlp4s0 processes respectivelys
    queWlp2 = Queue()
    queWlp4 = Queue()

    #two processes representing sending data from either wlp2s0 or wlp4s0
    proc1 = Process(target=runWlpProc,args=(queWlp4,"192.168.2.1",5005))
    proc2 = Process(target=runWlpProc,args=(queWlp2,"192.168.5.94",5005))
    proc1.start()
    proc2.start()

if __name__ == "__main__":
    main()