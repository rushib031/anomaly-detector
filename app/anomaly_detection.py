import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(input_file, output_file):
    df = pd.read_csv(input_file)
    model = IsolationForest(contamination=0.1)
    df['anomaly'] = model.fit_predict(df[['src_ip', 'dst_ip', 'protocol', 'length']])
    df['anomaly'] = df['anomaly'].apply(lambda x: 'Anomaly' if x == -1 else 'Normal')
    df.to_csv(output_file, index=False)

if __name__ == '__main__':
    detect_anomalies('data/processed_data.csv', 'data/processed_data.csv')
