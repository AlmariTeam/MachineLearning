# Almari
Bangkit Academy 2022 Captsone Project

## Initial Setup
Setup to run tensorflow in local machine with nvidia gpu (CUDA and cuDNN), follow the instruction in [tensorflow-local-gpu](https://github.com/feranteef/tensorflow-local-gpu#tensorflow-local-gpu) or [Tensorflow_GPU_Setup](https://github.com/feranteef/Almari/blob/main/Setup/Tensorflow_GPU_Setup.md) github repositories

## Fashion Classfication
1.Download the dataset from and replace to `Fashion Classfication/` Folder
run 

## Fashion Color Classfication
1. Download the dataset from and replace to `Fashion Color Classfication/Dataset/` Folder
2. Run [Split_train_val.ipynb](https://github.com/feranteef/Almari/blob/main/Fashion%20Color%20Classfication/Split_train_val.ipynb) to split the dataset into `train and val` folder in `Dataset_Split` folder
3. Run [Standard_Model.ipynb](https://github.com/feranteef/Almari/blob/main/Fashion%20Color%20Classfication/Standard_Model.ipynb) to train the model and export trained model into `my_model.h5`
