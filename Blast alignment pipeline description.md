# Principle
The goal is to have an automatic pipeline that Blast a sequence agains NCBI databases.
We will use it to blast our potential candidates guide RNA to check where the there is alignments.
The analysis will be ran via python through the NCBI server

The principle is : 

- Open the sequence and transform the file type as an object 
- Call the Blast function with adjusted parameters
- Extract the results and filter them 

## Pipeline in practice
### open a sequence file
```python
from Bio import SeqIO 

seq_record = SeqIO.read('sequences/test/ELF3.fa','fasta')
seq_record.seq 
```
### Open multiple sequences
```python
seq = list(SeqIO.parse('sequences/test/sequences.fa','fasta'))
seq[0].seq # to see one of the sequence
```
### Call the blast function
You need to have blast installed locally to be able to run it. You can find it [there](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)

```python
from Bio.Blast import NCBIWWW

result_handle = NCBIWWW.qblast("blastn", "nt", seq[i].seq)

help(NCBIWWW.qblast) # to find description about the functions

```

The function takes multiples arguments that are listed on the NCBI website, but a summary of the main functions is available [here](https://biopython-tutorial.readthedocs.io/en/latest/notebooks/07%20-%20Blast.html#Running-BLAST-over-the-Internet)


## Optimization 
Usefull websites:
- [FAQ from NCBI](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=FAQ#entrez)
- [Biopython function doc](https://biopython.org/docs/1.75/api/Bio.Blast.NCBIWWW.html)


# Limits
1.  The Expect Value Threshold default setting will be reduced to 0.05.
2.  The maximum number of target sequences (Max target sequences) limit will be no more than 5,000.
3.  The maximum allowed query length for nucleotide queries (blastn, blastx, and tblastx) will be 1,000,000 and 100,000 for protein queries (blastp and tblastn).
[source](https://ncbiinsights.ncbi.nlm.nih.gov/2020/06/18/new-blast-settings/)
4. Submitting searches on off-hours (8 pm to 8 am EST) may provide better throughput. Morning in european time. 
5. Multiple sequences (I tried 50 random and it didn't work)
