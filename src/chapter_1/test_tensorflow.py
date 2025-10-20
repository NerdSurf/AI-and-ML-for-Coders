# test_tensorflow.py
# ------------------
# This short script checks if TensorFlow is installed correctly.
# It also suppresses unnecessary info messages (like oneDNN optimizations)
# so your output is clean and easy to read.

import os

# Suppress TensorFlow info and optimization messages
# TF_CPP_MIN_LOG_LEVEL:
#   0 = all logs (default)
#   1 = filter out INFO logs
#   2 = filter out INFO and WARNING logs
#   3 = only show ERROR logs
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# Optionally disable oneDNN optimizations to remove extra startup messages.
# This won't affect normal functionality.
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import tensorflow as tf

# Print TensorFlow version
print("TensorFlow version:", tf.__version__)

# Check if TensorFlow can access a GPU
gpu_devices = tf.config.list_physical_devices('GPU')
if gpu_devices:
    print("GPU detected:", gpu_devices)
else:
    print("No GPU detected, running on CPU.")

# Simple test: create and run a constant tensor
hello = tf.constant("Hello, TensorFlow!")
print(hello.numpy().decode("utf-8"))
