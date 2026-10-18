
# Answers

## Q1.
I install dependencies before copying the application code to improve Docker's cache. If the code changes, Docker can reuse the dependency layer and build faster. Changing the order could make builds slower.

## Q2.
Data inside a container is normally lost when the container is removed. Docker volumes or bind mounts can preserve data. Important application data should be stored in a database or other persistent storage.

## Q3. 
The "latest" tag can point to different versions over time. This makes builds less reproducible. I used python:3.12.11-slim and pinned Flask to version 3.1.2.

## Image size
I checked the image size using docker images. My image's disk usage is 184MB and the content size is 44.8MB.


## AI assistant disclosure

I used the AI assistant to understand the homework requirements, learn the Dockerfile instructions.I reviewed the app code and it helped me with an error.
