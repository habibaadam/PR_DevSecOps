# DevSecOps Linux Hands-On Assignment Documentation

## Overview

This documentation provides a complete walkthrough of the Linux & DevSecOps assignment scenarios. Each section includes screenshots of executed, terminal output evidence, observation, and security considerations.

### Scenario 1 - Password State Investigation & Remediation
<p>
During a routine security audit, the Security Director asks:
**Show me how you identify users on this system who do not have passwords set, and then demonstrate how you would remediate one."**.

The objective of this scenario is to identify users on system who do not have passwords set,and to demonstrate remediation of the said scenario.

Below are the steps taken to achieve the objective.
</p>

#### Step 1 - Creating A User With No Password
![Creating audit_test user](Scenario_1/Part_A.png)

**What was done:**
- A new user named "audit_test" was created using:
  ```
  sudo useradd -m -s /bin/bash audit_test
  ```
- Verified the account exists in `/etc/passwd`

**Why It was Done:**
- The `-m` flag in the sudo useradd command ensures a home directory is created for `audit_test
- The `-s` flag followed by the `/bin/bash` sets a default bash shell for the newly created user.

**Observation Made:**
- After checking the `etc/passwd` file where all users exist:
   - User `audit_test` was assigned UID(userId) 1004
   - User `audit_test` was assigned GID(groupId) 1004
   - User `audit_test` was given a home directory and also a default bash shell.
