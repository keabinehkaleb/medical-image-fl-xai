# Medical Image Federated Learning with Explainable AI

This project demonstrates a **Federated Learning framework for medical image classification** combined with **Explainable AI (XAI)** techniques.
The goal is to train machine learning models across distributed medical datasets while preserving patient privacy and providing interpretable model predictions.

## Objectives

* Train models on **distributed medical datasets**
* Preserve **patient privacy** using Federated Learning
* Improve **model transparency and trust** using Explainable AI (XAI)

## Technologies

* Python
* TensorFlow / PyTorch
* Federated Learning (FedAvg algorithm)
* Explainable AI methods (SHAP, LIME)

## Dataset

Example dataset used for experiments:

* **ISIC 2019 Skin Lesion Dataset**

This dataset contains dermoscopic images used for **skin cancer classification** with multiple diagnostic categories.

## Features

* Medical image classification
* Federated learning across multiple clients
* Privacy-preserving distributed training
* Explainable AI visualization for model predictions

## Installation

Install the required dependencies:

pip install -r requirements.txt

## Run the Project

Run the main application:

python app.py

## Research Focus

This project explores the integration of:

* Federated Learning for privacy-preserving medical AI
* Medical image analysis
* Explainable AI for clinical decision support

## Experimental Results

The performance results of the proposed Federated Learning + XAI model are stored in the Excel file below.

[Download Results](results/results.xlsx)
## Medical Image Dataset and Research Approach

This study utilizes the **ISIC 2019 skin lesion dataset**, which contains dermoscopic images used for the classification of different skin conditions, including various types of skin cancer. The dataset provides a diverse collection of labeled medical images that are widely used for developing and evaluating deep learning models for dermatological diagnosis.

In this project, we explore the use of **Federated Learning (FL)** to train machine learning and deep learning models on patient image datasets distributed across multiple hospitals. Instead of sharing sensitive medical data, each hospital trains the model locally on its own dataset, and only the learned model parameters are shared with a central server for aggregation. This approach helps preserve **patient privacy while enabling collaborative learning** across institutions.

We apply **deep learning and machine learning algorithms** for medical image classification and compare their performance using common evaluation metrics such as accuracy, precision, recall, and F1-score. The goal is to improve diagnostic performance while maintaining data confidentiality across healthcare institutions.

As part of future work, we plan to integrate **Explainable AI (XAI)** techniques such as **SHAP (SHapley Additive exPlanations)** and **LIME (Local Interpretable Model-agnostic Explanations)**. These methods will help highlight the important regions or features in medical images that influence model predictions. By providing interpretable insights, the system can support doctors in making **timely and more reliable clinical decisions**, ultimately improving patient monitoring and follow-up care.
## Experimental Results

The performance comparison of deep learning models on the ISIC 2019 dataset is available below:

[Download Results](results/results.xlsx)

## Author

**Keabineh Kaleb keba**
