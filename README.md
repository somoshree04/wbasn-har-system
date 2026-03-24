# Wireless Body Area Sensor Network (WBASN) 
## Human Activity Recognition & Physiological Monitoring System

### 📝 Project Overview
This project focuses on the design and implementation of a **Wireless Body Area Sensor Network (WBASN)** for the continuous monitoring of physiological and motion-related signals. By leveraging sensor fusion, the system recognizes and classifies human activities in real-time.

The architecture follows a robust **Edge-to-Hub** data pipeline:
* **Edge Node:** Raspberry Pi Pico W / Arduino Nano for real-time data acquisition from body-worn sensors.
* **Central Hub:** Raspberry Pi 4 Model B acting as a dedicated gateway running a **Node.js** server and **MongoDB** for data aggregation, storage, and visualization.

---

### 🛠️ Hardware Stack

#### **Biomedical & Motion Sensors**
* **MPU-9250:** 9-Axis IMU (Accelerometer, Gyroscope, Magnetometer) for gait and motion analysis.
* **MAX-30102:** High-sensitivity Pulse Oximeter for Heart Rate and $SpO_2$ monitoring.
* **MLX-90614:** Contactless Infrared sensor for continuous body temperature tracking.
* **AD8232:** Single-lead heart rate monitor for ECG signal acquisition.

#### **Processing & Connectivity**
* **Microcontrollers:** Raspberry Pi Pico W (Dual-core ARM Cortex M0+) & Arduino Nano.
* **Microcomputer:** Raspberry Pi 4 Model B (Data Logger & Analytics Server).
* **Communication:** I2C Protocol for sensor bus; Wi-Fi (HTTP/WebSockets) for wireless transmission to the hub.

---

### 📈 Development Progress

- [x] **Environment Setup:** Configured Arduino IDE and MicroPython (Thonny) development environments.
- [x] **Library Validation:** Successfully installed and verified drivers for MPU9250, MAX30102, and MLX90614.
- [x] **Component Testing:** Validated individual sensor logic and data output on Arduino Nano.
- [ ] **Multi-Sensor Fusion:** Consolidating I2C data streams into a unified packet structure for transmission.
- [ ] **Wireless Pipeline:** Establishing Wi-Fi data streaming from Pico W to the Pi 4 Local Server.

---

### 🚀 Research & ML Workflow

1.  **Data Acquisition:** Simultaneous sampling of ECG, $SpO_2$, and 9-axis motion data at calibrated intervals.
2.  **Edge Transmission:** Wireless streaming of raw data packets to a **Node.js/MongoDB** backend.
3.  **Dataset Preparation:** Logging and labeling data for various activities (e.g., Walking, Sitting, Climbing).
4.  **Signal Processing:** Feature extraction, filtering, and noise reduction of raw physiological signals.
5.  **ML Implementation:** Classification using **Random Forest** and **Bi-directional LSTM (BiLSTM)** architectures for automated activity recognition.

---

### 🚦 Project Status
* **Software Layer:** 🟢 Stable
* **Hardware Integration:** 🟡 In Progress (Transitioning to Pico W Edge Node)
* **Data Analysis:** ⚪ Pending

---

**Maintainer:** [somoshree04](https://github.com/somoshree04)  
**Affiliation:** RCC Institute of Information Technology  
**Event:** Prepared for UEMGREEN 2026 Conference




