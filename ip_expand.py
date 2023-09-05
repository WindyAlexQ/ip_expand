from IPy import IP

def ip_to_int(ip_address):  
    parts = ip_address.split('.')  
    num = 0  
    for part in parts:  
        num = num * 256 + int(part)  
    return num

def int_to_ip(num):  
    parts = []  
    while num > 0:  
        num, remainder = divmod(num, 256)  
        parts.append(remainder)  
    if len(parts) < 4:  
        parts.extend([0] * (4 - len(parts)))  
    return "{}.{}.{}.{}".format(parts[3], parts[2], parts[1], parts[0])

def ip_expand(ip):

    #去除IP内空格字符
    ip_str=ip.strip().replace(' ','')

    #斜杆类IP转换,IP只要在地址范围内都适用，无需 全零地址/掩码
    if ip_str.find('/')!=-1:
        ip_temp,mask=ip_str.split('/')
        ip_res=list(i.strNormal() for i in IP(IP(ip_temp).make_net(mask).strNormal()))

    #横杠类IP转换,支持横杠前后不在同一个c段的转换
    elif ip_str.find('-')!=-1:
        ip_res=[]
        ip_start_int,ip_end_int=list(ip_to_int(i) for i in (ip_str.split('-')))

        for ip in range(ip_start_int,ip_end_int+1):
            ip_res.append(int_to_ip(ip))
    else:
        ip_res=[ip]

    return ip_res


if __name__ == '__main__':

    print(ip_expand('192.168.1.35/29'))
    print(ip_expand('192.168.2.252-192.168.3.11'))
    print(ip_expand('192.168.3.6'))


#['192.168.1.32', '192.168.1.33', '192.168.1.34', '192.168.1.35', '192.168.1.36', '192.168.1.37', '192.168.1.38', '192.168.1.39']
#['192.168.2.252', '192.168.2.253', '192.168.2.254', '192.168.2.255', '192.168.3.0', '192.168.3.1', '192.168.3.2', '192.168.3.3', '192.168.3.4', '192.168.3.5', '192.168.3.6', '192.168.3.7', '192.168.3.8', '192.168.3.9', '192.168.3.10', '192.168.3.11']
#['192.168.3.6']
