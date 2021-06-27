class IP_address:
    def __init__(self, name, ip, status, modify):
        self.name = name
        self.ip = ip
        self.status = status
        self.modify = modify

    def __str__(self):
        return self.name + " " + self.ip + " " + str(self.status) + " " + str(self.modify)

    def print_all_addresses(addresses):
        for address in addresses:
            print(addresses[address])
    def get_name(self):
        return self.name

    def get_ip(self):
        return self.ip

    def get_status(self):
        return self.status

    def get_modify(self):
        return self.modify

    def set_status(self, new_status):
        self.status = new_status

    def set_modify(self, new_modify):
        self.modify = new_modify


# class All_addresses:
#     def __init__(self, number_of_addresses, list_of_all_addresses):
#         number_of_addresses = 0
#         list_of_all_addresses = 0
#
#     def get_number_of_addresses(self):
#         return self.number_of_addresses
#
#     def get_list_of_all_addresses(self):
#         return self.llist_of_all_addresses
#
#     def add_address(self, new_address):
#         self.number_of_addresses +=1
#         self.list_of_all_addresses.append(new_address)
