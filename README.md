# CSCI-5409-Adv-Topics-in-Cloud-Computing

## Assignments and Topics

1. **[Assignment 1](https://github.com/VikramVenkatapathi/CSCI-5409-Adv-Topics-in-Cloud-Computing/tree/main/A1): Docker**
   - This assignment involves building a microservice architecture using Docker containers.
   - Container 1:
     - Implemented in Flask, acts as an orchestrator and gatekeeper.
     - It listens for JSON input on port 6000, validates the input, checks file existence, and forwards parameters to Container 2.
   - Container 2:
     - also using Flask, operates on port 8001, checks CSV file format, calculates sum based on 'product,' and responds to Container 1.
   - This architecture showcases microservice communication and orchestration, enabling efficient handling of specific tasks through RESTful APIs and Dockerization.
   - **Keywords: Containers, Docker Images**

2. **Assignment 2: gRPC**
   - This assignment involves creating a gRPC server that provides three essential operations: storing data in an AWS S3 bucket, appending data to an existing file in the same bucket, and deleting a file from the bucket.
   - The server utilizes gRPC technology to efficiently handle data interactions, making it suitable for various distributed and scalable applications.
   - **Keywords: gRPC, Protobuf, Boto3, S3**

3. **Assignment 3: Bastian Hosts**
   - This assignment focuses on AWS network and security mechanisms. It requires deploying a web application on an EC2 instance within a Virtual Private Cloud (VPC).
   - The application interacts with AWS RDS and involves receiving JSON data through POST requests, storing it in a private database, and responding to GET requests.
   - **Keywords: AWS, VPC, EC2, RDS, JSON, Network Security**

4. **Assignment 4: State Machine**
   - Describe Assignment 4 here.
   - This assignment involves implementing a serverless application on AWS using Lambda functions, Step Functions, and API Gateway to perform hashing operations based on provided input.
   - The application receives JSON input, processes it through a state machine, and triggers Lambda functions to hash the data. The results are sent back to another endpoint.
   - **Keywords: AWS Lambda, Step Functions, API Gateway, Serverless Computing, Hashing, REST API**

5. **Kubernetes (K8s)**
   - Describe Kubernetes usage here.
   - This setup involves two Docker containers (Cntr1 and Cntr2) running Flask applications, interacting with each other via RESTful endpoints. Cntr1 handles file storage and data validation, while Cntr2 performs calculations on CSV data.
   - The infrastructure is provisioned using Terraform on Google Cloud, creating a container cluster. Keywords: Docker, Flask, REST API, Terraform, Google Cloud.
   - **Keywords: Docker, Flask, REST API, Terraform, Google Cloud**

