from speedtest import Speedtest
import socket


def calculateNetworkSpeedTest():
    inet = Speedtest()
    return {
        "uploadSpeed": float(str(inet.upload())[0:2] + "." + str(round(inet.upload(), 2))[1]) * 0.125,
        "downloadSpeed": float(str(inet.download())[0:2] + "." + str(round(inet.download(), 2))[1]) * 0.125
    }


def settleSshHoneyPot():  # TODO: tests required
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((socket.gethostbyname(socket.gethostname()), 22))
    sock.listen()
    connection, address = sock.accept()
    print("{} {}".format(connection, address))


if __name__ == "__main__":
    settleSshHoneyPot()
