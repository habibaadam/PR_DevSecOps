# DevSecOps Linux Hands-On Assignment 2 Documentation

![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)
![DevSecOps](https://img.shields.io/badge/DevSecOps-Security-red)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat&logo=ubuntu&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat&logo=gnu-bash&logoColor=white)
![File Security](https://img.shields.io/badge/File-Security-blue)
![Access Control](https://img.shields.io/badge/Access-Control-green)
![Forensics](https://img.shields.io/badge/Log-Forensics-orange)
![Audit](https://img.shields.io/badge/Security-Audit-purple)


## Overview

This documentation provides a complete walkthrough of Linux file security, permissions, and forensic scenarios. Each section includes executed commands, terminal output evidence, observations, and security implication.

## Scenario 1 – Shared Document Deletion Incident

<p>
<strong>Context:</strong> An intern accidentally deleted a shared design document. The objective is to reproduce the incident and implement controls to prevent recurrence.
</p>

### Part A – Multi-User Simulation

#### Step 1 - Creating Users (intern_a, dev_user, ops_user)
#### Step 2 - Creating Group and Assigning Users
![User Creation](Scenario_1/Part_A.png)


### Part B – Reproducing the Incident

#### Step 1 - Creating Shared Directory and File
#### Step 2 - Logging in as intern_a and Deleting the File

![Shared Directory](Scenario_1/Part_B.png)


### Part C – Preventing Recurrence
#### Step 1 - Recreating the File
#### Step 2 - Applying Immutability Protection (chattr +i)

![Immutable Protection](Scenario_1/Part_C.png)

**What was done:**

-
-
-

**Observations Made And Explanation :**

-
-
-
