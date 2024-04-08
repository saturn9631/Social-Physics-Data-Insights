# PoliDataRectifier
## Summary
In modern times there is a firehose of information and politics is no different, so this project was made to parse down all the data into a usable format. In this is a project to analyze politics using data and math borrowed from physics, economics and other places; all of which can be used to analyze everything from power structures, to relationship markets, to the shifting of opinions of a population. 
## Math
Most of the math used in this library will be calculus, linear algebra, statistics, and game theory however more advanced math is planned: group theory, differential geometry, and functional analysis as well as some other miscellaneous stuff. One of the main goals of the library is to produce differential equations that predicts the decisions made by the entities (people, groups, organizations) based off of their payoffs, which will be called their strategy. The strategy and the associated DE can be shown along with the data to give insights as to what the entities are doing, why they are doining it, and what they will do in the future.
## Necessary Packages
### Python
1. sympy
2. numpy
3. pandas
4. scipy
5. torch (cuda/rocm)
  1. torchaudio and torchvision
6. transformers (torch version) by huggingface
7. matplotlib
8. seaborn
9. bokeh
10. plotly
11. jupyter
### DataBase
As of now the only database is MySql, however any sql relational database would probably work. At a certain point a vector database and a search engine might be useful.
### Commit Rules
As of now there is not many since it is a small project, but code is welcome and so is math; it just needs to be in an issue or in a pull request to modify documentation.
