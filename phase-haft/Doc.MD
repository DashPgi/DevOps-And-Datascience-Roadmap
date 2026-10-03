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

### Type of SDN
* Open SDN
    - Relies on open-sources tech like openflow and openstack
* Hybrid SDN
    - Employs tradiotional and SDN protocols to operate itself
* SDN Overlay
    - A method of using software to create layers of network obstruction that can be used to run multiple separate virtualized network layers on top of the  physical network 

### Advantage of SDN
1. Flexibility
2. Scalability
3. Cost-effectiveness
4. Better-Security
5.  Improved-Network-Performance 
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
# DNS
Domain Name Server
## 5 Level of DNS Hierarchy
1. **Root**
    - Root name server
2. **TLD**
    - Top-level domain
3. **SLD**
    - Second-level domain
4. **Subdomain**
    - Server underneath the SDL
5. **Host**
# Load Balancing
### Layer 4
Uses the transport layer (TCP/UDP) to distribute traffic among servers
### Layer 7
Uses application layer (HTTP/HTTPS) to distribute 
### Cloud-based
### DNS-based

# Storage in cloud 
## Object storage
### Save data , likes object
- **Advantage**
    - Scalability
    - Large-scale
    - high-scalability
    - Less expensive
- **Disadvantage** 
    - May have not strong data protection all the time
    - Unstructured data
## Block storage
### Save data , like block
- **Advantage**
    - High level data security 
    - includes built-in collabration features
- **Disadvantage**
    - More expensive
    - Less scalable
## File storage
### Save data , like file
- **Advantage**
    - includes buitl-in collabration features
    - File-level access and collabration
- **Disadvantage**
    - More expensive
    - Less scalable
## Software define storage
#### Seprate the managment of storage sources
- Uses a policy-based
- Just adminstrator can define configoration

Type pf storage hardware :
- Flash Drivers
- Solid-state drivers
- Virtual-disks
- Cloud-disks

## CDN
### Content Delivery Network
#### System of distributed servers used to deliver web content to users based on their geographic location
- **Advantage**
    - Provides faster and more
    - Improves the performance and speed of a website or application
    - Improvess the security too
- **Disadvantage**
    - Expensive
    - Slower load time (if the nearest server is not located)
    - it adds complexity to a website or application
# Cloud-Migration
Is the process of moving data,app and other business processes from an on-premise enviroment to a cloud-based infrastructure
### 3 Main Phases of CM
1. Planning 
    - create a roadmap for CM and asesst systems
2. implementation 
    - Move app or data and test functionaly 
3. Optimization and Security 
    - Improve performance , security and monitoring

## Strategies
### 1. Rehosting
Lift and shift

Move apps to cloud with minimal or no changes
### 2. Replatforming
Change DB service 

Make small optimization while moving to cloud 
### 3. Retaining 
Keep some apps on permises
### 4. Retiring
Don't use apps no longer use
### 5. Refactoring 
Replace and rearchietect,redsign app to fully leverage cloud-natvie feature
### 6. Repurching   
Drop and shop 

Replace existing app with cloud-based solution (SaaS)


# VPC
Virtual Private Cloud

is an isolated and configurable virtual network inside a cloud provider's infrastructure

*It allows you to control how your cloud resources communicate with each other and with the Internet*

With a VPC, you can define:

- IP address ranges
- Subnets
- Routing
- Internet access
- Security rules
- Public and private resources

## Main uses
- Network isolation 
    - separate your cloud resources from other environments
- Network segmentation
    - divide your network into different subnets
- Internet connectivity 
    - control which resources can access the Internet
- Traffic control 
    - control which resources can communicate with each other
- Security 
    - restrict access using Security Groups and Network ACLs
- Private communication 
    - connect applications, databases, servers, and other cloud services privately
- Hybrid networking 
    - connect your cloud network to an on-premises network using VPN or dedicated connections

# IAM
Identity and Access Management

is a system used to manage identities and control access to cloud resources

## Main IAM components

| Component      | Meaning                                           |
| -------------- | ------------------------------------------------- |
| **User**       | An identity representing a person/application     |
| **Group**      | A collection of users                             |
| **Role**       | An identity that can be assumed by users/services |
| **Policy**     | Defines permissions                               |
| **Permission** | Specifies what actions are allowed or denied      |
| **MFA**        | Adds an additional authentication factor          |


# Cloud-Operation

## Data Management
For ensure critical aspect of cloud computing with integrity,security and availablity of data

### 1. Data Replication
Is a key aspect of disaster recovery
- **Reproduction** : Process to creating multiple copies of data across different location or server 
- **Increase availabiliy**

### 2. Backup and Recovery
- Snapshot
- Increment backup
- Full backup

### 3. Data Gravity
*Save data in a spesefic location*

### 4. Locality
**Location of data** , if we having a large amounts of data,it efficient to use CPU resource pool closer to the data

### 5. Data Compression
**Removing unnecessary data** for improve performance and dicrease costs

### 6. Deduplication
Eleminate duplicated data 