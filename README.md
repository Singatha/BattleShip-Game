# BattleShip Game

- Download the zip file or clone the repo
- Download python if you don't have it on your machine and set it up on your terminal.
  - (https://www.python.org/)
- Install PyQt5 for python GUI using the terminal
  - **_pip install pyqt5_**
- Running the code on the one machine
  - open three terminals
    - run the BattleShipGameServer.py on one to run the server
      - **_python BattleShipGameServer.py_**
    - on the remaining two run GameDemo.py and then enter **localhost** on both to connect
      - **_python GameDemo.py_**
- Running the code on two machines
  - ping the IP address of the other machine
  - decide which machine will run the server with the command:
    - **_python BattleShipGameServer.py_**
  - run GameDemo.py on both machines
    - **_python GameDemo.py_**
  - and then one machine that is running the server will connect to **localhost** and the with the ip address of the machine running the server.
