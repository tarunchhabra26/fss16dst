# Anh Tuan Nguyen, Tung Thanh Nguyen, Tien N. Nguyen, David Lo, Chengnian Sun. 2012. Duplicate Bug Report Detection with a Combination of Information Retrieval and Topic Modeling. Automated Software Engineering (ASE), 2012 Proceedings of the 27th IEEE/ACM International Conference.

## Keywords 

#### ii1 Duplicate Bug Reports - Duplicate bug report is a report  that has description of such technical issues of a system that are already encountered in a previous report. The technical issues are the same but with different defining terms.

#### ii2 Topic Model - A topic model is a type of statistical model for analyzing the abstract topics that occur in a set of documents. Topic modeling is frequently used as a text-mining tool for discovery of hidden semantic structures in a text body.

#### ii3 Information Retrieval - Information retrieval is a process of gathering information from the information resources. It is an approach also used in detecting whether the bug report is new or duplicate.

#### ii4 DBTM - Duplicate bug report topic model is introduced in this paper, which uses both the information retrieval and topic search algorithms to detect a duplicate bug report more accurately. IT is designed to address textual dissimilarity between two duplicate reports.

## iii1 Motivation: There are users of a system, interacting with the system and encountering issues in it. The user submits a bug report describing the problems he encounters. There are times when other user encounters a similar problem in the same technical function, reports the error in a different context or by giving a detailed description on the code. This can result in text dissimilarity of natural language but technical issue remains the same. Topics are invisible and semantic features, while terms are visible and textual features of the duplicate report.

## iii2 Patterns: Reporters might discuss other relevant topics and phenomena, and provide the insights on the bug including suggested fixes and relevant technical functions. It is indicated from the observation that the detection of duplicate bug reports could rely on the technical topics in the reports as well.

## iii3 Hypotheses: If duplicate bug reports is detected properly, it helps save time for developers in fixing the same issues and reduce some triaging efforts.

## iii4 Scope of improvement: Potential buggy files can be categorized. A set of technical and textual context can be created from the original bug report and all the duplicate ones should be compared to that rather than comparing two error reports overtime. A prior knowledge of software quality, software architecture and system development can help improve the bug duplication when the combination of information retrieval tools and topic modeling is used to detect duplicate reports. Also, there is no comparison
 with T-model for Duplicate bug report and BM25F model for textual similarity measure in terms of accuracy.

