class Config:
    # ==================================================================
    # SOCKET configuration
    # ==================================================================
    SERVER = "192.168.178.75"  # SERVER = "127.0.0.1"
    PORT = 4000

    TIMEOUT_RECONNECTING = 30
    DELAY_RETRY_CONNECTING = 2

    ENCODING = "utf-8"
    MSG_LENGTH = 1024

    # ==================================================================
    # Program Handler configuration
    # ==================================================================
    PATH_DATA = "data/data.json"

    # ==================================================================
    # Sync configuration
    # ==================================================================
    USE_PC = False
    PATH_PC = "/home/max/Schreibtisch/Python/PiCar/pi"
    PATH_LAPTOP = "C:/Users/Max/Desktop/Daten/Python/PiCar/pi"

    PATH_PI = "/home/pi/PiCar"  # "C:/Users/Max/Desktop/Test"
