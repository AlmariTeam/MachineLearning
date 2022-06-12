# Almari
Bangkit Academy 2022 Captsone Project, This project classify fashion model into 46 fashion classes using [Deepfashion dataset](https://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html) and 10 fashion color using [Deepfashion dataset](https://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html) and some picture on the internet we find.

## Initial Setup
Setup to run tensorflow in local machine with nvidia gpu (CUDA and cuDNN), follow the instruction in [tensorflow-local-gpu](https://github.com/feranteef/tensorflow-local-gpu#tensorflow-local-gpu) or [Tensorflow_GPU_Setup](https://github.com/feranteef/Almari/blob/main/Setup/Tensorflow_GPU_Setup.md) github repositories

## Fashion Classfication
1. Download the dataset from and replace to `Fashion Classfication/` Folder
2. Run [Split Categorical.ipynb](https://github.com/feranteef/Almari/blob/main/Fashion%20Classification/Split%20Categorical.ipynb) to split the dataset into `46 fashion` folder
3. Select all `46 fashion` folder and replace into `Fashion Classfication/Dataset` folder
4. Run [Split_train_val.ipynb](https://github.com/feranteef/Almari/blob/main/Fashion%20Classification/Split_train_val.ipynb) to split the dataset into `train and val` folder in `Fashion Color Classfication/Dataset_Split/` folder
5. Run [VGG16_Model.ipynb](https://github.com/feranteef/Almari/blob/main/Fashion%20Classification/VGG16_Model.ipynb) to train the model and export trained model into `my_model3.h5`


## Fashion Color Classfication
1. Download the dataset from [here](https://drive.google.com/file/d/1oEpUbio4mCvsAr2ByPYi-kAfTMqT_BFq/view?usp=sharing) and replace to `Fashion Color Classfication/Dataset/` folder
2. Run [Split_train_val.ipynb](https://github.com/feranteef/Almari/blob/main/Fashion%20Color%20Classfication/Split_train_val.ipynb) to split the dataset into `train and val` folder in `Fashion Color Classfication/Dataset_Split/` folder
3. Run [Standard_Model.ipynb](https://github.com/feranteef/Almari/blob/main/Fashion%20Color%20Classfication/Standard_Model.ipynb) to train the model and export trained model into `my_model.h5`

## Deployment
