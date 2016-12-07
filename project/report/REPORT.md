# Cloud Infrastructure Optimization
## Team Members
* Devika Desai (dndesai@ncsu.edu)
* Tarun Chhabra (tchhabr@ncsu.edu)
* sudipto Biswas (sbiswas4@ncsu.edu)

## Date: December 07, 2016

## Abstract 

In this project we modeled a cloud based datacenters with multiple hosts,VMs with varying hardware and power aware configurations using CloudSim library. The aim of the project was to optimize a power aware datacenter by varying decisions of VM allocation, selection algoriths and hardware configurations. In order to find solutiong to the optimization problem we used [SMPSO](http://jmetal.sourceforge.net/smpso.html)(Spread Measured Particle Swarm Optimization), [NSGAII](http://ieeexplore.ieee.org/iel5/4235/21497/00996017.pdf) and [MOEAD](http://ieeexplore.ieee.org/iel5/4235/4358751/04358754.pdf) algorithms. Not only did we aim to try and find an answer to multi-objective optimization problem in this domain, we also tried to compare the outcomes of these algorithm for the given problem[.


## Introduction
Cloud computing is one of leading technologies which help deliver scalable computations services in a fault-tolerant and sustainable way. In the past decade SaaS, IaaS and PaaS have changed the way large scale computing used to work. Moreover, while some big organizations have been working towards creating cheaper and reliable public cloud offerings, many have contributed towards private and hybrid cloud configurations. Cost of infrastructure and the massive scale of operations make it hard evaluate performance of such platforms. Simulation studies help fill this gap and with tools like CloudSim. Due to such tools it has become possible to model such environments to optimize different performance, reliability, security and control methodologies. We used [CloudSim](http://www.cloudbus.org/cloudsim/) to generate our power aware datacenter model.

### About CloudSim:
An extensible simulation framework which is generalized in order to enable seamless modelling, simulation and experimentation of emerging cloud computing services and infrastructures. Before actual development of cloud products, controllable methodologies for evaluation of algorithms and policies is required to match the increasing demand of energy efficient IT technologies. By CloudSim, researchers and industry-based developers can take care of system design issues without the concerns of issues related to cloud based infrastructure. So, by utilization of simulation tools, hypothesis can be evaluated prior to software development.

In large data centers energy and resource consumption grows rapidly. Energy and resource aware computing are key challenges of cloud datacenters, which  deal with computing, storage and communication resources. Minimization of energy consumption is achieved through increased resource utilization. Typically, such large scale data centers are concerned with the following four objectives: 

1. Energy usage optimization 
2. Reduction of execution time 
3. Maximum utilization of resources
4. Optimize task scheduling 

The source of inspiration of our problem has been primarily from [1],[2]. 
 
### Background 
Cloud computing is a fast growing area in computing research and industry today. With the advancement of the Cloud, there are new possibilities opening up on how applications can be built on the Internet. On one hand there are the cloud service providers who are willing to provide large scaled computing infrastructure at a cheaper price which is often defined on usage, eliminating the high initial cost of setting up an application deployment environment, and provide the infrastructure services in a very flexible manner which the users can scale up or down at will. On the other hand there are large scaled software systems such as social networking sites and e-commerce applications gaining popularity today which can benefit greatly by using such cloud services to minimize costs and improve service quality to the end users. But when bringing these two ends together there are several factors that will impact the net benefit such as the distribution (geographic) of the user bases, the available Internet infrastructure within those geographic areas, the dynamic nature of the usage patterns of the user base and how well the cloud services can adapt or dynamically reconfigure itself, etc. Doing a comprehensive study on this overall problem in the real world will be extremely difficult, and the best approach to study such a dynamic and massively distributed environment is through simulation. 

Following Figure. 1 depicts the flow of communication among core CloudSim entities. In the beginning of the simulation, each Datacenter entity registers itself with the CIS (Cloud Information Service) Registry. Brokers acting on behalf of users consult the CIS service about the list of Clouds who offer infrastructure services matching user’s application requirements. In case the match occurs the broker deploys the application with the Cloud that was suggested by the CIS. 

![](/project/report/Model.png?) 

Figure 1: Cloud Model 

## Related Work 
The Cloud computing has become the fast spread in the field of computing, research and industry in the last few years. As part of the service offered, there are new possibilities to build applications and provide various services to the end user by virtualization through the internet. Task scheduling is the most significant matter in the cloud computing because the user has to pay for resource using on the basis of time, which acts to distribute the load evenly among the system resources by maximizing utilization and reducing task execution Time. Many heuristic algorithms have been existed to resolve the task scheduling problem such as a Particle Swarm Optimization algorithm (PSO), Genetic Algorithm (GA), Ant Colony Optimization (ACO) and Cuckoo search (CS) algorithms, etc. A Dynamic Adaptive Particle Swarm Optimization algorithm (DAPSO) has been implemented to enhance the performance of the basic PSO algorithm to optimize the task runtime by minimizing the makespan of a particular task set, and in the same time, maximizing resource utilization. Also, .a task scheduling algorithm has been proposed to schedule the independent task over the Cloud Computing. The algorithm is considered an amalgamation of the Dynamic PSO (DAPSO) algorithm and the Cuckoo search (CS) algorithm; called MDAPSO. According to the experimental results, it is found that MDAPSO and DAPSO algorithms outperform the original PSO algorithm. Also, a comparative study has been done to evaluate the performance of the proposed MDAPSO with respect to the original PSO[3]. 
In [5] proposed a PSO algorithm to schedule jobs that are targeted at paid Clouds, i.e., those that charge users for CPU, storage and network usage, to minimize mon- etary cost. The algorithm considers both job computation costs and job data transfer costs. Moreover, this approach is based on static resource allocation, which forces users to feed the scheduler with the estimated running times of jobs on the set of Cloud re- sources to be used. Another relevant approaches are [6,7]. In [6] the authors propose a PSO algorithm to solve the problem of load balancing in VMs. The goal of this work was to minimize the execution time of the jobs. In the work [7] an improved PSO is proposed to reduce job average execution time and increase the rate availability of resources. Finally, in [9] the authors propose a novel self-adaptive Particle Swarm Optimization scheduler to map efficiently a set of VM instances onto a set of Cloud physical resources and reduce energy consumption. Indeed, energy consumption has become a crucial problem [8], on one hand because it has started to limit further performance growth due to expensive electricity bills, and also by the environmental impact in terms of carbon dioxide (CO2) emissions caused by high energy consumption. 
Another relevant approaches, but based on ACO, are the works in [10,2]. In [10], the authors propose a scheduler to compute the placement of VMs according to the cur- rent load of the physical resources and minimize the energy consumption. The authors claim that, from the business perspective, reducing the energy consumption can lead to immense cost reductions. Moreover, the higher power consumption, the higher heat dissipation, and therefore the probability of hardware failures increases. In [11] the authors have proposed ACO-based Cloud schedulers for mapping jobs-VMs. The goal was to minimize makespan and maximize load balancing, respectively. Makespan is the maximum execution time of a set of jobs. Flowtime is the sum of job finish times minus job arrive times of a set of jobs. An interesting aspect of [11] is that it was evaluated using real Cloud platforms (Google App Engine and Microsoft Live Mesh), whereas the other work was evaluated through simulations. However, during the experiments, [11] used only 25 jobs and a Cloud comprising 5 machines. 
  
## Problem 
Data centers are the backbone of the modern economy, from the server rooms that power small- to medium-sized organizations, to the enterprise data centers that support american corporations, to the server farms that run cloud computing services hosted by amazon, Facebook, Google, and others. However, the explosion of digital content, big data, e-commerce, and Internet traffic is also making data centers one of the fastest-growing users of electricity in developed countries, and one of the key drivers in the construction of new power plants in the united states. 
While most media and public attention focuses on the largest data centers that power so-called cloud computing operations—companies that provide web-based and other Internet services to consumers and businesses—these hyper-scale cloud computing data centers represent only a small fraction of data center energy consumption in the united states. 
as NrDC initially found in its groundbreaking 2012 analysis, Is Cloud Computing Always Greener? Finding the Most Energy and Carbon Efficient Information Technology Solutions for Small- and Medium-Sized Organizations, smaller server rooms and closets are responsible for about half of all U.S. server electricity consumption—but 50 percent of that is wasted due to lack of awareness and incentives to make them more efficient. There remains a critical need for action, including developing utility incentive programs to reduce waste in the massive amounts of electricity used by data centers small and large. 
In 2013, u.s. data centers consumed an estimated 91 billion kilowatt-hours of electricity. This is the equivalent annual output of 34 large (500-megawatt) coal- red power plants, enough electricity to power all the households in New York City twice over. Data center electricity consumption is projected to increase to roughly 140 billion kilowatt-hours annually by 2020, the equivalent annual output of 50 power plants, costing american businesses 
$13 billion per year in electricity bills and causing the emission of nearly 150 million metric tons of carbon pollution annually.1 
If just half of the technical savings potential for data center effciency were realized (to take into account the market barriers discussed in this report), electricity consumption in u.s. data centers could be cut by as much as 40 percent. In 2014, this represents a **savings of 39 billion kilowatt-hours annually**, equivalent to the annual electricity consumption of all the households in the state of Michigan. __Such improvement would save U.S. businesses $3.8 billion a year.__

### Difference between our problem and related work
In the related work we can see that most of the authors have tried to optimize the load balancing at broker level of a cloud infrastructure. Those works aim to provide a deterministic cum heuristicially adaptive algorithms which compute and adapt the most power aware workflow and load for a datacenter. All these works have compared their performances on different loads and experimental settings. However, if these algorithms and hardware are varied it is hard to determine which combination of algorithm and hardware would lead to the best results. Our, problem aims to answer this question.

### Assumption
Due to runtime constraints and challenges we were able to solve the problem for upto 100 hosts. Many application and commercial clouds currently operate in such configurations also. Hence, the results cannot be completely ignored. However, they do not fully mimic a large public cloud as the variances in outputs may grow with more machines being added to it. Since, this study is a very early attempt towards such a problem we encourage more extensive results to come up in future studies.

## Implementation 
Cloudsim model:
CloudSim is a framework for modeling and simulation of cloud computing infrastructures and services.
* Clouds enable platform for dynamic and flexible application provisioning by exposing data center’s capabilities as a network of virtual services. 
So users can access and deploy applications from anywhere in the Internet driven by demand and QoS requirements.  
* So users can access and deploy applications from anywhere in the Internet driven by demand and QoS requirements. 
* So users can access and deploy applications from anywhere in the Internet driven by demand and QoS requirements.  
* Main contribution: A holistic software framework for modeling Cloud computing environments and performance testing application services.
* We were able to simulate an entire power-aware datacenter using this framework.

## Allocation and Selection Algorithms 
In the next sections we will discuss the algorithm for detection of overloaded host, the selection algorithm that will pick the VMs to migrate from one host to the other, in CloudSim. Finally, modified techniques that we use for VM placement are discussed. 
  
### VM allocation
In order to decide the time to initiate the migration of VMs from a host, a heuristic for setting an upper and lower utilization threshold was first proposed by Beloglazov and Buyya [12]. But due to unpredictable and dynamic workload, a fixed value of utilization threshold was not suitable. Therefore, in the later work [13] the authors proposed an auto adjustment technique of utilization threshold based on statistical analysis of previous data which was gathered during the lifetime of VMs. The main idea of his heuristic was to adjust the upper bound considering the deviation of CPU utilization. Four overload detection techniques proposed in [13] are discussed below: 
* Median Absolute Deviation (MAD): For adjusting upper bound a statistical dispersion like MAD is used. The reason behind choosing MAD over standard deviation is that MAD is not heavily influenced by the outliers, so the magnitude of the distances of outliers is irrelevant. 
* Interquartile Range (IQR): This could be said as the second method for setting an adaptive upper threshold. For symmetric distribution half of IQR is equal to MAD. 
* Local Regression (LR): LR builds a curve that approximates original data by setting up the sample data models to localized subset of data. 
* Robust Local Regression (LRR): The local regression version was vulnerable to outliers that could be caused by heavy tailed distribution. In order to make a robust solution modification was proposed by adding the robust estimation method called bi-square which transformed LR onto an iterative method. 
More detail descriptions of these host overload detection algorithms could be found in [13].

### VM selection 
After finding out an overloaded host, the next step is to select the particular VMs to migrate from one host to the other. In this section, we will discuss about three VM selection policies that we used in our work. 
* Minimum migration time (MMT): This policy selects a VM to migrate that requires minimum amount of time to finish migrating, compared to other VMs allocated to the host. 
* Random Choice Policy (RC): This policy selects a VM that needs to be migrated according to a uniformly distributed discrete random variable Xd = U(0,|Vj|), whose values index a set of VMs Vj allocated to a host j. More details about RC is given in [13]. 
* Maximum Correlation policy (MC): According to the proposal of Verma et al. [14], the higher the correlation between the resource usage by applications running on an over subscript server, the higher the probability of the server being overloaded. Based on this idea Beloglazov and Buyya [13] selected VMs which are needed to be migrated in such a way that VMs with highest correlation of the CPU utilization with other VMs are considered first. To estimate correlation, multiple correlation coefficients were applied. 
* Random Selection(RS): Randomly selects any of the given policies described above.

## Decisions 
Our model had the following decision variances
1.	**Number of hosts** : 1 - 100
2.	**Number of Vms** 1 - 200 or 400
3.	**VM Types**  2, 4 (whether each host has 2 or 4 vms)
4.	**Host Types** 2, 4 (single or dual/quad)
5.	**VM Allocation Policy** iqr,lr,lrr,mad,thr
6.	**VM Selection Policy** mc,mmt,mu,rs 
7.	**Utilization threshold** 0.8 - 2.5 (Specific parameters for selection policies)
8.	**VM PES** {1,1}, {2,2,2,2} (based on the dual core or quad-core architecture selection)
9.	**VM MIPS** {2500, 100} ,{2500, 2000, 100, 500} (based on the dual core or quad-core architecture selection)
10.	**VM RAM** { 870,  1740}, { 870,  1740, 1740, 613 } MB (based on the dual core or quad-core architecture selection)
11.	**VM Bandwidth** 100000 to 200000 (100 Mbit/s to 200 Mbit/s)
12.	**Host PES** {2,2} , {2,2,4,4} (based on the dual core or quad-core architecture selection)
13.	**Host MIPS** { 1860, 2660} , { 1860, 2660, 5000, 6000 } (based on the dual core or quad-core architecture selection)
14.	**Host RAM** { 4096, 4096},{ 4096, 4096, 8192,8192 } MB (based on the dual core or quad-core architecture selection)
15.	**Host Bandwidth** 500000 - 1000000 (500 Mbit/s to 1 Gbit/s)
16.	**Host storage** 1000000 - 2000000 (1-2 GB)
  
### Runs
Each run of CloudSim model used to mimic 6 hours of actualy datacenter run. Hence, SLA has also been computed accordingly. 
In average case each run used to take about **30 seconds**. In worst case a single run could take upto **2 minutes and 30 seconds**.
It was quite challenging to stabalize and optimize such a complicated model. 

The code base and instructions to run could be access from [here](https://github.com/tarunchhabra26/fss16dst/tree/master/project)

Every run used to compute suh values :

```
New resource usage for the time frame starting at 5000.10:

5000.10: [Host #0] Total allocated MIPS for VM #49 (Host #0) is 12.28, was requested 12.28 out of total 100.00 (12.28%)
5000.10: [Host #0] MIPS for VM #49 by PEs (2 * 1860.0). PE #0: 12.28.
5000.10: [Host #0] Total allocated MIPS for VM #74 (Host #0) is 10.86, was requested 10.86 out of total 100.00 (10.86%)
5000.10: [Host #0] MIPS for VM #74 by PEs (2 * 1860.0). PE #0: 10.86.
5000.10: [Host #0] utilization is 0.62%

5000.10: [Host #1] Total allocated MIPS for VM #0 (Host #1) is 601.34, was requested 601.34 out of total 2500.00 (24.05%)
5000.10: [Host #1] MIPS for VM #0 by PEs (2 * 5000.0). PE #0: 601.34.
5000.10: [Host #1] Total allocated MIPS for VM #24 (Host #1) is 2210.45, was requested 2210.45 out of total 2500.00 (88.42%)
5000.10: [Host #1] MIPS for VM #24 by PEs (2 * 5000.0). PE #0: 2015.54. PE #1: 194.91.
5000.10: [Host #1] Total allocated MIPS for VM #48 (Host #1) is 2383.12, was requested 2383.12 out of total 2500.00 (95.32%)
5000.10: [Host #1] MIPS for VM #48 by PEs (2 * 5000.0). PE #0: 2383.12.
5000.10: [Host #1] utilization is 51.95%

5000.10: [Host #2] Total allocated MIPS for VM #50 (Host #2) is 61.42, was requested 61.42 out of total 100.00 (61.42%)
5000.10: [Host #2] MIPS for VM #50 by PEs (2 * 1860.0). PE #0: 61.42.
5000.10: [Host #2] Total allocated MIPS for VM #75 (Host #2) is 27.82, was requested 27.82 out of total 100.00 (27.82%)
5000.10: [Host #2] MIPS for VM #75 by PEs (2 * 1860.0). PE #0: 27.82.
5000.10: [Host #2] utilization is 2.40%
........
```
The final output of the runs was as follows :

```
Simulation: Reached termination time.
CloudInformationService: Notify all CloudSim entities for shutting down.
Broker is shutting down...
Datacenter is shutting down...
Simulation completed.
Received 0 cloudlets
Simulation completed.

Experiment name: random_lr_mu_1.393674679793466
Number of hosts: 49
Number of VMs: 97
Total simulation time: 21600.00 sec
Energy consumption: 8.57 kWh
Number of VM migrations: 121
SLA: 0.00006%
SLA perf degradation due to migration: 0.01%
SLA time per active host: 0.78%
Overall SLA violation: 0.01%
Average SLA violation: 10.00%
Number of host shutdowns: 35
Mean time before a host shutdown: 7032.09 sec
StDev time before a host shutdown: 3472.58 sec
Mean time before a VM migration: 28.16 sec
StDev time before a VM migration: 6.86 sec
Execution time - VM selection mean: 0.00025 sec
Execution time - VM selection stDev: 0.00050 sec
Execution time - host selection mean: 0.00075 sec
Execution time - host selection stDev: 0.00150 sec
Execution time - VM reallocation mean: 0.01400 sec
Execution time - VM reallocation stDev: 0.02078 sec
Execution time - total mean: 0.05175 sec
Execution time - total stDev: 0.04378 sec


Total simulation time : 1936 ms
```

We then used [jMetal](http://jmetal.sourceforge.net/) as our libarary to run and configure our optimizers. The pareto fronts generated by each algorithm were then used to generate a reference pareto front. All the results were then computed using that reference pareto front.

## Objectives 
1.	Energy consumption kWh(minimize) - As our main goal was to achieve most power aware configuration, minimizing energy consumption was one of our primary goals.

2.	Average SLA violation %(minimize) - Although we wanted our implementation to utilize minimum power we did not expect it to violate SLA more that 0.1%.

3.	Mean time before host shutdown seconds(maximize) -  This goal was added to make sure that maximum unitizilation of each resource happens.

 
## Results 
### 1.	Overall ranking:   

It has been tough to make an overall ranking. If we look at the statistics then the overall best algorithm for our problem is (1)MOEAD. The results were quite well however, it wasn't the best algorithm in terms for spread. (2)NSGAII was consistently and undoubltly second in the overall aspects. (3) SMPSO was last in this race but it still produced some really good results for the problem. Although it was very slow, it was the best algorithm in terms of spread.
   
### 2. Statistics:    

#### Spread:
SMPSO had the best spread out of all the algorithms.

![](/project/report/SPREAD. Mean and Standard Deviation .png) 

Figure 3: SPREAD. Mean and Standard Deviation 


![](/project/report/SPREAD. Median and Interquartile Range.png) 

Figure 4: SPREAD. Median and Interquartile Range 


![](/project/report/HyperVolume. Mean and Standard Deviation.png) 

Figure 5: HyperVolume. Mean and Standard Deviation  


![](/project/report/HyperVolume. Median and Interquartile Range.png) 

Figure 6: HyperVolume. Median and Interquartile Range 


![](/project/report/IGD. Mean and Standard Deviation.png) 

Figure 7: IGD. Mean and Standard Deviation 


![](/project/report/IGD. Median and Interquartile Range.png) 

Figure 8: IGD. Median and Interquartile Range 


## Challenges 
*	Long runtimes for high number of hosts and VMs
*	Choice of algorithms 
*	Best algorithm depends on the choice of models 

## Future Work 
*	Parallel execution
*	Comparisons using more algorithms(DE, GA, SPEA2 etc.)
*	With speed up more variance can be added. 

## Conclusion: 

## Acknowledgement: 
We earnestly thank course instructor Dr. Tim Menzies, and teaching assistant George Mathew for giving us valuable advice in implementing the project.  

##References  
[1] Lee, Young Choon, and Albert Y. Zomaya. "Energy efficient utilization of resources in cloud computing systems." The Journal of Supercomputing 60.2 (2012): 268-280.  

[2] Wang, Zhiming, et al. "Energy-aware and revenue-enhancing Combinatorial Scheduling in Virtualized of Cloud Datacenter." JCIT 7.1 (2012): 62-70.  

[3] P. -Y. Yin, S. -S. Yu, P. -P. Wang and Y. -T. Wang, "A hybrid particle swarm optimization algorithm for optimal task assignment in distributed systems”, Computer Standards & Interfaces, vol. 28, (2006), pp. 441-450.   

[4] Yan Gao-wei,Hao Zhanju, A Novel Atmosphere Clouds Model Optimization Algorithm, International Conference on Computing, Measurement, Control and Sensor Network,2012,ISBN: 978-1-4673-2033-7,Pg 217.   

[5] Pandey, S., Wu, L., Guru, S., Buyya, R.: A particle swarm optimization-based heuristic for scheduling workflow applications in Cloud Computing environments. In: International Con- ference on Advanced Information Networking and Applications. pp. 400–407. IEEE Computer Society (2010)   

[6] Liu, Z., Wang, X.: A pso-based algorithm for load balancing in virtual machines of cloud computing environment. In: et al., Y.T. (ed.) Advances in Swarm Intelligence, Lecture Notes in Computer Science, vol. 7331, pp. 142–147. Springer Berlin Heidelberg (2012)  

[7] Zhan, S., Huo, H.: Improved PSO-based Task Scheduling Algorithm in Cloud Computing. Journal of Information & Computational Science 9(13), 3821–3829 (2012)  

[8] Liu, Y., Zhu, H.: A survey of the research on power management techniques for high-performance systems. Software Practice & Experience 40(11), 943–964 (October 2010)  

[9] Jeyarani,R.,Nagaveni,N.,VasanthRam,R.:Designandimplementationofadaptivepower-aware virtual machine provisioner (APA-VMP) using swarm intelligence. Future Generation Computer Systems 28(5), 811–821 (2012)   

[10] Feller, E., Rilling, L., Morin, C.: Energy-Aware Ant Colony Based Workload Placement in Clouds. In: 12th International Conference on Grid Computing. pp. 26–33. No. 8 in Grid ’11, IEEE Computer Society (2011)  

[11] Banerjee, S., Mukherjee, I., Mahanti, P.: Cloud Computing initiative using modified ant colony framework. In: World Academy of Science, Engineering and Technology. pp. 221– 224. WASET (2009)   

[12] Beloglazov A, Abawajy J, Buyya R (2011) Energy-aware resource allocation heuristics for efficient management of data centers for cloud computing. Future Generat Comput Syst. doi:10.1016/j.future.2011.04.017  

[13] Beloglazov A, Buyya R (2012) Optimal online deterministic algorithms and adaptive heuristics for energy and performance efficient dynamic consolidation of virtual machines in Cloud data centers. Concurrency Computat. Pract Exper 24:1397–1420. doi:10.1002/cpe.1867  

[14] Verma A, Dasgupta G, Nayak TK, De P, Kothari R (2009) Server workload analysis for power minimization using consolidation. Proceedings of the 2009 USENIX Annual Technical Conference, San Diego, CA, USA, pp 28–28  
