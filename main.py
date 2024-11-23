import os
from app.capture import capture_packets
from app.preprocess import preprocess_data
from app.anomaly_detection import detect_anomalies
from app.visualize import visualize_data

DATA_RAW = 'data/network_data.csv'
DATA_PROCESSED = 'data/processed_data.csv'

if not os.path.exists('data'):
    os.makedirs('data')

# Step 1: Capture packets
capture_packets(DATA_RAW)

# Step 2: Preprocess data
preprocess_data(DATA_RAW, DATA_PROCESSED)

# Step 3: Detect anomalies
detect_anomalies(DATA_PROCESSED, DATA_PROCESSED)

# Step 4: Visualize results
visualize_data(DATA_PROCESSED)
