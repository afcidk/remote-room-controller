#include <LWiFi.h>
#include <WiFiClient.h>
#define TCP_IP "10.0.0.1"
#define TCP_PORT 5000
#define WIFI_SSID "wifibb"
#define WIFI_PASS "0910943024"
#define PINA 6
#define PINB 7
#define FULLA 8
#define FULLB 9
WiFiClient client;
int WIFI_STATUS;

void decision(char ch[]) {
  if (strcmp(buf, "light") == 0) turn();
}

void pinSetup() {
  pinMode(PINA, OUTPUT); pinMode(PINB, OUTPUT); pinMode(FULLA, OUTPUT); pinMode(FULLB, OUTPUT);
  digitalWrite(FULLA, HIGH); digitalWrite(FULLB, HIGH);
  digitalWrite(PINA, LOW); digitalWrite(PINB, LOW);
}

void turn() {
  digitalWrite(PINA, HIGH); digitalWrite(PINB, LOW);
  delay(1000);
  digitalWrite(PINA, LOW); digitalWrite(PINB, LOW);
}

void setup() {
  
  pinSetup();
  Serial.begin(9600);
  Serial.print("SSID: ");
  Serial.println(WIFI_SSID);

  WIFI_STATUS = WL_IDLE_STATUS;
  
  do {
    Serial.println("attempting to connect to WiFi");
    WIFI_STATUS = WiFi.begin(WIFI_SSID, WIFI_PASS);
    Serial.println(WIFI_STATUS);
  } while (WIFI_STATUS != WL_CONNECTED);

  Serial.println("Connected");
  while (!client.connect(TCP_IP, TCP_PORT)) {
    delay(300);
  }
  Serial.print("Connected to ");
  Serial.print(TCP_IP);
  Serial.print(":");
  Serial.println(TCP_PORT);

}

void loop() {

 while (WIFI_STATUS != WL_CONNECTED) {
  Serial.println("attempting to connect to WiFi");
  WIFI_STATUS = WiFi.begin(WIFI_SSID, WIFI_PASS);
  Serial.println(WIFI_STATUS);
 }

 while (!client.connected()) {
  client.connect(TCP_IP, TCP_PORT);
  delay(300);
  Serial.println("trying to connect again");
 }

 int mesLen;
 if ((mesLen = client.available()) > 0) {
  char buf[64];
  int i = 0;
  do {
    buf[i++] = client.read();
  } while (i<64 && buf[i-1]!='\n');

  buf[i-1] = '\0';
  Serial.println(strlen(buf));
  Serial.println(buf);

  decision(buf);
 }
}
