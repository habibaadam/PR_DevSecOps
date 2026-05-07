# Docker Container Security — Hands-On Lab Documentation

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Security](https://img.shields.io/badge/Security-Hardening-red?style=for-the-badge)

---

## Introduction

This documentation records a hands-on self-study lab I completed covering Docker container security from first principles. Rather than simply listing commands, each scenario explains the *why* behind every decision and demonstrates the security implications through direct observation. Every scenario includes screenshots from the lab as a source of verification.

By completing these scenarios, I built progressively more secure versions of the same Node.js application and developed a concrete understanding of:

- Why the default Docker configuration is insecure
- How privilege escalation risk is introduced by running as root
- How secrets leak into images unintentionally
- How multi-stage builds reduce the attack surface
- How runtime hardening restricts container capabilities

---


## The Sample Application

The application is intentionally minimal. Its sole purpose is to report the user ID of the process running inside the container, making the root vs. non-root difference immediately visible in terminal output.

**`app.js`** — starts an HTTP server on port 3000 and responds with:
- The numeric user ID (`process.getuid()`)
- A human-readable label (`root -- DANGER` or `non-root (uid: N)`)
- The container hostname

**`package.json`** — declares the project metadata and `npm start` script.

**`.env`** — simulates a production secrets file containing a database password, API key, and Stripe secret. Used in Scenario 1 to demonstrate accidental secret leakage.

---

## Scenario 1 — The Insecure Default

### Objective

In this scenario, I examined what a basic Dockerfile looks like, why it is insecure by default, and how Docker layer caching works in practice using timed builds.

### Dockerfile Used

> Check this file -> [`Dockerfile`](./Dockerfile)

### Key Concepts Demonstrated

- Running as root (UID 0)
- Unfiltered `COPY . .` leaking secrets into the image
- Layer caching behaviour and how instruction order affects build speed

### Steps & Observations

#### Step 1 — Build the Image (First Build)

**Command:**
```bash
time docker build -f Dockerfile -t insecure-app .
```

**Observed output / screenshot:**
![First Build](screenshots/The_Insecure_Default/first_build.png)
-

**Observation:**
-
-

---

#### Step 2 — Second Build (Cached)

**Command:**
```bash
time docker build -f Dockerfile -t insecure-app .
```

**Observed output/screenshot:**

![Second Build Cache](screenshots/The_Insecure_Default/second_build_cached.png)

**Observation:**
-


#### Step 3 — Third Build (Code Change — Cache Invalidation)

Added `// version 2` comment to the top of `app.js`, then rebuilt.

**Command:**
```bash
time docker build -f Dockerfile -t insecure-app .
```

**Observed output / screenshot:**

![Code Update](screenshots/The_Insecure_Default/code_update.png)


**Observation:**
-
-

---

#### Step 4 — Running the Container

**Command:**
```bash
docker run -p 3000:3000 insecure-app
curl http://localhost:3000
```

**Observed output / screenshot:**

![Insecure Container](screenshots/The_Insecure_Default/insecure_container_run.png)

**Observation:**
-

#### Step 5 — Confirming the Secret Leak

**Commands:**
```bash
docker exec -it $(docker ps -q) sh
cat /app/.env
```

**Observed output / screenshot:**
![Baked Credentials](screenshots/The_Insecure_Default/baked_credentials.png)

**Observation:**
-
-

#### Final System Resetting

**Commands:**
```bash
docker system prune -af
```
![Pruning](screenshots/The_Insecure_Default/s1_pruning.png)


### Checkpoint Answers

1.
2.
3.

### Reflection

1.
2.

### Summary



## Scenario 2 — Running as a Non-Root User

### Objective

In this scenario, I stopped the application from running as root and observed concretely what that change protects against.

### Dockerfile Used

> Check this file -> [`Dockerfile.nonroot`](./Dockerfile.nonroot)

### Key Concepts Demonstrated

- Creating a dedicated system user and group inside the image
- The `USER` instruction and when it takes effect
- `chown` to transfer file ownership before switching users

### Steps & Observations

#### Step 1 — Resetting the Environment

**Command:**
```bash
docker system prune -af
```

---

#### Step 2 — Building and Running the Non-Root Image

**Commands:**
```bash
docker build -f Dockerfile.nonroot -t nonroot-app .
docker run -p 3000:3000 nonroot-app
curl http://localhost:3000
```

**Screenshot:**

![Non-root app running](screenshots/Running_Non_Root_User/non_root_apprun.png)

**Observation:**
-
-

---

#### Step 3 — Verifying the Permission Boundary

**Commands:**
```bash
docker exec -it $(docker ps -q) sh
echo "test" > /etc/passwd
apt-get install curl
touch /bin/backdoor
```

**Screenshot:**

![Permission boundary verification](screenshots/Running_Non_Root_User/verify_permissions_boundary.png)

![App user permission details](screenshots/Running_Non_Root_User/app_user_permissions.png)

**Observation:**
-
-
-
---

#### Step 5 — Resetting the Environment

**Command:**
```bash
docker system prune -af
```

**Screenshot:**

![Pruning](screenshots/Running_Non_Root_User/s2_pruning.png)

### Checkpoint Answers

1.
2.
3.

### Reflection

1.
2.

### Summary



---

## Scenario 3 — Protecting Secrets with .dockerignore

### Objective

In this scenario, I prevented sensitive files from ever entering the image build context by introducing a `.dockerignore` file.

### Dockerfile Used

`Dockerfile` (with `.dockerignore` now present)

### Key Concepts Demonstrated

- The Docker build context and what `COPY . .` actually copies
- How `.dockerignore` filters files before they reach the daemon
- Verifying that a file is absent from a built image

### Steps & Observations

#### Step 1 — Creating the `.dockerignore` File

The following entries were added to exclude sensitive and unnecessary files from the build context:

> File can be found here >  [`.dockerignore`](./.dockerignore)

```
.env
.git
*.md
node_modules
```

---

#### Step 2 — Rebuilding the Image and Inspecting for the Secret

**Commands:**
```bash
docker build -f Dockerfile.nonroot -t secure-copy-app .
docker run --rm secure-copy-app find /app -type f

```

**Screenshot:**

![Secure app env check](screenshots/Protecting_Secrets/secure_app_inspect.png)

**Observation:**
-
-

---

#### Step 3 — Confirming Secret Cannot Be Read

**Command:**
```bash
docker exec -it $(docker ps -q) sh
cat /app/.env
```

**Screenshot:**

![Secure app inspect](screenshots/Protecting_Secrets/secure_app_env.png)

**Observation:**
-
-

---

#### Step 4 — Resetting the Environment

**Command:**
```bash
docker system prune -af
```

**Screenshot:**

![Pruning](screenshots/Protecting_Secrets/s3_pruning.png)

### Checkpoint Answers

1.
2.
3.

### Reflection

1.
2.

### Summary



---

## Scenario 4 — Multi-Stage Builds

### Objective

In this scenario, I reduced the final image size and attack surface by separating the build environment from the runtime environment using a multi-stage Dockerfile.

### Dockerfile Used

> Check this file -> [`Dockerfile.nultistage`](./Dockerfile.multistage)

### Key Concepts Demonstrated

- Named build stages (`AS builder`)
- `--from=builder` to copy only the necessary artefacts into the final image
- The size difference between `node:20` and `node:20-alpine`
- Build tools and source files that do not appear in the final image

### Steps & Observations

#### Step 1 — Building the Multi-Stage Image

**Command:**
```bash
docker build -f Dockerfile.multistage -t multistage-app .
```

---

#### Step 2 — Comparing Image Sizes

**Command:**
```bash
docker images
```

**Screenshot:**

![Comparing image sizes](screenshots/Multi_Stage_Builds/comparing_sizes.png)

**Observation:**
-
-

---

#### Step 3 — Running the Multi-Stage Image

**Commands:**
```bash
docker run -p 3000:3000 multistage-app
curl http://localhost:3000
```

**Screenshot:**

![Running multistage app](screenshots/Multi_Stage_Builds/running_multistage.png)

**Observation:**
-
-

---

#### Step 4 — Confirming the Reduced Attack Surface

**Commands:**
```bash
docker exec -it $(docker ps -q) sh

npm --version
curl --version
git --version
apt-get install wget
```

**Screenshot:**

![Reduced attack surface](screenshots/Multi_Stage_Builds/reduced_attack_surface.png)

**Observation:**
-
-

---

### Step 5 - Confirming MultiStage App Works

![Running multistage app](screenshots/Multi_Stage_Builds//running_multistage.png)


#### Step 6 — Resetting the Environment

**Command:**
```bash
docker system prune -af
```

**Screenshot:**

![Pruning](screenshots/Multi_Stage_Builds/s4_pruning.png)

### Checkpoint Answers

1.
2.
3.

### Reflection

1.
2.

### Summary



---

## Scenario 5 — Runtime Hardening

### Objective

In this scenario, I applied Linux kernel-level restrictions to a running container to limit what a compromised process can do.

### Dockerfile Used

`Dockerfile.multistage` (with runtime flags applied at `docker run`)

### Key Concepts Demonstrated

- `--read-only` filesystem to prevent writes at runtime
- `--cap-drop ALL` to remove all Linux capabilities
- `--no-new-privileges` to prevent privilege escalation via setuid binaries
- `--memory` and `--cpus` to constrain resource usage
- `--security-opt` and seccomp profiles

### Steps & Observations

#### Step 1 - Rebuilding MultiStage App

```bash

docker build -f Dockerfile.multistage -t multistage-app .
```

### Step 2 - Applying The First Flag - Read Only File System

```bash
docker run --read-only --tmpfs /tmp -p 3000:3000 multistage-app
```

Second Terminal
```bash
docker exec -it $(docker ps -q) sh -c "echo test > /app/hacked.txt"
```

Stopping The Container
```bash
docker stop $(docker ps -q)
```

**Screenshot:**
[Read only File System Flag](screenshots/Runtime_Hardening/read_only_fs.png)

**Observations:**
-
-

### Step 3 - Applying The Memory and Cpu Limits

```bash
docker run --memory="128m" --cpus="0.5" -p 3000:3000 multistage-app
```

Verifying The Limits

```bash
docker inspect $(docker ps -q) | grep -E '"Memory"|"NanoCpus"'
```

Stopping The Container
```bash
docker stop $(docker ps -q)
```

**Screenshot:**
[Memory and Cpu Limits](screenshots/Runtime_Hardening/mem_cpu_limits.png)


**Observations:**
-
-

### Step 3.1 - Dropping Linux Capabilities

```bash
docker run --cap-drop=ALL -p 3000:3000 multistage-app
```

Confirming The Application Responds By Running

```bash
curl http://localhost:3000
```

**Screenshot:**
[Linux Cap Drop](screenshots/Runtime_Hardening/linux_cap_dropped.png)


#### Step 4 — Running the Fully Hardened Container

**Command:**
```bash
docker run -d -p 3000:3000 \
  --read-only \
  --cap-drop ALL \
  --no-new-privileges \
  --memory 128m --cpus 0.5 \
  --tmpfs /tmp \
  multistage-app
```

**Screenshot:**

![Fully hardened container](screenshots/Runtime_Hardening/fully_hardened_container.png)

**Observation:**
-
-

---

#### Step 5 — Further Inspection

**Screenshot:**

![Further inspection](screenshots/Runtime_Hardening/further_inspection.png)

**Observation:**
-
-

---

#### Step 6 — Resetting the Environment

**Command:**
```bash
docker system prune -af
```

**Screenshot:**

![Pruning](screenshots/Runtime_Hardening/s5_pruning.png)

### Checkpoint Answers

1.
2.
3.

### Reflection

1.
2.

### Summary


## Key Takeaways



## References

- [Docker Official Documentation](https://docs.docker.com/)
- [OWASP Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker)
- [Node.js Docker Best Practices](https://github.com/nodejs/docker-node/blob/main/docs/BestPractices.md)
