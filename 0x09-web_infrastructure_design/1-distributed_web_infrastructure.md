![Image 2](https://github.com/MelSaina/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure.png)

Designing a Three-Server Web Infrastructure for www.foobar.com:

1. User Accessing the Website:
Let's start with a user who wants to access the website hosted at www.foobar.com.

2. Server 1:
This will be the first server in the infrastructure.

3. Server 2:
The second server is added to introduce redundancy and reduce the risk of a single point of failure (SPOF).

4. Web Server (Nginx):
The web server (Nginx) is added to handle incoming HTTP/HTTPS requests, serve static files, and forward dynamic requests to the application server.

5. Application Server:
The application server processes dynamic content requests, executes the application code, interacts with the database, and generates responses for the web server.

6. Load Balancer (HAProxy):
The load balancer (HAProxy) is introduced to distribute incoming traffic across the two application servers using a distribution algorithm. This helps balance the load and improve performance.

7. Application Files (Code Base):
The set of application files contains the source code of the website's application. This code is executed by the application server to generate dynamic content based on user requests.

8. Database (MySQL):
The database (MySQL) is added to store and manage the website's data.

9. Load Balancer Configuration:
The load balancer (HAProxy) is configured with a Round-Robin distribution algorithm. This means it distributes incoming requests in a circular manner, evenly sending requests to each application server in turn.

10. Active-Active Setup:
The load balancer is enabling an Active-Active setup, where both application servers are actively serving requests simultaneously. This increases availability and ensures that traffic is distributed among multiple servers.

11. Primary-Replica (Master-Slave) Database Cluster:
The database is configured as a Primary-Replica (Master-Slave) cluster. The Primary (Master) node handles write operations and replicates data changes to the Replica (Slave) node. This setup improves data availability and provides a backup in case the Primary node fails.

12. Difference Between Primary and Replica Nodes:

Primary Node: Handles write operations and is the authoritative source of data changes. It's directly used by the application for data modifications.
Replica Node: Replicates data changes from the Primary node and can be used for read operations to distribute read traffic and improve performance. It provides data redundancy.
Issues with this Infrastructure:

1. Single Points of Failure (SPOFs):

The load balancer can be a single point of failure. If it fails, traffic distribution is disrupted.
The database Primary node can also be a SPOF. If it fails, write operations and data changes are affected.
2. Security Issues:

Lack of firewall exposes servers to potential security threats.
Lack of HTTPS leaves data transmitted between users and servers vulnerable to interception.
3. No Monitoring:
Without monitoring tools and practices, it's difficult to detect and address performance issues, downtime, or security breaches promptly.

Implementing redundancy, security measures (firewalls, HTTPS), and monitoring tools can help address these issues and create a more robust and secure infrastructure.
