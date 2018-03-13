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
The original training data set is from pdb. The pdb format file contains full structure information about the known structure protein which we get the structure from either X-ray method or NMR method. The set of pdb files were selected by Olga Troyanskaya's lab in Princeton University - the data set were used in training their Supervised Convolutional GSN model for protein secondary structure. WHY THE DATA SET IS GOOD. <br />
For pre-processing, the X value of the training data is reshaped into a N*(20+1) matrix - N is the length of the protein sequence, 20 represents the number of total amino acids and 1 is a vector.  
### Testing data

## Result


