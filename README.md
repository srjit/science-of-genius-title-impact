# Science of Genius - Analysis of Titles and Abstracts


Communication is an essential component of the scientific endeavor, yet the relationship between the textual properties of scientific papers and their reception by the scientific community is relatively unknown. As a component of the [Science of Success project](https://www.barabasilab.com/publications/quantifying-the-evolution-of-individual-scientific-impact), this project will explore whether specific lexical factors are indicative of the attention an article received, as measured by normalized citation indices, by combining analytical tools from natural language processing, data science, and the science of science.
The initial stages of the study will focus on the temporal and disciplinary variance in the length and syntactic features of article titles in the [Web of Science](https://en.wikipedia.org/wiki/Web_of_Science), a massive dataset containing over 50 million articles published since 1900. The project also aims to develop a quantitative model, which can estimate the impact a scientific article could create in the community.

This quantitative model of article presentation will be useful for maximizing the impact of future articles and thereby accelerate scientific growth.


### We hypothesize that
---
- There is a relationship between the length of the title and impact of the article, which also depends on the popularity of the journal where it was published.
- The reputation of the authors/co-author has a positive effect on the impact of the article.
- Topic popularity reflected in the title or abstract may contribute to the impact.
- The clarity of the abstract has a positive influence on the impact of the article.
- The sentiment of the abstract has a positive influence on the impact of the article.
	

### Environment
---
- Installing dependecies for the project

  * `sudo apt-get install python3-tables`
  * `sudo pip3 install seaborn pandas networkx`

### Building Data For Analysis
---
-[These](https://github.com/srjit/science-of-genius-title-impact/tree/master/src/create-data) notebooks shows data preparation steps for the analysis.

### Exploratory Data Analysis
---
- [These](https://github.com/srjit/science-of-genius-title-impact/tree/master/src/data-exploration) notebooks explore the temporal distribution of structures in titles of Applied Physics articles conditioned on Journals in which they appear.

### Models - Title
---
-[These](https://github.com/srjit/science-of-genius-title-impact/tree/master/src/models) models show how linear/weighted linear regression models have been used to predict log c5 (citation counts five years from the year of publication).

### Novelty
---
-[These](https://github.com/srjit/science-of-genius-title-impact/tree/master/src/novelty-eda) notebooks show how new (interesting) words come up in literature (titles) and how they decay through time.

### Interdisciplinary Novelty
---
-[These](https://github.com/srjit/science-of-genius-title-impact/tree/master/src/word%20propagation) notebooks shows building a framework for selecting interesting words and how those words move from one disciple to another through time.
	







