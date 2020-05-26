# I/O Model

对于一个network I/O (以下以read为范例), 基本上会涉及到两个系统层面的对象: 其一是呼叫此I/O的process/thread, 再来就是系统kernel, 而一个read operation基本上又会经历以下两个阶段(phase):

1. 等待资料准备(Waiting for the data to be ready)
2. 将资料从kernel copy至process/thread中(Copying the data from the kernel to the process)

### Blocking I/O

![](https://ftp.bmp.ovh/imgs/2020/05/e1f247de4ca236c4.png)

### Nonblocking I/O

![](https://ftp.bmp.ovh/imgs/2020/05/de0371f4e49822d4.png)

### I/O Multiplexing

![](https://ftp.bmp.ovh/imgs/2020/05/3a8ce2fd6274569c.png)

### Signal Driven I/O

![](https://ftp.bmp.ovh/imgs/2020/05/c31817a71657758e.png)

### Asynchronous I/O

![](https://ftp.bmp.ovh/imgs/2020/05/c31817a71657758e.png)

### Conclusion

![](https://ftp.bmp.ovh/imgs/2020/05/a8cf3d0fdb8f3da7.jpeg)

# References

1. [淺談I/O Model](https://medium.com/@clu1022/%E6%B7%BA%E8%AB%87i-o-model-32da09c619e6)
2. [五种IO模型详解](https://blog.csdn.net/ocean_fan/article/details/79622956)