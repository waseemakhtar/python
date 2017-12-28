'''
   Log workers login & logout time in a stack order i.e; LIFO order
   Invokes thread for each worker's login
'''

import threading
import sys
import datetime
import time

def worker(fd, index):
  fd.write("worker %d login at %s\n" % (index+1, datetime.datetime.now()))
  time.sleep(5 - index)
  fd.write("worker %d logout at %s\n" % (index+1, datetime.datetime.now()))

'''
   Following statement if __name__ == '__main__' makes sure, the code under it i
   doesn't get executed if this file is imported in another file
'''
if __name__ == '__main__':
  #Log file to create workers login and logout time
  fd = open("Worker_log_track.txt", "w")

  #Create an empty list
  threads = list()

  for i in xrange(5):
    #Instantiate a 'Thread' object from a 'threading' class
    th = threading.Thread(target=worker, args=(fd, i))
    #Maintain the list of threads instantiated
    threads.append(th)
    #Run the thread
    th.start()

  #Wait for the threads to terminate
  for each in threads:
    each.join()
  #Close the file descriptor
  fd.close()
