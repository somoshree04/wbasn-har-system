#include <Wire.h>
#include <MPU9250.h>
#include "MAX30105.h"
#include <Adafruit_MLX90614.h> // New Library

#define MPU9250_ADDRESS MPU9250_ADDRESS_AD0
MPU9250 myIMU;
MAX30105 particleSensor;
Adafruit_MLX90614 mlx = Adafruit_MLX90614(); // Temperature Object

void setup() {
  Wire.begin();
  Serial.begin(115200);

  // Init MPU-9250
  byte c = myIMU.readByte(MPU9250_ADDRESS, WHO_AM_I_MPU9250);
  if (c == 0x71 || c == 0x70) {
    myIMU.initMPU9250();
    myIMU.Ascale = MPU9250::AFS_8G;
  }

  // Init MAX30102
  particleSensor.begin(Wire, I2C_SPEED_FAST);
  particleSensor.setup();

  // Init MLX90614
  if (!mlx.begin()) {
    Serial.println("Error connecting to MLX90614");
  }
}

void loop() {
  // Read Accel
  myIMU.readAccelData(myIMU.accelCount);
  myIMU.getAres();
float ax = (float)myIMU.accelCount[0] * myIMU.aRes;

  // Read Pulse IR
  long irValue = particleSensor.getIR();

  // Read Temperature (Object temp is what it "sees")
  float tempC = mlx.readObjectTempC();

  // Format for Python: Accel,IR,Temp
  Serial.print(ax, 2);
  Serial.print(",");
  Serial.print(irValue);
  Serial.print(",");
  Serial.println(tempC, 2);

  delay(100);
}
