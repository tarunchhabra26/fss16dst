# Cloud Infrastructure Optimization
## Team Members
* ### Devika Desai (dndesai@ncsu.edu)
* ### Tarun Chhabra (tchhabr@ncsu.edu)
* ### Sudipto Biswas (sbiswas4@ncsu.edu)

## Date: December 07, 2016

## Abstract 

Cloud computing is one of leading technologies which help deliver scalable computations services in a fault-tolerant and sustainable way. In the past decade SaaS, IaaS and PaaS have changed the way large scale computing used to work. Moreover, while some big organizations have been working towards creating cheaper and reliable public cloud offerings, many have contributed towards private and hybrid cloud configurations. Cost of infrastructure and the massive scale of operations make it hard evaluate performance of such platforms. Simulation studies help fill this gap and with tools like CloudSim. Due to such tools it has become possible to model such environments to optimize different performance, reliability, security and control methodologies. In this project we propose to model multiple cloud datacenters with multiple hosts,VMs and container configurations. Using PSO(Particle Swarm Optimization) we aim to try and find an answer to multi-objective optimization problem in this domain. 

## Introduction 
About CloudSim:
An extensible simulation framework which is generalized in order to enable seamless modelling, simulation and experimentation of emerging cloud computing services and infrastructures. Before actual development of cloud products, controllable methodologies for evaluation of algorithms and policies is required to match the increasing demand of energy efficient IT technologies. By CloudSim, researchers and industry-based developers can take care of system design issues without the concerns of issues related to cloud based infrastructure. So, by utilization of simulation tools, hypothesis can be evaluated prior to software development.

In large data centers energy and resource consumption grows rapidly. Energy and resource aware computing are key challenges of cloud datacenters, which  deal with computing, storage and communication resources. Minimization of energy consumption is achieved through increased resource utilization. Typically, such large scale data centers are concerned with the following four objectives: 

1. Energy usage optimization 
2. Reduced execution time 
3. Reduced execution time
4. Reduced execution time 

The source of inspiration of these problems have been primarily from [1],[2]. 

## Background 
Cloud computing is a fast growing area in computing research and industry today. With the advancement of the Cloud, there are new possibilities opening up on how applications can be built on the Internet. On one hand there are the cloud service providers who are willing to provide large scaled computing infrastructure at a cheaper price which is often defined on usage, eliminating the high initial cost of setting up an application deployment environment, and provide the infrastructure services in a very flexible manner which the users can scale up or down at will. On the other hand there are large scaled software systems such as social networking sites and e-commerce applications gaining popularity today which can benefit greatly by using such cloud services to minimize costs and improve service quality to the end users. But when bringing these two ends together there are several factors that will impact the net benefit such as the distribution (geographic) of the user bases, the available Internet infrastructure within those geographic areas, the dynamic nature of the usage patterns of the user base and how well the cloud services can adapt or dynamically reconfigure itself, etc. Doing a comprehensive study on this overall problem in the real world will be extremely difficult, and the best approach to study such a dynamic and massively distributed environment is through simulation. 

Following Figure. 1 depicts the flow of communication among core CloudSim entities. In the beginning of the simulation, each Datacenter entity registers itself with the CIS (Cloud Information Service) Registry. Brokers acting on behalf of users consult the CIS service about the list of Clouds who offer infrastructure services matching user’s application requirements. In case the match occurs the broker deploys the application with the Cloud that was suggested by the CIS. 

 
![Cloud Model](/pproject/report/Model.png)

