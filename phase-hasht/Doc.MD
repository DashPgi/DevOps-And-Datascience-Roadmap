# SDLC 
Software \ System Development Life Cycle

### 1. Requirment Analysis
### 2. Design
### 3. Implementation
### 4. Testing 
### 6. Evolution 

# Iteration Cycle
### 2 week to  2 month

Software Development Team $\rightarrow$ Git
$\rightarrow$  Build Teams $\rightarrow$  Compile $\rightarrow$  Package $\rightarrow$  Operations Team

**Development** : Software Development Team $\rightarrow$ Git
$\rightarrow$  Build Teams $\rightarrow$  Compile $\rightarrow$  Package $\rightarrow$ 

**Operation** : Operations team $\rightarrow$  Deployment $\rightarrow$  Test Or Public

$First$ $\rightarrow$  Deploy into **Test Environment** 

$If$ In Testing we not having bug $\rightarrow$ **Deploy into Public**

$If$ In Testing we not having bug $\rightarrow$ **Return to Public** 

### Git's Madules

1. Customer Profile
2. Product Catalog
3. Order Tracking

# Pain Point 
1. Integration is painful and effort consuming
2. Fixing issues at the end of iterations
3. Intermediate merge  issues can hold up teams
4. Long feedback cycle for funcctional defects 
5. Long iterations  
$$Solution \rightarrow CI$$
# CI
### Continuous Integration
Is a development practice that requires  developers to integrat code into a shared repository several time a day

#### 1. A single centeral repository where the code lives
#### 2. Developers check in/commit their code frequently (*minimum every day*)
#### 3. Build should be trigged every time a developer check in code 
#### 4. Build should be automated and fast 
#### 5. Build should be compile as well as run automated 
#### 6. Fixing a faild build should be top priority for the developers
#### 7. Build resault should be always be communicated to all developers

In this way **Operation team have new roadmap to operate code** :
Operation Team $\rightarrow$ Read Instructions $\rightarrow$ Prepare Enviroment $\rightarrow$ Deployment

# Pipeline 

In process of integration when a code is in progress,The preceding stages are waiting for that code until process is done

*But In Pipeline* :
**No process or developers remains idle; they can utilize this process to achieve results more quickly and ahead of schedule**  

### Build Pipeline Parts :
#### Integration or Merging
#### Compiletion
#### Automates units tests
#### Automated ui tests

# Pain Point