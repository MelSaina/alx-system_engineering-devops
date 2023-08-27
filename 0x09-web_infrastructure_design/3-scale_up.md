![SCALE UP IMAGE](https://github.com/MelSaina/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/3-scale_up.png )
In this representation, the user's computer accesses the website through a browser. The load balancer (HAProxy Cluster) distributes incoming requests to Server 1 and Server 2. Each server hosts its own Nginx web server, which communicates with the application server. The application server processes dynamic content requests and communicates with the database (MySQL). This layout ensures load balancing, redundancy, and separation of components for better performance and fault tolerance.
Designing a Two-Server Web Infrastructure with HAProxy Load Balancer:

1. User Accessing the Website:
A user wants to access the website hosted at www.foobar.com.

2. Server 1:
The first server in the infrastructure.

3. Server 2:
The second server for redundancy and load distribution.

4. Load Balancer (HAProxy):
The load balancer (HAProxy) is configured as a cluster to distribute incoming traffic across multiple servers. It ensures high availability and improved performance.

5. Web Server (Nginx):
The web server (Nginx) handles incoming HTTP/HTTPS requests, serves static files, and forwards dynamic requests to the application server.

6. Application Server:
The application server processes dynamic content requests, executes the application code, interacts with the database, and generates responses for the web server.

7. Database (MySQL):
The database (MySQL) stores and manages the website's data.

Why Each Component:

Server 1 and Server 2: Adding two servers provides redundancy, fault tolerance, and load distribution. If one server fails, the other can continue handling requests, reducing the risk of downtime.

Load Balancer (HAProxy): The load balancer distributes incoming traffic across multiple servers. This ensures even load distribution, improves response time, and enhances availability. Configuring HAProxy as a cluster increases fault tolerance; if one HAProxy instance fails, the other can take over.

Web Server (Nginx): The web server handles incoming requests, serves static files, and forwards dynamic requests to the application server. It also enhances security by isolating the application server from direct access.

Application Server: The application server processes dynamic content, executes the application's logic, and interacts with the database. Separating it from the web server improves security and enables scalability.

Database (MySQL): The database stores and manages website data. Isolating the database on its own server helps improve performance and security.

By distributing components across servers and using a load balancer, this design ensures better resource utilization, scalability, and fault tolerance, contributing to an efficient and robust web infrastructure.
