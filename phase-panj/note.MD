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
