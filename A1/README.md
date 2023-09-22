 ## Docker
   - This assignment involves building a microservice architecture using Docker containers.
   - **Container 1**:
     - Implemented in Flask, acts as an orchestrator and gatekeeper.
     - It listens for JSON input on port 6000, validates the input, checks file existence, and forwards parameters to Container 2.
   - **Container 2**:
     - also using Flask, operates on port 8001, checks CSV file format, calculates sum based on 'product,' and responds to Container 1.
   - This architecture showcases microservice communication and orchestration, enabling efficient handling of specific tasks through RESTful APIs and Dockerization.
   - **Keywords: Containers, Docker Images**
