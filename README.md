  GNU nano 2.5.3              File: README.md                         Modified  

=================== Message broker model in Python ======================
===================     by Tabirta Adrian          ======================
=========================================================================

        [Client] ----> |------- |
        [Client] ----> | Broker | ---> [Reciever]
        [Client] ----> |________|

_________________________________________________________________________

                        SCENARIO

1. Many clients send messages to broker using IP address and port
        [Client] --->  [Hello world] ---> [Broker]

2. Broker recieve message, display it and send forward to recievers.
        [Broker] ---> [Print "Hello world"]
        [Broker] ---> [Hello world] ---> [Reciever]

3. Reciever listening to Broker and display messages emited by him.
   Also, Reciever should notify Broker when message arrive.
        [Reciever] ---> [Print "Hello world"]

For this exemple  I used UDP protocol to send packets between network nodes.



