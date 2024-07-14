# 0x0D. Web Stack Debugging #0

## Description
This project involves debugging a Docker container to get Apache to run and return a page containing "Hello Holberton" when querying the root. The objective is to diagnose and fix issues within the container so that it serves the correct web page.

## Task

### Getting Apache to Serve "Hello Holberton"
- **Goal**: Ensure that when the root of the container is queried, it returns a page containing "Hello Holberton".
- **Example**: 
  ```sh
  vagrant@vagrant:~$ curl 0:8080
  Hello Holberton
  ```

### Steps to Achieve the Goal
1. **Run the Docker Container**: 
   Start the Docker container using the provided image and map the container's port 80 to the host's port 8080.
   ```sh
   docker run -p 8080:80 -d -it holbertonschool/265-0
   ```

2. **Access the Running Container**: 
   Access the running container using the container ID.
   ```sh
   docker exec -it CONTAINER_ID /bin/bash
   ```

3. **Install and Start Apache**: 
   Inside the container, install Apache and start the service.
   ```sh
   apt-get update
   apt-get install -y apache2
   service apache2 start
   ```

4. **Create a Web Page**: 
   Create an HTML file in the Apache web root directory to display "Hello Holberton".
   ```sh
   echo "Hello Holberton" > /var/www/html/index.html
   ```

5. **Verify Apache is Running**: 
   Ensure that Apache is running correctly.
   ```sh
   service apache2 status
   ```

6. **Test the Setup**: 
   Exit the container and test the setup by curling the port 8080 on your host machine.
   ```sh
   exit
   curl 0:8080
   ```

### Expected Output
The expected output when querying `0:8080` should be:
```
Hello Holberton
```

## Commands Used
1. **Run the Docker container**:
   ```sh
   docker run -p 8080:80 -d -it holbertonschool/265-0
   ```

2. **Access the running container**:
   ```sh
   docker exec -it CONTAINER_ID /bin/bash
   ```

3. **Install and start Apache inside the container**:
   ```sh
   apt-get update
   apt-get install -y apache2
   service apache2 start
   ```

4. **Create the web page**:
   ```sh
   echo "Hello Holberton" > /var/www/html/index.html
   ```

5. **Exit the container and test**:
   ```sh
   exit
   curl 0:8080
   ```

Make sure to replace `CONTAINER_ID` with the actual ID of your running container.

## Repository
- **GitHub repository**: `alx-system_engineering-devops`
- **Directory**: `0x0D-web_stack_debugging_0`
- **File**: `0-give_me_a_page`

By following these steps, you should be able to resolve the issue and ensure that the Apache server inside the Docker container serves the "Hello Holberton" page correctly.
