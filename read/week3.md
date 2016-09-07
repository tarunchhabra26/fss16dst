# **Paper Review: Reading 3**
## **Reading**
Chengnian Sun, David Lo, Xiaoyin Wang, Jing Jiang, Siau-Cheng Khoo, A Discriminative Model Approach for Accurate Duplicate
Bug Report Retrieval. In Proceedings of ICSE '10 Proceedings of the 32nd ACM/IEEE International Conference on Software Engineering - Volume 1.
## **Keywords**
1.	**Discriminative model:** Unlike some approaches that rank similar bug reports based on similarity score of vector space representation,we develop a discriminative model to retrieve similar bug reports from a bug repository. Authors make use of the recent advances in information retrieval community that uses a classifier to retrieve similar documents from a collection. A new model has been suggested which contrasts duplicate bug reports from non-duplicate bug reports and utilize this model to extract similar bug reports, given a query bug report under consideration.
2.	**Information retrieval (IR):** This approach aims to extract useful information from unstructured data. Most of such data is expressed in natural language. The data is treated like a document which has a collection of words which is represented in high-dimension vector space where each dimension corresponds to a unique word or term.
3. **Pre-processing:** In this technique the document undergoes process of tokenization, stemming and stop word removal using natural language techniques. The purpose behind doing this is to find words which belong to the same root.
4. **Term Frequency-Inverse Document Frequency (TF-IDF):** It is a stistical approach to evaluating the importance of a term in a corpus
5. **Support Vector Machine (SVM):** It is an approach to build a discriminative model based on a set of labeled vectors. Based on positive class and negative class panes, SVM tries to build a hyperplane which finds the difference between the two planes with least margins. The paper used libsvm library to do so.

## **Notes**
1. **Motivational Statements:** Despite the benefits of a bug reporting system, it does cause some challenges. As bug reporting process is often uncoordinated and ad-hoc, often the same bugs could bereported more than once by different users. Hence, there is often a need for manual inspection to detect whether the bug has been reported before. 
2. **Future Work:** Future work of this paper is a plan to investigate the utility ofparaphrases in discriminative models for potential improvement in accuracy.
3. **Baseline Results:** The peresented approach outperforms existing techniques by a relative improvement of 17–31%, 22–26%, and 35–43% on OpenOffice, Firefox, and Eclipse dataset respectively
## **Scope of Improvement**
1.	The results are based on the bug report database of 3 projects only with more or less structured reporting. The techniques should be applied to other open source as well as proprietary projects to check for its correctness and universal applicability. 
