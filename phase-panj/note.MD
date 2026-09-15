# Type of Volume
## Volume
- Managed by docker 
- Saving data permanetly
## Bind Mount 
- Specific path on the host
- for develop and - access to files
## tmpfs Mount 
- hosted by RAM 
- Sensitive and Temporary data
## Overlay 2 
- docker storage driver
## Anonymous
- hard to manage
- save data 
- not good for important data

# Networking
- Bridge
- Host
- Null

**Busybox** : best package's tool for networking

**Mac Vlan** : Independent network interface in docker

**Port Mapping** : A technique for connecting a container to the host os

# Compose

**a manifest file for specific data (like log or cmd) with .yml format**

- useable for automate
- structure : 
    ```
    Version
    Services :
        Servicename :
            Servicedetail
    ```
- useable for config multi container

command
- stop -> just for stop
- down -> for stop and remove containers and networks

# Registry



    Docker Hub (Registry)
    │
    ├── nginx (Repository)
    │   ├── nginx:latest
    │   ├── nginx:1.27
    │   └── nginx:alpine
    │
    ├── redis (Repository)
    │   ├── redis:latest
    │   └── redis:7
    │
    └── mysql (Repository)
        ├── mysql:latest
        └── mysql:8

**Registry** = a service that stores and distributes Docker images

**Repository** = a collection of related images within a registry, usually identified by a project/image name