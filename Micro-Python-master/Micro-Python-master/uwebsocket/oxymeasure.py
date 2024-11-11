import max30100
mx30 = max30100.MAX30100()

mx30.read_sensor()

# The latest values are now available via .ir and .red
print(mx30.ir)
print(mx30.red)

mx30.set_mode(max30100.MODE_SPO2)
mx30.read_sensor()
print(mx30.ir)
print(mx30.red)