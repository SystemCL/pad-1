=================== Message broker model in Python =============================
================================================================================
			 powered by Tabirta Adrian 
================================================================================
Instalation: 

For this project you need to install:
 - Python version greater than 3.0 
 - Nano or another text editor if you use UNIX destribution without 
   graphical interface. 

Running project

This project have 3 separated components:

* Client - runs on localhost (127.0.0.1) and sends text messages to the broker  

* Broker - runs on 0.0.0.0 on port 5000. Listening for messages from everybody
	   Display message on the screen and then convert in UPERCASE and
	   send to the recievers.

* Reciever - listening messages from Broker and display on the screen

To run one file(s) you should: 

1. Open console if you use Linux

2. Go to files directory

3. Type in in comand line: YOUR_NAME@Linux_machine:# python client.py

4. Voila :), program start runing

Note: 
	Program files should be run from separated terminal and simultaneously
to see logs on each separated terminal.

	For this propose I had used UDP as trasnfer protocol so there is no garantee 
thad all the messages will arrive.

Good luck :)

________________________________________________________________________

        [Client] ----> |------- |
        [Client] ----> | Broker | ---> [Reciever]
        [Client] ----> |________| ---> [Reciever]
_________________________________________________________________________

 


