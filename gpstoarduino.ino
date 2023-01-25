	//To receive data from NEO-7M Gps module and send received GPS co-ordinate to ESP8266-01 using serial communication.
	#include<TinyGPS++.h>  //include tiny GPS library
	#include <SoftwareSerial.h> // to define additional serial port
	#include <String.h> //to perform string operations
	static const int RXPin=3, TXPin=4; // rxPin: the pin on which to receive serial data. txPin: the pin on which to transmit serial data.
	static const uint32_t GPSBaud= 9600;
	String data="";
	TinyGPSPlus gps; //Create TinyGPS++ object
	SoftwareSerial ssgps(RXPin,TXPin); // Serial connection to the GPS device

	void setup() {
	  
	  Serial.begin(115200);  // match with baud rate of ESP8266-01
	  ssgps.begin(GPSBaud);

	}

	void loop() {
	  // This sketch displays and sends innformation every time a new sentence is correctly encoded.
	   while (ssgps.available() > 0){
		gps.encode(ssgps.read());
		if (gps.location.isUpdated()){
		  // Latitude in degrees (double)
		//  Serial.print("Latitude= "); 
		 // Serial.print(gps.location.lat(), 6);
		 data=data+"<";
		  data=data+String(gps.location.lat(),6);
		  data=data+",";      
		  // Longitude in degrees (double)
		 // Serial.print(" Longitude= "); 
		 // Serial.println(gps.location.lng(), 6); 
		  data=data+String(gps.location.lng(),6);
		  data=data+",";
		 // Serial.println("Time in HHMMSS");
		  //Serial.println(gps.time.value());
		  data=data+String(gps.time.value());
		  data=data+">";
		  Serial.println(data);
		  delay(2000);
		}
	}
	}
