# TES-Teaching-Job-Scraper
A Program that Scrapes basic job information for a variety of Teaching Jobs posted on TES (GB Only).

# Contents

###  * What this WebScraper does
###  * Pre-requisites/Requirements to use the WebScraper
###  * Using the WebScraper

  
  
   
<br/><br/><br/>

# What This WebScraper Does
This webscraper scrapes TES Job data of the following types: 
- Job ID, 
- Job name, 
- Tenure type, 
- Starting date, 
- Application deadline, 
- Employer name, 
- Location (Name), 
- Salary (Range or Payscale type),
- Job posting url

This data is saved in a .csv format. This format should easily viewed in common spreadsheet programs such as Microsoft Excel and Google Sheets.
<br/><br/>

# Pre-requisites/Requirements to use the WebScraper

- Python version 3.9+ (Program originally written using Python 3.10.6 interpreter)
- A standard Command line/prompt or Console (for setting up and running the program)

### Setting up the Virtual Environment
It is good practice to create a virtual environment for this project (and for any other project with non-standard-library dependencies).
See this guide for how to setup and activate a virtual environment: [Python docs](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment "Python docs")

NOTE: Ensure that you activate the environment once you have created it.

To install the relevant packages, select the directory that requirements.txt is in and run the following command:
```
pip install -r requirements.txt
```

To check that all the packages have been installed, run the following command:
```
pip list
```
This should produce an output that looks contains these items
```
Package            Version
------------------ ---------
anyio              3.6.2
asttokens          2.0.8
backcall           0.2.0
certifi            2022.9.24
charset-normalizer 2.1.1
colorama           0.4.5
debugpy            1.6.3
decorator          5.1.1
entrypoints        0.4
executing          1.1.1
h11                0.12.0
httpcore           0.15.0
httpx              0.23.0
idna               3.4
ipykernel          6.16.0
ipython            8.5.0
jedi               0.18.1
jupyter_client     7.3.5
jupyter-core       4.11.1
matplotlib-inline  0.1.6
nest-asyncio       1.5.6
numpy              1.23.3
packaging          21.3
pandas             1.5.0
parso              0.8.3
pickleshare        0.7.5
pip                22.2.1
prompt-toolkit     3.0.31
psutil             5.9.2
pure-eval          0.2.2
Pygments           2.13.0
pyparsing          3.0.9
traitlets          5.4.0
urllib3            1.26.12
wcwidth            0.2.5
```

If all of these commands were executed successfully, you can now use the Scraper.

<br/>
<br/>
