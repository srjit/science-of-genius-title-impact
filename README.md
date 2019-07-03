# Science of Genius - Analysis of Titles and Abstracts


Communication is an essential component of the scientific endeavor, yet the relationship between the textual properties of scientific papers and their reception by the scientific community is relatively unknown. As a component of the [Science of Success project](https://www.barabasilab.com/publications/quantifying-the-evolution-of-individual-scientific-impact), this project will explore whether specific lexical factors are indicative of the attention an article received, as measured by normalized citation indices, by combining analytical tools from natural language processing, data science, and the science of science.
The initial stages of the study will focus on the temporal and disciplinary variance in the length and syntactic features of article titles in the [Web of Science](https://en.wikipedia.org/wiki/Web_of_Science), a massive dataset containing over 50 million articles published since 1900. The project also aims to develop a quantitative model, which can estimate the impact a scientific article could create in the community.

This quantitative model of article presentation will be useful for maximizing the impact of future articles and thereby accelerate scientific growth.


### Environment
---
- Installing dependecies for the project

  * `sudo apt-get install python3-tables`
  * `sudo pip3 install seaborn pandas networkx`


### Building Data For Analysis
---
- [These](https://github.com/srjit/science-of-genius-title-impact/tree/master/src/1.%20Build%20Data%20for%20Analysis) notebooks shows data preparation steps for the analysis.


### Exploratory Data Analysis
---
- [These](https://github.com/srjit/science-of-genius-title-impact/tree/master/src/2.%20Explore%20Data%20-%20Title%20Length%20Analysis) notebooks explore the temporal distribution of structures in titles of Applied Physics articles conditioned on Journals in which they appear.


### Models - Title
---
- [These](https://github.com/srjit/science-of-genius-title-impact/tree/master/src/3.%20Title%20Length%20-%20Citation%20Counts%20:%20Curve%20Fitting) models show how linear/weighted linear regression models have been used to predict log c5 (citation counts five years from the year of publication).


### Novelty
---
- [These](https://github.com/srjit/science-of-genius-title-impact/tree/master/src/4.%20Word%20Overlap%20with%20Previous%20N%20Years)
  notebooks show how new (interesting) words come up in literature (titles) and how they decay
  through time.


### Semantics EDA
---
- [These](https://github.com/srjit/science-of-genius-title-impact/tree/master/src/5.%20Variations%20in%20Parts%20of%20Speech%20-%20Impact%20on%20Citations)
  notebooks show how variations in parts of speech of titles have changed over the years for different disciplines.


### Propagation of Words
---
- [These](https://github.com/srjit/science-of-genius-title-impact/tree/master/src/6.%20Propagation%20of%20words%20-%20Growth%20and%20Decay)
  notebooks show different methods of selecting concepts from titles of publications and how growth
  and decay of concepts happen for different disciplines.
  

### Word Usage Fluctuations
---
- [These](https://github.com/srjit/science-of-genius-title-impact/tree/master/src/7.%20Temporal%20Word%20Variations)
  notebooks show how much fluctuations occur in word usage. We also try to characterize these
  fluctuations to known distributions.
