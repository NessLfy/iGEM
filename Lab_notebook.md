# Previous work on the sequences
More information on what I did can be found in the file *BLAST analysis results.pptx* 

# 05_07_2022 16s V2, tox genes and oyster genes
The sequences I analysed are contained in *sequences/pathogens/16s_tox_genes_oyster_genes.fa*.

With previous analysis results I concluded that the 16s RNA was not enough variable to be a good target. However by looking at the alignment file given by Marie-Agnes TRAVERS I created a logo sequence to see where the variable reions were ![](images/logo_16s.png)
We see that there are region where the sequence is hyper variable across the different species. Hence we tried 2 new 16s guide sequences. 

## 16s_01

The first sequence (16s_01) BLAST against the specie *Vibrio metschnikovii* by looking at the alignment : ![](images/16s_01_alignement.png)Query : Guide sequence 
Subject: *Vibrio metschnikovii* 

The guide is in the hypervariable region but the two species are still too close...

## The second sequence 16s02: 

It matches with *Vibrio sp.* which means an unidentified vibrio strain (which thus could mean the one we want but not only...) 

But it matches mostly with 16s region 520 - 550 which is not a variable region as shown above... 

## VAM
Matches with only *Vibrio aestuarianus* 
|Sequence name|Match|e_value|
|-----------------|------|--------|
|VAM| Vibrio aestuarianus clone 12830515 secreted zinc metalloprotease Vam (vam) gene|0.000627875|
|VAM|Vibrio aestuarianus metalloprotease precursor (VAM) gene|0.000627875|

