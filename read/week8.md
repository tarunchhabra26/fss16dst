# **Paper Review: Reading 8**
## **Reading**
Bowen Xu, David Lo, Xin Xia, Ashish Sureka and Shanping Li, EFSPredictor: Predicting Configuration Bugs With Ensemble Feature Selection. Conference: 2015 Asia-Pacific Software Engineering Conference (APSEC), Year: 2015. 

## **Keywords**
1. **Configuration bugs:** Wrong configuration settings of a system can adversely impact system’s availability, performance, and correctness. This has been referred to as configuration bugs. In this paper the researchers have focused on the detection of configuration bugs, and in particular, they follow the line-of-work that tries to predict if a bug report is caused by a wrong configuration setting.

2. **Ensemble Feature Selection:** Feature selection algorithms proposed till now in the machine learning field are based on different heuristics to evaluate the importance of a feature. As heuristics, they may perform better or worse on different problems on a case by case basis. To address this weakness this paper proposes to integrate a multitude of them together to make a comprehensive judgment. It has cited research which argue that ensemble feature selection show promise for high dimensional problem with small sample sizes. The algorithm initially performs the experiment with 5 feature selection algorithms: ChiSquare, Filter, GainRatio, OneR, Relief. Then using statistical models like Naive Bayes  multinomial a prediction model for the features is built. 

3. **Data Mining:** Data mining (sometimes called data or knowledge discovery) is the process of analyzing data from different perspectives and summarizing it into useful information - information that can be used to increase revenue, cuts costs, or both. It allows users to analyze data from many different dimensions or angles, categorize it, and summarize the relationships identified. Technically, data mining is the process of finding correlations or patterns among dozens of fields in large relational databases. 

4. **EFSPredictor:** This algorithm applies ensemble feature selection on the natural-language description of a bug report. It uses different feature selection approaches (e.g., ChiSquare,
GainRatio and Relief) which output different ranked lists of textual features. Then, to obtain a set of representative textual features, EFSPredictor assigns different scores to the features given by these feature selection approaches. Next, for each feature, EFSPredictor sums up the scores outputted by the multiple ranked lists, and outputs the top features as the selected features. After which EFSPredictor builds a prediction model based on the selected features.

## **Notes**
1. **Motivational Statements:**  Through customization of system behaviours via configuration options and through sharing of libraries, registry entries, environment variables and configuration files causes software systems to become complex and hard to set up resulting in various configuration problems. A number of studies show that configuration bugs (i.e., misconfiguration) significantly impact the availability, performance, and correct working of software systems. Misconfigurations can cause crashes, hangs, severe performance degradation, indicating that systems should be better equipped to handle misconfigurations. This will substantially reduce  support time, which contributes 17% of the total cost of ownership of today’s desktop PCs. It can also reduce various availability and performance problems over the internet. Such configuration bugs by API users are also the main factor leading to interaction faults.

2. **Future Work:** Additional bug reports from more projects is to be investigated to reduce threats to external validity. Design of additional solutions can help boost the effectiveness of EFSPredictor.

3. **Related Work:** Xia et al. proposed a text mining technique to predict if a bug
report is due to a misconfiguration. This technique builds on their work by integrating multiple feature selection algorithm i.e. ChiSquare, Filter, GainRatio etc. to produce a set of representative features. Wang et al. presented PeerPressure, which leverages statistical methods to diagnose the root-cause of configuration errors. Yin et al. performed an empirical study on configuration bugs in five
software systems, and they find that most configuration bugs are due to incorrect parameter setting. Zhang and Ernst used static analysis, dynamic profiling, and statistical analysis to detect configuration issues. Xu et al. had proposed a tool SPEX to expose misconfiguration vulnerabilities, and detect error-prone configuration design in software systems

## **Scope of Improvement**
The experiments have been conducted on 5 bug report datasets (i.e., accumulo, activemq, camel, flume, and wicket) containing a total of 3,203 bugs. The experiment results show that, on average across
the 5 projects, EFSPredictor achieves an F1-score to 0.57, which improves the state-of-the-art approach proposed by Xia et al. by 14%. Although this is a significant result, the datasets on which the model has been tested is not sufficiently big and can be improved upon by testing on new datasets such as Amazon EC2 APIs.

## **References**
1.  http://www.anderson.ucla.edu/faculty/jason.frand/teacher/technologies/palace/datamining.htm
