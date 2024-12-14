# Network Anomaly Detection with Real-Time Dashboard

This project is a real-time **Network Anomaly Detection System** that captures live network traffic, processes it to detect anomalies using machine learning, and visualizes the results on a dynamic web dashboard. 

---

## Features
- **Real-Time Packet Capture**: Uses Scapy to sniff live network traffic.
- **Anomaly Detection**: Employs Isolation Forest for detecting anomalous network activity.
- **Interactive Dashboard**: Visualizes normal and anomalous traffic using Flask and Chart.js.
- **Extensible Design**: Easily extendable for custom anomaly detection models or additional network features.

---

## How It Works
1. **Packet Capture**:
   - Scapy captures live packets and extracts features like source IP, destination IP, protocol, and packet length.

2. **Preprocessing**:
   - Captured packet data is converted into a DataFrame.
   - Data is normalized to prepare it for machine learning models.

3. **Anomaly Detection**:
   - An Isolation Forest model classifies traffic as normal or anomalous.

4. **Visualization**:
   - Detected anomalies and normal traffic are sent to the dashboard using Flask-SocketIO.
   - Traffic is visualized using a scatter plot on a browser-based dashboard.

---

## Technologies Used
- **Python**: Core language for backend development.
- **Scapy**: For live packet sniffing.
- **Pandas**: For data preprocessing and normalization.
- **Scikit-learn**: Machine learning for anomaly detection.
- **Flask**: Backend server for the web application.
- **Flask-SocketIO**: Real-time communication between the server and dashboard.
- **Chart.js**: Visualization library for the dashboard.

---

## Requirements
- Python 3.8+
- Pip installed (or pip3)
- Administrator privileges (required for packet sniffing)

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/network-anomaly-detection.git
   cd network-anomaly-detection
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application with administrator privileges:
   ```bash
   sudo python main.py  # Use admin privileges for packet sniffing
   ```

4. Open the web browser and visit:
   ```
   http://localhost:5000
   ```

---

## File Structure
```
network-anomaly-detection/
│
├── live_capture.py        # Captures live network packets
├── preprocess.py          # Preprocesses packet data
├── anomaly_detection.py   # Machine learning-based anomaly detection
├── dashboard.py           # Flask app for real-time visualization
├── main.py                # Main entry point for the project
├── templates/
│   └── dashboard.html     # Front-end web interface
└── README.md              # Project documentation
```

---

## Usage
- Start the application:
  ```bash
  python main.py
  ```
- Visit `http://localhost:5000` in your browser.
- View live network traffic updates on the dashboard.

---

## Example Output
The dashboard displays:
- **Normal Traffic**: Shown in blue on the scatter plot.
- **Anomalous Traffic**: Highlighted in red for easy identification.

---

## Acknowledgments
This project was created with the assistance of **ChatGPT**, an AI assistant by OpenAI. Many thanks for its guidance in setting up the project structure, debugging, and ensuring functionality.

---

## Future Improvements
- Add support for additional features like DNS analysis and port scanning.
- Enhance anomaly detection with custom models or advanced algorithms.
- Implement a logging system to store historical anomaly data for analysis.

---

## License
This project is open-source and available under the MIT License.

---

Feel free to adapt or update this `README.md` file based on your preferences or additional project requirements!
