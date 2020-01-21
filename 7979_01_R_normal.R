library(dplyr)
library(lubridate)
library(readxl)
library(tidyr)
d1<- read_excel("SaleData.xlsx")

#1. Find the least amount sale that was done for each item.
aggregate(d1[,c('Sale_amt')],by=list(d1$Item),FUN = min)

# 2. Compute the total sales for each year and region across all items 
d1['year']=format(as.Date(d1$OrderDate, format="%m/%d/%Y"),"%Y")
aggregate(d1[,'Sale_amt'], list(d1$year,d1$Region), sum)

# 3. Create new column 'days_diff' with number of days difference between reference date passed and each order date 
d1$days_diff <-as.Date('12-06-2019','%m-%d-%Y')
d1$days_diff<- difftime(d1$days_diff ,d1$OrderDate , units = c("days"))
d1$days_diff


# 4. Create a dataframe with two columns: 'manager', 'list_of_salesmen'. Column 'manager' will contain the unique managers present and column 'list_of_salesmen' will contain an array of all salesmen under each manager. 

aggregate(d1['SalesMan'], list(d1$Manager), unique)


#6. Create a dataframe with total sales as percentage for each manager. Dataframe to contain manager and percent_sales
d<-aggregate(d1['Sale_amt'], list(d1$Manager), sum)
d['percent_sales']<-(d['Sale_amt']/sum(d1$Sale_amt))*100
d

d1<- read.csv("imdb.csv")
d1
#7. Get the imdb rating for fifth movie of dataframe
d1[['imdbRating']][5]

#8. Return titles of movies with shortest and longest run time
d1[which.min(d1$imdbRating),3]
d1[which.max(d1$imdbRating),3]

#9. Sort the data frame by in the order of when they where released and have higer ratings, Hint : release_date (earliest) and Imdb rating(highest to lowest)
arrange(d1,year,desc(imdbRating))

d1<- read.csv("diamonds.csv")

#11. Count the duplicate rows of diamonds DataFrame.
sum(duplicated(d1))

#12. Drop rows in case of missing values in carat and cut columns.

na.omit(d1,col=c("carat","cut"))

#13. Subset the dataframe with only numeric columns.
nums <- unlist(lapply(d1, is.numeric)) 
d1[nums]

#14. Compute volume as (xyz) when depth is greater than 60. In case of depth less than 60 default volume to 8.
vol<-function(depth,x,y,z)
{
  if(depth>60)
    d1['volume']=x*y*z
  else
    d1['volume']=8
}
d1['volume']<- mapply(vol,d1$depth,d1$x,d1$y,d1$z)

#15. Impute missing price values with mean.
d1$price[is.na(d1$price)]<-mean(d1$price,na.rm=TRUE)
