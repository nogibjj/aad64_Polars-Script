# Week 3 Mini Project:

![example workflow](https://github.com/nogibjj/aad64_Polars-Script/actions/workflows/actions.yml/badge.svg)

This assignment is designed to introduce us to polars descriptive scripts. For the same, the main edit made was to add polars==2.1.0 to my requirements.txt file.

Here, I have created a project which has functions dedicated to doing the following on a given dataset and returning the output: 
* Calculating the `mean`,
* Calculating the `median`,
* Calculating the `standard deviation`,


<p align = "center"><img width="467" alt="Screenshot 2023-09-12 at 6 55 15 PM" src="https://github.com/nogibjj/aad64_Polars-Script/assets/143753050/fb862ae7-ac3f-40ad-8276-40f7c900e67e"></p>


* Displaying the overall `summmary statistics` of a dataset.
<p align = "center"><img width="618" alt="Screenshot 2023-09-12 at 6 55 27 PM" src="https://github.com/nogibjj/aad64_Polars-Script/assets/143753050/4b81c6a1-4449-4656-97d6-fe17c01487ff"></p>

* `Visualizing` data in the form of a _boxplot_ (below is the function run on a small, example dataset created in the ![image](https://github.com/nogibjj/aad64_Polars-Script/assets/143753050/26b476a1-1784-4688-be8b-afdafa6a0c9a)



I have also created a test file to ensure that the mean, median, and standard deviation functions are correctly functioning (using asserts).

The contents of this project are: 
* `.devcontainer` (with a [devcontainer.json](https://github.com/nogibjj/aad64_Polars-Script/edit/main/.devcontainer/devcontainer.json) and a [Dockerfile](https://github.com/nogibjj/aad64_Polars-Script/edit/main/.devcontainer/Dockerfile)), 
* [Github Actions](https://github.com/nogibjj/aad64_Polars-Script/edit/main/.github/workflows/actions.yml), 
* `.gitignore file`, 
* [Makefile](https://github.com/nogibjj/aad64_Polars-Script/edit/main/Makefile), 
* [requirements.txt](https://github.com/nogibjj/aad64_Polars-Script/edit/main/requirements.txt), 
* [main.py](https://github.com/nogibjj/aad64_Polars-Script/edit/main/main.py), 
* [test_main.py](https://github.com/nogibjj/aad64_Polars-Script/edit/main/test_main.py), and 
* [iris.csv](https://github.com/nogibjj/aad64_Polars-Script/edit/main/iris.csv).

As visible below, my project is passing all formatting, linting, and tests:

### Linting
For this assignment, I switched over from pylint to ruff, thus, was not able to get a linting score. However, the actions badge provides information about my project passing all phases of the Makefile, including linting.
<p align = "center"></p>

### Formatting
<p align = "center"><img width="1288" alt="Screenshot 2023-09-12 at 7 47 28 PM" src="https://github.com/nogibjj/aad64_Polars-Script/assets/143753050/c1270129-31ff-4837-8eb3-3caad6c59755"></p>


### Testing
<p align = "center"><img width="407" alt="Screenshot 2023-09-12 at 7 47 53 PM" src="https://github.com/nogibjj/aad64_Polars-Script/assets/143753050/583977cd-4e93-4b19-957c-6b2960cbbd41"></p>

