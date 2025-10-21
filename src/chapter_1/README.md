# Chapter 1: Introduction to Tensorflow

## Traditional Programming vs. Machine Learning

I’ve tinkered with TensorFlow and a few other ML tools before, but this project is all about learning the 
bigger picture. These are my notes and examples along the way — hopefully they’ll make it easier for anyone 
new to Python to follow along and pick up the core ideas.

### What is Traditional Programming?
Traditional Programming has limitations in which you utilize rules and data to return answers - this could be 
demonstrated with a basic if, else statement, in which you return a specific value. 

### Streetlamp Example
For example, you might want to have a game that needs to determine how bright the environment is 
in order to turn on streetlamps. This could be shown as something like this:

```python
streetlamp: bool = False
light: float = 1.50

if light > 1.00:
    streetlamp = False
elif light < 1.00:
    streetlamp = True
```

### The Limits of Rule-Based Logic
Traditional programming relies on rules you define to generate answers. Machine learning flips that logic — 
you give it the data and examples of the answers, and it figures out the rules for itself using pattern 
recognition and other algorithms.

With our example above, we used a single threshold to decide whether the streetlamp should turn on — a simple 
case of data + rules = results.

Now imagine we want something smarter: the light should turn on when it’s dark or when a person passes by — 
maybe walking, biking, or skateboarding — but not when a car drives past. This adds a lot more complexity 
than our simple if statement can handle.

To make that work, we’d need to track several things at once — brightness, object size, movement speed, 
distance from the lamp, and so on. Writing manual rules for all of that would quickly become messy and 
hard to maintain.

### Where Machine Learning Fits In
This is where machine learning comes in.
Instead of programming every condition by hand, we can feed the system lots of examples — labeled 
data showing what’s “day,” “night,” “person,” “bike,” “car,” and so on — and let the model learn the 
patterns on its own. 

With enough data, the computer can start recognizing the right situations to turn the lamp on 
or off, even when it encounters new scenarios it’s never seen before.

In order to utilize this technology, we need to use a library known as **TensorFlow**, a machine learning
library that allows you to create your own models.

---
## How To: Installing TensorFlow
Below is a simple, step-by-step guide to installing TensorFlow on Windows, macOS, and Linux — using either 
**PyCharm** or **VS Code** as your development environment.

Before you start, make sure you have **Python 3.8** or newer installed.
You can check your Python version by running:
```css
python --version
```

