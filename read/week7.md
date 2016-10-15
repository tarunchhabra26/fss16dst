# **Paper Review: Reading 7**
## **Reading**
Published in Empirical Software Engineering, 2015 October, Volume 20 Issue 5, 1354-1383. 
Automated prediction of bug report priority using multi-factor analysis
Yuan Tian, David Lo, Xin Xia and Chengnian Sun
## **Keywords**
1. **Bug report management:** Developers often allow users to report bugs that they found using a bug tracking system, to improve software quality. Bug reports would be investigated based on their priority levels. This priority assignment process however is a manual oneis report management.  

2. **Priority prediction:** The priority of a bug to be fixed which is assigned by a bug triager. When the bug report is submitted, this field would be blank. The triager would then decide an appropriate priority level for a bug report. There are five priority levels: P1, P2, P3, P4, and P5.Propose a new problem of predicting the priority of a bug given its report. Past studies on bug report analysis has only considered the problem of predicting the severity of bug reports which is an orthogonal problem.

3. **Text Preprocessing:** Preprocessing is an important task and critical step in Text mining, Natural Language Processing (NLP) and information retrieval (IR). In the area of Text Mining, data preprocessing used for extracting interesting and non-trivial and knowledge from unstructured text data.There are three common text preprocessing  steps:  tokenization,  stop  word  removal,  and stemming.   At  the  end  of  these  steps,  each  bug  report  is represented as a bag (i.e., multiset) of words. The authors remove special symbols, punctuation marks, and number literals from bug reports in the tokenization step.  In the stop word removal step they remove the commonly occurring English words such as \I", \you", \we','  etc.  from the bug reports as most of them carry little meaning. In  the  stemming phase they reduce all words to their root form. 

4. **Multi-factor analysis:** Various fields of bug reports are used for comparison including the textual and non-textual contents of bug reports. The goal of the analysis is to characterize a bug report in several dimensions: temporal, textual, author, related-report, severity, and product.

## **Notes**
1. **Motivational Statements:**  Due to system complexity and inadequate testing, many software systems are often released with defects. To address these defects and improve the next releases, developers need to get feedback on defects that are present in released systems. Thus, they often allow users to report such defects using bug reporting systems. Bug reporting is a standard practice in both open source software development and closed source software development. 

2. **Future Work:** Developers can use the tool as a recommender system to prioritize bugs to be fixed. In the future, they plan to integrate the tool to Bugzilla or other open source bug tracking systems to make it easier for developers to adopt solution. It is proposed to include more bug reports from more open source projects to experiment with. They also plan to further improve the accuracy of our approach.

3. **Related Work:** A number of studies try to predict the time it takes to fix a bug. Kim and Whitehead perform an empirical study on the time needed to fix bugs (Kim and Whitehead 2006). Relevant statistics like average bug fixing time, the distribution of bug fixing time, and the files with the highest bug fixing time are reported. Weiß et al. propose an automated approach that predicts the number of developer hours needed to fix a bug by analyzing the time needed to fix similar bugs.

## **Scope of Improvement**
1. The results are based on the bug report database of projects only with more or less structured reporting. The techniques should be applied to other open source as well as proprietary projects to check for its correctness and universal applicability.

