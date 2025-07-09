#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "oled_frames.h"  // your generated file

#define OLED_SDA 14
#define OLED_SCL 12

Adafruit_SSD1306 display(128, 64, &Wire, -1);

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
    delay(73); //
  }
}
