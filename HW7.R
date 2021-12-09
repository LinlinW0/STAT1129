#Q1
#(a)
Data_Frame1 <- data.frame (
  id = c(1,2,3,4,5),
  name = c("Peter","Amy","Ryan","Gary","Michelle"),
  salary = c(623.30,515.20,611.00,729.00,843.25)
)
Data_Frame1
#(b)
New_col <- data.frame(
  department = c("IT", "Finance","Accounting","Math","Stat")
)
Data_Frame2<-cbind(Data_Frame1,New_col)
Data_Frame2
#(c)
Data_Frame3 <- Data_Frame2[-c(2), -c(1)]
Data_Frame3
Data_Frame4 <- Data_Frame3[-c(3), -c(3)]
Data_Frame4
#(d)
x<-c("Peter","Gary","Michelle")
y<-c(623.30,729.00,843.25)
barplot(y,names.arg=x)
#(e)
summary(Data_Frame1)
mylabel <- c("Highest", "Lowest", "Median")
colors <- c("blue", "yellow", "green")
x <- c(843.25,515.20,623.30)
pie(x, label = mylabel, main = "Salary", col = colors)
legend("bottomright", mylabel, fill = colors)

#Q2:
#if else
color<-function(get_color){
  if (get_color=="old_glory_red") {
    return("179,25,66")
  }else if (get_color=="old_glory_blue"){
    return("10,49,97")
  }else if (get_color=="white"){
    return("255,255,255")
  }else{
    return("0,0,0")
  }
}
color("white")
color("Blue")
color("old_glory_blue")

# for loop 
stripes<-1:13
for (x in stripes){
  if (x %% 2==0){
    color="white"
    print(paste("The",x,"stripe is",color))
  }else{
    color="red"
    print(paste("The",x,"stripe is",color))
  }
}
