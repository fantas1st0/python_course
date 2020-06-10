ip_add = input("Enter the ip address in format X.X.X.X/Z: ")

subnet = ip_add.split("/")[0]
subnet_mask = ip_add.split("/")[1]

subnet_list = subnet.split(".")
oct1 = subnet_list[0]
oct2 = subnet_list[1]
oct3 = subnet_list[2]
oct4 = subnet_list[3]

subnet_mask_int = int(subnet_mask)
interesting_octet = int(subnet_mask_int/8)
subnet_mask_str = "1" * int(subnet_mask)
num_zeros = 32 - subnet_mask_int
num_zeros_str = "0" * num_zeros
subnet_mask_str = subnet_mask_str + num_zeros_str
mask_oct1 = subnet_mask_str[:8]   
mask_oct2 = subnet_mask_str[8:16] 
mask_oct3 = subnet_mask_str[16:24] 
mask_oct4 = subnet_mask_str[24:32]

oct1 = int(oct1) & int(mask_oct1, 2)
oct2 = int(oct2) & int(mask_oct2, 2)
oct3 = int(oct3) & int(mask_oct3, 2)
oct4 = int(oct3) & int(mask_oct4, 2)

print("Network:")
print("{:<8} {:<8} {:<8} {:<8}".format(oct1, oct2, oct3, oct4))
print("{:08b} {:08b} {:08b} {:08b} \n".format(oct1, oct2, oct3, oct4))

print("Mask:")
print(subnet_mask)
print("{:8} {:8} {:8} {:8}".format(str(int(mask_oct1, 2)), str(int(mask_oct2, 2)), str(int(mask_oct3, 2)), str(int(mask_oct4, 2))))
print("{:8} {:8} {:8} {:8}".format(mask_oct1, mask_oct2, mask_oct3, mask_oct4))