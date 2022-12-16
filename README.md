# Housing_Price_Analysis


![house](https://user-images.githubusercontent.com/108366412/202578852-4a87745b-9a9a-4e15-a6e1-f992e4395957.jpg)

## Background of the Project
Canada is one of the top real estate market in world. The aftermath of covid pandemic and economic downturn has slowed down real estate market of Canada with declining sales in 2022. However, real estate market in Canada is very competitive and is often considered by majority of people as best long term investment.

## Problem Statement
In this project, we will
- Analyse the relation of house prices with various factors such as  year, region, immigration and lending rate
- Predict house prices for next 5 years

## Methodology 
- Collect data from different sources
- Prepare ERD Schema using QuickDB
- Clean and merge data to create final database
- Perform Exploratory Data analysis on the datasets
- Create a machine learning model and estimate accuracy
- Create a visualization of the result and display on webpage.
- Create [Google Slides](https://docs.google.com/presentation/d/17urz7OMdW8Qi5NzWePaZ6ScvPWxBlKx10AwSCiOk1jo/edit#slide=id.g17505948ed0_0_140)

## Tools and Technologies used
- Git Bash
- Python 3.7
- Jupyter Notebook
- PostgreSQL
- Python Packages
    - NumPy
    - SciPy
    - Scikit Learn
- Machine learning algorithm: Linear regression
- Visualisation: Plotly, Json, Javascript, HTML, seaborn

## ERD Schema
![ERD diagram](https://user-images.githubusercontent.com/108366412/205193712-24614d09-6b1f-42c7-ae5b-ad0b7c8e4512.png)

## Datasets
![Final_Data](https://user-images.githubusercontent.com/108366412/205194249-444d2bda-9b2d-4c73-a2b5-ce9bd7c89cf9.png)

- Features of model: Lending Rate, Immigration, Region, Year
- Target variable: Price
- Timeframe of analysis: January 2005-September 2022

## Assumptions
- Prime lending rate is used for all region

## Visualization

![webpage5](https://user-images.githubusercontent.com/108366412/205196546-4226030e-0462-4ee1-84a8-bf2d273bd3f0.png)

![webpage2](https://user-images.githubusercontent.com/108366412/205196526-cb3b3af7-5669-4ed2-abf9-24ed0dc6e6c9.png)

![webpage3](https://user-images.githubusercontent.com/108366412/205196565-8389a5a0-9f77-44dc-8e7b-e4d96c53479f.png)

![webpage4](https://user-images.githubusercontent.com/108366412/205196574-eeb9b396-535b-41fe-ba15-d6ea768d30d4.png)

## Machine Learning Model
Linear Regression Model is used as we are predicting house price based on a combination of input variables like interest rate, immigrant population. The model was selected as it can be implemented, trained and interpret easily. 
Following results were acheived from the model
* **R-squared: 0.94358**
* **Mean squared error:  745478395.75**

[Link to video of dashboard](https://drive.google.com/file/d/1LkXaRTK2GIWdTqEQUBEOD_eCigLtQAXK/view)

