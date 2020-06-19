# Car damage detection

## Background
Car damage claims typically include pictures of damaged vehicles and parts. 
Claim handlers or experts use those pictures to assess the damage and come up with a 
fair offer to settle the claim. 

Currently this process is mostly manual and based on experience of the handlers. 
The main idea behind this assignement is a possibility to automate this process at least
for small claims and come up with automated damage assessment. This can be divided into following steps:
1. Automatic damage detection
1. Damage assessment
1. Claim settlement

## Problem description

### Damage detection
This step is the main part of the hands-on assignment. We have provided a set of labeled 
data that can be used for model training (`images/train`). The folder contains ~50 
images of car damages. In the same folder there is a `json` file that contains annotation of each image.
The tool used for annotation can be accessed via the following link http://www.robots.ox.ac.uk/~vgg/software/via/via-1.0.6.html

Jupyter notebook  `car_damage_case.ipynb` contains useful script that can be used for 
understanding the data and visualising it.

**The main objective is to build a model that given a new image would be able to detect the damaged part (if it exists).**

Given the limited time for this assignment do not worry too much about the quality of the model.
Also, in case you are not able to fully develop a baseline model feel free to elaborate the missing steps.
How would you perform them if you had more time? 

Feel free to leverage transfer learning. 
Pretrained models and some useful functions and ideas for model development can be found here:
https://github.com/matterport/Mask_RCNN

**During the interview please be prepared to discuss the details of your approach. 
It is important that you are able to motivate each decision and assumption you made during model development**

### Damage assesment

During the interview please describe how would you assess the damage:

- Which data would you use?
- How would you develop the model?
- How you assess it's performance?

### Putting it all to production

Please prepare one slide where you will highlight your approach for productionizing the models.

Feel free to make any assumptions regarding the enterprise systems. 
- How would the solution architecture look like?
from the moment the customer uploads the picture using web form to the final settlement proposal?
- Which technologies would you use for exposing the model? (open source)
- Which other components would you need to develop to integrate the model in production environment?
- How would you manage CI/CD, logging, model updating? 



