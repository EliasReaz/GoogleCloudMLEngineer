import tensorflow as tf

import pathlib

parent_dir = pathlib.Path().resolve().parent
cur_dir = parent_dir / "Course2" / "Module2_design_build_input_datapipeline"

# Make an in-memory dataset
X = [1, 2, 3, 4, 5]
Y = [10, 25, 40, 55, 70]

# Create a TensorFlow Dataset from the in-memory data
dataset = tf.data.Dataset.from_tensor_slices((X, Y))

# Repeat for multiple epochs and batches
# repeat(3 )cycles through the dataset 3 times (like 3 epochs).
# batch(2) creates batches of size 2.
dataset = dataset.repeat(3).batch(2)

# Iterate through the dataset and print the batches
for batch in dataset:
    print(batch)
# Output will show batches of (X, Y) pairs

