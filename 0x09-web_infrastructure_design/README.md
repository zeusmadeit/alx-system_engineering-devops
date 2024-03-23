# Web infrastructure design

``` DevOps, SysAdmin, web infrastructure ```

### What is a database
A database is an organized collection of structured information, or data, typically stored electronically in a computer system

### What’s the difference between a web server and an app server?
A Web server handles the HTTP protocol. When the Web server receives a HTTP request, it responds with a HTTP response, such as sending back a HTML page While an application server exposes business logic to client applications through various protocols, possibly including HTTP. While a Web server mainly deals with sending HTML for display in a Web browser, an application server provides access to business logic for use by client application programs.

### DNS record types
The domain name system, or DNS, is a global system responsible for mapping human-readable hostnames to their corresponding Internet Protocol (IP) addresses.
The following are the five major DNS record types:
TYPE    | DESCRIPTION
------- | -------
A record| The A record is the most important DNS record type.The "A" in A record stands for "address." An A record shows the IP address for a specific hostname or domain
AAAA record| AAAA record, just like A record, point to the IP address for a domain. However, this DNS record type is different in the sense that it points to IPV6 addresses.
CNAME record| CNAME—or, in full, "canonical name"—is a DNS record that points a domain name (an alias) to another domain. In a CNAME record, the alias doesn't point to an IP address. And the domain name that the alias points to is the canonical name. For example, the subdomain ng.example.com can point to example.com using CNAME. Here example.com points to the actual IP address using an A record.
Nameserver (NS) record| A nameserver (NS) record specifies the authoritative DNS server for a domain. In other words, the NS record helps point to where internet applications like a web browser can find the IP address for a domain name. Usually, multiple nameservers are specified for a domain. 
Mail exchange (MX) record| A mail exchange (MX) record, is a DNS record type that shows where emails for a domain should be routed to. In other words, an MX record makes it possible to direct emails to a mail server. You can have multiple MX records for a single domain name.

### High availability cluster (active-active/active-passive)
An active-active high availability cluster distributes workloads evenly across all nodes, ensuring load balancing. An active-passive setup involves not all nodes being active, with the other node(s) on standby to take over if the active node fails, ensuring service continuity without load distribution.

### What is HTTPS
Hypertext transfer protocol secure (HTTPS) is the secure version of HTTP, which is the primary protocol used to send data between a web browser and a website. HTTPS is encrypted in order to increase security of data transfer.

### What is a firewall
A firewall is a division between a private network and an outer network, often the internet, that manages traffic passing between the two networks. It’s implemented through either hardware or software.

## General
You must be able to explain: 
### system redundancy
System Redundancy works by creating duplicates of critical components or functions of a system. Redundancy is the practice of having multiple copies or alternatives of your resources, such as servers, networks, or storage. Redundancy can help you avoid single points of failure, improve performance, and balance the load.
### LAMP
LAMP is an acronym for the operating system, Linux; the web server, Apache; the database server, MySQL; and the programming language, PHP.
### SPOF (Single point of failure)
A single point of failure (SPOF) is a potential risk posed by a flaw in the design, implementation or configuration of a circuit or system. SPOF refers to one fault or malfunction that can cause an entire system to stop operating.
### QPS
QPS is defined as queries per second. QPS is used to describe the total number of bid requests that can be sent per second.

