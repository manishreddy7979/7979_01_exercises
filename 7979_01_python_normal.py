# import pandas, numpy
# Create the required data frames by reading in the files

# Q1 Find least sales amount for each item
# has been solved as an example
def least_sales(df):
    # write code to return pandas dataframe
	a=df.groupby("Item")["Sale_amt"].min()
    return a

# Q2 compute total sales at each year X region
def sales_year_region(df):
    # write code to return pandas dataframe
    a=df.groupby([df["OrderDate"].apply(lambda x:x.year),"Region"])["Sale_amt"].sum()
    return a

# Q3 append column with no of days difference from present date to each order date
def days_diff(df):
    # write code to return pandas dataframe
    date=pd.to_datetime("2020-01-08")
    a=df['days_diff']=abs(df['OrderDate'].sub(date))
    return a

# Q4 get dataframe with manager as first column and  salesman under them as lists in rows in second column.
def mgr_slsmn(df):
    # write code to return pandas dataframe
    a=df.groupby("Manager")["SalesMan"].apply(set)
    return a

# Q5 For all regions find number of salesman and number of units
def slsmn_units(df):
    # write code to return pandas dataframe
    a=pd.DataFrame()
    a["salesman_count"]=df.groupby("Region")["SalesMan"].count()
    a["total_sales"]=df.groupby("Region")["Sale_amt"].sum()
    return a


# Q6 Find total sales as percentage for each manager
def sales_pct(df):
    # write code to return pandas dataframe
    a=df.groupby("Manager")["Sale_amt"].sum()/df["Sale_amt"].sum()*100
    return a

# Q7 get imdb rating for fifth movie of dataframe
def fifth_movie(df):
	# write code here
    return df["imdbRating"][4]

# Q8 return titles of movies with shortest and longest run time
def movies(df):
	# write code here
    print("shortest movie length :")
    a=df[df["duration"]==df["duration"].min()]['title'].reset_index()
    print("longest movie length :")
    b=df[df["duration"]==df["duration"].max()]['title'].reset_index()
    return a,b

# Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)
def sort_df(df):
	# write code here
    a=df.sort_values(by=['imdbRating', 'year'],ascending=[False,True])
    return a

# Q10 subset revenue more than 2 million and spent less than 1 million & duration between 30 mintues to 180 minutes
def subset_df(df):
	# write code here
    

# Q11 count the duplicate rows of diamonds DataFrame.
def dupl_rows(df):
	# write code here
    dup=df.duplicated().count()
    return dup

# Q12 droping those rows where any value in a row is missing in carat and cut columns
def drop_row(df):
	# write code here
    df.dropna(subset=['carat','cut'])
    return df.head()
# Q13 subset only numeric columns
def sub_numeric(df):
	# write code here
    return df._get_numeric_data()

# Q14 compute volume as (x*y*z) when depth > 60 else 8
def volume(df):
	# write code here
    df['volume'] = df.apply(lambda df: (df['x']*df['y']*df['z'] if df['depth'] > 60 else 8),axis=1)
    return df

# Q15 impute missing price values with mean
def impute(df):
	# write code here
    df.fillna(value=df.mean())
    return df
