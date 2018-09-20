#include <LWiFi.h>
#include <LWiFi.h>
#define TCP_IP "10.0.0.1"
#define TCP_PORT 5000
#define WIFI_SSID "wifibb"
#define WIFI_PASS "0910943024"
WiFiClient client;


void setup() {
  Serial.begin(9600);
  Serial.print("SSID: ");
  Serial.println(WIFI_SSID);

  int status = WL_IDLE_STATUS;
  
  do {
    Serial.println("attempting to connect to WiFi");
    status = WiFi.begin(WIFI_SSID, WIFI_PASS);
    Serial.println(status);
  } while (status != WL_CONNECTED);

  Serial.println("Connected");
  while (!client.connect(TCP_IP, TCP_PORT)) {
    delay(300);
    Serial.println("trying to connect again");
  }
  Serial.println("Connected to "+TCP_IP+":"+TCP_PORT);

}

void loop() {
 int mesLen;
 if ((mesLen = client.available()) > 0) {
  char buf[64];
  int i = 0;
  do {
    buf[i++] = client.read();
  } while (i<64 && buf[i-1]!='\r' && buf[i-1]!='\n');

  buf[i-1] = '\0';
  Serial.println(strlen(buf));
  Serial.println(buf);

   
 }
}
