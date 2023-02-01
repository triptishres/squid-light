#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <String.h>
const char* ssid = "OnePlus";
const char* password = "RANJAN2020";
const byte numChars=64;
char receivedChars[numChars];
boolean newData=false;

ESP8266WebServer server(80);

void setup() {1
  pinMode(LED_PIN,OUTPUT);
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }
  Serial.print("\n IP address: ");
  Serial.println(WiFi.localIP());
  digital.Write(LED_PIN,HIGH);
  delay(1000);
  digital.Write(LED_PIN,LOW)
  delay(1000);
  server.on("/", handleRoot);
  //server.on("/data", handleData);
  server.on("/data1", handleData1);
  server.begin();
}

void loop() {
  
  server.handleClient();
  recvWithStartEndMarkers();
  showNewData();
}

void handleRoot() {
  // Send the web page to the client
  server.send(200, "text/html", "<html><body><h1>Sensor Data</h1><p>Note: <span id='data1'></span></p><script>setInterval(() => {fetch('/data1').then(response => response.text()).then(data1 => {document.getElementById('data1').innerHTML = data1;});},2000 );</script></body></html>");
}

/* void handleData() {
  int sensorValue = analogRead(A0);
  String data = String(sensorValue);
 // String data1="This is Testing data send to server";
  server.send(200, "text/plain", data);
  //server.send(200, "text/plain", data1);
}*/
void handleData1() {
  //int sensorValue = analogRead(A0);
 // String data= String(sensorValue);
  String data1=receivedChars;
  //server.send(200, "text/plain", data);
  server.send(200, "text/plain", data1);
}
void recvWithStartEndMarkers(){
  static boolean recvInProgress=false;
  static byte ndx=0;
  char startMarker='<';
  char endMarker='>';
  char rc;
  while(Serial.available()>0 && newData==false){
    rc=Serial.read();
    if(recvInProgress==true){
      if(rc!=endMarker){
        receivedChars[ndx]=rc;
        ndx++;
        if(ndx>=numChars){
          ndx=numChars-1;
        }
      }
      else{
        receivedChars[ndx]='\0';//terminate the string
        recvInProgress=false;
        ndx=0;
        newData=true;
        
      }
    }
    else if(rc==startMarker){
      recvInProgress=true;
    }
  }
  
}
void showNewData(){
  if(newData==true){
    Serial.print("This just in ...");
    Serial.println(receivedChars);
    newData=false;
  }
}

