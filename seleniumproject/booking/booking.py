from selenium import webdriver


class Booking(webdriver.Chrome()):
    def __init__(self, driver_path=r"C:/SeleniumDrivers"):
        self.driverpath = driver_path
        super()