from speedtest import Speedtest


def calculate():
    inet = Speedtest()
    return {
        "uploadSpeed": float(str(inet.upload())[0:2] + "." + str(round(inet.upload(), 2))[1]) * 0.125,
        "downloadSpeed": float(str(inet.download())[0:2] + "." + str(round(inet.download(), 2))[1]) * 0.125
    }