## Hsp70 (oyster genes)
|Match name|ID of match|db|Accession|Name|E_value|Specie|
|-------------|-|-|-|-|-|-|
|match: gi|1843003221|ref|XM_034461664.1| PREDICTED: Crassostrea gigas heat shock 70 kDa protein cognate 4-like (LOC117686547)|e value: 0.000627875|Oyster|
|match: gi|31322196|gb|AY172024.1| Crassostrea ariakensis heat shock protein 70 mRNA, complete cds|e value: 0.000627875|Oyster|
|match: gi|46359615|dbj|AB122064.1| Crassostrea gigas HSC71 mRNA for 71kDa heat shock connate protein, complete cds|e value: 0.000627875|Oyster|
|match: gi|27125467|emb|AJ318883.1| Ostrea edulis partial hsp70 gene for heat shock protein 70 |e value: 0.000627875|Oyster|
|match: gi|27124645|emb|AJ318882.1| Crassostrea gigas partial hsp70 gene for heat shock protein 70 |e value: 0.000627875|Oyster|
|match: gi|4838560|gb|AF144646.1|AF144646 Crassostrea gigas heat shock protein 70 (hsp70) mRNA, complete cds |e value: 0.000627875|Oyster|
|match: gi|985397949|ref|XM_015511049.1| PREDICTED: Diuraphis noxia heat shock 70 kDa protein cognate 4-like (LOC107163583), mRN |e value: 0.0021915|Wheat insect|
|match: gi|188532069|gb|EU684308.1| Exorista civilis heat shock protein 70A (hsp70A) mRNA, complete cds |e value: 0.0021915|Fly|
|match: gi|1060235638|ref|XM_017987196.1| PREDICTED: Drosophila busckii heat shock 70 kDa protein cognate 1 (LOC108599948), mRNA |e value: 0.00764908|Fly|
|match: gi|2261262504|emb|OX090951.1| Heterocephalus glaber genome assembly, chromosome: 11 |e value: 0.00764908|Rat|
|match: gi|2261216452|emb|OX090919.1| Heterocephalus glaber genome assembly, chromosome: 11 |e value: 0.00764908|Rat|
|match: gi|1803972830|ref|XM_032235350.1| PREDICTED: Thamnophis elegans heat shock protein family A (Hsp70) member 2 (HSPA2), mR |e value: 0.0266979|Snake|
|match: gi|927185275|ref|XM_014071980.1| PREDICTED: Thamnophis sirtalis heat shock 70kDa protein 2 (HSPA2), mRNA |e value: 0.0266979|Snake|
|match: gi|1931678519|ref|XM_017722022.2| PREDICTED: Pygocentrus nattereri heat shock protein family A (Hsp70) member 1B (hspa1b |e value: 0.0266979|Piranha|
|match: gi|1916991832|ref|XM_036579327.1| PREDICTED: Colossoma macropomum heat shock protein family A (Hsp70) member 1B (hspa1b) |e value: 0.0266979|Fish produced in venezuela|

For this sequence even though it matches with other stuff, they are far from the oyster or are differen species of oyster that are not farmed in Thau which is where we will perfrom the test

## SD
Matches only with *Crassostrea gigas*

## IL17
Matches only with *Crassostrea gigas* 

It would be nice to have the results already in a dataframe

# 06/07/2022 - 16s Hypervariable region test
We tried to redesign sequences in the hypervariable regions of the 16s DNA of *Vibrio aestuarianus* namely region 22-53 and region 

## First sequence
Matches mainly with *Shewanella algae* ,another bacteria, with a low e-value wich means no specificity

## Second sequence 
Matches with different vibrio which is also not good

In conclusion using the 16s RNA is not very suited to perform specificity tests...


# 11/07/2022
## Team meeting
Protocol to remove the SUMO:

- PCR to remove the SUMO -> transformation -> Colony PCR -> Sequencing
- Use a restriction enzyme in between the annealing part of the primers to check the PCR 
- Have C's at the 5' end on the reverse primer 
- Add a negative control (no polymerase) for the PCR 
- control for the transcription : no polymerase


# 12/07/2022
## Guide sequences order
Guide sequences are found in the file *"C:/Users/nessl/Documents/iGEM/guides.xlsx"* 
They can also be found in the [drive](https://docs.google.com/spreadsheets/d/17rd2V9CkcU9Tw9LNlGdgd1L7_eiWqh9UtgJRLARWOBE/edit#gid=0) 

### Removing the SUMO tag
First idea : Remove by PCR amplification. The problem is the size of the plasmid (9kb) which is going to introduce mutations. Solution we found is to use infusion assembly. 
You amplify on the gene in the origin plasmid and also amplify a part of the vector plasmid (open it). On the gene you add overhangs to the primers that are complementary to the primers used for the amplification of the gene. Protocol: amplify the gene (thus adding the overhangs) and in a second step amplify the vector in the presence of the amplified gene : 
![[cas13a.png]]
The plasmids and the primers can be found on benchling: 
![[images/plasmid.png|300]]
# 13/07/2022

SUMO tag excision + ordering of targets

# 18/07/2022
Labeling of the primers received : *"drive/Shell'lock/sequences"* 

Model : ![[model_figure.png]]

Modeling advancement : 

Following ![[ODEs.png]]
```python
#System of ODEs
def syst(t,z,param):
    
    C,GC,GCT,T,G,Pi,Pa = z
    
    Kcdiss,Kcbind,Kcrdiss,Kcrbind,g,Ksn,Kun= param
    
    dPadt = (Kun*GCT*Pi)-(g*Pi)
    dCdt = (Kcdiss*GC)-(Kcbind*C*G)-(g*C)
    dGCdt = (Kcbind*C*G)-(Kcdiss*GC)-(Kcrbind*GC*T)+(Kcrdiss*GCT) 
    dGCTdt = (Kcrbind*GC*T)-(Ksn*T-Kcrdiss*GCT)
    dTdt = Ksn*GCT
    dGdt = (Kcdiss*GC)-(Kcbind*C*G)-(g*G)
    dPidt = -(Kun*GCT*Pa)
    
    return [dPadt,dCdt,dGCdt,dGCTdt,dTdt,dPidt,dGdt]
```

```python
#integrator

z=[(45*10**-9),0.00000000001,0.00000000001,(10**-8),(10**-8),0.000002,0.00000000001] #more or less the initial concentration 

param  = [0.1,0.01,0.1,0.1,0.1,0.1,9] #guess

t = np.linspace(0, 50, 100)

sol =  solve_ivp(syst, t_span=[0, t.max()], y0=z, dense_output=True, atol=1e-8, rtol=1e-8,args=([param]))
z = sol.sol(t) 
```

```python
# error and minimization

def error(param,obs):
    
    times = np.linspace(0,500,97)
    t = np.linspace(0,500,500)
    
    sol = solve_ivp(syst,t_span =[0, times.max()], y0= z , args =([param]),t_eval=times,method='DOP853',dense_output=True,rtol=1e-8,atol=1e-8)
    
    z = sol.sol(times)
    
    err = []
        
    for i in range(len(z.tolist()[0])):
        err.append((obs[i]-z.tolist()[0][i])**2)    
    
    erro = np.sum(err)

    return erro

res = minimize(error, param, args=(obs))
```

The presenatation I did for the team meeting can be found in : *"C:/Users/nessl/Documents/iGEM/team_meeting_18_07_2022.pptx"*

# 19/07/2022 
Final model : 
![[Final_model.png]]

Modeling meeting : 
- Need to add that when the cas complex cuts (target or probe it "recreates" the complex)
- For parameters use [Nalefski.E et al ,*iscience*, 2021](https://doi.org/10.1016/j.isci.2021.102996 "Persistent link using digital object identifier") and [Mahas A. et al, *applied biological science*, 2022](https://doi.org/10.1073/pnas.2118260119)
- Main question remains whether the Cas13 cuts the target to get activated and/or when it cuts the target is it still active ? 

It looks that untill the Cas13 hasn't cut its target but recognized it it is active : 
![[Cas13a_reaction.png]]

Project advancement : 

Because probes are taking long to produce and receive we looked for paper based options. We found a company that sells paper for latteral flow detection and order them.
The kit contains the gold beads linked to the $\alpha$-FITC antibody the paper with the $\alpha$-rabbbit antibody and the streptavidin antibody
![[paper_test.jpeg]]

We thus also ordered the correcponding probes rom IDT : 
**/56-FAM/rUrUrUrUrUrUrUrUrUrUrUrUrUrU/3Bio/** It contains a 5' FITC (to be captured by the bead) and a 3' Biotin to be captured by the streptavidin. 

I don't know whether the orientation matters ? I would say no because the probe can be flipped in all direction but I followed the construction proposed by *Kellner et al.* in the original SHERLOCK paper. 

# 20/07/2022 
Modeling: Best attempt so far 
![[modeling_poc_V2.png]]
with parameters : ![[parameters_v2.png|100]]
I used the parameters from the artciles mentionned previously. The shape of the curve look more or less right for $P_{inactive}$ , GCT, GC

Ideas to move forward: make the model simpler and consider for example a Michaelis menten system for the cas reaction: 
- First with 2 same products ( K_sn equals K_un)
- Then with 2 different products  ( K_sn diff K_un)

## FSDIE
Called Jeremy Esteves (director of the Service Vie Etudiante), results: 
	- Everything the is on the UGAP website, they can order it
	- For the rest they can pay back the CNRS account as long as the association name figures on the RIB (*I asked Didier for this information*)

# 21/07/2022
Follow up on the FSDIE situation, wrote to Peter for the video

### Modeling 
A summary of everything I did can be found there [[Modeling.pdf]]


