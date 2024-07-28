# LicenseMiniSPEC

**License Plate Detection and Recognition using YOLOv8 and EasyOCR**

**Final Year Computer Science Engineering Mini Project**

This project is a part of our final year mini project for Computer Science Engineering. The goal of this project is to design and develop a system that can detect and recognize license plates in videos using YOLOv8 and EasyOCR.

**Project Overview**

The project involves two main tasks:

1. **License Plate Detection**: Using YOLOv8, a real-time object detection system, to detect license plates in videos.
2. **License Plate Recognition**: Using EasyOCR, an optical character recognition system, to recognize the text in the detected license plates.

**Installation**

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

**Usage**

To run the project, use the following command:

```bash
python predictWithOCR.py model='/content/LicenseMiniSPEC/best.pt' source='/content/LicenseMiniSPEC/demo.mp4'
```

This will detect and recognize license plates in the specified video and save the results to the `runs/detect/train3` directory.

**Requirements**

* Python 3.10+
* Torch 2.0.1+
* CUDA 11.8+
* YOLOv8 8.0.3
* EasyOCR 1.7.1
* Other dependencies listed in `requirements.txt`

**Model**

The model used in this project is a YOLOv8 model trained on a dataset of license plates. The model is stored in the `best.pt` file in the `LicenseMiniSPEC` directory.

**Dataset**

The dataset used to train the model is not included in this repository. However, you can use your own dataset of license plates to train the model.

**Results**

The results of the project are saved to the `runs/detect/train3` directory. This directory contains the output of the model, including the detected license plates and their corresponding text recognition results.

**Project Timeline**

* Literature Review: 1 week
* Dataset Collection and Preparation: 2 weeks
* Model Training and Testing: 4 weeks
* Integration and Deployment: 2 weeks
* Evaluation and Testing: 1 week

**Project Members**

* Safzan Pirani
* Vinitha Mandari
* Aditya V.

**Guides**

* Dr. Sushma Dutta
* CSE (AI&ML) Department

**Acknowledgments**

We would like to thank Dr. Sushma Dutta for guiding us throughout the project. We would also like to thank Vinitha Mandari and Aditya V. for their contributions to the project.

**Note**

This project is for educational purposes only. The accuracy of the model may vary depending on the quality of the input video/image and the dataset used to train the model.
