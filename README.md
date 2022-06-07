<p align="center"> <img src="https://user-images.githubusercontent.com/105408877/172390195-f1e83ed3-a905-4bf9-8205-abd5730f077a.png" width="600" height="375"> </p>

This repository contains a deep learning model that can detect drugs with the help of yolov5. Currently the available drugs are heroin, cocaine, marijuana and shrooms.

![all4](https://user-images.githubusercontent.com/105408877/172393929-b852ac2d-e8ab-4c13-9a7a-8f08facae1b2.jpg)



## Dataset

![Picture2](https://user-images.githubusercontent.com/105408877/172394271-d4237401-26ee-4708-834c-d1808fd2850a.png)


The dataset currently includes 1,149 images:
959 images for training
113 images for validating
77 images for testing

We have a total of 4,064 labels:
1,042 for heroin
1,010 for shrooms
1,009 for marijuana
1,003 for shrooms

![Picture3](https://user-images.githubusercontent.com/105408877/172396142-57308da2-fcc6-45fe-9bd7-20bb1f0a7b45.png)


To see the dataset: https://app.roboflow.com/vanessa-garza/drug-detection/images/?split=train
To download the dataset: https://app.roboflow.com/ds/cOAubjHwVB?key=5gPBzA80Ha
To download the dateaset in a notebook:
```python
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="FsN2lxpZFkeJdUOIAgEl")
project = rf.workspace("vanessa-garza").project("drug-detection")
dataset = project.version(3).download("yolov5")
```

We labeled all the data individually with the help of RoboFlow.
For more information about RoboFlow, visit https://roboflow.com/

![Screenshot 2022-06-07 223914](https://user-images.githubusercontent.com/105408877/172394764-d3c5afe3-e28d-4c3e-9da7-02781d91757e.png)

## Installing Requirements

Before anything, you have to install the requirements by typing the following code in the command line:
```bash
pip install -r requirements.txt
```

## Train Model

To train the model we used the "Drug_Detection_v2.ipynb" file in Google Colab by following the steps included the code: 
1. Cloning the YOLOv5 repository into Google Colab.
2. Import roboflow (where we have our dataset).
3. Set up an environment.
4. Download the dataset by giving the dataset API key (unique id), the username, the project name, and the dataset version (the latest version is version 3).
5. Train the deep learning model with 400 epochs, 12 batch,set up images size to 640, set dataset location.
6. Load tensorboard to see your model statistics like train loss, model accuracy, etc.
7. Once you finish training your model you can check how its working with excecuting the "detect.py" file.
8. You can display the images that you detected in step 7.
9. Download your new trained model to be used offline. In this case we named our model "drugs237.pt"

Here is an exmaple for the training parameters:
```bash
python train.py --img 640 --batch 16 --epochs 400 --data {dataset.location}/data.yaml --weights yolov5x.pt --cache
```

Once you have your .pt file of your new trained model you can add it to the folder where your project is.


## Drug Detection

You can detect drugs 2 ways: with the help of the interface or by running the following code in the command line.

Now to be able to detect drugs you can run the "detect.py" file with the weights set up to your new model's name and by choosing the source you want to dectct. For example run this code in the terminal:
```bash
python detect.py --weights drugs277.pt --source photo.jpg
```
"drugs277.pt" is the model trained with the dataset version 4 which includes cocaine, heroin, marijuana, and shrooms. This model was trained with 277 epochs hence the name.

## Interface

To run the interface, run the code "DrugDetection.py" by typing the following line of code in the command line.

```bash
python DrugDetection.py
```
After running the interface you will see the main page.

![Screenshot 2022-06-04 154307](https://user-images.githubusercontent.com/105408877/172398042-c4b3149f-2934-4b04-9b0b-a612eb8437a6.png)

If you click "Help" button it will take you to the steps on how to use the software.

![Picture4](https://user-images.githubusercontent.com/105408877/172398442-7132479b-bf43-45e6-8a61-bd097ccdecd2.png)

To quit the software click on the "X" or "Exit".

To start detecting click either on "Upload Image" or "Upload Video" depending on what file you want to detect.

![Picture5](https://user-images.githubusercontent.com/105408877/172398981-ab5be55d-dc26-43cd-bb35-878a1bad25a2.png)

Then after choosing your file, click upload. The green progress bar will start filling up until the detection is completed, then the result will be automatically displayed.

![Picture6](https://user-images.githubusercontent.com/105408877/172399319-9b71700d-3b60-4da7-83bc-92bc45978043.png)

## Supported Formats
This is the list of file formats supported for detecting the drugs:

Pictures:
bmp, dng, jpeg, jpg, mpo, png, tif, tiff, webp

Videos:
asf, avi, gif, m4v, mkv, mov, mp4, mpeg, mpg, ts, wmv


## Contribution
This project was made by Amazon Team from Woosong University. The team members are:

Vanessa Garza Enriquez
vanessagzae@gmail.com

Yang Seong Jin
hyysj0103@gmail.com

Jamshidbek Urolov
maxboy19992001@gmail.com

<p align="center"> <img src="https://user-images.githubusercontent.com/105408877/168080675-bf8fd5cd-fe1d-4418-a50f-6d6a870dadee.png" width="300" height="300"> </p>
