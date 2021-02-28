from speedtest import Speedtest
import socket
import sys


def scanOpenPorts():  # FIXME
    try:
        for port in range(1, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((socket.gethostbyname(sys.argv[1]), port))
            if result == 0:
                yield port
            s.close()
    except socket.gaierror:
        return "Hostname Could Not Be Resolved"
    except socket.error:
        return "Server not responding"


def calculateNetworkSpeedTest():
    inet = Speedtest()
    return {
        "uploadSpeed": float(str(inet.upload())[0:2] + "." + str(round(inet.upload(), 2))[1]) * 0.125,
        "downloadSpeed": float(str(inet.download())[0:2] + "." + str(round(inet.download(), 2))[1]) * 0.125
    }


def settleSshHoneyPot():  # TODO: tests required
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((socket.gethostbyname(socket.gethostname()), 23))
    sock.listen()
    connection, address = sock.accept()
    print(address)
