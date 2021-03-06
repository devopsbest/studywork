my_list = [m + n for m in 'ABC' for n in 'XYZ']
print(my_list)


en0 = """
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether ac:bc:32:9b:a8:43
	inet6 fe80::1c2a:a657:8d99:c399%en0 prefixlen 64 secured scopeid 0x4
	inet 192.168.100.104 netmask 0xffffff00 broadcast 192.168.100.255
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
"""
import re
my_reg = re.compile("inet\s(\d+.\d+.\d+.\d+)")
result = re.search(my_reg,en0)
print(result.group(1))

#也可以写成：
import re
my_reg = re.compile("inet\s((\d+.){3}\d+)")
result = re.search(my_reg,en0)
print(result.group(1))
