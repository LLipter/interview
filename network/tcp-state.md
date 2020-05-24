# TCP State Transition Diagram

A TCP connection progresses through a series of states during its lifetime. The following diagram illustrates the possible states for a TCP connection and how the states transition based on various events from either the network or from the local TCP sockets application.

![](https://ftp.bmp.ovh/imgs/2020/05/879955791c9e6ef7.png)

# Check TCP Status

The `netstat` command lets you print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.


# References

1. [TCP connection status](https://www.ibm.com/support/knowledgecenter/en/SSLTBW_2.1.0/com.ibm.zos.v2r1.halu101/constatus.htm)
2. [TCP/IP State Transition Diagram (RFC793)](https://users.cs.northwestern.edu/~kch670/eecs340/proj2-TCP_IP_State_Transition_Diagram.pdf)
3. [Linux netstat Command Tutorial for Beginners (8 Examples)](https://www.howtoforge.com/linux-netstat-command/)