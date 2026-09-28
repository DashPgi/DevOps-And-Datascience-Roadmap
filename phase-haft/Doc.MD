# Cloud Principles

### Elasticity

Change volume based on consumption of resources

### Self Service

User have all access to  manage all config without need for assistance from a third party

### Scalability

User can handle all workloads by adding or removing resources

### Board Network Access

User have an access in everytime and everywhere

### Pay As You Go

User paying just for the used resources

### Availability

User have access services all 24/7 without any problem or issues

# Cloud Computing Models

### 1. SaaS

#### Software as a Service

Installed are necessary software and tools
ForExample :

* Microsoft-Tools
* Chrome
* Google-Driver

### 2. IaaS

#### Infrastructure as a Service

Installed and Configured infrastructures
ForExmaple :

* Azure
* Aws
* Server
* Storage

### 3. XaaS

#### Anything as a Service

Have any service and tools
ForExample :

* DaaS
* MlaaS

### 4. PaaS

#### Platform as a Service

Delivered all platform , tools and software for developers
ForExample :

* Manage code
* Run code

# Cloud Deployment Models

### Public CDM

A cloud computing service that is owned and operated by third party provider and made available to the public over the intrenet **(somtimes only user and providers have an accesss btw)**\
ForExmaple :

* AWS
* Azure
* GCP

### Private CDM

A cloud computing service that is owned and operated by single organization for privatly use **(No one have an access except for user)**
ForExample :

* IBM
* Azure Stack
* Open Stack
* Oracle
* Vmware

### Hybrid CDM

A Combination of public and private cloud service

### Community CDM

A cloud computing service where infrastructure and services are shared by a group or something like that

### Multi-Tenancy CDM

A cloud computing service where multiple customers share the same infrastructure and resources

### Single-Tenancy CDM

A cloud computing service where the customer has own dedicated infrastructure and resources

## Access Level Management

Who-manage? | On-site | IaaS | PaaS | SaaS |
\---|----|-----|-----|---
Appliction |You-Manage |You-Manage|You-Manage|Sp-Manage
Data | You-Manage | You-Manage| You-Manage | Sp-Manage
Runtime | You-Manage | You-Manage | Sp-Manage | Sp-Manage
Middleware | You-Manage | You-Manage | Sp-Manage|Sp-Manage
O/S | You-Manage | You-Manage | Sp-Manage | Sp-Manage
Virtualization | You-Manage | Sp-Manage | Sp-Manage | Sp-Manage
Servers | You-Manage | Sp-Manage | Sp-Manage |Sp-Manage
Storage | You-Manage | Sp-Manage | Sp-Manage |Sp-Manage
Networking | You-Manage | Sp-Manage | Sp-Manage |Sp-Manage

# Scalling

A Scalling is the process of increasing or decreasing the resources of a cloud system to meel the changing need of an organization

## Vertical Scalling

**Just increasing and decreasing the resource** of a single server

* Easy to manage
* Efficient
* Workload that requires high performance
* Cost-Effective

## Horizontal Scalling

**adding or removing servers from a system** to increasing or decreasing resources

* More scalable
* Can handle more traffic
* add more nodes as demand increases easy to balance betwen nodes and workloads
* Expensive

## Hybrid Scalling

Combination Vertical and Horizontal

# Redundancy

Is the process of creating multiple copies of data or resources to ensure the availabily and reliablity of system (**Like Backup**)

### High Availablity

Helps to ensure that systems continue to operate when failure occurs

**Fault-Tolerance** > **High-Availablity** *like* **100** > **99.9%**

### Improved Performance

Provide backup system in case of a failure

### Increased Resiliency

Ready for any attack and recovery in fastest time

### Imporved Security

***

### Load-Balancing

Distributes incoming traffic to multiple servers

### Failover

transport to secendary system in emergency events

### Disaster-Recovery

Recovery systems after any natural or cyber disaster and attack

#### Type of DR :

Feature | Cold-site | Warm-Site | Hot-Site
---|---|---|---|
Secondary Location | + | + | +
Equipment at Location | - | + | +
Connectivity at Location | - | + | +
Active before failover | - | - | +
Outage measured in | Weeks | Days-Hours | Hours-Minutes

### Fault Tolerance

Provides a backup in case of failures or errors,which helps to prevent data loss and minimize downtime

## Advantage

* Minimize Downtime
* Improved Performance
* Increased resiliency
* Improved Security
* Enhanced user experience

# IaC

Infrastructure as Code

$\rightarrow$ Manage and control all infrastructure with code

**SDN is a subset of this concept**

## SDN

Software Definde Networking

$\rightarrow$ Seprate Network from harfware and manage easier

* Software controller or APIs

## 3 Portions of Typical Network Architechture

**High Level** :

### Management-Plane

Used to administrator the routers and switches inside of the network

* SSH
* SNMP
* CLI

### Control-Plane

* Static Router
* GDP
* OSPF
* MPLS portocols
  **Low Level** :

### Data-Plane
For control and config
* Forwarding-table
* Routing-table
