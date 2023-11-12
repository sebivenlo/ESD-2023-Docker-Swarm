# Assignment

This is description for the practical part of the workshop

## Setup

1. Do docker-compose up
2. Access the terminal of the following containers:
    1. worker_two_container
    2. worker_one_container
    3. one_service_container
3. Paste this command into it and execute it:
    1. sh script.sh
4. You are finished with the setup

## Exercises

### Setup a docker swarm

1. Initialize a docker swarm inside the one_service_container and copy the command to join a node
2. Add the worker_one_container and worker_two_container as workers to the swarm
3. Add the multiple_service_container as manager to the swarm (Tipp: Use docker swarm join-token manager inside the already
   existing manager container)
4. Execute "docker node ls" and copy on off the names 
5. Paste the copied node name at the end of this command "docker node inspect"
6. You are finished with the first exercises

### Setup a docker service

1. Start the multipleservice.py class inside the multiple_service_container and open 127.0.0.1:5000
2. Create a service inside the one_service_container using the dockerfile image
3. Reload the 127.0.0.1:5000 website as soon the service is converged
4. Execute "docker node ls" command inside the one_service_container and compare the ids
5. Open the 127.0.0.1:4000 website and reload it multiple times.

### Scale the service

1. Scale the service, you just created, to 2 nodes
2. Reload the 127.0.0.1:5000 website as soon the service is converged
3. Execute "docker node ls" command inside the one_service_container and compare the ids
4. Open the 127.0.0.1:4000 website and reload it multiple times
5. Execute "docker service ps" command inside the one_service_container