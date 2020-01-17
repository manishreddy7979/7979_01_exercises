library(dplyr)
library(lubridate)
library(readxl) #read excel files
library(tidyr)
library(varhandle) #unfactor
library(readr) #read_lim
library(descr) #crosstab
library(imputeTS)#impute values
library(mltools)#create bins
library(assertr)
library(stringr)
data.1<-read_delim('C:/Users/manish.tanuboddi/Desktop/mine/movie_metadata.csv', delim=',', escape_double=FALSE, escape_backslash=TRUE)
data.2<-read_delim("C:/Users/manish.tanuboddi/Desktop/mine/imdb.csv", delim=',', escape_double=FALSE, escape_backslash=TRUE)
data.3<-read_delim("C:/Users/manish.tanuboddi/Desktop/mine/diamonds.csv", delim=',', escape_double=FALSE, escape_backslash=TRUE)

#B1!
question.1 <- function(df){
  df2<-df %>%select(16:44)
  df['genre_combo'] <- apply(df2,1,function(x) paste(names(x[x==1]),collapse=" "))
  df2<- df%>% group_by(year,type,genre_combo)%>%
    summarise(avg_rating=mean(imdbRating),min_rating=min(imdbRating),max_rating=max(imdbRating),total_run_time_mins=(sum(duration)/60))
  return(df2)
}
#question.1(data.2)

#B2@
question.2<-function(data.2)
{ 
  x<-na_mean(data.2)
  x$year=floor(x$year)
  x$len=nchar(x$wordsInTitle)
  x[is.na(x$wordsInTitle),"len"]=nchar(as.character(unlist(x[is.na(x$wordsInTitle),"title"])))
  x$percentile<-bin_data(x$duration,bins=4,binType = "quantile")
  d<-as.data.frame.matrix(table(x$year,x$percentile))
  colnames(d)<-c("num_videos_less_than25Percentile","num_videos_25_50Percentile ","num_videos_50_75Percentile","num_videos_greaterthan75Precentile")
  y<-x%>%group_by(year)%>%summarise(min=min(len),max=max(len))
  print(cbind(y,d))
}
#question.2(data.2)

#B3#
question.3<-function(data.3)
{
  data.3$z[data.3$z=="None"]<-NA
  data.3$z<-as.numeric(data.3$z)
  x<-na_mean(data.3)
  x$volume <- ifelse(x$depth>60,(x$x)*(x$y)*(as.integer(x$z)), 8)
  x$quant<-as.numeric(ntile(x$volume,5))
  y<-crosstab(x$quant,x$cut,plot=FALSE,prop.c=TRUE)
  print(y)
}
#question.3(data.3)

#B4$
question.4<-function(df)
{
  df=na.omit(df)
  x=df %>% group_by(title_year)
  x=x[with(x,order(-gross)),]
  x<-x %>% group_map(~head(.x,ifelse(nrow(.x)<10,1,as.numeric(0.1*nrow(.x)))),keep=TRUE)%>%bind_rows()
  t<-x %>%group_by(title_year,genres)%>%summarise(avg=mean(imdb_score),count=n())
  return(t)
}
#question.4(data.1)

#B5%
question.5<-function(data.2)
{
  data.2<-data.2[!is.na(data.2$duration),]
  data.2$decile=as.numeric(bin_data(data.2$duration,bins=10,binType="quantile"))
  a<-data.2[,17:45]
  b<-a%>%group_by(decile)%>%summarise_all(sum)
  x<-data.2%>%group_by(decile)%>%summarise(nominations=sum(nrOfNominations),wins=sum(nrOfWins),count=n())
  x$top_genres=top_genre=col_concat(t(as.data.frame(apply(b,1,function(x) head(names(b)[order(-x)],3)),stringsAsFactors = FALSE)),sep="|")
  print(x)
}
#question.5(data.2)