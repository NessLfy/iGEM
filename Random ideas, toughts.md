# General ideas for the project
We want to be able to detect oyster pathogens

We want to detect multiple oyster pathogens : alexandrium, OshV-1 (µvariant)

We want to give quantitative information on the detection : are they present and if so is it dangerous

We could have like a growth curve and then the detection creating a point smewhere on the curve and thus we can estimate wether the oyster is "at risk" 

We could have multiple targets for one pathogen (still multiplex) but specific metabolic targets and thus be able to say the "state" of infection. This might be easier for the vius but less litterature...
If we set on doing that for alexandrium it might be more complicated because it is not a host-pathogen situation...
For the virus it might be diffucult as it is a DNA virus that might not be active all the time. 

For the virus: as it is a DNA virus:
- First we might have problem extracting the DNA/RNA
- Also we could design the sequences for specific machnieries so that in the end we have an answer on the activity level 
- But in that case the answer will not tell wether there is or isn't a virus but rather if there is at which state it is
- otherwise if we have a quantification we can in any case transcribe the DNA of the virus and if the detection for the machinery is higher than the basal level then we can conclude on the activation state

Is there a way to have markers of matobolism in the pathogens to be able to conclude on their state.
This information could be infered from a network if we have acess to the transcriptome 

We could also want to target something in the oyster that would reflect on their metabolic state. Maybe an imune marker for example.

Otherwise use something as an environmental probe....

# Bioinformatics
Choice of target:
- first idea : 16S rRNA -> good idea but might be difficult bc 2nd structure of RNA and presence of proteins around RNA but easy in the sense that it is higly produced.

## Workflow of "automatic" target screening
If we have transcriptome:
	Find the "most abundant" RNA and design couple of targets from there.
	With these targets blast them against NCBI database to see where it lands
	Filter the results with possible water species
	If the results are in multiple species:
		Find wether or not they are present in Thau
		If they are present we could design spacer for flanking sequence and if all 3 targets are positive then it is the patogens
	Iterate over all the spacers and create a library of guides

Complementary: take a water sample and try to have the metagenome of it:
	From there we can also blast all the spacers we designed to see wether:
		our organism is present in the water
		if some other organisms are also detected by the same sequence 



# Multiplexing, practical thinking: 

We need to figure out what will make our project different from the rest. Our idea of multiplexing makes the project unique as it creates a semi quantitative analysis. Hence the importance of the modeling to be able to be even more quantitative. 

Now in the amount of time we have we need to figure out what our project will be: 
- Either we want to develop a paper based test:
	- Need to figure out how we can multiplex in a single paper test : difficulties with the lyophylisation of the protein the migration of the probe, we need at least 4 different antibodies with catch proteins (streptaviin for example)
	- Or we can multiplex in the sense where we have 4 different papers (with each the same probe basically) and we can still target different genes.
		- The problem with this approach is how do you link the 4 test, how can you compare "different experiences" (might not be the same concentration of sample in the 4, pipetting errors,...)
- We can also stick with the in-vitro technique (in a single tube):
	- Problem is that its not really usable in the field (need a plate reader) 
	- But it brings a new dimension of estimating the well being of the oyster plus the pathogen which is not done with the actual tests (pcrs)
	- We can also do the multiplexing in different tubes (only need one probe)
	- Issue with one pot sherlock is the need for different cas and different probes with different fluorophore which might not be easy to order and to have... 

