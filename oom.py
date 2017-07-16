'''
Onion Omega 2 Monitor v0.1

Program that periodically monitors, records, and stores information about the Onion Omega 2

Github.com/OGLinuk/oom

Update - v0.2
    Cut out unnecessary code
    Added processCommunication() method to cut out repetitive code
'''
import subprocess
import time
import logging

def processCommunication(prSubprocess):
    # https://stackoverflow.com/a/3503909
    _proc = subprocess.Popen(['%s' % (prSubprocess)], stdout=subprocess.PIPE, shell=True)
    exe_proc = _proc.communicate()
    return exe_proc

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
    # transmitted bytes
    tx_bytes = 'ifconfig apcli0 | awk \'{print $5 $6}\' | grep "TXbytes:"'
    rx_bytes = 'ifconfig apcli0 | awk \'{print $1 $2}\' | grep "RXbytes:"'
    # transmitted packets
    tx_packets = 'ifconfig apcli0 | awk \'{print $1 $2}\' | grep "TXpackets:"'
    rx_packets = 'ifconfig apcli0 | awk \'{print $1 $2}\' | grep "RXpackets:"'

    while True:
        # System variables
        _ipv4_omega2 = processCommunication(ipv4_omega2)
        _uptime_omega2 = processCommunication(uptime_omega2)
        _cpu = processCommunication(cpu_usage)
        _mem_usage = processCommunication(mem_info_usage)
        _mem_available = processCommunication(mem_info_available)
        _tx_bytes = processCommunication(tx_bytes)
        _rx_bytes = processCommunication(rx_bytes)
        _tx_packets = processCommunication(tx_packets)
        _rx_packets = processCommunication(rx_packets)

        print()
        print('IPv4: %s' % (str(_ipv4_omega2[0], 'UTF-8')))
        print('Uptime (M): %s' % (str(_uptime_omega2[0], 'UTF-8')))
        logger.info('Uptime: %s' % (str(_uptime_omega2[0], 'UTF-8')))
        print('CPU Usage: %s' % (str(_cpu[0], 'UTF-8')))
        logger.info('CPU Usage: %s' % (str(_cpu[0], 'UTF-8')))
        print('Memory Usage: %s' % (str(_mem_usage[0], 'UTF-8')))
        logger.info('Memory Usage: %s' % (str(_mem_usage[0], 'UTF-8')))
        print('%s' % (str(_mem_available[0], 'UTF-8')))
        logger.info('%s' % (str(_mem_available[0], 'UTF-8')))
        print(str(_tx_bytes[0], 'UTF-8'))
        logger.info('%s' % (str(_tx_bytes[0], 'UTF-8')))
        print(str(_tx_packets[0], 'UTF-8'))
        logger.info('%s' % (str(_tx_packets[0], 'UTF-8')))
        print(str(_rx_bytes[0], 'UTF-8'))
        logger.info('%s' % (str(_rx_bytes[0], 'UTF-8')))
        print(str(_rx_packets[0], 'UTF-8'))
        logger.info('%s' % (str(_rx_packets[0], 'UTF-8')))
        print('----------------------------')
        time.sleep(0.5)

if __name__ == '__main__':
    main()
