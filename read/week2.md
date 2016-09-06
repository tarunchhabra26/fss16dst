# **Paper Review: Reading 2**
## **Reading**
Chengnian Sun , David Lo , Siau-Cheng Khoo , Jing Jiang, Towards more accurate retrieval of duplicate bug reports. In Proceedings of the 2011 26th IEEE/ACM International Conference on Automated Software Engineering.
## **Keywords**
1.	**Duplicate/Master bug reports:** In large projects when a bug manifests end-user/testers can submit bug reports. However, multiple reports from different submitters may correspond to the same bug report. In this situation the first report of the bug is termed a Master and the later reported instances of the same bug as duplicates.
2.	**BMF25F:** In information retrieval, BM25F is a textual similarity classification algorithm for structured text retrieval. It is composed from several fields (such as headlines, main text, anchor text) with possibly different degrees of importance, term relevance saturation and length normalization.
3.	**Gradient Descent:** Gradient descent is a first-order iterative optimization algorithm. It is used to find a local minimum of a function by taking steps proportional to the negative of the gradient of the function at the current point. For the paper’s BM25F extension approach a stochastic gradient descent technique is used.
4.	**REP:**  REP is the novel technique introduced in this paper to measure the similarity between two bug reports. It uses not only the similarity of textual content in summary and description fields available in a bug report including, but also similarity of non-textual fields such as product, component, version etc. 

## **Notes**
1.	**Motivational Statements:** The complexities of software systems make software bugs quite prevalent. Bug reporting, however, is an uncoordinated distributed process. In a bug tracking system, different testers or users may submit multiple reports on the same bugs, referred to as duplicates, which may cost extra maintenance efforts in tracking and fixing bugs. This causes an issue as different developers should not be assigned the same defect. Therefore detecting duplicate bug reports reduces development time and effort and also correctly points out open or partially open defects.
2.	**Future work:** In future the authors plan to build an indexing structure of bug
report repository to speed up the retrieval process. Along with that they also plan to integrate their technique into the Bugzilla reporting system.
3.	**Study Instruments:** The authors have evaluated their approach on bug report datasets of Mozilla which include subprojects such as Firefox(web-browser), Thunderbird(email client), and Eclipse(Integrated development environment) and Open Office. 
4.	**Baseline Results:** The effectiveness of the BM25F extension is compared against a standard BM25F method. On each dataset, the proposed BM25F-extension performs constantly better than BM25F and it  gains 4%–11%, 7%–13%, 3%–6% and 3%–5% relative improvement over BM25F on Open Office, Mozilla, Eclipse and Large Eclipse datasets respectively. 

## **Scope of Improvement**
1.	The results are based on the bug report database of 4 projects only with more or less structured reporting. The techniques should be applied to other open source as well as proprietary projects to check for its correctness and universal applicability. 

## **References:**
1.	https://en.wikipedia.org/wiki/Okapi_BM25
2.	http://sebastianruder.com/optimizing-gradient-descent/
3.	https://en.wikipedia.org/wiki/Gradient_descent
