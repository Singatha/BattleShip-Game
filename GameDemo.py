import sys
from PyQt5.QtWidgets import * #QApplication, QMainWindow, QWidget
from PyQt5.QtGui import * #QPainter, QColor, QFont
from GameClient import *
from GameThread import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        widget = QWidget()
        self.setCentralWidget(widget)   
        
        topFiller = QWidget()
        topFiller.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)        

        bottomFiller = QWidget()
        bottomFiller.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        
        
        self.setGeometry(200,200,1000,600)          # sets the window size 	
        self.setWindowTitle('BattleShip Game')       # creates the window's name 
        
        self.current_role = ''
        self.Captain_Score = 0
        self.General_Score = 0
        self.board = [x[:] for x in [[' ']*6]*6] 
        
        
        
        #self.opponent_role = ''
        #self.menu_bar =  .QMenuBar(self)
        #exitMenu = self.menu_bar.addMenu('')
        
        #exitAction =  .QAction('How to play', self)        
        #exitMenu.addAction(exitAction) 
        
        
        #self.setPalette( .QPalette( .QColor('powderblue')))      # sets the background colour of the window
        #self.setAutoFillBackground(True)       
        
        
        #self.palette =  .QPalette()
        #self.palette.setBrush( .QPalette.Background,QBrush(QPixmap("pirate.jpg")))
        #self.setPalette(self.palette)

         
        
        server_hbox = QHBoxLayout()                                  # creates a horizontal box layout for the label enter server, line edit and connect button 
        
        self.server_label = QLabel('Enter Server:',self)            # creates a the enter server label 
        self.server_label.setFont(QFont('Arial',10,2))             # sets the font of the enter server label    
        self.edit_server = QLineEdit(self)                        # creates the line edit for the user to enter IP address 
        self.connect = QPushButton('Connect')                    # creates the connect button
        #self.how_to_play =  .QPushButton('How to play')           # creates the how to play button
        
        self.label = QLabel('Waiting for opponent to connect...',self)      # creates a label that sends the status of the game to the user 
        self.label.setFont(QFont('Arial',10,2))                   # sets the font of the label
        
        server_hbox.addWidget(self.server_label)                 # adds the server label to the server hbox layout  
        server_hbox.addWidget(self.edit_server)                # adds the line edit to the server hboxl ayout
        server_hbox.addWidget(self.connect)                   # adds the connect button to the server hbox layout   
        #server_hbox.addWidget(self.how_to_play)                # adds the how to play button to the server hbox layout
        server_hbox_widget = QWidget()                    # creates a widget for the server hbox layouyt
        server_hbox_widget.setLayout(server_hbox)                 # sets the server hbox layout       
    
        
        
        self.role_frame = QGroupBox('Role')                       # creates a frame around the role panel
        self.role_frame.setFont(QFont('Arial',10,2,))            # sets font of the heading of the frame
        self.transition = QPushButton("")
        self.transition.setFixedHeight(60)
        
        role_hbox = QHBoxLayout()                               # creates a vertical box layout
        
        self.role = QLabel('You are the General',self)         # creates the role label  
        self.role.setFont(QFont('Arial',10,2))                # sets the font of the character label
        
        role_hbox.addWidget(self.role)
        role_hbox.addWidget(self.transition)
        self.role_frame.setLayout(role_hbox)                      # sets the GroupBox frame and the role vbox layout
         
        
        
        self.message_frame = QGroupBox("Messages from the Server")       # creates a frame around the message label, captain's score label and general's score label
        self.message_frame.setFont(QFont('Arial',10,2,))               # sets the font of the message label
            
        
        message_grid = QGridLayout()                           # sets the grid layout 
        
        self.message_text = QTextEdit()                      # creates the text edit  
        
        
        message_grid.addWidget(self.message_text,1,0,3,0)      # adds the text edit to the grid layout 
        self.message_frame.setLayout(message_grid)          # sets the groupbox frame and the grid layout 

        
        
        button_hbox = QHBoxLayout()                        # creates a horizontal box layout
        
        #self.close =  .QPushButton('Close')                   # creates the close button  
        #self.new_game =  .QPushButton('New Game')              # creates the New game button  

        #button_hbox.addWidget(self.close)         # adds the close to the layout
        #button_hbox.addWidget(self.new_game)         # adds the new game to the layout
        button_hbox_widget = QWidget()           # creates a widget for the layouyt
        button_hbox_widget.setLayout(button_hbox)        # sets the groupbox frame and the grid layout 
        
        self.score_frame = QGroupBox("Score")             # creates a frame around the score panel 
        self.score_frame.setFont(QFont('Arial',10,2))    # sets the heading of the frame 
        
        score_grid = QGridLayout()       # sets the grid layout for the main window
        
        self.captain_score_label = QLabel('Captain:',self)      # creates a captain label   
        self.general_score_label = QLabel('General:',self)     # creates a general label
        self.captain_score_label.setFont(QFont('Arial',10,2))   # sets the captain label font
        self.general_score_label.setFont(QFont('Arial',10,2))  # sets the general label font
        
        
        self.captain_score = QLabel('0',self)     # creates a label for the captain's score
        self.general_score = QLabel('0',self)     # creates a label for the general's score

        score_grid.addWidget(self.captain_score_label,1,0)    # adds the captain  label to the layout 
        score_grid.addWidget(self.general_score_label,2,0)    # adds the general label to the layout
        score_grid.addWidget(self.captain_score,1,1)        # adds the captain score label to the layout
        score_grid.addWidget(self.general_score,2,1)        # adds the captain score label to the layout
        self.score_frame.setLayout(score_grid) 
    # sets the groupbox frame and the grid layout 
        
        
        self.board_frame = QGroupBox("Board")           # creates a frame around the board panel
        self.board_frame.setFont(QFont('Arial',10,2,))   # sets the heading of the frame
        
 
        self.target = QPixmap('target.png')
        self.target.setMask(self.target.mask())
        self.target_cursor = QCursor(self.target)
        self.board_frame.setCursor(self.target_cursor)        

        board_grid = QGridLayout()                             # creates a grid layout
        
        
        # creates 6x6 buttons
        
        self.button_1 = QPushButton('',self)
        self.button_1.setFixedHeight(60)            #  sets the height of the buttons
        
        self.button_2 = QPushButton('',self)
        self.button_2.setFixedHeight(60)
        
        self.button_3 = QPushButton('',self)
        self.button_3.setFixedHeight(60)
        
        self.button_4 = QPushButton('',self)
        self.button_4.setFixedHeight(60)
        
        self.button_5 = QPushButton('',self)
        self.button_5.setFixedHeight(60)
        
        self.button_6 = QPushButton('',self)
        self.button_6.setFixedHeight(60)
        
        self.button_7 = QPushButton('',self)
        self.button_7.setFixedHeight(60)
        
        self.button_8 = QPushButton('',self)
        self.button_8.setFixedHeight(60)
        
        self.button_9 = QPushButton('',self)
        self.button_9.setFixedHeight(60)
        
        self.button_10 = QPushButton('',self)
        self.button_10.setFixedHeight(60)
        
        self.button_11 = QPushButton('',self)
        self.button_11.setFixedHeight(60)
        
        self.button_12 = QPushButton('',self)
        self.button_12.setFixedHeight(60)
        
        self.button_13 = QPushButton('',self) 
        self.button_13.setFixedHeight(60)
        
        self.button_14 = QPushButton('',self)
        self.button_14.setFixedHeight(60)
        
        self.button_15 = QPushButton('',self)
        self.button_15.setFixedHeight(60)
        
        self.button_16 = QPushButton('',self)
        self.button_16.setFixedHeight(60)
        
        self.button_17 = QPushButton('',self)
        self.button_17.setFixedHeight(60)
        
        self.button_18 = QPushButton('',self)
        self.button_18.setFixedHeight(60)
        
        self.button_19 = QPushButton('',self)
        self.button_19.setFixedHeight(60)
        
        self.button_20 = QPushButton('',self)
        self.button_20.setFixedHeight(60)
        
        self.button_21 = QPushButton('',self)
        self.button_21.setFixedHeight(60)
        
        self.button_22 = QPushButton('',self)
        self.button_22.setFixedHeight(60)
        
        self.button_23 = QPushButton('',self)
        self.button_23.setFixedHeight(60)
        
        self.button_24 = QPushButton('',self)
        self.button_24.setFixedHeight(60)
        
        self.button_25 = QPushButton('',self)
        self.button_25.setFixedHeight(60)
        
        self.button_26 = QPushButton('',self)
        self.button_26.setFixedHeight(60)
        
        self.button_27 = QPushButton('',self)
        self.button_27.setFixedHeight(60)
        
        self.button_28 = QPushButton('',self)
        self.button_28.setFixedHeight(60)
        
        self.button_29 = QPushButton('',self)
        self.button_29.setFixedHeight(60)
        
        self.button_30 = QPushButton('',self)
        self.button_30.setFixedHeight(60)
        
        self.button_31 = QPushButton('',self)
        self.button_31.setFixedHeight(60)
        
        self.button_32 = QPushButton('',self)
        self.button_32.setFixedHeight(60)
        
        self.button_33 = QPushButton('',self)
        self.button_33.setFixedHeight(60)
        
        self.button_34 = QPushButton('',self)
        self.button_34.setFixedHeight(60)
        
        self.button_35 = QPushButton('',self)
        self.button_35.setFixedHeight(60)
        
        self.button_36 = QPushButton('',self)
        self.button_36.setFixedHeight(60)
        
        
        self.button_1.clicked.connect(self.set_move_1) 
        self.button_2.clicked.connect(self.set_move_2) 
        self.button_3.clicked.connect(self.set_move_3) 
        self.button_4.clicked.connect(self.set_move_4) 
        self.button_5.clicked.connect(self.set_move_5) 
        self.button_6.clicked.connect(self.set_move_6) 
        
        self.button_7.clicked.connect(self.set_move_7) 
        self.button_8.clicked.connect(self.set_move_8) 
        self.button_9.clicked.connect(self.set_move_9) 
        self.button_10.clicked.connect(self.set_move_10) 
        self.button_11.clicked.connect(self.set_move_11) 
        self.button_12.clicked.connect(self.set_move_12) 
        
        self.button_13.clicked.connect(self.set_move_13) 
        self.button_14.clicked.connect(self.set_move_14) 
        self.button_15.clicked.connect(self.set_move_15) 
        self.button_16.clicked.connect(self.set_move_16) 
        self.button_17.clicked.connect(self.set_move_17) 
        self.button_18.clicked.connect(self.set_move_18)
        
        self.button_19.clicked.connect(self.set_move_19) 
        self.button_20.clicked.connect(self.set_move_20) 
        self.button_21.clicked.connect(self.set_move_21) 
        self.button_22.clicked.connect(self.set_move_22) 
        self.button_23.clicked.connect(self.set_move_23) 
        self.button_24.clicked.connect(self.set_move_24) 
        
        self.button_25.clicked.connect(self.set_move_25) 
        self.button_26.clicked.connect(self.set_move_26) 
        self.button_27.clicked.connect(self.set_move_27) 
        self.button_28.clicked.connect(self.set_move_28) 
        self.button_29.clicked.connect(self.set_move_29) 
        self.button_30.clicked.connect(self.set_move_30) 
        
        self.button_31.clicked.connect(self.set_move_31) 
        self.button_32.clicked.connect(self.set_move_32) 
        self.button_33.clicked.connect(self.set_move_33) 
        self.button_34.clicked.connect(self.set_move_34) 
        self.button_35.clicked.connect(self.set_move_35) 
        self.button_36.clicked.connect(self.set_move_36) 
        

        # adds buttons to the layout          
    
        board_grid.addWidget(self.button_1,0,0)               
        board_grid.addWidget(self.button_2,0,1)
        board_grid.addWidget(self.button_3,0,2)
        board_grid.addWidget(self.button_4,0,3)
        board_grid.addWidget(self.button_5,0,4)
        board_grid.addWidget(self.button_6,0,5)
        board_grid.addWidget(self.button_7,1,0)
        board_grid.addWidget(self.button_8,1,1)
        board_grid.addWidget(self.button_9,1,2)
        board_grid.addWidget(self.button_10,1,3)
        board_grid.addWidget(self.button_11,1,4)
        board_grid.addWidget(self.button_12,1,5)
        board_grid.addWidget(self.button_13,2,0)
        board_grid.addWidget(self.button_14,2,1)
        board_grid.addWidget(self.button_15,2,2)
        board_grid.addWidget(self.button_16,2,3)
        board_grid.addWidget(self.button_17,2,4)
        board_grid.addWidget(self.button_18,2,5)
        board_grid.addWidget(self.button_19,3,0)
        board_grid.addWidget(self.button_20,3,1)
        board_grid.addWidget(self.button_21,3,2)
        board_grid.addWidget(self.button_22,3,3)
        board_grid.addWidget(self.button_23,3,4)
        board_grid.addWidget(self.button_24,3,5)
        board_grid.addWidget(self.button_25,4,0)
        board_grid.addWidget(self.button_26,4,1)
        board_grid.addWidget(self.button_27,4,2)
        board_grid.addWidget(self.button_28,4,3)
        board_grid.addWidget(self.button_29,4,4)
        board_grid.addWidget(self.button_30,4,5)           
        board_grid.addWidget(self.button_31,5,0)
        board_grid.addWidget(self.button_32,5,1)
        board_grid.addWidget(self.button_33,5,2)
        board_grid.addWidget(self.button_34,5,3)
        board_grid.addWidget(self.button_35,5,4)
        board_grid.addWidget(self.button_36,5,5)
        
        self.board_frame.setLayout(board_grid)                # sets the groupbox frame and the grid layout around the grid buttons
        
        
        board_vbox = QVBoxLayout()              # creates a vertical box layout
        board_vbox.addWidget(self.board_frame)        # adds the groupbox frame and the grid layout to the vbox layout 
        board_vbox_widget = QWidget()           # creates widget for the vbox layout
        board_vbox_widget.setLayout(board_vbox)        # sets the board vbox layout 

        
        main_grid = QGridLayout()             # creates a main grid layout
        
        main_grid.addWidget(server_hbox_widget,2,1)   # adds server hbox widget to the main grid layout
        #main_grid.addWidget(self.label,2,2) 
        main_grid.addWidget(self.role_frame,3,1)  # adds role_spin_box to the main grid layout
        main_grid.addWidget(self.board_frame,4,1)  # adds board_spin_box to the main grid layout
        main_grid.addWidget(button_hbox_widget,5,1)   # adds button_hbox_widget to the main grid layout
        main_grid.addWidget(self.score_frame,3,2)   # adds score_spin_box to the main grid layout
        main_grid.addWidget(self.message_frame,4,2)  # adds message_spin_box to the main grid layout

        widget.setLayout(main_grid)                        # sets the layout of the main grid layout
    
        #self.close.clicked.connect(self.close_button)         # connects the connect button to the connect_button function  
        self.connect.clicked.connect(self.connect_button)    # connects the close button to the close_button function
        #self.how_to_play.clicked.connect(self.help)          # connects the how to play button to the help function 
        #self.new_game.clicked.connect(self.clear_board)
        self.game_thread = GameThread()                                                     # creates an instance for the class GameThread  
        self.game_thread.update_label_signal.connect(self.game_thread_slot)                 # connects the signal from the loop thread to the slot game_thread_slot 
       
    
      
      
      
        self.moves = {self.button_1:'0,0', self.button_2:'0,1', self.button_3:'0,2', self.button_4:'0,3', self.button_5:'0,4', self.button_6:'0,5', self.button_7:'1,0', self.button_8:'1,1', self.button_9:'1,2', self.button_10:'1,3', self.button_11:'1,4', self.button_12:'1,5', self.button_13:'2,0', self.button_14:'2,1', self.button_15:'2,2', self.button_16:'2,3', self. button_17:'2,4', self.button_18:'2,5', self.button_19:'3,0', self.button_20:'3,1', self.button_21:'3,2', self.button_22:'3,3', self.button_23:'3,4', self.button_24:'3,5', self.button_25:'4,0', self.button_26:'4,1', self.button_27:'4,2', self.button_28:'4,3', self.button_29:'4,4', self.button_30:'4,5', self.button_31:'5,0', self.button_32:'5,1', self.button_33:'5,2', self.button_34:'5,3', self.button_35:'5,4', self.button_36:'5,5'}   
      
      
        self.createActions()
        self.createMenus()
        message = "Click the Options drop-down menu for more functionality"
        self.statusBar().showMessage(message)
        
      
      
      
    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction(self.cutAct)
        menu.addAction(self.copyAct)
        menu.addAction(self.pasteAct)
        menu.exec_(event.globalPos())      
      
    def createActions(self):
        self.newGameAct = QAction("&New Game", self,
                shortcut= QKeySequence.New,
                statusTip="Create a new Game", triggered=self.clear_board)
 
        self.closeAct = QAction("&Close...", self,
                shortcut= QKeySequence.Close,
                statusTip="Close the game", triggered=self.close_button)
        self.descriptionAct = QAction("&Description", self,
                        shortcut = "Ctrl+D",
                        statusTip="Open Game Description Window",
                        triggered=self.help)    
        
    def createMenus(self):
        
            self.fileMenu = self.menuBar().addMenu("&Options")
            self.fileMenu.addAction(self.newGameAct)
            self.fileMenu.addAction(self.closeAct)
            self.fileMenu.addAction(self.descriptionAct)
        
    # creates a pop window which gives a description about the game and how to play it 
    def help(self):
        self.choice = QMessageBox.information(self, 'How to play',"The game involves two officers in the same army, a Captain and a General. Both of you will be responsible for sinking enemy ships, the officer with most ship hits wins. You wil be assigned either a Captain's role or the General's role. Fire a shot by clicking at one of the buttons in the grid.")
        self.choice.setFont(QFont('Arial',20,2))
     
    # a function that handles the signal from the loop thread   
    def game_thread_slot(self,txt):
        self.message_text.append(txt)   # displays the messages from the loop thread to the message text edit 
        #self.clear_board()
        
        msg = txt.split(",")
        
        if msg[0] == "new game":
            self.clear_board()
            self.Update_Board()
            
            if msg[1] == "G":
                self.role.setText("You are the General!")
                self.transition.setIcon(QIcon("general.png"))
                
                message = "Ahoy General"
                self.statusBar().showMessage(message)                
                
                self.transition.setIconSize(QtCore.QSize(55,55))
                self.role.setFont(QFont('Arial',10,2))
                self.label.setText('Connected')
                self.captain_score.setText('0')
                self.general_score.setText('0')
                
            elif msg[1] == "C":
                self.role.setText("you are the Captain!")
                self.transition.setIcon(QIcon("captain.png"))
                
                message = "Ahoy General"
                self.statusBar().showMessage(message)                 
                
                self.transition.setIconSize(QtCore.QSize(55,55))
                self.role.setFont(QFont('Arial',10,2))
                self.label.setText('Connected')
                self.captain_score.setText('0')
                self.general_score.setText('0')
                
        elif msg[0] == "your move":
    
            self.Update_Board
            
            message = "Your Move"
            self.statusBar().showMessage(message)   
            
        elif msg[0] == "opponent":
            
            
            self.Update_Board
        
        
        elif msg[0] == "valid move":
            Captain_Score = msg[4]
            General_Score = msg[5]
            Role = msg[1]
            
            row = int(msg[2])
            col = int(msg[3])
            
            if Role == "C":

                '''
                Captain
                places C if its a hit
                       c if its not  a hit
                '''
                if int(Captain_Score)> self.Captain_Score:  
                    self.board[row][col] = Role
                    self.Captain_Score = int(Captain_Score)
                    self.captain_score.setText(str(Captain_Score))
                    self.Update_Board()
                elif int(Captain_Score) == self.Captain_Score:
                    self.board[row][col] = Role.lower()
                    self.Update_Board()
                    
            elif Role == "G":
                '''
                Sent Message Client 0: valid move,C,0,4,0,0
                General
                places G if its a hit
                       g if its not a hit
                '''
                
                if int(General_Score)> self.General_Score:                          
                    self.board[row][col] = Role
                    self.General_Score = int(General_Score)
                    self.general_score.setText(str(General_Score))
                    self.Update_Board()
                    
                elif int(General_Score) ==self.General_Score:
                    self.board[row][col] = Role.lower() 
                    self.Update_Board()   
                    
        elif msg[0] == "invalid move":
            QMessageBox.warning(self,"Notification","Invalid, Play again")
            
        elif msg[0] == "play again":
            self.Option = QMessageBox.information(self,"Notification","Would you like to play again",  QMessageBox.Yes|  QMessageBox.No)
            
            if self.Option == QMessageBox.Yes:
                self.game_thread.send("Yes")
            else:
                self.game_thread.send("No")
                
        elif msg == "game over":
            
            if msg[0] == "G":
                QMessageBox.information(self,"Announcement","The General emerged Victorious")
            elif msg[0] == "C":
                
                QMessageBox.information(self,"Announcement","The Captain emerged Victorious")
                
            elif msg[0] == "T":
                QMessageBox.information(self,"Announcement","It is a tie")
                
            elif msg[0] == "exit game":

                self.Option = QMessageBox.warning(self,"Notification","Are you sure you want to exit",  QMessageBox.Yes|  QMessageBox.No)
                 
                if self.Option ==  QMessageBox.Yes:
                    self.game_thread.send("Yes")
                else:
                    self.game_thread.send("No")                                               
                                        
    def set_move_1(self):
        self.move1 = self.moves[self.button_1]
        self.Shot
        self.game_thread.send(self.move1)

        
    def set_move_2(self):
        self.move2 = self.moves[self.button_2]
        self.Shot
        self.game_thread.send(self.move2)     
            
        
    def set_move_3(self):
        self.move3 = self.moves[self.button_3]
        self.Shot
        self.game_thread.send(self.move3)            
        
        
    def set_move_4(self):
        self.move4 = self.moves[self.button_4]
        self.Shot
        self.game_thread.send(self.move4)    
        
        
    def set_move_5(self):
        self.move5 = self.moves[self.button_5]
        self.Shot
        self.game_thread.send(self.move5)                
        
    
    def set_move_6(self):
        self.move6 = self.moves[self.button_6]
        self.Shot
        self.game_thread.send(self.move6)                
        
        
    def set_move_7(self):
        self.move7 = self.moves[self.button_7]
        self.Shot
        self.game_thread.send(self.move7)                
        
        
    def set_move_8(self):
        self.move8 = self.moves[self.button_8]
        self.Shot
        self.game_thread.send(self.move8)                
        
        
    def set_move_9(self):
        self.move9 = self.moves[self.button_9]
        self.Shot
        self.game_thread.send(self.move9)                
        
    
    def set_move_10(self):
        self.move10 = self.moves[self.button_10]
        self.Shot
        self.game_thread.send(self.move10)                
        

    def set_move_11(self):
        self.move11 = self.moves[self.button_11]
        self.Shot
        self.game_thread.send(self.move11)                
        
        
    def set_move_12(self):
        self.move12 = self.moves[self.button_12]
        self.Shot
        self.game_thread.send(self.move12)                
        
        
    def set_move_13(self):
        self.move13 = self.moves[self.button_13]
        self.Shot
        self.game_thread.send(self.move13)                
        
        
    def set_move_14(self):
        
        self.move14 = self.moves[self.button_14]
        self.Shot
        self.game_thread.send(self.move14)                
        
        
    def set_move_15(self):
        self.move15 = self.moves[self.button_15]
        self.Shot
        self.game_thread.send(self.move15)                
        
        
    def set_move_16(self):
        self.move16 = self.moves[self.button_16]
        self.Shot
        self.game_thread.send(self.move16)                
        
        
    def set_move_17(self):
        self.move17 = self.moves[self.button_17]
        self.Shot
        self.game_thread.send(self.move17)                
        
        
    def set_move_18(self):
        self.move18 = self.moves[self.button_18]
        self.Shot
        self.game_thread.send(self.move18)                
        
        
    def set_move_19(self):
        self.move19 = self.moves[self.button_19]
        self.Shot
        self.game_thread.send(self.move19)                
        
        
    def set_move_20(self):
        self.move20 = self.moves[self.button_20]
        self.Shot
        self.game_thread.send(self.move20)                
        
        
    def set_move_21(self):
        self.move21 = self.moves[self.button_21]
        self.Shot
        self.game_thread.send(self.move21)                
                
    def set_move_22(self):
        self.move22 = self.moves[self.button_22]
        self.Shot
        self.game_thread.send(self.move22)                
        
        
    def set_move_23(self):
        self.move23 = self.moves[self.button_23]
        self.Shot
        self.game_thread.send(self.move23)                
        
    def set_move_24(self):
        self.move24 = self.moves[self.button_24]
        self.Shot
        self.game_thread.send(self.move24)                
    
    def set_move_25(self):
        self.move25 = self.moves[self.button_25]
        self.Shot
        self.game_thread.send(self.move25)                
                
    def set_move_26(self):
        self.move26 = self.moves[self.button_26]
        self.Shot
        self.game_thread.send(self.move26)                
    
    def set_move_27(self):
        self.move27 = self.moves[self.button_27]
        self.Shot
        self.game_thread.send(self.move27)                
        
    def set_move_28(self):
        self.move28 = self.moves[self.button_28]
        self.Shot
        self.game_thread.send(self.move28) 
        
          
    def set_move_29(self):
        self.move29 = self.moves[self.button_29]
        self.Shot
        self.game_thread.send(self.move29)                
    
    def set_move_30(self):
        self.move30 = self.moves[self.button_30]
        self.Shot
        self.game_thread.send(self.move30)                

    def set_move_31(self):
        self.move31 = self.moves[self.button_31]
        self.Shot
        self.game_thread.send(self.move31)                
    
    def set_move_32(self):
        self.move32 = self.moves[self.button_32]
        self.Shot
        self.game_thread.send(self.move32)                

    def set_move_33(self):
        self.move33 = self.moves[self.button_33]
        self.Shot
        self.game_thread.send(self.move33)                
    
    def set_move_34(self):
        self.move34 = self.moves[self.button_34]
        self.Shot
        self.game_thread.send(self.move34)                
               
    def set_move_35(self):
        self.move35 = self.moves[self.button_35]
        self.Shot
        self.game_thread.send(self.move35)
        self.button_35.setText
    
    def set_move_36(self):
        self.move36 = self.moves[self.button_36]
        self.Shot
        self.game_thread.send(self.move36)                
                   
     
                
                
    def clear_board(self):
        self.board_ = [x[:] for x in [[' ']*6]*6]  
        self.board = [x[:] for x in [[' ']*6]*6]
        self.current_role = ''
        self.Captain_Score = 0
        self.General_Score = 0        
        
        self.button_1.setIcon(QIcon("default.png"))
        self.button_1.setIconSize(QtCore.QSize(65,65))
        
        self.button_2.setIcon(QIcon("default.png"))
        self.button_2.setIconSize(QtCore.QSize(65,65))
        
        self.button_3.setIcon(QIcon("default.png"))
        self.button_3.setIconSize(QtCore.QSize(65,65))

        self.button_4.setIcon(QIcon("default.png"))
        self.button_4.setIconSize(QtCore.QSize(65,65))

        self.button_5.setIcon(QIcon("default.png"))
        self.button_5.setIconSize(QtCore.QSize(65,65))

        self.button_6.setIcon(QIcon("default.png"))
        self.button_6.setIconSize(QtCore.QSize(65,65))

        self.button_7.setIcon(QIcon("default.png"))
        self.button_7.setIconSize(QtCore.QSize(65,65))
        
        self.button_8.setIcon(QIcon("default.png"))
        self.button_8.setIconSize(QtCore.QSize(65,65))
        
        self.button_9.setIcon(QIcon("default.png"))
        self.button_9.setIconSize(QtCore.QSize(65,65))

        self.button_10.setIcon(QIcon("default.png"))
        self.button_10.setIconSize(QtCore.QSize(65,65))
        
        self.button_11.setIcon(QIcon("default.png"))
        self.button_11.setIconSize(QtCore.QSize(65,65))
        
        self.button_12.setIcon(QIcon("default.png"))
        self.button_12.setIconSize(QtCore.QSize(65,65))
        
        self.button_13.setIcon(QIcon("default.png"))
        self.button_13.setIconSize(QtCore.QSize(65,65))
     
        self.button_14.setIcon(QIcon("default.png"))
        self.button_14.setIconSize(QtCore.QSize(65,65))
  
        self.button_15.setIcon(QIcon("default.png"))
        self.button_15.setIconSize(QtCore.QSize(65,65))
     
        self.button_16.setIcon(QIcon("default.png"))
        self.button_16.setIconSize(QtCore.QSize(65,65))
      
        self.button_17.setIcon(QIcon("default.png"))
        self.button_17.setIconSize(QtCore.QSize(65,65))
        
        self.button_18.setIcon(QIcon("default.png"))
        self.button_18.setIconSize(QtCore.QSize(65,65))
        
        self.button_19.setIcon(QIcon("default.png"))
        self.button_19.setIconSize(QtCore.QSize(65,65))
        
        self.button_20.setIcon(QIcon("default.png"))
        self.button_20.setIconSize(QtCore.QSize(65,65))
        

        self.button_21.setIcon(QIcon("default.png"))
        self.button_21.setIconSize(QtCore.QSize(65,65))

        self.button_22.setIcon(QIcon("default.png"))
        self.button_22.setIconSize(QtCore.QSize(65,65))

        self.button_23.setIcon(QIcon("default.png"))
        self.button_23.setIconSize(QtCore.QSize(65,65))

        self.button_24.setIcon(QIcon("default.png"))
        self.button_24.setIconSize(QtCore.QSize(65,65))

        self.button_25.setIcon(QIcon("default.png"))
        self.button_25.setIconSize(QtCore.QSize(65,65))

        self.button_26.setIcon(QIcon("default.png"))
        self.button_26.setIconSize(QtCore.QSize(65,65))

        self.button_27.setIcon(QIcon("default.png"))
        self.button_27.setIconSize(QtCore.QSize(65,65))

        self.button_28.setIcon(QIcon("default.png"))
        self.button_28.setIconSize(QtCore.QSize(65,65))

        self.button_29.setIcon(QIcon("default.png"))
        self.button_29.setIconSize(QtCore.QSize(65,65))

        self.button_30.setIcon(QIcon("default.png"))
        self.button_30.setIconSize(QtCore.QSize(65,65))

        self.button_31.setIcon(QIcon("default.png"))
        self.button_31.setIconSize(QtCore.QSize(65,65))

        self.button_32.setIcon(QIcon("default.png"))
        self.button_32.setIconSize(QtCore.QSize(65,65))

        self.button_33.setIcon(QIcon("default.png"))
        self.button_33.setIconSize(QtCore.QSize(65,65))

        self.button_34.setIcon(QIcon("default.png"))
        self.button_34.setIconSize(QtCore.QSize(65,65))

        self.button_35.setIcon(QIcon("default.png"))
        self.button_35.setIconSize(QtCore.QSize(65,65))

        self.button_36.setIcon(QIcon("default.png"))
        self.button_36.setIconSize(QtCore.QSize(65,65))
        
    def Update_Board(self):
        self.board_ = [x[:] for x in [[' ']*6]*6]
        for i in range(0,6):
            for j in range(0,6):
                if self.board[i][j] == "G":
                    photo = "CapitalG.png"
                    self.board_[i][j] = photo
                elif self.board[i][j] == "C":
                    photo = "CapitalC.png"
                    self.board_[i][j] = photo
                elif self.board[i][j] == "g":
                    photo = "Smallg.png"
                    self.board_[i][j] = photo
                elif self.board[i][j] == "c":
                    photo = "Smallc.png"
                    self.board_[i][j] = photo
                    
                    
        self.button_1.setIcon(QIcon(self.board_[0][0]))
        self.button_1.setIconSize(QtCore.QSize(55,55))

        self.button_2.setIcon(QIcon(self.board_[0][1]))
        self.button_2.setIconSize(QtCore.QSize(55,55))

        self.button_3.setIcon(QIcon(self.board_[0][2]))
        self.button_3.setIconSize(QtCore.QSize(55,55))

        self.button_4.setIcon(QIcon(self.board_[0][3]))
        self.button_4.setIconSize(QtCore.QSize(55,55))

        self.button_5.setIcon(QIcon(self.board_[0][4]))
        self.button_5.setIconSize(QtCore.QSize(55,55))

        self.button_6.setIcon(QIcon(self.board_[0][5]))
        self.button_6.setIconSize(QtCore.QSize(55,55))

        self.button_7.setIcon(QIcon(self.board_[1][0]))
        self.button_7.setIconSize(QtCore.QSize(55,55))
        
        self.button_8.setIcon(QIcon(self.board_[1][1]))
        self.button_8.setIconSize(QtCore.QSize(55,55))
        
        self.button_9.setIcon(QIcon(self.board_[1][2]))
        self.button_9.setIconSize(QtCore.QSize(55,55))

        self.button_10.setIcon(QIcon(self.board_[1][3]))
        self.button_10.setIconSize(QtCore.QSize(55,55))
        
        self.button_11.setIcon(QIcon(self.board_[1][4]))
        self.button_11.setIconSize(QtCore.QSize(55,55))
        
        self.button_12.setIcon(QIcon(self.board_[1][5]))
        self.button_12.setIconSize(QtCore.QSize(55,55))
        
        self.button_13.setIcon(QIcon(self.board_[2][0]))
        self.button_13.setIconSize(QtCore.QSize(55,55))
     
        self.button_14.setIcon(QIcon(self.board_[2][1]))
        self.button_14.setIconSize(QtCore.QSize(55,55))
  
        self.button_15.setIcon(QIcon(self.board_[2][2]))
        self.button_15.setIconSize(QtCore.QSize(55,55))
     
        self.button_16.setIcon(QIcon(self.board_[2][3]))
        self.button_16.setIconSize(QtCore.QSize(55,55))
        
        self.button_17.setIcon(QIcon(self.board_[2][4]))
        self.button_17.setIconSize(QtCore.QSize(55,55))
        
        self.button_18.setIcon(QIcon(self.board_[2][5]))
        self.button_18.setIconSize(QtCore.QSize(55,55))
        
        self.button_19.setIcon(QIcon(self.board_[3][0]))
        self.button_19.setIconSize(QtCore.QSize(55,55))
        
        self.button_20.setIcon(QIcon(self.board_[3][1]))
        self.button_20.setIconSize(QtCore.QSize(55,55))
        
        self.button_21.setIcon(QIcon(self.board_[3][2]))
        self.button_21.setIconSize(QtCore.QSize(55,55))
        
        self.button_22.setIcon(QIcon(self.board_[3][3]))
        self.button_22.setIconSize(QtCore.QSize(55,55))
        
        self.button_23.setIcon(QIcon(self.board_[3][4]))
        self.button_23.setIconSize(QtCore.QSize(55,55))
        
        self.button_24.setIcon(QIcon(self.board_[3][5]))
        self.button_24.setIconSize(QtCore.QSize(55,55))
        
        self.button_25.setIcon(QIcon(self.board_[4][0]))
        self.button_25.setIconSize(QtCore.QSize(55,55))
        
        self.button_26.setIcon(QIcon(self.board_[4][1]))
        self.button_26.setIconSize(QtCore.QSize(55,55))
        
        self.button_27.setIcon(QIcon(self.board_[4][2]))
        self.button_27.setIconSize(QtCore.QSize(55,55))
        
        self.button_28.setIcon(QIcon(self.board_[4][3]))
        self.button_28.setIconSize(QtCore.QSize(55,55))
    
        self.button_29.setIcon( QIcon(self.board_[4][4]))
        self.button_29.setIconSize(QtCore.QSize(55,55))
        
        self.button_30.setIcon(QIcon(self.board_[4][5]))
        self.button_30.setIconSize(QtCore.QSize(55,55))
        
        self.button_31.setIcon(QIcon(self.board_[5][0]))
        self.button_31.setIconSize(QtCore.QSize(55,55))
        
        self.button_32.setIcon(QIcon(self.board_[5][1]))
        self.button_32.setIconSize(QtCore.QSize(55,55))
        
        self.button_33.setIcon(QIcon(self.board_[5][2]))
        self.button_33.setIconSize(QtCore.QSize(55,55))
     
        self.button_34.setIcon(QIcon(self.board_[5][3]))
        self.button_34.setIconSize(QtCore.QSize(55,55))
    
        self.button_35.setIcon(QIcon(self.board_[5][4]))
        self.button_35.setIconSize(QtCore.QSize(55,55))

        self.button_36.setIcon(QIcon(self.board_[5][5]))   
        self.button_36.setIconSize(QtCore.QSize(55,55))        
        

    # A function that is called to connect to the server the window when the connect button is clicked    
    def connect_button(self):
        self.address = self.edit_server.displayText()           # gets the IP address on the line edit 
        self.game_thread.connect(self.address)                # connects to the server          
        self.game_thread.start()                            # initiates the run method      
        
        
    # A function that is called to close the window when the close button is clicked         
    def close_button(self):
        sys.exit()
        
    def Shot(self):
        QSound("explosion.wmp").play()
                
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()    
    sys.exit(app.exec_())

main()