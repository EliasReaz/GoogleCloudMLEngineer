import tensorflow as tf

def parse_row(row):
    cols = tf.io.decode_csv(row, record_defaults=[[0], ['house'], [0]])
    features = {'sq_footage': cols[0], 'type': cols[1]}
    label = cols[2]
    return features, label

def create_dataset(csv_file_path):
    dataset = tf.data.TextLineDataset(csv_file_path)
    dataset = dataset.map(parse_row)
    dataset = dataset.shuffle(1000).repeat(15).batch(128)
    return dataset

# Usage
dataset = create_dataset("train.csv")
for features, label in dataset.take(1):
    print(features, label)