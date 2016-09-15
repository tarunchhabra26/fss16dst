# N. Bettenburg, R. Premraj, T. Zimmermann, and S. Kim. Extracting structural information from bug reports. In MSR ’08: Proceedings of the 2008 international working conference on Mining software repositories, pages 27–30, 2008.

## Keywords 

#### **infoZilla** - A tool called infoZilla detects structural elements from bug reports with near perfect accuracy and allows us to extract them. infoZilla can be used to leverage data from bug reports at a different granularity level that can facilitate interesting research in the future.

####  **Patches** - The common format of a patch is the uniform diff format. Elements that often provide hints at a problem’s cause, come in form of technical entities like stack traces or patches. They represent a small piece of software designed to update or fix problems with a computer program or its supporting data.

#### **Stack Traces Filter** - A stack trace is a record of the execution of a software, showing the sequence of instructions executed up to an occurred crash. Typically stack traces have several well-defined parts as well:the exception, error or assertion that has been violated, an optional exception or error message, a calling stack.

#### **Order of Filters** - The order in which these filters are executed is important since some structural elements interfere. To cope with such interferences, the filter sequence is used.

## Motivation: 
The focus is to correctly identify the presence of enumerations, patches, stack traces, and source code in bug reports. Bug reports typically comprise a problem description in natural language text and often, structural elements such as patches, stack traces and source code.

## Patterns: 
The implementation of infoZilla moves on to its evaluation that entailed manual inspection of 800 ECLIPSE bug reports. It is found that tool comes with very high accuracy, precision, and recall, all very close to perfect. 

## Hypothesis: 
Bug reports typically contain a detailed description of the problem in natural language text, which is used by researchers to automatically assign developers and locations, recognize bug duplicates, and predict correction effort. Occasionally bug reports also hint at the location of the defect in form of stack traces, source code fragments, and patches that we together refer to as elements.

## Future work: 
A tool, infoZilla, is developed that extracts elements from the reports with near perfect accuracy, as demonstrated by evaluation of 800 ECLIPSE bug reports. Access to such piecewise elements from bug reports opens doors to several possibilities for research, for example, assignment of bug reports to developers and detection of duplicates, and more. 
