write("", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex",append=FALSE)
resultDirectory<-"TestRuns/CloudComputeProblemStudy/data"
latexHeader <- function() {
  write("\\documentclass{article}", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write("\\title{StandardStudy}", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write("\\usepackage{amssymb}", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write("\\author{A.J.Nebro}", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write("\\begin{document}", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write("\\maketitle", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write("\\section{Tables}", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write("\\", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
}

latexTableHeader <- function(problem, tabularString, latexTableFirstLine) {
  write("\\begin{table}", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write("\\caption{", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write(problem, "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write(".IGD+.}", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)

  write("\\label{Table:", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write(problem, "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write(".IGD+.}", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)

  write("\\centering", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write("\\begin{scriptsize}", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write("\\begin{tabular}{", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write(tabularString, "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write("}", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write(latexTableFirstLine, "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write("\\hline ", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
}

printTableLine <- function(indicator, algorithm1, algorithm2, i, j, problem) { 
  file1<-paste(resultDirectory, algorithm1, sep="/")
  file1<-paste(file1, problem, sep="/")
  file1<-paste(file1, indicator, sep="/")
  data1<-scan(file1)
  file2<-paste(resultDirectory, algorithm2, sep="/")
  file2<-paste(file2, problem, sep="/")
  file2<-paste(file2, indicator, sep="/")
  data2<-scan(file2)
  if (i == j) {
    write("-- ", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  }
  else if (i < j) {
    if (is.finite(wilcox.test(data1, data2)$p.value) & wilcox.test(data1, data2)$p.value <= 0.05) {
      if (median(data1) <= median(data2)) {
        write("$\\blacktriangle$", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
      }
      else {
        write("$\\triangledown$", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE) 
      }
    }
    else {
      write("--", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE) 
    }
  }
  else {
    write(" ", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  }
}

latexTableTail <- function() { 
  write("\\hline", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write("\\end{tabular}", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write("\\end{scriptsize}", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
  write("\\end{table}", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
}

latexTail <- function() { 
  write("\\end{document}", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
}

### START OF SCRIPT 
# Constants
problemList <-c("CloudSimPower") 
algorithmList <-c("NSGAII", "MOEAD", "SMPSO") 
tabularString <-c("lcc") 
latexTableFirstLine <-c("\\hline  & MOEAD & SMPSO\\\\ ") 
indicator<-"IGD+"

 # Step 1.  Writes the latex header
latexHeader()
tabularString <-c("| l | p{0.15cm } | p{0.15cm } | ") 

latexTableFirstLine <-c("\\hline \\multicolumn{1}{|c|}{} & \\multicolumn{1}{c|}{MOEAD} & \\multicolumn{1}{c|}{SMPSO} \\\\") 

# Step 3. Problem loop 
latexTableHeader("CloudSimPower ", tabularString, latexTableFirstLine)

indx = 0
for (i in algorithmList) {
  if (i != "SMPSO") {
    write(i , "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
    write(" & ", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)

    jndx = 0
    for (j in algorithmList) {
      for (problem in problemList) {
        if (jndx != 0) {
          if (i != j) {
            printTableLine(indicator, i, j, indx, jndx, problem)
          }
          else {
            write("  ", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
          } 
          if (problem == "CloudSimPower") {
            if (j == "SMPSO") {
              write(" \\\\ ", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
            } 
            else {
              write(" & ", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
            }
          }
     else {
    write("&", "TestRuns/CloudComputeProblemStudy/R/IGD+.Wilcoxon.tex", append=TRUE)
     }
        }
      }
      jndx = jndx + 1
    }
    indx = indx + 1
  }
} # for algorithm

  latexTableTail()

#Step 3. Writes the end of latex file 
latexTail()

