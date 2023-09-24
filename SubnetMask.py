
ip = str(input("Net IP : "))

sub  = int(input("Subnet : "))

host = int(input("Host : "))

print(ip,sub,host)

def new_netmask(host):
    
    for i in range(0,199):
        nearestHost = pow(2,i) - 2
        if(host <= nearestHost):
            print("Host : ",pow(2,i) - 2, "\n n Bit : ", i)
            n_bit = i
            break
        
    print("new Netmask : ", 32 - n_bit)
    return n_bit, 32-n_bit
    
def net_host(n_bit, n_netmask, sub_kelas):
    print("Host bit (n) : ", n_bit)
    
    print("Jumlah Host  : ", pow(2,n_bit) - 2)

    m = n_netmask - sub_kelas
    print("Network Bit(m) : ", m)

    print("Jumlah Network : ", pow(2,m))


def get_interval(n_netmask):
    
    sisa_bagi = n_netmask % 8
    hasil_bagi = (n_netmask - n_netmask % 8) / 8
    print("KELAS : ", hasil_bagi)
    hasil = ""

    for i in range(0,sisa_bagi):
        hasil = hasil + ("1")

    for i in range(0, 8 - sisa_bagi):
        hasil = hasil + ("0")

    dec = 0
    for digit in hasil:
        dec = dec * 2 + int(digit) #turn into binary


    interval = ""
    for i in range(0,4):
        if(i == hasil_bagi):
            interval = interval + str(dec)
        elif(i < hasil_bagi ): 
            interval = interval + "255"
        else:
            interval = interval + "0"
        if(i != 3):
            interval = interval + "."

    interval_r = ""
    for i in range(0,4):
        if(i == hasil_bagi):
            interval_r = interval_r + str(256 - dec)
        else: 
            interval_r = interval_r + "0"
        if(i != 3):
            interval_r = interval_r + "."


    print("Interval : ",interval)
    print("Interval Range :",interval_r)
    # n_interval = 
    return interval, interval_r

# def new_ip(ip, inter,inter_r):
#     ip = ip.split('.')

# Fungsi untuk melakukan operasi bitwise AND pada dua alamat IP
def bitwise_and_ip(ip1, ip2):
    ip1_parts = [int(part) for part in ip1.split('.')]
    ip2_parts = [int(part) for part in ip2.split('.')]
    
    result_parts = []
    for i in range(4):
        result_parts.append(ip1_parts[i] & ip2_parts[i])
    
    result_ip = '.'.join(map(str, result_parts))
    print("new IP : " ,result_ip)
    return result_ip

def generate_interval(base_ip, interval, jumlah):
    base_ip_parts = [int(part) for part in base_ip.split('.')]
    interval_parts = [int(part) for part in interval.split('.')]
    
    new_interval = []

    for i in range(jumlah):
        subnet_parts = []
        
        for j in range(4):
            subnet_parts.append(str(base_ip_parts[j] + interval_parts[j] * i))
            
        subnet = '.'.join(subnet_parts)
        subnet_cidr = f"{subnet}"
        new_interval.append(subnet_cidr)

    return new_interval

hasil_bit , hasil_netmask = new_netmask(int(host))

net_host(hasil_bit , hasil_netmask, sub)

interval, interval_r = get_interval(hasil_netmask)


ip_address = ip
ip_address = bitwise_and_ip(ip_address, interval)

subnets = generate_interval(ip_address, interval_r, 5)

for subnet in subnets:
    print(subnet, end=", ") # MAKS 256 masih error <3 by Reza!

