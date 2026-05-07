# Docker Hub, CI/CD & Security Automation — Beginner Lab Documentation

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Docker Hub](https://img.shields.io/badge/Docker%20Hub-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Trivy](https://img.shields.io/badge/Trivy-1904DA?style=for-the-badge&logo=aquasecurity&logoColor=white)

---

## Overview

This documentation records a hands-on beginner lab designed to simulate the way real-world DevSecOps teams work with containers and registries. Rather than treating Docker Hub as a black box, each phase breaks down the mechanics of pulling, building, tagging, pushing, and automating images, while keeping security visible at every step.

By completing these phases, I developed a concrete understanding of:

- How to authenticate with Docker Hub using access tokens instead of passwords
- How to build a minimal, production-grade Flask application and containerise it securely
- How layer caching, non-root users, and `.dockerignore` reduce risk at build time
- How to push, pull, and share images via a public registry
- How GitHub Actions automates the entire workflow and gates pushes behind a Trivy vulnerability scan


---
## The Sample Application

The application is intentionally simple — its purpose is to demonstrate containerisation and CI/CD concepts, not complex application logic.

**`app.py`** — starts a Flask web server on port 5000 and exposes two routes:
- `/` — renders an HTML greeting page, injecting a configurable node name via a Jinja2 template
- `/health` — returns a JSON response with status, node name, and UTC timestamp; used by Docker's `HEALTHCHECK` and the pipeline's smoke test

**`templates/index.html`** — a minimal HTML page that displays the greeting injected by Flask.

**`requirements.txt`** — pins the Flask version for reproducible builds across all environments.

**`dockerfile`** — builds from `python:3.11-slim`, creates a non-root user, optimises layer caching by copying `requirements.txt` before application code, and declares a `HEALTHCHECK`.

**`.dockerignore`** — prevents development artefacts, `.git`, `.env` files, and Markdown from entering the image.

---


## Initial Step - Generating a Docker Hub Access Token

The objective of this step is to generate a scoped access token for Docker Hub to authenticate without exposing an account password — following the principle of least privilege for credentials.

**What was done:**
- Logged in to hub.docker.com
- Navigated to: Avatar → Account Settings → Security → New Access Token
- Named the token `lab-token` and selected **Read & Write** permissions
- Copied the generated token immediately


**Security Implications:**
- Access tokens can be scoped and revoked independently of the account password
- Using a token instead of a password means a leaked credential cannot be used to modify account settings or generate further tokens

---


## Phase 0 — Pull and Inspect a Public Container

The objective is to act as an image consumer: pull an existing public image from Docker Hub, run it, inspect it, and observe how Docker manages layers and containers.

### Key Concepts Demonstrated

- `docker pull` and image layer downloading
- Running a detached container with port mapping
- Inspecting running containers and logs
- Cleaning up with `docker rm -f`

### Steps & Observations

#### Step 1 — Pulling the Nginx Alpine Image

**Command:**
```bash
docker pull nginx:alpine
```

#### Step 2 — Running the Container

**Command:**
```bash
docker run -d -p 8080:80 --name my-nginx nginx:alpine
```


#### Step 3 — Inspect Running Containers and Logs

**Commands:**
```bash
docker ps
docker logs my-nginx
```

**Screenshot:**

![Pulling nginx:alpine](screenshots/Phase_0/pull_inspect.png)


### Step 4 - Confirming On Browser on Port 8080

**Commands:**
```bash
# Opening http://localhost:8080 in browser
```

**Screenshot:**

![Running nginx container](screenshots/Phase_0/nginx-check.png)

**Overall Observation:**
- An image built and published by another person was pulled and downlaoded unto my machine
- A container was derived/created from the pulled image.
- Port mapping made the image accessible from the browser.

---



## Phase 1 — Build, Push, Pull & Share Your Own Image


The objective of this phase is to transition from image consumer to image creator: build a Flask web application, containerise it securely, push it to Docker Hub, pull it back, and share it with others.

---

### Step 1 — Creating the Web Application

#### Key Concepts Demonstrated

- Flask routing and JSON health endpoints
- Environment variable injection for configurable behaviour
- Jinja2 HTML templating

#### Write `app.py` and `templates/index.html`

> Check [`app.py`](app.py) and [`templates/index.html`](templates/index.html) for the full content.



### Step 2 — Writing A Secure Dockerfile

#### Key Concepts Demonstrated

- `python:3.13-slim` as a minimal base image, the base image was initially set to `python:3.11-slim`
- Non-root user creation with `groupadd` / `useradd`
- Layer caching optimisation by copying `requirements.txt` first
- `HEALTHCHECK` instruction for container liveness monitoring
- `.dockerignore` to exclude unwanted files from the build context

> Check [`dockerfile`](dockerfile) for the full content.


### Step 3 — Building and Testing Locally

#### Key Concepts Demonstrated

- `docker build` and the build context
- Running and verifying a container locally before pushing
- Testing both the home page and the `/health` endpoint

#### Step 3.1 — Building the Image

**Command:**
```bash
docker build -t my-web-app .
```

#### Step 3.2 — Running and Testing Locally
**Commands:**
```bash
docker run -d -p 5001:5000 --name webapp-test my-web-app
```
**Screenshot:**

![Local build output](screenshots/Phase_1/running_web_app.png)

```
NB: Instead of port 5000, the port mapping was changed to 5001 because an important running process was utilizing port 5000
```

**Screenshot:**

![Container running, browser test](screenshots/Phase_1/localhost_5001.png)

![Container running, browser test, health check](screenshots/Phase_1//localhost_5001:health.png)
---

#### Step 3.3 — Stopping and Removing The Test Container

**Command:**
```bash
docker rm -f webapp-test
```

### Step 4 — Pushing to Docker Hub

#### Key Concepts Demonstrated

- Authenticating with Docker Hub using an access token
- Tagging an image with a registry path and personal identifier
- Uploading image layers to the registry

#### Step 1 — Log In to Docker Hub

**Command:**
```bash
docker login -u your-dockerhub-username
```

#### Step 2 — Tag and Push the Image

**Commands:**
```bash
docker tag my-web-app your-dockerhub-username/my-web-app:v1.0.0-habi
docker push your-dockerhub-username/my-web-app:v1.0.0-habi
```

**Screenshot:**

![Tag and push output](screenshots/Phase_1/docker_hub_push.png)



**Observation:**
-
-

**What was done:**
-
-

**Reasons Why:**
-
-

---

### Step 5 — Pull Your Own Image

#### Key Concepts Demonstrated

- Simulating a fresh environment by removing the local image
- Pulling from Docker Hub to verify the push succeeded

#### Step 1 — Remove Local Image and Pull from Registry

**Commands:**
```bash
docker rmi your-dockerhub-username/my-web-app:v1.0.0-habi
docker pull your-dockerhub-username/my-web-app:v1.0.0-habi
docker run -d -p 5000:5000 --name pulled-app your-dockerhub-username/my-web-app:v1.0.0-habi
```

**Screenshot:**

![Pull and run from registry](screenshots/Phase_1/pull_own_image.png)

**Observation:**
-
-

**What was done:**
-
-

**Reasons Why:**
-
-

---

### Step 6 — Share with Others

#### Key Concepts Demonstrated

- Public vs private Docker Hub repositories
- Cross-machine reproducibility as a core container value

#### Step 1 — Verify Repository Visibility and Share Tag

**Screenshot:**

![Docker Hub public repo](screenshots/Phase_1/share_image.png)

**Observation:**
-
-

**What was done:**
-
-

**Security/System Implications:**
-
-

### Checkpoint Answers

1.
2.
3.

### Reflection

1.
2.

### Summary



---

## Phase 2 — Automate with a DevSecOps Pipeline

### Objective

Build a GitHub Actions CI/CD workflow that builds, vulnerability-scans, and pushes the image automatically on every push to `main` — ensuring no unscanned image ever reaches the registry.

### Key Concepts Demonstrated

- GitHub Actions workflow syntax and triggers with `paths` filters
- Storing credentials as encrypted GitHub secrets
- `docker/build-push-action` for building and loading images
- Trivy (`aquasecurity/trivy-action`) for scanning before pushing
- Conditional steps with `if: success()`
- Smoke testing a running container inside the pipeline

---

### Part 1 — Set Up the GitHub Repository

#### Step 1 — Initialise Git and Push to GitHub

**Commands:**
```bash
git init
git add .
git commit -m "Initial commit: Flask app, Dockerfile, and workflow"
git branch -M main
git remote add origin https://github.com/your-github-username/your-repo.git
git push -u origin main
```

**Screenshot:**

![Git init and push](screenshots/Phase_2/git_init_push.png)

**Observation:**
-
-

---

### Part 2 — Add Secrets to GitHub

#### Step 1 — Add DOCKERHUB_USERNAME and DOCKERHUB_TOKEN

**Screenshot:**

![GitHub secrets configured](screenshots/Phase_2/github_secrets.png)

**Observation:**
-
-

**What was done:**
-
-

**Security/System Implications:**
-
-

---

### Part 3 — The Workflow File

#### Step 1 — Review `docker-build-push.yml`

**Screenshot:**

![Workflow file in editor](screenshots/Phase_2/workflow_file.png)

**Observation:**
-
-

**What was done:**
-
-

**Reasons Why:**
-
-

---

### Part 4 — Trigger the Pipeline

#### Step 1 — Push a Change and Watch the Actions Tab

**Screenshot:**

![GitHub Actions run in progress](screenshots/Phase_2/actions_run.png)

**Observation:**
-
-

---

#### Step 2 — Trivy Scan Results

**Screenshot:**

![Trivy vulnerability scan output](screenshots/Phase_2/trivy_scan.png)

**Observation:**
-
-

---

#### Step 3 — Successful Push and Smoke Test

**Screenshot:**

![Push and smoke test passed](screenshots/Phase_2/push_smoke_test.png)

**Observation:**
-
-

**What was done:**
-
-

**Reasons Why:**
-
-

**Security/System Implications:**
-
-

---

### Part 5 — Pull the Automatically Built Image

#### Step 1 — Pull the Pipeline-Built Image Locally

**Command:**
```bash
docker pull your-dockerhub-username/my-web-app:v1.0.0-habi
```

**Screenshot:**

![Pull pipeline image](screenshots/Phase_2/pull_pipeline_image.png)

**Observation:**
-
-

### Checkpoint Answers

1.
2.
3.

### Reflection

1.
2.

### Summary



---

## Clean Up

**Commands used to remove all lab resources:**
```bash
docker rm -f $(docker ps -aq)
docker rmi $(docker images -q)
```

**Screenshot:**

![Cleanup complete](screenshots/Phase_2/cleanup.png)

**Observation:**
-
-

---

## Key Takeaways



---

## References

- [Docker Official Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Trivy — Aqua Security](https://github.com/aquasecurity/trivy)
- [OWASP Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Node.js Docker Best Practices](https://github.com/nodejs/docker-node/blob/main/docs/BestPractices.md)
