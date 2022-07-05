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



