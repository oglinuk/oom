'''
Onion Omega 2 Monitor

Program that periodically monitors, records, and stores information about the Onion Omega 2

Github.com/OGLinuk/oom
'''
import subprocess
import time
import logging

def main():

    # logger config
    logger = logging.getLogger('OOM')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s.%(name)s.%(levelname)s.%(message)s')
    file_handler = logging.FileHandler('oomLogs.txt')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    ipv4_omega2 = 'ifconfig apcli0 | awk \'{print $1 $2}\' | grep "inetaddr:"'
    # https://askubuntu.com/a/335682
    uptime_omega2 = "awk '{print $1/60}' /proc/uptime"
    # https://stackoverflow.com/a/9229580
    cpu_usage = 'grep "cpu" /proc/stat | awk \'{usage=($2+$4)*100/($2+$4+$5)} END {print usage "%"}\''
    # https://stackoverflow.com/a/10586020
    mem_info_usage = 'free | grep Mem | awk \'{print $3/$2 * 100 "%"}\''
    # https://stackoverflow.com/a/29811379
    mem_info_available = 'awk \'$3=="kB"{$2=$2/1024;$3="MB"} 1\' /proc/meminfo | grep "MemAvailable:"'
    # https://www.cyberciti.biz/faq/linux-ethernet-statistics/
    tx_bytes = 'ifconfig apcli0 | awk \'{print $5 $6}\' | grep "TXbytes:"'
    tx_packets = 'ifconfig apcli0 | awk \'{print $1 $2}\' | grep "TXpackets:"'
    rx_bytes = 'ifconfig apcli0 | awk \'{print $1 $2}\' | grep "RXbytes:"'
    rx_packets = 'ifconfig apcli0 | awk \'{print $1 $2}\' | grep "RXpackets:"'

    while True:
        # https://stackoverflow.com/a/3503909
        ipv4_omega2_proc = subprocess.Popen([ipv4_omega2], stdout=subprocess.PIPE, shell=True)
        _ipv4_omega2 = ipv4_omega2_proc.communicate()

        uptime_proc = subprocess.Popen([uptime_omega2], stdout=subprocess.PIPE, shell=True)
        _uptime_omega2 = uptime_proc.communicate()

        cpu_proc = subprocess.Popen([cpu_usage], stdout=subprocess.PIPE, shell=True)
        _cpu = cpu_proc.communicate()

        usage_mem_proc = subprocess.Popen([mem_info_usage], stdout=subprocess.PIPE, shell=True)
        _mem_usage = usage_mem_proc.communicate()

        available_mem_proc = subprocess.Popen([mem_info_available], stdout=subprocess.PIPE, shell=True)
        _mem_available = available_mem_proc.communicate()

        tx_bytes_proc = subprocess.Popen([tx_bytes], stdout=subprocess.PIPE, shell=True)
        _tx_bytes = tx_bytes_proc.communicate()

        rx_bytes_proc = subprocess.Popen([rx_bytes], stdout=subprocess.PIPE, shell=True)
        _rx_bytes = rx_bytes_proc.communicate()

        tx_packets_proc = subprocess.Popen([tx_packets], stdout=subprocess.PIPE, shell=True)
        _tx_packets = tx_packets_proc.communicate()

        rx_packets_proc = subprocess.Popen([rx_packets], stdout=subprocess.PIPE, shell=True)
        _rx_packets = rx_packets_proc.communicate()

        # https://stackoverflow.com/a/43680634
        ipv4 = b'%s' % (_ipv4_omega2[0])
        uptime = b'%s' % (_uptime_omega2[0])
        cpu = b'%s' % (_cpu[0])
        mem_usage = b'%s' % (_mem_usage[0])
        mem_available = b'%s' % (_mem_available[0])
        TXbytes = b'%s' % (_tx_bytes[0])
        RXbytes = b'%s' % (_rx_bytes[0])
        TXpackets = b'%s' % (_tx_packets[0])
        RXpackets = b'%s' % (_rx_packets[0])

        print()
        print(ipv4.decode('UTF-8'))
        print('Uptime(M): %s' % (uptime.decode('UTF-8')))
        logger.info('Uptime: %s' % (uptime.decode('UTF-8')))
        print('CPU Usage: %s' % (cpu.decode('UTF-8')))
        logger.info('CPU Usage: %s' % (cpu.decode('UTF-8')))
        print('Memory Usage: %s' % (mem_usage.decode('UTF-8')))
        logger.info('Memory Usage: %s' % (mem_usage.decode('UTF-8')))
        print(mem_available.decode('UTF-8'))
        logger.info('%s' % (mem_available.decode('UTF-8')))
        print(TXbytes.decode('UTF-8'))
        logger.info('%s' % (TXbytes.decode('UTF-8')))
        print(TXpackets.decode('UTF-8'))
        logger.info('%s' % (TXpackets.decode('UTF-8')))
        print(RXbytes.decode('UTF-8'))
        logger.info('%s' % (RXbytes.decode('UTF-8')))
        print(RXpackets.decode('UTF-8'))
        logger.info('%s' % (RXpackets.decode('UTF-8')))
        print('-----------------------------')
        time.sleep(0.5)

if __name__ == '__main__':
    main()
