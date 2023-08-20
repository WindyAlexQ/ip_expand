from IPy import IP

def ip_expand(ip):

    #去除IP内空格字符
    ip_str=ip.strip().replace(' ','')

    #斜杆类IP转换,IP只要在地址范围内都适用，无需 全零地址/掩码
    if ip_str.find('/')!=-1:
        ip_temp,mask=ip_str.split('/')
        ip_res=list(i.strNormal() for i in IP(IP(ip_temp).make_net(mask).strNormal()))

    #横杠类IP转换,目前仅支持横杠前后在同一个c段
    elif ip_str.find('-')!=-1:
        ip_res=[]
        ip_start,ip_end=ip_str.split('-')
        ip_start_sp=ip_start.split('.')
        ip_end_sp=ip_end.split('.')

        assert(ip_start_sp[0]==ip_end_sp[0])
        assert(ip_start_sp[1]==ip_end_sp[1])
        assert(ip_start_sp[2]==ip_end_sp[2])

        for i in range(int(ip_start_sp[3]),int(ip_end_sp[3])+1):
            ip_res.append('.'.join([ip_start_sp[0],ip_start_sp[1],ip_start_sp[2],str(i)]))
    else:
        ip_res=[ip]

    return ip_res


if __name__ == '__main__':

    print(ip_expand('192.168.1.35/29'))
    print(ip_expand('192.168.2.25-192.168.2.35'))
    print(ip_expand('192.168.3.6'))

# ['192.168.1.32', '192.168.1.33', '192.168.1.34', '192.168.1.35', '192.168.1.36', '192.168.1.37', '192.168.1.38', '192.168.1.39']
# ['192.168.2.25', '192.168.2.26', '192.168.2.27', '192.168.2.28', '192.168.2.29', '192.168.2.30', '192.168.2.31', '192.168.2.32', '192.168.2.33', '192.168.2.34', '192.168.2.35']
# ['192.168.3.6']
