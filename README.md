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
### Testing data

## Result


