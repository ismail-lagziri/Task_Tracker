# Task_Tracker

The **Task_Tracker** API is a RESTful API designed to manage and monitor tasks while ensuring that tasks available to the user to edit are the ones corresponding to his ip address

## Prerequisites

Before you begin, make sure you have the following installed:

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:
    ```bash
    git clone [repository_link]
    ```

2. Navigate to the project directory:
    ```bash
    cd Task_Tracker
    ```

3. Configure the necessary environment variables in the Dockerfile located in the root of the project:
    ```bash
    SERVER_HOST=0.0.0.0
    SERVER_PORT=8000
    ```

## Build and Run

Build and run your Docker container using Docker Compose:
```bash
docker-compose build
docker-compose up
```
The **Task_Tracker** API should now be accessible at http://${SERVER_HOST}:${SERVER_PORT}

## Turn it off

```bash
docker-compose down
```
## Note
### All remarks and suggestions are encouraged

