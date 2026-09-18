########### builder design pattern ###############

# without builder design pattern
class Laptop:
    def __init__(
        self,
        cpu,
        ram,
        storage,
        gpu=None,
        wifi=False,
        bluetooth=False,
        webcam=False
    ):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu
        self.wifi = wifi
        self.bluetooth = bluetooth
        self.webcam = webcam

    def __repr__(self):
        return str(vars(laptop))
laptop = Laptop(
    "Intel i9",
    "32GB",
    "1TB SSD",
    "RTX 4090",
    True,
    True,
    True
)

print(laptop)





# builder design pattern 

class Laptop:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None
        self.wifi = False
        self.bluetooth = False
        self.webcam = False

    def show(self):
        print(vars(self))

class LaptopBuilder:

    def __init__(self):
        self.laptop = Laptop()

    def set_cpu(self, cpu):
        self.laptop.cpu = cpu
        return self

    def set_ram(self, ram):
        self.laptop.ram = ram
        return self

    def set_storage(self, storage):
        self.laptop.storage = storage
        return self

    def set_gpu(self, gpu):
        self.laptop.gpu = gpu
        return self

    def enable_wifi(self):
        self.laptop.wifi = True
        return self

    def enable_bluetooth(self):
        self.laptop.bluetooth = True
        return self

    def enable_webcam(self):
        self.laptop.webcam = True
        return self

    def build(self):
        return self.laptop



laptop = (
    LaptopBuilder()
        .set_cpu("Intel i9")
        .set_ram("32GB")
        .set_storage("1TB SSD")
        .set_gpu("RTX 4090")
        .enable_wifi()
        .enable_bluetooth()
        .build()
)

laptop.show()
