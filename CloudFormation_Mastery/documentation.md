# AWS CloudFormation Mastery — Lab Documentation

![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)
![CloudFormation](https://img.shields.io/badge/CloudFormation-FF4F8B?style=for-the-badge&logo=amazonaws&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?style=for-the-badge&logo=yaml&logoColor=white)
![IaC](https://img.shields.io/badge/Infrastructure_as_Code-blue?style=for-the-badge)

---

## Introduction

This documentation records a hands-on CloudFormation lab I completed working across three levels of infrastructure complexity. Rather than clicking through the AWS console to provision resources manually, each level involved writing a CloudFormation template, deploying it as a stack, and observing how AWS orchestrates the provisioning process.

The three levels I worked through each demonstrate a distinct concept:

- **Level 5 — [Compute & Wiring: EC2, Security Groups & Intrinsic Functions]:** Demonstrates how to set up EC2 instances with security groups and use intrinsic functions for dynamic resource configuration.

- **Level 6 — [Composition: Nested Stacks]:** Demonstrates how to break down complex infrastructure into reusable nested stacks.

- **Level 7 — [ Dynamic Intelligence: Custom Resources]:** Demonstrates how to extend CloudFormation's capabilities by creating custom resources that can execute arbitrary logic during stack operations.

By completing these levels, I developed a practical understanding of:

- How CloudFormation templates are structured and validated
- How Stack Events expose exactly what AWS is doing — and where it fails
- How parameters, outputs, and resource dependencies work together
- How rollback behaviour protects infrastructure consistency
- How to iterate on a template based on real deployment errors

---

## Level 5 — [Compute & Wiring: EC2, Security Groups & Intrinsic Functions]

### What This Level Demonstrates
This level demonstrates how to provision an EC2 instance with a security group, and how to use intrinsic functions to dynamically configure resources based on parameters and other resource attributes.
### Template Overview

> Template file: [`webserver.yaml`](templates/webserver.yaml)

**Key resources defined:**
- **Web Server EC2 Instance:** The virtual server that will run the web application.
- **Web Server Security Group:** Defines the firewall rules that control inbound and outbound traffic to the EC2 instance.
- **Key parameters:**
  - **InstanceType:** Allows the user to specify the type of EC2 instance to launch
  - **KeyName:** The name of the SSH key pair to allow secure access to the instance.

### Prediction

Before deploying, I expected the following outcomes due to content of the template:
- The EC2 instance will be launched with the specified instance type and key pair.
- The security group will allow inbound traffic according to the defined rules.
- An output will be generated with the public IP address of the EC2 instance.

### Steps & Observations

#### Step 1: Creating the Stack

**Console action Screenshot:**

![Level 5 Stack Events](screenshots/level_5/web_server_stack.png)

**Stack Outcome/Creation Output Screenshot:**

![Level 5 Stack Outcome/Creation Output](screenshots/level_5/web_server_stackinfo.png)

**Observation:**
- The stack was successfully created, and the EC2 instance is running with the expected configuration, with apache installed and serving a default web page. The security group is correctly configured to allow inbound HTTP traffic on port 80.

#### Step 2: Verifying the Deployed Resources

**Screenshot:**

![Level 5 Resources](screenshots/level_5/web_server_ip.png)

**Observation:**
An EC2 instance was successfully created with the specified parameters. The security group was also created and associated with the instance, allowing the expected inbound traffic.

#### Step 3: Updating the Stack
**Screenshot — Updating Instance Type Parameter:**
![Level 5 Stack Update](screenshots/level_5/web_server_update_parameter.png)

**Screenshot — Stack Update Events:**
![Level 5 Stack Update Events](screenshots/level_5/web_server_update_complete.png)

**Screenshot - Output after Update:**
![Level 5 Stack Update Output](screenshots/level_5/web_server_changed_ip_output.png)

**Observation:**
The stack was successfully updated to change the instance type. The EC2 instance was replaced with a new instance of the specified type, and the public IP address changed accordingly.


### Lessons Learned
If something like the instance type is changed, CloudFormation will replace the resource rather than update it in place, which can lead to downtime if not planned for.

---

## Level 6 — [Composition: Nested Stacks]

### What This Level Demonstrates

### Template Overview

> Template file: [`level6.yaml`](level6.yaml)

**Key resources defined:**
-
-
-

**New CloudFormation features introduced:**
-
-

### Prediction

Before deploying, I expected:

### Steps & Observations

#### Step 1: Creating the Stack

**Command / Console action:**


**Screenshot — Stack Events:**

![Level 6 Stack Events](screenshots/level6_stack_events.png)

**Observation:**

#### Step 2: Verifying the Deployed Resources

**Screenshot:**

![Level 6 Resources](screenshots/level6_resources.png)

**Observation:**

#### Step 3: Updating the Stack

**Screenshot — Update Stack Events:**

![Level 6 Stack Update](screenshots/level6_stack_update.png)

**Screenshot — Stack Update Complete:**
![Level 6 Stack Update Complete](screenshots/level6_stack_update_complete.png)

**Observations:**

#### Step 4: Deleting the Stack

**Screenshot:**

![Level 6 Stack Deleted](screenshots/level6_stack_deleted.png)

### Lessons Learned

-

---

## Level 7 — [Dynamic Intelligence: Custom Resources]

### What This Level Demonstrates

### Template Overview

> Template file: [`level7.yaml`](level7.yaml)

**Key resources defined:**
-
-
-

**New CloudFormation features introduced:**
-
-

### Prediction

Before deploying, I expected:

### Steps & Observations

#### Step 1: Creating the Stack

**Command / Console action:**


**Screenshot — Stack Events:**

![Level 7 Stack Events](screenshots/level7_stack_events.png)

**Observation:**

#### Step 2: Verifying the Deployed Resources

**Screenshot:**

![Level 7 Resources](screenshots/level7_resources.png)

**Observation:**

#### Step 3: [Additional verification — e.g. testing an endpoint, checking outputs]

**Screenshot:**

![Level 7 Verification](screenshots/level7_verification.png)

**Observation:**

#### Step 4: Deleting the Stack

**Screenshot:**

![Level 7 Stack Deleted](screenshots/level7_stack_deleted.png)


### Lessons Learned

-

---

## Overall Reflection

### What I Predicted vs What Actually Happened

### What I Would Explore Next

---

## Conclusion

---

## References

- [AWS CloudFormation Documentation](https://docs.aws.amazon.com/cloudformation/)
- [AWS CloudFormation Template Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-reference.html)
- [AWS Resource and Property Types Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html)
- [CloudFormation Best Practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html)
