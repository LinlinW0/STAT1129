#Q1
A<-matrix(c(7,2,9,4,12,13),nrow=2,ncol=3)
A
B<-matrix(c(1,2,3,7,8,9,12,13,14,19,20,21),nrow=3,ncol=4)
B
A%*%B

#Q2
amazon=read.csv('Amazon-orders.csv')
head(amazon)
dim(amazon)
amazon$Item.Total <- gsub("[$]","",as.character(amazon$Item.Total))
amazon$Item_total<-as.numeric(amazon$Item.Total)
amazon$Item_total
sum(amazon$Item_total)
max(amazon$Item_total)
min(amazon$Item_total)
mean(amazon$Item_total)
median(amazon$Item_total)

date<-as.Date(amazon$Order.Date, format="%m/%d/%y")
plot(amazon$Item_total~date,main="Item Total Per Day", type="l",col="red",axes=F)
box()
axis(1,date,format(date,"%m-%y"))
library(tidyverse)
library(lubridate)
library(nycflights13)

amazon$month<-format(date, "%m")
amazon$monthname<-format(date, "%b")
amazon$year<-format(date, "%Y")
amazon
plot(amazon$Item_total~amazon$month)



