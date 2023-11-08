# mini-fix-client
FIX Client: A Python-based Financial Information Exchange (FIX) Protocol Client

## Usage
To use this application, you can run it in a Docker container. Ensure you have Docker installed on your system.
Test session configs available in config/config.json.

##### 1. Navigate into project directory
```bash
cd mini-fix-client

```

##### 2. Build docker image
```bash
docker build -t mini-fix-client .
```

##### 3. Run the Docker Container
```bash
docker run mini-fix-client
```