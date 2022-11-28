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

NOTE: Ensure that you activate the environment once you have created it (See Python docs)

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

# Using the WebScraper

To use the webscraper:

- Open a Command prompt
- Navigate to the folder that contains the program (Should contain the following files):
```
README.md  __pycache__/  data/  main.py  requirements.txt  src/  test/
```
- Make sure you have activated the virtual environment created in the previous section. [See Python Docs](https://docs.python.org/3/tutorial/venv.html "Python docs")
- Run main.py and follow the prompts raised by the program.


### Following the Prompts

The first prompt you will see will ask you for a location
```
Enter the county, city or town which you would like to find jobs around.
```
Location provided must be in Great Britain. Location search functionality is non-case sensitive.
<br/>

The next prompt will ask you to select the radius around the location requested to search for jobs.
```
Enter the distance you would like to be search from the target location in miles (choice will be rounded to values specified below).
1. 3                                    2. 5
3. 10                                   4. 15
5. 20                                   6. 30
7. 50                                   8. 70
9. 100                                  10. 500
```
Select a number between 1 and 10 to choose a search radius of between 3 and 500 miles. (Search Radius < 20 miles recommended)
<br/>

The next prompt will ask you to select the workplace type/s you are searching for
```
Select the workplace numbers that you would like to search for jobs for. Separate choices with commas (,)
1. Secondary                            2. Primary
3. Special Education                    4. Further Education
5. Independent Senior
```
Similar to the previous prompt, you choose answers by inputting numbers. 
You can pick multiple workplace types by seperating your choices with a comma e.g. 
```
1, 3
```
<br/>

Next, you can select the type of role you are looking for. Choose these using the same method as used for choosing the workplace.
```
Select the position numbers you would like to search jobs for. Separate choices with commas (,)
1. Teaching and Lecturing               2. Leadership
3. Non-Teaching/Support
```
<br/>

Next, choose the subjects you would like to search for jobs for. Choose this using the same method as used for choosing the workplace and role type.
```
Select the subjects you would like to search for jobs for. Separate choices with commas (,)
1. Science                              2. Mathematics
3. English                              4. Special Needs
5. Physical Education                   6. Information Technology
7. Design and Technology                8. Modern Languages
9. Physics                              10. Chemistry
11. Biology                             12. Art and Design
13. Food Technolgy/Hospitality and Catering    14. Music
15. Performing Arts                     16. Computer Science

```

Finally, Select the maximum number of pages of results you would like to retrieve (the default maximum number is 3 pages, which works out as 60 job postings)
```
Enter the maximum number of pages of results you would like to scrape (page size is 20, default number of pages is 3)
```
You can leave this blank to limit the number of posting retrieved to the default value (60).

<br/>
<br/>

Once you have completed these actions, the program will output to the console the urls of any job postings it finds. It will then save the job postings' data to a .csv file located in the /data folder included in this program.

You can now view the results!

NOTE: Sometimes, an empty csv file will be created. This signals that no job postings were found that matched your criteria. Consider re-running the program and relaxing the criteria you use to filter job applications.

END
