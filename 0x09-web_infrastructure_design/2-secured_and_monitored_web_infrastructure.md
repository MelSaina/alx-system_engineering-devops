![3rd Image ](https://github.com/MelSaina/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.png)

Designing a Secure and Monitored Three-Server Web Infrastructure for www.foobar.com:

1. User Accessing the Website:
A user wants to access the website hosted at www.foobar.com.

2. Server 1:
The first server in the infrastructure.

3. Server 2:
The second server for redundancy and load distribution.

4. Server 3:
The third server for further redundancy and load distribution.

5. Firewalls:
Three firewalls are added to enhance security. Firewalls control incoming and outgoing network traffic, protecting the servers from unauthorized access and potential threats.

6. Web Server (Nginx):
The web server (Nginx) is used to handle incoming HTTP/HTTPS requests. It's responsible for serving static content and forwarding dynamic requests to the application servers.

7. Application Server:
The application server processes dynamic content requests, executes the application code, interacts with the database, and generates responses for the web server.

8. Load Balancer (HAProxy):
The load balancer (HAProxy) distributes incoming traffic across the application servers, improving performance and redundancy.

9. SSL Certificate:
An SSL certificate is added to enable HTTPS, securing data transmission between users and the servers.

10. Monitoring Clients:
Three monitoring clients are integrated to collect data for monitoring and analysis purposes.

11. Monitoring Tool and Data Collection:
The monitoring tool (e.g., Sumo Logic) collects data from the monitoring clients, providing insights into server performance, resource utilization, security events, and more.

12. HTTPS Traffic:
HTTPS traffic is utilized to encrypt data between users and servers, ensuring data confidentiality and integrity during transmission.

13. Monitoring Purpose:
Monitoring is used to track server health, detect anomalies, identify performance bottlenecks, and ensure optimal system operation.

14. Monitoring Data Collection:
The monitoring tool collects data by receiving logs, metrics, and performance information from the monitoring clients on each server.

15. Monitoring Web Server QPS:
To monitor web server QPS (Queries Per Second), you would configure the monitoring tool to collect metrics related to incoming requests and their frequency.

Issues with this Infrastructure:

1. Terminating SSL at Load Balancer:
Terminating SSL at the load balancer can expose decrypted traffic within the internal network, potentially compromising security.

2. Single MySQL Server for Writes:
Having only one MySQL server capable of accepting writes creates a single point of failure. If it goes down, write operations are affected.

3. Homogeneous Server Components:
Using identical components for all servers might lead to a lack of diversity in case of component failures. A failure affecting one server might impact others with the same components.

By addressing these issues, such as implementing end-to-end SSL encryption, setting up database replication for failover, and diversifying server components, the infrastructure can become more secure, resilient, and effective.
