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

## Scenario 1 – Shared Document Deletion Incident(Outlined Steps)

<p>
<strong>Context:</strong> An intern accidentally deleted a shared design document. The objective is to reproduce the incident and implement controls to prevent recurrence.
</p>

### Part A – Multi-User Simulation(Outlined Steps)

#### Step 1 - Creating Users (intern_a, dev_user, ops_user)
#### Step 2 - Creating Group and Assigning Users
![User Creation](Scenario_1/Part_A.png)


### Part B – Reproducing the Incident

#### Step 1 - Creating Shared Directory and File
#### Step 2 - Logging in as intern_a and Deleting the File

![Shared Directory](Scenario_1/Part_B.png)


### Part C – Preventing Recurrence (Outlined Steps)

#### Step 1 - Recreating the File
#### Step 2 - Applying Immutability Protection (chattr +i)
#### Step 3 - Testing Deletion as intern_a

![Immutable Protection](Scenario_1/Part_C.png)

**What was done:**

-
-
-

**Explanations & Observations:**

-
-
-
-


## Scenario 2 – Log Overwrite Incident
<p>
<strong>Context:</strong> Application logs were overwritten, destroying forensic history. The objective is to simulate, prevent, and backup logs with proper metadata preservation.
</p>

#### Step 1 - Creating logs/app.log with 100+ Lines
![Log Creation](Scenario_2/log_overwrite-01.png)

#### Step 2 - Simulating Accidental Overwrite And Seeing Line Counts
![Log Creation](Scenario_2/log_overwrite_02.png)

#### Step 3 - Applying Overwrite Prevention Mechanism And Creating Backup
![Log Creation](Scenario_2/log_overwrite_03.png)

---

**What was done:**

-
-
-

**Explanations & Observations:**

-
-
-
-


## Scenario 3 – Permission & Ownership Drift
<p>
<strong>Context:</strong> A deployment script copied incorrect data due to relative path usage. The objective is to reproduce and fix the issue using absolute paths.
</p>

#### Step 1 - Creating Files with Varying Permissions
#### Step 2 - Changing Ownership and Groups (chown, chgrp)
#### Step 3 - Copying Files WITHOUT Preservation Flags
![Ownership Change](Scenario_3/permission_drift_CP.png)

#### Step 4 - Copying Files WITH Preservation Flags (cp -p)
![Copying With Preservation -P](Scenario_3/permission_drift_CP-P.png)

#### Step 5 - Copying Files & Folders WITH Preservation Flags (cp -r)
![Copying With Preservation -R](Scenario_3/permission_drift_CP-R.png)

---

**What was done:**

-

**Explanations & Observations:**

-
-
-
-

---

## Scenario 4 – Relative Path Deployment Failure

<p>
<strong>Context:</strong> A deployment script copied incorrect data due to relative path usage. The objective is to reproduce and fix the issue using absolute paths.
</p>


- Incoming Step Evaluation Soon


---

## Scenario 5 – Monitoring Failure After Log Cleanup

#### Step 1 - Creating the Original Log File
#### Step 2 - Creating a Hard Link
#### Step 3 - Creating a Symbolic Link
#### Step 4 - Removing the Original File
![SymLink Versus HardLink](Scenario_5/monitoring_failure.png)

**What was done:**

-

**Explanations & Observations:**

-
-
-
-

---

## Scenario 6 – Sensitive Data Exposure Hunt

<p>
<strong>Context:</strong> Security team suspects secrets are hidden in logs and config files. The objective is to scan for sensitive data using grep techniques and proper output redirection.
</p>

---

#### Step 1 - Simulating Logs and Using Recursive Scanning (grep -r)

#### Step 2 - Using Multiple Expressions (grep -e)

![Recursive Scan](Scenario_6/sensitive_data_hunt-01.png)

#### Step 3 - Using Pattern File (grep -f)
![Recursive Scan](Scenario_6/sensitive_data_hunt-02.png)

---

**What was done:**

-

**Explanations & Observations:**

-
-
-
-

---

## Scenario 7 – Shared Directory Stability Controls

<p>
<strong>Context:</strong> Developers report files disappearing from shared directories. The objective is to implement controls allowing file creation but preventing deletion of others' files.
</p>

