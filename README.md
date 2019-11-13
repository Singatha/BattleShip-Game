# BattleShip Game

Download the zip file or clone the repo
Install python on the command if you don't have it on your machine.
pip install python
Install PyQt5 for python graphical interfaces
Running the code on the one machine
open three terminals
run the BattleShipGameServer.py on one to run the server
> python BattleShipGameServer.py
on the remaining two run GameDemo.py and then enter localhost on both to connect
> python GameDemo.py
Running the code on two machines
ping the IP address of the other machine
decide which machine will run the server with the command:
> python BattleShipGameServer.py
run GameDemo.py on both machines
> python GameDemo.py
and then one machine that is running the server will connect to localhost and the with the ip address of the machine running the server.
