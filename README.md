*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.

# Facial Paralysis Classification

*TODO:* Write a short introduction to your project.

Unilateral facial weakness (facial palsy) can be caused by a dysfunction of the lower motor neuron (‘peripheral facial palsy’) or the central motor neuron (‘central facial palsy’). Most frequent underlying diseases include Bell’s palsy (peripheral origin)and stroke (central origin). The goal of this study is to correctly classify individuals as healthy, having a peripheral or having a central facial palsy, given 68 landmarks of their face. These landmarks were automatically annotated by an algorithm for healthy individuals and manually annotated for patients, since the algorithm does not perform well on those patients (algorithm trained only on images of facial symmetry whereas these patients have facial assymmetry). The position of those landmarks were extracted from 900*900 images in which the face is centered and converted into a csv file. Even though the spatial structure of these landmarks is not preserved, some performance metrics of common ML algorithms could be checked.  

![landmarks]( https://ibug.doc.ic.ac.uk/media/uploads/images/300-w/figure_1_68.jpg)

## Project Set Up and Installation
*OPTIONAL:* If your project has any special installation steps, this is where you should put it. To turn this project into a professional portfolio project, you are encouraged to explain how to set up this project in AzureML.

## Dataset

### Overview
*TODO*: Explain about the data you are using and where you got it from.

Patient images with unilateral facial weakness were obtained from the web and classified separately and blindly for a presumed (internet) diagnosis by experienced doctors in neurology (S.B., W.A.), both from Haga Teaching Hospital, as having peripheral or central facial palsy, and blindly checked by the diagnosis provided on the web, if available. Patient
images were included in our study if S.B. and W.A. agreed on the clinical phenotype of the facial palsy(peripheral vs. central facial palsy). In total, 203 images were collected and used in our study: 103 images of patients with a peripheral facial palsy, 40 images of patients with a central facial palsy, along with 60 images of healthy individuals.

### Task
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.

The task is to distinguish between healthy individuals, patients with a central, and patients with a peripheral facial palsy from the (x,y) positions of 68 landmarks of their face, annotated on a 900*900 image with the face centered on it. 

### Access
*TODO*: Explain how you are accessing the data in your workspace.

The dataset was converted to csv format and uploaded to github, from where it was inserted into the azure workspace.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

For the AutoML settings, we enabled the onnx compatible models, we set the primary metric to AUC_weighted, the number of max concurrent iterations to 5 and the timeout minutes to 20. In the configuration we specified the compute target, the task to classification, the training data, and the target (diagnosis).

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

The best results were obtained using a voting ensemble with which an AUC_weighted of 0.9346 was achieved. The model can be improved by allowing more iterations and giving it more time to test more models. 

*TODO* Remember to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

RunWidgets after execution
![alt text](https://github.com/nsourlos/palda_azure/blob/main/images/runwidgets.png)

AUC_weighted graph that shows changes after each experiment
![alt text](https://github.com/nsourlos/palda_azure/blob/main/images/automl_2.png)

Detailed list of experiments performed and their AUC_weighted value
![alt text](https://github.com/nsourlos/palda_azure/blob/main/images/automl_1.png)


## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search

A logistic regression model was chosen to see how well it can perform after hyperparameter tuning. We used random parameter sampling for the two parameters of that model, the inverse of regularization strenth (C), in which smaller valeus cause stronger regularization, and the maximum number of iterations to covnerge (max_iter). The values of C range from 0.01 to 1 and for max_iter it can take powers of 2, from 4 to 256.

### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

With this model, the best result obtained is an accuracy of 0.878, which was obtained for a parameter C=0.01 and max iterations=128. To improve it we can try Bayesian sampling, allow more total runs, use AUC_weighted instead of accuracy as optimizing metric, and increase experiment timeout to perform more experiments.

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

RunWidgets for hyperdrive
![alt text](https://github.com/nsourlos/palda_azure/blob/main/images/runwidgets1.png)

Accuracy evolution for the experiments performed
![alt text](https://github.com/nsourlos/palda_azure/blob/main/images/accuracy.png)

List of hyperparameters sampled by hyperdrive
![alt text](https://github.com/nsourlos/palda_azure/blob/main/images/hyper_params.png)

Best hyperparameters after hyperdrive run
![alt text](https://github.com/nsourlos/palda_azure/blob/main/images/best_hyper_params.png)


## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

The model was deployed using aci_webservice. Some of the datapoints of the test dataset were converted to a dictionary and provided as input to the model to get results. The data were given as input in JSON format and we made a request to the model and got its output. It correctly predicted all the 3 datapoints as belonging to either a healthy individual, a patient with a peripheral and a patient with a central palsy respectively.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

The link for the screen recording is:

https://drive.google.com/file/d/1N_R263BnOlI6flhiLiRgCR0OjOp0B7Zw/view?usp=sharing

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
