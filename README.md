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
Protein secondary structure is the first step towards prediction of protein tertiary structure, which is essential in protein structure and function. There are mainly three types of seconary structures: α-helix, β-strand and coil.  
### Capsule networks
Capsule networks is a kind of new nueral networks, which could imporve the shortage of convolutional neural networks - orientation problem.
## Goal

Here, we are trying to use capsule networks to do the protein seconary structure prediction to see if we can imporve protein secondary structure prediction accuracy. (Highest accuracy now: ~84%)

## Workflow
![alt text](https://github.com/NCBI-Hackathons/CapNetProtStruct/blob/master/image/workflow.png)
<br />
Just like other neural networks program, the workflow is simple: training the program and then testing the program. Idealy, for the user, they can just input the protein sequence and then, they can get the predicted secondary structure type for each amino acid in the protein sequence. Inside our program, we do pre-proccesing input data, which is to generate the format that can be used in capsule networks, run capsule networks, and post-processing output data to get the read-friendly output format. 

## Method and Data

### Training data
The original training data set is from CullPDB with 5600 pdb files. The pdb format file contains full structure information about the known structure protein which we get the structure from either X-ray method or NMR method. The set of pdb files were selected by Olga Troyanskaya's lab in Princeton University - the data set were used in training their Supervised Convolutional GSN model for protein secondary structure. The similarity between any two protain sequence from the data set is less than 30%, which is a good property for training the protain structure prediction model. <br />
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
There are two sets of testing data: 514 pdb files from Cb513 and 272 pdb files from CullPDB. All pdb files were pre-proceed into the data format as training data. 
### Validation data
There are 256 pdb files from CullPDB we can use to validate our Capsule networks. 
## Usage
Usage is modified from the original Capsule networks code.[1]
### Requirement
Install Keras>=2.0.7 with TensorFlow>=1.2 backend.

### Usage
```
python capsulenet.py input sequence.txt
```

## Reference
