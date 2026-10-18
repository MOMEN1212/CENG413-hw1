
# CENG413 HW-1

A Flask web app with `/`, `/health`, and `/info` endpoints, configured using environment variables. The Docker image uses a pinned Python base image and runs as a non-root user.

Build: `docker build -t hw1-app:1.0 .`

Run: `docker run -d --name hw1-container -p 8080:8080 -e APP_NAME="My CENG413 App" hw1-app:1.0`

Test: Open `http://localhost:8080/health`. 

Cleanup: `docker rm -f hw1-container`.