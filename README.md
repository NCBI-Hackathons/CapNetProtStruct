# CNPSP, CNPDP and CNPDP 2.0
![alt text](https://github.com/NCBI-Hackathons/CapNetProtStruct/blob/master/image/logo_2.png)
<br />

- Capsule Networks for improving protein secondary structure prediction accuracy
- Capsule Networks for protein chain domain number prediction based on protein structure image
- Capsule Networks for protein chain domain number prediction based on amino acid coordinates

## Team members

- Jia Wen (Lead)
- Clark Huang (Magician)
- Yangqi Su (Magician)
- Maoxuan Lin (Sysadmin)
- Jing Chen (Writer)



## Background

### Capsule networks
![alt text](https://github.com/NCBI-Hackathons/CapNetProtStruct/blob/master/image/CapsNet.png)
<br />
![alt text](https://github.com/NCBI-Hackathons/CapNetProtStruct/blob/master/image/Capsule_333.png)
<br />
Capsule networks is a kind of new neural networks, which could improve the shortage of convolutional neural networks - orientation problem.
### Secondary structure prediction

![alt text](https://github.com/NCBI-Hackathons/CapNetProtStruct/blob/master/image/pymol_2.png)
<br />
Protein secondary structure is the first step towards prediction of protein tertiary structure, which is essential in protein structure and function. There are mainly three types of secondary structures: α-helix, β-strand, and coil.  
### Domain partition

Protein Domain is generally considered as a compact, semi-indipendent units with identifiable hydrophobic core. The intersections between domains are weak.[5,6] It is important in protein structure and function assignment and prediction. Domain identification is still a big problem. The two most important points in domain identification are the number of domains and the boundary of domains.  

## Goal

Here, we are trying to use capsule networks to:
- do the protein secondary structure prediction to see if we can improve protein secondary structure prediction accuracy. (Highest accuracy now: ~84%)
- do protein chain domain number prediction based on protein structure image.
- protein chain domain number prediction based on amino acid coordinates. 

## Workflow
![alt text](https://github.com/NCBI-Hackathons/CapNetProtStruct/blob/master/image/flowchart.png)
<br />
Just like other neural networks program, the workflow is simple: training the program and then testing the program. 
- CNPSP : Ideally, for the user, they can just input the protein sequence and then, they can get the predicted secondary structure type for each amino acid in the protein sequence. Inside our program, we do pre-processing input data, which is to generate the format that can be used in capsule networks, run capsule networks, and post-processing output data to get the read-friendly output format.  
![alt text](https://github.com/NCBI-Hackathons/CapNetProtStruct/blob/master/image/workflow_3.png)
<br />

- CNPDP : User can use protein structure image as input. Inside our program, we parsed the image files and trained the model. The output daata will be the predicted number of domains for the protein chain. 
![alt text](https://github.com/NCBI-Hackathons/CapNetProtStruct/blob/master/image/PDP.png)
<br />

- CNPDP 2.0 : User can use protein chain PDB ID as input. Inside our program, we searched the PDB ID from database, get the atom coordinates information and use these information generate input matrix. Finally, they can also get the predicted number of domains for the protein chain. 
![alt text](https://github.com/NCBI-Hackathons/CapNetProtStruct/blob/master/image/PDP2.png)
<br />

## Method and Data
The protein secondry structure datasets are collected from Protein Data Bank(PDB, https://www.rcsb.org/) which is established since 1970's. The PDB provides s standard representation of molecular structure datasets which are derived from X-ray crystallography, NMR spectroscopy, and increasingly, cryo-electron microscopy,which are sumbitted by scientists around the world.
### Training data
- CNPSP: The original training data set is from CullPDB with 5600 PDB files. The PDB format file contains full structure information about the known structure protein which we get the structure from either X-ray method or NMR method. The set of PDB files were selected by Olga Troyanskaya's lab in Princeton University - the data set was used in training their Supervised Convolutional GSN model for protein secondary structure.[3] The similarity between any two protein sequence from the data set is less than 30%, which is a good property for training the protein structure prediction model. 

The CullPDB dataset was constructed before CASP10 (i.e., May 2012), in which any two proteins in this set share around 20% sequence identity with each other(http://www.princeton.edu/~jzthree/datasets/ICML2014/). CB513 dataset contains 513 non-redauntant sequences which can be used to test protein secondary structure methods.Both CullPDB and CB513 can be used as benchmark datasets.

- CNPDP: We generate the training data set malually from Pymol. We generated 32 protein structure images with labels as training data set. The label information is from CATH. 

CATH can help group protein domains based on their folding patterns, the domains prediction ar downloaded from Protein Data Bank. It includes four levels of classes that ar chlassification,architecture (A), topology (T) and homologous superfamily (H)[7].

- CNPDP 2.0: We get the atom coordinates from PDB file for each protein chain, training the model using xxx protein chain information with labels. The label information is from CATH. 
### Capsule networks
The original Capsule networks code is from https://github.com/XifengGuo/CapsNet-Keras, which is a Keras implementation of CapsNet in the paper:
Sara Sabour, Nicholas Frosst, Geoffrey E Hinton. Dynamic Routing Between Capsules. NIPS 2017
We modified the code to do the protein secondary structure prediction. 
### Testing data
- CNPSP: There are two sets of testing data: 513 PDB files from Cb513 and 272 PDB files from CullPDB. All PDB files were pre-proceed into the data format as training data. 
- CNPDP: The testing data set is manually generated. We test oue model using 2 labeled images.  
- CNPDP 2.0: The testing data set is manually generated. We test oue model using yyy labeled images. 
### Validation data
- CNPSP: There are 256 PDB files from CullPDB we can use to validate our Capsule networks. 
## Usage
Usage is modified from the original Capsule networks code [2].

### Requirement
Install Keras>=2.0.7 with TensorFlow>=1.2 backend.

### CNPSP
#### Example

```
python capsulenet_CNPSP.py sequence.txt
```
The sequences.txt includes sequence like "MQVWPIEGIKKFETLSYLPPLTVEDLLKQIEYLLRSKWVPCLEFSKVGFVYRENHRSPGY...".
 <br />
The expected output would be "----------EEEEEEE-----HHHHHHHHHHHHH---EEEEEE----EEEEE-------".
### CNPSP
#### Example
```
python capsulenet_CNPDP.py image.png
```
The image.png can be any protein structure image generated by Pymol like: 
![alt text](https://github.com/NCBI-Hackathons/CapNetProtStruct/blob/master/domain/pymol/1_1.png)
<br />
The expected output would be "1".
### CNPSP
#### Example
```
python capsulenet_CNPDP2.py protein_chain_PDB_ID
```
The protein_chain_PDB_ID can be any protain chain PDB ID like: 
1CHJ.
<br />
The expected output would be "1".



## Reference
[1] Sabour, Sara, Nicholas Frosst, and Geoffrey E. Hinton. "Dynamic routing between capsules." Advances in Neural Information Processing Systems. 2017.<br />
[2] Keas, https://github.com/XifengGuo/CapsNet-Keras. <br />
[3] Zhou, Jian, and Olga Troyanskaya. "Deep supervised and convolutional generative stochastic network for protein secondary structure prediction." International Conference on Machine Learning. 2014. <br />
[4] Protein Data Bank, https://en.wikipedia.org/wiki/Protein_Data_Bank.<br />
[5] Wetlaufer, Donald B. "Nucleation, rapid folding, and globular intrachain regions in proteins." Proceedings of the National Academy of Sciences70(3): 697-701, 1973.<br />
[6] Swindells, Mark B. "A procedure for detecting structural domains in proteins." Protein Science, 4(1):103-112, 1995.
[7] Orengo, Christine A., et al. "CATH–a hierarchic classification of protein domain structures." Structure 5.8:1093-1109, 1997.
