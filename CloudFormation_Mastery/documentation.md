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

- **Level 7 — [ Dynamic Intelligence: Custom Resources]:** [One line: what this level demonstrates]

By completing these levels, I developed a practical understanding of:

- How CloudFormation templates are structured and validated
- How Stack Events expose exactly what AWS is doing — and where it fails
- How parameters, outputs, and resource dependencies work together
- How rollback behaviour protects infrastructure consistency
- How to iterate on a template based on real deployment errors

---

## Level 5 — [Compute & Wiring: EC2, Security Groups & Intrinsic Functions]

### What This Level Demonstrates

### Template Overview

> Template file: [`level5.yaml`](level5.yaml)

**Key resources defined:**
-
-

### Prediction

Before deploying, I expected:

### Steps & Observations

#### Step 1: Creating the Stack

**Command / Console action:**
```bash
aws cloudformation deploy \
  --template-file level5.yaml \
  --stack-name [stack-name]
```

**Screenshot — Stack Events:**

![Level 5 Stack Events](screenshots/level5_stack_events.png)

**Observation:**

#### Step 2: Verifying the Deployed Resources

**Screenshot:**

![Level 5 Resources](screenshots/level5_resources.png)

**Observation:**

#### Step 3: Deleting the Stack

**Command / Console action:**
```bash
aws cloudformation delete-stack --stack-name [stack-name]
```

**Screenshot:**

![Level 5 Stack Deleted](screenshots/level5_stack_deleted.png)

### Troubleshooting

> *(If applicable — describe any errors encountered, what the Stack Events showed, and how it was resolved)*

### Lessons Learned

-

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
```bash
aws cloudformation deploy \
  --template-file level6.yaml \
  --stack-name [stack-name]
```

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

**Observation:**

#### Step 4: Deleting the Stack

**Screenshot:**

![Level 6 Stack Deleted](screenshots/level6_stack_deleted.png)

### Troubleshooting

> *(If applicable)*

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
```bash
aws cloudformation deploy \
  --template-file level7.yaml \
  --stack-name [stack-name] \
  --capabilities CAPABILITY_IAM
```

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

### Troubleshooting

> *(If applicable)*

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
