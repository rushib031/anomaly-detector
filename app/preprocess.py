import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(input_file, output_file):
    df = pd.read_csv(input_file, names=["src_ip", "dst_ip", "protocol", "length"])
    df['src_ip'] = df['src_ip'].astype('category').cat.codes
    df['dst_ip'] = df['dst_ip'].astype('category').cat.codes

    scaler = MinMaxScaler()
    df[['src_ip', 'dst_ip', 'protocol', 'length']] = scaler.fit_transform(df[['src_ip', 'dst_ip', 'protocol', 'length']])

    df.to_csv(output_file, index=False)

if __name__ == '__main__':
    preprocess_data('data/network_data.csv', 'data/processed_data.csv')
