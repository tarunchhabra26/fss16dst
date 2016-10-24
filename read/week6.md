# **Paper Review: Reading 6**
## **Reading**
Ferdian Thung, Pavneet Singh Kochhar, and David Lo, DupFinder: Integrated Tool Support for Duplicate Bug Report Detection. ASE '14 Proceedings of the 29th ACM/IEEE 
international conference on Automated software engineering.
## **Keywords**
1. **Vector space model:** Vector space model is an algebraic model for representing text documents or any objects as vectors of identifiers. It can be divided in to three stages. The first stage is the document indexing where content bearing terms are extracted from the document text. The second stage is the weighting of the indexed terms to enhance retrieval of document relevant to the user. The last stage ranks the document with respect to the query according to a similarity measure. It is used in information filtering, information retrieval, indexing and relevancy rankings. The paper cites Runeson  et  al.'s proposal of  an  unsupervised  technique that takes a new bug report and returns a ranked list of top-k most similar reports to help detect duplicate reports. Being an unsupervised technique, Runeson et al.'s approach does  not  require  any  training  data  and  thus  can  be  used for any bug tracking systems even those with a small number of bug reports. 

2. **Text Preprocessing:** Preprocessing is an important task and critical step in Text mining, Natural Language Processing (NLP) and information retrieval (IR). In the area of Text Mining, data preprocessing used for extracting interesting and non-trivial and knowledge from unstructured text data.There are three common text preprocessing  steps:  tokenization,  stop  word  removal,  and stemming.   At  the  end  of  these  steps,  each  bug  report  is represented as a bag (i.e., multiset) of words. The authors remove special symbols, punctuation marks, and number literals from bug reports in the tokenization step.  In the stop word removal step they remove the commonly occurring English words such as \I", \you", \we','  etc.  from the bug reports as most of them carry little meaning. In  the  stemming phase they reduce all words to their root form. 

3. **Representation and Similarity:** With the help of this approach the weight of each word is usually computed using the product of its term frequency  and  its  inverse  document  frequency,  following  the standard tf-idf weighting scheme. 

4. **DupFinder** DupFinder, which implements the state-of-the-art unsupervised duplicate bug report approach by Runeson et al., as a Bugzilla extension. DupFinder does not require any  training  data  and  thus  can  easily  be  deployed  to  any project.   DupFinder  extracts  texts  from  summary  and  description fields of a new bug report and recent bug reports present in a bug tracking system, uses vector space model to measure similarity of bug reports, and provides developers with a list of potential duplicate bug reports based on the similarity of these reports with the new bug report. 

5. **Unsupervised learning:** Unsupervised learning is the task of inferring a function to describe hidden structure from unlabeled data. Unsupervised learning encompasses many techniques that seek to summarize and explain key features of the data, which is why it is a good fit for finding duplicate bug report.

## **Notes**
1. **Motivational Statements:**  Bug reporting is inherently an uncoordinated  distributed  process. This gives rise to a number of duplicate bug reports. Even though there are a number of unsupervised machine learning approcahes to find such duplicate reports, DupFinder actually integrates one of those (Runeson et al's) approach to provide a list of potential duplicates. The goal of this paper is not to design a new algorithm but rather to implement an existing technique into a tool integrated to a bug tracking system that can be used by practitioners to help them deal with duplicate bug report problem.  

2. **Future Work:** One of the major areas of enhancement in the future for DupFinder will be the implementation of supervised duplicate bug reportdetection techniques along with the current unsupervised techniques.

3. **Related Work:** Sureka and Jalote proposed a novel technique which uses N-gram  based  model  to  detect  duplicate  bug  reports  and evaluate  their  technique  on  bug  reports  from  Eclipse. Wang et al.  extend the work by Runeson et al.  to consider execution traces and show that by considering execution traces, duplicate bug report can be identi ed more accurately. Their techniques have never been compared against a common dataset and thus it is unclear which technique is the best performing one. 

## **Scope of Improvement**
1. DupFinder only applies a single unsupervised learning algorithm propsed by Runeson et al. to find duplicate bug reports. Other unsupervised as well as supervised learning approaches should be incorporated for wider applicability.


## **References**
1. http://cogsys.imm.dtu.dk/thor/projects/multimedia/textmining/node5.html
2. https://en.wikipedia.org/wiki/Vector_space_model
3. https://www.researchgate.net/publication/273127322_Preprocessing_Techniques_for_Text_Mining
