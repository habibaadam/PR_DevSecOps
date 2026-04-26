# Docker Container Security — Hands-On Lab Documentation

> A practical walkthrough of Docker container security concepts, progressing from an insecure default configuration to a hardened runtime. Each scenario is documented with commands, observed outputs, and screenshots taken during execution.

---

## Introduction

This documentation records a hands-on self-study lab covering Docker container security from first principles. Rather than simply listing commands, each scenario explains the *why* behind every decision and demonstrates the security implications through direct observation. Every scenario would have screenshots from the lab as a source of verification

By completing these four scenarios, I built progressively more secure versions of the same Node.js application and developed a concrete understanding of:

- Why the default Docker configuration is insecure
- How privilege escalation risk is introduced by running as root
- How secrets leak into images unintentionally
- How multi-stage builds reduce the attack surface
- How runtime hardening restricts container capabilities

---

## Repository Structure

```
docker-labs/
├── app.js                  # Sample Node.js application
├── package.json            # Node package manifest
├── .env                    # Simulated secrets file (intentionally insecure in S1)
├── .dockerignore           # Created in Scenario 3
├── Dockerfile              # Scenario 1 — insecure default
├── Dockerfile.nonroot      # Scenario 2 — non-root user
└── Dockerfile.multistage   # Scenario 4 — multi-stage build
```

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

Understand what a basic Dockerfile looks like, why it is insecure by default, and how Docker layer caching works in practice using timed builds.

### Dockerfile Used

`Dockerfile`

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

**Observed output / screenshot:**

-

**Observation:**


#### Step 3 — Third Build (Code Change — Cache Invalidation)

Added `// version 2` comment to the top of `app.js`, then rebuilt.

**Command:**
```bash
time docker build -f Dockerfile -t insecure-app .
```

**Observed output / screenshot:**

-

**Observation:**

-

---

#### Step 4 — Run the Container

**Command:**
```bash
docker run -p 3000:3000 insecure-app
curl http://localhost:3000
```

**Observed output / screenshot:**
-

**Observation:**
-

#### Step 5 — Confirm the Secret Leak

**Commands:**
```bash
docker exec -it $(docker ps -q) sh
cat /app/.env
```

**Observed output / screenshot:**

-

**Observation:**
-

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

Stop the application from running as root and understand concretely what that change protects against.

### Dockerfile Used

`Dockerfile.nonroot`

### Key Concepts Demonstrated

- Creating a dedicated system user and group inside the image
- The `USER` instruction and when it takes effect
- `chown` to transfer file ownership before switching users

### Steps & Observations



### Checkpoint Answers



### Reflection



### Summary



---

## Scenario 3 — Protecting Secrets with .dockerignore

### Objective

Prevent sensitive files from ever entering the image build context.

### Dockerfile Used

`Dockerfile` (with `.dockerignore` now present)

### Key Concepts Demonstrated

- The Docker build context and what `COPY . .` actually copies
- How `.dockerignore` filters files before they reach the daemon
- Verifying that a file is absent from a built image

### Steps & Observations


### Checkpoint Answers



### Reflection



### Summary



---

## Scenario 4 — Multi-Stage Builds

### Objective

Reduce the final image size and attack surface by separating the build environment from the runtime environment.

### Dockerfile Used

`Dockerfile.multistage`

### Key Concepts Demonstrated

- Named build stages (`AS builder`)
- `--from=builder` to copy only the necessary artefacts
- The difference in image size between `node:20` and `node:20-alpine`
- Build tools and source files that do not appear in the final image

### Steps & Observations



### Checkpoint Answers



### Reflection



### Summary



---

## Scenario 5 — Runtime Hardening

### Objective

Apply Linux kernel-level restrictions to a running container to limit what a compromised process can do.

### Dockerfile Used

`Dockerfile.multistage` (with runtime flags applied at `docker run`)

### Key Concepts Demonstrated

- `--read-only` filesystem
- `--cap-drop ALL` to remove Linux capabilities
- `--no-new-privileges` to prevent privilege escalation via setuid binaries
- `--security-opt` and seccomp profiles

### Steps & Observations



### Checkpoint Answers


### Reflection


### Summary


## Key Takeaways



## References

- [Docker Official Documentation](https://docs.docker.com/)
- [OWASP Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker)
- [Node.js Docker Best Practices](https://github.com/nodejs/docker-node/blob/main/docs/BestPractices.md)
