# CapNetProtStruct
Capsule Networks for improving protein secondary structure prediction accuracy

## Team members

- Jia Wen (Lead)
- Clark Huang
- Jing Chen
- Maoxuan Lin
- Yangqi Su

## Background

### Secondary structure prediction

![alt text](https://github.com/NCBI-Hackathons/CapNetProtStruct/blob/master/image/pymol_2.png)
<br />
Protein secondary structure is the first step towards prediction of protein tertiary structure, which is essential in protein structure and function. There are mainly three types of secondary structures: α-helix, β-strand, and coil.  
### Capsule networks
Capsule networks is a kind of new neural networks, which could improve the shortage of convolutional neural networks - orientation problem.
## Goal

Here, we are trying to use capsule networks to do the protein secondary structure prediction to see if we can improve protein secondary structure prediction accuracy. (Highest accuracy now: ~84%)

## Workflow
![alt text](https://github.com/NCBI-Hackathons/CapNetProtStruct/blob/master/image/workflow.png)
<br />
Just like other neural networks program, the workflow is simple: training the program and then testing the program. Ideally, for the user, they can just input the protein sequence and then, they can get the predicted secondary structure type for each amino acid in the protein sequence. Inside our program, we do pre-processing input data, which is to generate the format that can be used in capsule networks, run capsule networks, and post-processing output data to get the read-friendly output format.  

## Method and Data

### Training data
The original training data set is from CullPDB with 5600 PDB files. The PDB format file contains full structure information about the known structure protein which we get the structure from either X-ray method or NMR method. The set of PDB files were selected by Olga Troyanskaya's lab in Princeton University - the data set was used in training their Supervised Convolutional GSN model for protein secondary structure. The similarity between any two protein sequence from the data set is less than 30%, which is a good property for training the protein structure prediction model.  <br />
After pre-processing, the X value and Y value will look like this: 
![alt text](https://github.com/NCBI-Hackathons/CapNetProtStruct/blob/master/image/Input.png)
<br />
![alt text](https://github.com/NCBI-Hackathons/CapNetProtStruct/blob/master/image/Intput_Y.png)
<br />
### Capsule networks
The original Capsule networks code is from https://github.com/XifengGuo/CapsNet-Keras, which is a Keras implementation of CapsNet in the paper:
Sara Sabour, Nicholas Frosst, Geoffrey E Hinton. Dynamic Routing Between Capsules. NIPS 2017
We modified the code to do the protein secondary structure prediction. 
### Testing data
There are two sets of testing data: 514 PDB files from Cb513 and 272 PDB files from CullPDB. All PDB files were pre-proceed into the data format as training data. 
### Validation data
There are 256 PDB files from CullPDB we can use to validate our Capsule networks. 
## Usage
Usage is modified from the original Capsule networks code.[2]
### Requirement
Install Keras>=2.0.7 with TensorFlow>=1.2 backend.

### Usage
```
python capsulenet.py sequence.txt
```

## Reference
[1] Sabour, Sara, Nicholas Frosst, and Geoffrey E. Hinton. "Dynamic routing between capsules." Advances in Neural Information Processing Systems. 2017.<br />
[2]  https://github.com/XifengGuo/CapsNet-Keras
