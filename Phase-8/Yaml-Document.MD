# Yaml
**A Serialization language**

## All Type of Language programming 

### 1. Scripting 
A Type of languages that don't need compiler :
- Python
- Js
- Php
- Perl
- Bash
### 2. Programming
A Type of languages that need a compiler and convert to machine's language :
- C
- C#
- C++ 
- Rust
- Java
### 3. Markup 
A Type of languages that isn't programming language just have a rule or specific pattern and syntax (*it is Just a joke*) :
- Html

### 4. Serialization 
A type of languages that uses for **Data Transfer** :
- Xml
- Yaml
- Json
- CSV


#### Different between Yaml , Xml, Json :

Xml :
```
<Server>
    <Server>
        <name>Server1</name>
    </Server>
</Server>
```
Json : 
```
{
    Server:{
        name:server1
    }
}
```

Yaml : 
```
Servers : 
    - name : server1
```


# Yaml Use cases :

### Configuration management 
### infrastructure as code
### CD\CI
### APIs
### Data Serialization 
### Container orchestration 


# Syntax

```
Key : Value
# Comment


Object :
    feature : any

Array :
    - first-index 
    - second-index
    - third-index
    
```