If you get an error or see a version older than 3.8, visit 
[https://www.python.org/downloads](https://www.python.org/downloads/) to install or update Python.

### Installing Tensorflow on Windows (PyCharm)
1. **Open PyCharm** and create a new project. When prompted, select **new virtual environment (venv)** using
your installed Python interpreter.
2. **Open** the **Terminal** inside PyCharm (bottom-left of the window)
3. **Install TensorFlow** by running:
```bash
pip install tensorflow
```
4. Wait for the installation to finish. You'll see several dependencies being downloaded and installed.
5. **Verify the installation:**  
Open a new Python file and run:
```python
import tensorflow as tf
print(tf.__version__)
```
If it prints a version number without errors. TensorFlow is ready to go.

### Installing Tensorflow on macOS
1. Open **Terminal** or the integrated terminal inside **VS Code** or **PyCharm**
2. (Optional but recommended) Create a virtual environment to keep dependencies clean:
```bash
python3 -m venv tf-venv
source tf-env/bin/activate
```
3. **Install TensorFlow**:
```nginx
pip install tensorflow
```
4. Verify the installation:
```python
import tensorflow as tf
print(tf.__version__)
```
If you're using an Apple Silicon (M1/M2/M3) Mac, you can install a version optimized for your hardware:
```nginx
pip install tensorflow-metal
```

### Installing Tensorflow on Linux
1. Open your **terminal**.
2. Make sure Python and pip are installed:
```css
python3 --version
pip3 --version
```
3. Create a virtual environment (recommended):
```bash
python3 -m venv tf-venv
source tf-env/bin/activate
```
4. Install TensorFlow:
```nginx
pip install tensorflow
```
5. Verify it's working:
```python
import tensorflow as tf
print(tf.__version__)
```
---
### Testing Your Installation
Once you've installed TensorFlow. It's always a good idea to make sure everything is working properly.
You can do this by running a short test script in either a new python file, or directly from your IDE's
terminal (VS Code or PyCharm).

I would recommend creating a new file called **test_tensorflow.py** and paste in the following code:
```python
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
```
---
### Using Your GPU with TensorFlow (Optional)

TensorFlow runs perfectly fine on your CPU, which is all you need for learning and small projects.
However, if you have a dedicated GPU (graphics card), you can use it to dramatically speed 
up training on larger models.

This section is optional — you don’t need to do this unless you want to experiment with GPU 
acceleration.

### Step 1: Check if TensorFlow Detects a GPU
```python
import tensorflow as tf
print("TensorFlow version:", tf.__version__)
print("GPUs available:", tf.config.list_physical_devices('GPU'))
```

If TensorFlow lists one or more GPUs, you're all set.  
If it shows an empty list ```([])``` don't worry - it just means TensorFlow is running on your CPU,
which is completely fine for now.

### Step 2: How to Enable GPU Support (Optional)
The process depends on your operating system and GPU type.
Below are the simplest modern setups for each platform.

#### Windows (via WSL2)

TensorFlow no longer provides native GPU support for Windows, but you can use it inside **WSL2 
(Windows Subsystem for Linux)**.

If that sounds complicated — skip it! You can still follow this entire project on CPU.

If you *do* want to try GPU mode on Windows:
1. Install **WSL2** and choose Ubuntu from the Microsoft Store.
2. Make sure your **NVIDIA GPU drivers** are up to date and WSL-compatible.
3. Inside your Ubuntu terminal. create a virtual environment and install TensorFlow with CUDA support:
```bash
python3 -m venv tf-venv
source tf-env/bin/activate
pip install --upgrade pip
pip install "tensorflow[and-cuda]"
```
4. Run your test again:
```bash
python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

If you see something like ```[PhysicalDevice(name='/physical_device:GPU:0', ...)]```,
congratulations - TensorFlow is using your GPU

#### macOS (Apple Silicon: M1, M2, M3)

Apple has its own GPU system called **Metal**. TensorFlow supports it through and extra package.
```bash
python3 -m venv tf-venv
source tf-env/bin/activate
pip install --upgrade pip
pip install tensorflow tensorflow-metal
```
Then run your test again to confirm the GPU is visible and in use.

#### Linux (NVIDIA GPUs)
If you're on Linux and have an NVIDIA GPU:
1. Install the **latest NVIDIA drivers, CUDA Toolkit, and cuDNN** (these can be installed via 
your package manager or from NVIDIA's website).
2. Then install TensorFlow with CUDA support:
```bash
pip install --upgrade pip
pip install "tensorflow[and-cuda]"
```
3. Verify with:
```bash
python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

### Step 3: Quick GPU Test (Optional)
If you’ve successfully set up GPU support, you can test it with a simple script:
```python
import tensorflow as tf

with tf.device('/GPU:0'):
    a = tf.random.normal([1000, 1000])
    b = tf.random.normal([1000, 1000])
    c = tf.matmul(a, b)

print("Matrix multiplication completed on GPU!")
```
If you don’t have a GPU, TensorFlow will automatically fall back to using your CPU, so 
this test will still run either way if you're curious.
---

## Investigating Basic Machine Learning Models



#### Definitions and Concepts to remember:
- Neural-Network:
- Sequential Models:
- Dense Layers:
- Loss Function:
- Optimizers:
- Stochastic Gradient Decent (sgd):
- Epochs:
- Weight and Bias:
