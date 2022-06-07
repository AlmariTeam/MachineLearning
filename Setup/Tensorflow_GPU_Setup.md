# Initial Setup
Setup to run tensorflow in local machine with nvidia gpu (CUDA and cuDNN)

## Compatibility
1. CUDA GPUs Compatibility : https://developer.nvidia.com/cuda-gpus
2. Tensorflow Compatibility : https://www.tensorflow.org/install/source#gpu

## Installation
1. Install [Anaconda](https://docs.anaconda.com/anaconda/install/windows/)
2. Install [Visual Studio Community](https://visualstudio.microsoft.com/downloads/) (Core Editor Only)
3. Install CUDA Toolkit and cuDNN that compatible with os machine and python version, respectively. (for example CUDA Toolkit v11.0 with cuDNN v8.0.05)
4. Install [CUDA Toolkit 11.0 Update](https://developer.download.nvidia.com/compute/cuda/11.0.3/network_installers/cuda_11.0.3_win10_network.exe)
5. Download [cuDNN 8.0.5 for CUDA 11.0](https://developer.nvidia.com/rdp/cudnn-archive#a-collapse805-110)

   - Extract cuDNN zip file, copy all folders in `cuda` folder to `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0` (select replace)
   - Add these to `Path` environment variables (`search "edit environment variables for your account" in windows start > advanced > Environment Variables... > select "path" on System variables > edit`)

      ```cmd
      C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\bin
      C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\libnvvp
      C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\extras\CUPTI\lib64
      C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\include
      ```

   - Reboot

6. Create virtual environment
   - `conda create --name tf(version) python==3.8`
   - `conda activate tf(version)`
   - `pip install tensorflow==2.8.0`
   - `pip install opencv-python`
   - `pip install numpy`

7. Install Jupyter Notebook
   - `conda install -y jupyter`
   - `conda install -y nb_conda`

## Testing
```Bash
import tensorflow as tf
if tf.test.gpu_device_name():
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
else:
    print("Please install GPU version of TF")
```

if the setup succeed, the output would be like
```Bash
Default GPU Device: /device:GPU:0
```
or if you want to check number of GPU
```Bash
import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
```
expected output
```Bash
Num GPUs Available:  1
```
check https://www.tensorflow.org/guide/gpu for more information on settings (single or multiple GPU, limiting GPU gorwth, etc)

