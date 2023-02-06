# Introduction

**SQUIDLIGHT** is a device that collects vehicle's live GPS data and communicates with local traffic light systems in each intersection to manage traffic.

# System Architecture 
**SQUIDLIGHT** is connected through serial communication and consists of:
* Arduino Uno Microcontroller 
* NEO-7M GPS Module
* ESP 8266-01 WIFI Module

![System_Architecture](https://user-images.githubusercontent.com/65053335/216851263-bc5d315c-0291-4ccc-b95c-844d03c7969f.png)

When the vehicle approaches the traffic light, it will connect to the WIFI network situated in the traffic light. After that, the GPS signal received by the GPS module fitted in the vehicle transmits the signal to the server via connected traffic light at a time interval of 20 seconds. The received GPS coordinate data is then processed in the server to calculate the vehicle's position. If the car is stationary for more than the predetermined time, the server detects higher vehicle density in that flow direction. It gives priority to the traffic light connected in that direction.

# System Design 

The coding for backend was done in C+ and the frontend was done in the Python language.