# Wireless Body Area Sensor Network Based Human Activity Recognition System

## 📝 Project Description
This project aims to design and implement a **Wireless Body Area Sensor Network (WBASN)** for monitoring physiological and motion-related signals from the human body. The collected data is used to recognize and classify different human activities using sensor fusion. 

The system integrates multiple biomedical and motion sensors connected to a microcontroller, which transmits data to a processing unit for real-time analysis and activity recognition.

---

## 🛠️ Hardware Stack
### Sensors Integrated:
*   **MPU-9250:** 9-axis motion sensor (Accelerometer, Gyroscope, Magnetometer).
*   **MAX-30102:** Pulse oximeter for Heart Rate and SpO₂ monitoring.
*   **MLX-90614:** Contactless Infrared temperature sensor.
*   **AD8232:** ECG sensor module for heart electrical activity monitoring.

### Processing Units:
*   **Arduino Uno:** Primary interface for sensor data acquisition and testing.
*   **Raspberry Pi:** Planned for data aggregation, storage, and advanced processing.

---

## 📈 Work Completed So Far
- [x] Configured **Arduino IDE** development environment.
- [x] Installed and tested required libraries for all sensors.
- [x] Verified successful compilation and execution of example programs for MPU9250, MAX30102, and MLX90614.
- [x] Prepared the software environment for multi-sensor integration.

---

## 🚀 Planned Workflow
1.  **Individual Testing:** Verify each sensor independently with the Arduino Uno.
2.  **Data Integration:** Combine code to collect simultaneous readings via I2C.
3.  **Data Transmission:** Transfer live sensor data to Raspberry Pi.
4.  **Dataset Creation:** Log signals for various human activities (walking, sitting, etc.).
5.  **ML Implementation:** Apply Machine Learning models for automated activity recognition.

---

## 🚦 Current Status
**Software Setup:** 🟢 Completed  
**Hardware Testing:** 🟡 In Progress (Initial testing with available components).

---
*Created by [somoshree04](https://github.com)*



