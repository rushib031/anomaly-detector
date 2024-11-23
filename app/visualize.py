import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(file):
    df = pd.read_csv(file)
    normal = df[df['anomaly'] == 'Normal']
    anomaly = df[df['anomaly'] == 'Anomaly']

    plt.scatter(normal['src_ip'], normal['dst_ip'], c='blue', label='Normal')
    plt.scatter(anomaly['src_ip'], anomaly['dst_ip'], c='red', label='Anomaly')
    plt.legend()
    plt.xlabel('Source IP')
    plt.ylabel('Destination IP')
    plt.title('Network Traffic Anomalies')
    plt.show()

if __name__ == '__main__':
    visualize_data('data/processed_data.csv')
