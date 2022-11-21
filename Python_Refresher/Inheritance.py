class Device:
    def __init__(self,name,connected_by):
        self.name=name
        self.connected_by=connected_by
        self.connected=True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected=False
        print("Disconnected")


class Printer(Device):
    def __init__(self,name,connected_by,capacity):
        super().__init__(name,connected_by)
        self.capacity=capacity
        self.remaining_pages=capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} remaining pages)"

    def printing(self,pages):
        if not self.connected :
            print("Your printer is not connected")
            return 
        print(f"printing {pages} pages")
        self.remaining_pages-=pages


d1=Device("Printer","USB")
print(d1)
d1.disconnect()

p1=Printer("Printer","USB",500)
p1.printing(20)

print(p1)

p1.disconnect()
p1.printing(20)