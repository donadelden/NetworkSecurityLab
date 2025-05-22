import easymodbus.modbusClient 

TARGET_IP = "localhost"

plc1 = easymodbus.modbusClient.ModbusClient(TARGET_IP, 502)
plc1.connect()

print("Reading from PLC...")
inputRegisters = plc1.read_inputregisters(0, 3)
coils = plc1.read_coils(0, 3)
print("Input Registers: ", inputRegisters)
print("Coils: ", coils)

plc1.close()

#print("Writing to PLC...")
#plc1.write_single_coil(0, True)