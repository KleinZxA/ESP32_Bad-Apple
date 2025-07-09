#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "oled_frames.h"

//Screen Width and size
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64 

//I2C declaration
//If using I2C Comment these 2
#define OLED_SDA 14
#define OLED_SCL 12
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

//SPI declaration
//If Using SPI version Uncomment below
//#include <SPI.h>
//#define OLED_MOSI   9
//#define OLED_CLK   10
//#define OLED_DC    11
//#define OLED_CS    12
//#define OLED_RESET 13
//Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT,OLED_MOSI, OLED_CLK, OLED_DC, OLED_RESET, OLED_CS);


void setup() {
  Wire.begin(OLED_SDA, OLED_SCL);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  display.display();
}

void loop() {
  for (int i = 0; i < FRAME_COUNT; i++) {
    display.clearDisplay();
    display.drawBitmap(0, 0, frames[i], 128, 64, SSD1306_WHITE);
    display.display();
    delay(73); //Adjust to your specifications (Adjusts Framerate, Although oled_frames.h is 10fps)
  }
}
