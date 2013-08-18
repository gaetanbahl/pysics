import threading,math,physics,time,gamephysics
import sqlite3,sql

import BaseHTTPServer
import SimpleHTTPServer

FILE = 'frontend.html'
PORT = 8080

boost = 2

#conn = sqlite.connect("db.db")
#c = conn.cursor()


class client:

    def __init__(self,id):
        self.id = id

class updateThread(threading.Thread):

    def __init__(self, systeme):

        threading.Thread.__init__(self)
        self.systeme = systeme

    def run(self):
        while 1:
            time.sleep(0.01)
            self.systeme.update_euler()

class lolThread(threading.Thread):

    def __init__(self, string):

        threading.Thread.__init__(self)
        self.string = string

    def run(self):
        self.value = analyse_commande(self.string)


class TestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """The test example handler."""

    def do_POST(self):
        """Handle a post request"""
        length = int(self.headers.getheader('content-length'))
        data_string = self.rfile.read(length)
        print data_string
        #the_thread = lolThread(data_string)
        #the_thread.start()
        #the_thread.join()
        self.wfile.write(analyse_commande(data_string))


def analyse_commande(string):
    l = string.split(" ")
    if l[0] == "newship":

        ship = gamephysics.Ship(int(l[1]),int(l[2]),100,l[3])
        print ship.id
        systeme.addobject(ship)
        return "ok"

    if l[0] == "getall":
        return gamephysics.make_string_of_coord(systeme.getallcoord())

    if l[0] == "newclient":

        cl = client(l[1])
        clientlist.append(cl)
        return "client cree"

    if l[0] == "delclient":

        for i in clientlist:
            if i.id == l[1]:
                del i
        for i in systeme.selectbyid(id):
            del i
        return "clientdeleted"

    if l[0] == "boost":
        for i in systeme.selectbyid(l[1]):

            global boost
            boost = physics.Force(boost*math.cos(i.theta),boost*math.sin(i.theta))
            boost.id = 'boost'
            i.addforce(boost)
        return "boostay"

    if l[0] == "noboost":
        for i in systeme.selectbyid(l[1]):
            for j in i.forces_fixes:
                if j.id == "boost":
                    del j
        return "dayboostay"

    if l[0] == "boostrev":
        for i in systeme.selectbyid(l[1]):

            global boost
            boost = physics.Force(-boost*math.cos(i.theta),-boost*math.sin(i.theta))
            boost.id = 'boost'
            i.addforce(boost)
        return revboostay

    if l[0] == "rotateleft":
        for i in systeme.selectbyid(l[1]):
            i.omega -=1
        return "tournay"

    if l[0] == "rotateright":
        for i in systeme.selectbyid(l[1]):
            i.omega +=1
        return "tournay"

def start_server():
    """Start the server."""
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, TestHandler)
    server.serve_forever()


if __name__ == "__main__":

    clientlist = []

    systeme = gamephysics.Universe(100,100)
    a = gamephysics.Ship(20,20,20,"a")
    b = gamephysics.Ship(100,100,20,"b")
    systeme.addobject(a)
    systeme.addobject(b)

    a.omega = 1
    a.vitx = 0
    b.vity = 0.1

    systeme.setgravity()
    curthread = updateThread(systeme)
    curthread.start()

    #open_browser()
    start_server()

