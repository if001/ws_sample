import subprocess
# from Queue import Queue
from multiprocessing import Queue


class RunPython():
    def __init__(self, prog_name):
        self.q = Queue()
        self.prog_name = prog_name
        self.th = myThread(prog_name, self.q);
        self.pid = ""


    def start(self):
        if self.pid == "":
            res = self.th.start()
            message = "start" + str(res)
            self.pid = self.get_pid()
        else :
            message = "It is already running"
        return message


    def get_result(self):
        if self.q.empty :
            res = "empty"
        else :
            res = self.q.get()
        return res


    def stop(self):
        subprocess.getoutput("kill "+str(self.pid))


    def get_pid(self):
        pid = subprocess.getoutput(" ps aux | grep -E -w 'python3.*." + self.prog_name + "'$ | awk '{ print $2 }' ")
        return pid


import time
import threading

class myThread(threading.Thread):
    def __init__(self, prog_name, q):
        super(myThread, self).__init__()
        self.prog_name = prog_name
        self.q = q


    def run(self):
        script_dir = "sample/script/"
        res = subprocess.getoutput("python3 " + script_dir + self.prog_name + " &")
        self.q.put(res)

