# indeed-jobs
Analysis of historical data scraped from Indeed.com

# About
- Most job website projects used one cross-sectional data, which restricts the kinds of analysis
- So, the plan was to collect historical data to find significant trends in the data job market.
- The biggest 
- Sample: 30,000 jobs scraped from indeed.com over 3 month periods, for 2019, 2020, 2021
  - note: since samples are relatively spaced apart, treat as cross-sectional samples
## Planned analyses:
- univariate:
  - region vs jobs
  - city vs jobs
  - employer vs jobs
  - levels of jobs
  - seniority vs jobs, region, skills
  - jobs vs skills 
  - jobs vs tools
- bivariate: 
  - what predicts salary?
  - what skills are in demand?
  - what skills are more demanded for senior roles (career progression)?

# What are data jobs:
- data scientist, machine learning, data architext, data engineer, Business Intelligence (BI) Developer, statistician, data analyst, database administrator, data modeler, marketing scientist, 

avoided: 
- niche roles (research scientists, quantitative analyst)
- engineering focused roles (Information architect, MLOps)

exceptions:
- 'scientist'
- titles with 'data'

links:
- https://www.northeastern.edu/graduate/blog/data-science-careers-shaping-our-future/
- https://www.kdnuggets.com/2021/10/guide-14-different-data-science-jobs.html 

# What are data skills and tools:
- skills:
  - Data transformation (cleaning, preparing, wrangling, manipulating)
  - Data analysis and exploration, Statistical knowledge, ML
  - Creating data visualizations, dashboards and reports
- tools:
  - Python, R, SQL/structured query language, Excel, Tableau, Power BI, git, cloud, version control, docker

links:
- https://www.dataquest.io/blog/data-analyst-skills/
- https://www.northeastern.edu/graduate/blog/data-analyst-skills/


#  Data changelog:
1. drop columns with mostly or all null values
2. drop un-useful columns
3. check data types and nulls
4. year indicator variables 
5. concat tables 
6. filtered exceptions to jobs only if they appeared more than once
  - so still some error in jobs 
7. reduced categories for states and industry frequency tables

# Data notes:
- not sure how to validate/correct outliers for categorical data
  - e.g. 'risk manager' for seniority
- handling mistypes and misspells
  - convert all to lower case and regex 
  - are there better methods? e.g. unsupervised classification algorithms


# Lessons:
- pre-optimizing is bad
  - There is a tendency to start optimizing code immediately, but since the biggest limit to efficiency is actually time, if one spends it solving problems that do not require the efficiency, then it slows the project down overall.
- Colab is (*very*) limited
  - I wanted to try cloud resources, but while Colab is fast it does not allow local storage and transferring the data over from Cloud Storage took 30 seconds on average
- analysis only as good as data source
  - The analysis was severely limited due to the available data. The key problem for this project was that salary information was mostly null. 
- time allocation
  - data cleaning/transformation/loading is 90% of the work
  - validate, prepare, transforming variables determines what analysis is possible, and comprises the major decisions of analysis

# Next time:
- For handling categorical data, there were a few methodologies that could be useful in the future
- logistic regression, GLM, ANOVA, factorial design