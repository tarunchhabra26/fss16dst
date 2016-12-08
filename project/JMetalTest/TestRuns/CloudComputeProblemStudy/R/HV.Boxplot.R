postscript("HV.Boxplot.eps", horizontal=FALSE, onefile=FALSE, height=8, width=12, pointsize=10)
resultDirectory<-"../data"
qIndicator <- function(indicator, problem)
{
fileNSGAII<-paste(resultDirectory, "NSGAII", sep="/")
fileNSGAII<-paste(fileNSGAII, problem, sep="/")
fileNSGAII<-paste(fileNSGAII, indicator, sep="/")
NSGAII<-scan(fileNSGAII)

fileMOEAD<-paste(resultDirectory, "MOEAD", sep="/")
fileMOEAD<-paste(fileMOEAD, problem, sep="/")
fileMOEAD<-paste(fileMOEAD, indicator, sep="/")
MOEAD<-scan(fileMOEAD)

fileSMPSO<-paste(resultDirectory, "SMPSO", sep="/")
fileSMPSO<-paste(fileSMPSO, problem, sep="/")
fileSMPSO<-paste(fileSMPSO, indicator, sep="/")
SMPSO<-scan(fileSMPSO)

algs<-c("NSGAII","MOEAD","SMPSO")
boxplot(NSGAII,MOEAD,SMPSO,names=algs, notch = TRUE)
titulo <-paste(indicator, problem, sep=":")
title(main=titulo)
}
par(mfrow=c(1,2))
indicator<-"HV"
qIndicator(indicator, "CloudSimPower")
