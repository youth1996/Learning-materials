# 网络编程：在同一个网络中不同的机器之间进行通信
# 计算机之间需要通信的条件: IP地址 端口 协议

# 1.TCPIP协议: Transimission Control Protocol ,传输控制协议，基于字节的传输层通信协议

#  特点：
# ​	a.安全的【确保接收方完全正确的获取发送方发送的全部数据】
#
# ​	b.面向连接的【数据传输必须要建立连接，连接的过程中需要时间】
#
# ​	c.数据传输的效率较低
#
# ​	d.传输的数据的大小有限制，一旦连接建立，双方可以通过指定的格式发送数据

# 三次握手: 发送传输请求

# a.客户端向服务端发送一个请求
#
# b.服务端收到请求之后，回客户端一个响应
#
# c.客户端收到服务端的响应之后，回复给服务端一个确认信息

# 四次挥手: 确认关闭请求

# （1） TCP客户端发送一个关闭请求给服务器.

# （2） 服务器回客户端一个响应,需要检查数据是否处理完毕.

# （3） 服务器回复客户端数据已经接受处理完毕,可以关闭链接.

# （4） 客户端传送关闭请求.

# 2.UDP协议: User Datagram Protocol,用户数据包协议，提供面向无连接的不可靠的信息传输服务
# 特点：  广播模式
#
# ​	a.不安全【发送方只负责将信息发送出去，数据能不能到达对方，或者到达对方的信息是否正确，都不做任何保证】
#
# ​	b.无连接的【进行信息发送之前，无需进行发送方和接收方之间的连接】
#
# ​	c.速度快
#
# ​	d.大小是有限制的，每个数据包的大小必须限制在64k以内