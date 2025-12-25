# Automated DevOps Container Pipeline

A robust, production-ready CI/CD pipeline demonstrating the containerization of a Python Flask application, automated builds via GitHub Actions, and deployment to the GitHub Container Registry (GHCR).

## The Tech Stack
- **Application:** Python 3.9 + Flask Web Framework
- **Containerization:** Podman (Daemonless Docker alternative)
- **Environment:** WSL2 (Ubuntu 22.04)
- **CI/CD:** GitHub Actions (Automated YAML Workflows)
- **Registry:** GitHub Container Registry (GHCR)

## Architecture Flow
1. **Develop:** Code is written in Python and containerized with a `Containerfile`.
2. **Commit:** Changes are pushed to the `main` branch.
3. **Automate:** GitHub Actions triggers a cloud-based Linux runner.
4. **Build & Push:** The runner builds the image and pushes it to GHCR.
5. **Deploy:** The image is ready to be pulled and run on any environment.



## How to Run Locally
Ensure you have Podman or Docker installed, then run:

```bash
# Pull the latest image from my registry
podman pull ghcr.io/tritmeri/podman-push:latest

# Run the container and map the web port
podman run -d -p 8080:5000 --name my-web-app ghcr.io/tritmeri/podman-push:latest
