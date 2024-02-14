class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnect")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        # super class method to access init class method
        return f"{super().__init__} ({self.remaining_pages}) pages remaining"

    def print(self, pages):
        if not self.connected:
            print("You are not connected")
            return
        self.remaining_pages -= pages


fax = Device("fax", "USB")
print(fax)

printer = Printer("Printer", "USB", 500)
printer.print(50)
print(printer)
printer.disconnect()
