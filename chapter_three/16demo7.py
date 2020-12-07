import ntplib
import time #通过ctime 转换请求到网络时间
#获取网络时间
ntp_client = ntplib.NTPClient()

response = ntp_client.request('pool.ntp.org')
print(response)
print(response.tx_time)
print(time.ctime(response.tx_time))