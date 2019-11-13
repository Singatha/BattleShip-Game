from PyQt5 import QtCore
from time import *
from GameClient import *

class GameThread(QtCore.QThread):
    update_label_signal = QtCore.pyqtSignal(str)   # creates a signal
    
    
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.game_client = GameClient()   # creates an instance for the class GameClient
        
        
    def connect(self,txt):
        while True:
            try:
                self.game_client.connect_to_server(txt)   # method for connecting to the server 
                break                                           
            
            except:
                print('Error connecting to server!')
                break
            
    def send(self,m):
        self.game_client.send_message(m)
        
        
    
    def run(self):              # run executed when start() method called

       
        while True:
            msg = self.game_client.receive_message()    # gets the message from the server
            sleep(1)                                    # wait a little before emitting next signal
            if len(msg):
                
                
                self.update_label_signal.emit(msg) # emits signal


            else:
                break
    