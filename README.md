# ParoCyber DevSecOps Program Assignment Documentation
This repository contains hands-on assignments and projects completed as part of the DevSecOps training program.

![DevSecOps](https://img.shields.io/badge/DevSecOps-Practice-red?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor!)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)



---

### Assignments

#### 1. Linux & DevSecOps Fundamentals
A comprehensive hands-on assignment covering Linux user management, password security auditing, and department-based access control implementation.
[View Linux Assignment Documentation](DevSecOps_LinuxAssignment1/documentation.MD)

**Topics Covered:**
- Password state investigation and remediation
- User and group management
- Service account configuration
- Sudo access control
- Security best practices

---

#### 2. Linux & DevSecOps 2
📁 **Folder:** `DevSecOps_LinuxAssignment2/`

[View Linux Assignment 2 Documentation](DevSecOps_LinuxAssignment2/documentation.MD)

**Topics Covered:**
- Shared directory access control & deletion prevention
- File attributes (chattr +i, +a) vs permissions
- Log integrity & overwrite prevention
- Permission & ownership preservation during file operations
- Hard links vs symbolic links behavior
- Sensitive data scanning with grep
- Sticky bit for shared directory stability

---

#### 3. Docker Container Security Lab
📁 **Folder:** `Dev_Sec_Ops_Docker/`

[View Docker Security Lab Documentation](Dev_Sec_Ops_Docker/documentation.md)

A hands-on lab progressively hardening a Node.js application containerised with Docker, moving from an insecure default configuration to a fully hardened runtime.

**Topics Covered:**
- Running containers as root and the privilege escalation risk
- Preventing secret leakage with `.dockerignore`
- Multi-stage builds to reduce image size and attack surface
- Runtime hardening: `--read-only`, `--cap-drop ALL`, `--no-new-privileges`
- Linux capabilities and seccomp profiles

---

#### 4. Docker Hub, CI/CD & Security Automation — Beginner Lab
📁 **Folder:** `DevSecOps_Beginner_Lab/`

[View Beginner Lab Documentation](DevSecOps_Beginner_Lab/documentation.md)

An entry-level lab that mirrors a real-world DevSecOps workflow: building and publishing a containerised web application, then automating the entire pipeline with security scanning and smoke testing.

**Topics Covered:**
- Pulling and inspecting public images from Docker Hub
- Building a Flask web application with an HTML front-end and JSON health endpoint
- Writing a secure, production-grade Dockerfile
- Tagging, pushing, and pulling images from Docker Hub
- Sharing images for cross-machine reproducibility
- GitHub Actions CI/CD pipeline 
- Generating and managing Docker Hub access tokens securely