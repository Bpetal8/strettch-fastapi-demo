# Deploying a Production-Ready FastAPI Service on Strettch Cloud

This project shows how to deploy a FastAPI application using a production-style Linux setup that mirrors how applications run on Strettch Cloud infrastructure.

Instead of relying on heavy abstractions, this approach uses standard, battle-tested components:

- **Nginx** for reverse proxy and request handling  
- **Gunicorn** as the application server  
- **systemd** for process management  

The result is a clean, reliable deployment that is easy to understand, debug, and run on a cloud VM such as Strettch Cloud.

This makes it a practical starting point for developers looking to move from local development to real-world cloud deployment.

---

## Why This Project

Many African teams build solid Python applications but struggle with:

- Reliable deployment  
- Predictable cloud costs  
- Data locality and compliance  

This project shows a clean, minimal path to running a FastAPI service using standard Linux tooling and honest architectural trade-offs.

---

## Why Strettch Cloud?

For developers building in Africa, infrastructure decisions matter.

Strettch Cloud provides:

- Local, Africa-based infrastructure
- Predictable pricing
- A simple VM-based model that aligns with standard Linux deployments

This makes it a strong fit for teams that want control, transparency, and reliable performance without unnecessary complexity.

---

## Architecture Overview
```
Client
|
v
Nginx (Reverse Proxy - Port 80)
|
v
Gunicorn (Application Server)
|
v
FastAPI Application
|
v
systemd (Process Manager)
|
v
Linux VM (Cloud Instance)
```
In this project, the Linux VM environment is replicated using Ubuntu on WSL, providing the same systemd, networking, and service management tools used in real cloud environments like Strettch Cloud.

This setup was run entirely in a local WSL environment, but follows the exact same steps and tooling used when deploying to a real cloud VM such as Strettch Cloud.

**Key Components**

- Linux VM (cloud-equivalent environment)
- Nginx for request routing and reverse proxy
- Gunicorn as the production application server
- FastAPI for application logic
- systemd for service lifecycle management

No Kubernetes or heavy abstractions are used to keep the setup simple and transparent.

---

## Project Structure
```
strettch-fastapi-demo/
├── app/
│   ├── main.py # FastAPI application
│   └── config.py # Environment configuration
├── deploy/
│   ├── nginx.conf # Nginx reverse proxy config
│   └── strettch.service # systemd service file
├── .env.example
├── requirements.txt
└── README.md
```
## Features

- FastAPI-based REST API
- Health check endpoint
- Simulated ML inference endpoint
- Environment-based configuration
- Production-ready server setup

---

## Getting Started

To explore the project locally:

```bash
git clone https://github.com/Bpetal8/strettch-fastapi-demo.git
cd strettch-fastapi-demo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
This installs the dependencies required to run the FastAPI application locally.
---

## Deployment Overview

Here’s a simple overview of how this application would be deployed on a cloud VM (e.g., Strettch Cloud):

1. Provision a Linux VM on Strettch Cloud
2. SSH into the server
3. Install Python and system dependencies
4. Configure environment variables
5. Run FastAPI as a systemd service
6. Expose the service using Nginx

These steps directly translate to deploying on a Strettch Cloud instance.

Detailed commands and configurations are documented in the repository.

---

## API Endpoints

### GET /

Returns the application status.

Example response:

{"status":"ok","message":"FastAPI is running"}

### GET /health

Health check endpoint used to verify service availability.

Example response:

{"status":"healthy"}

### POST /predict

Simulated ML inference endpoint.

Example request:

curl -X POST http://localhost/predict \
-H "Content-Type: application/json" \
-d '{"input": 12.5}'

Example response:

{
 "input": 12.5,
 "prediction": 18.75,
 "model": "demo-linear-model"
}
---

## Production Validation

The deployment was validated using standard Linux service management tools.

Verify application service:

```bash
sudo systemctl status strettch
```

Verify Nginx service:

```bash
sudo systemctl status nginx
```

Test application response:

```bash
curl http://localhost
```

Expected response:

```json
{"status":"ok","message":"FastAPI is running"}
```

## Linux Deployment (Example on Ubuntu VM)

Below is an example deployment process for a Linux VM, following the same steps used on platforms like Strettch Cloud.

### 1. Update server

```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Install Python and required system dependencies

```bash
sudo apt install python3 python3-venv python3-pip nginx -y
```

### 3. Clone repository

```bash
git clone https://github.com/Bpetal8/strettch-fastapi-demo.git
cd strettch-fastapi-demo
```

### 4. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Copy systemd service

```bash
sudo cp deploy/strettch.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start strettch
sudo systemctl enable strettch
```

### 7. Configure Nginx

```bash
sudo cp deploy/nginx.conf /etc/nginx/sites-available/strettch
sudo ln -s /etc/nginx/sites-available/strettch /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

Your API is now accessible via port 80.

---

## Why This Architecture?

### Why Gunicorn in Production?

The built-in development server is single-process and not suitable for production concurrency. Gunicorn manages multiple worker processes and provides stable request handling under load.

### Why systemd?

systemd ensures:

- Automatic restart if the application crashes
- Background execution
- Automatic startup on server reboot

### Why Bind to 127.0.0.1?

Gunicorn listens internally only.
Only Nginx is exposed publicly, reducing the attack surface.

## Observations & Learnings

While setting up this deployment, here are some practical takeaways:

- The stack (Nginx + Gunicorn + systemd) is simple and reliable
- Debugging is straightforward compared to container-heavy setups
- The setup process is transparent and easy to reason about

These insights are important when thinking about developer experience and how platforms like Strettch Cloud can lower the barrier to production deployment.
---

## Future Enhancements

This project intentionally focuses on a minimal production deployment.

Possible future enhancements include:

- Authentication and API access control
- Structured logging and monitoring integration
- Background task processing using a queue system
- Horizontal scaling behind a load balancer

These additions would further align the architecture with production workloads running on cloud infrastructure.

## Demo

Watch the full deployment walkthrough here:  
[Add your video link]