london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

dev_name = input("Enter the device name: ")
dev_name_vocab = london_co[dev_name]
dev_args = list(dev_name_vocab.keys())
dev_args = ", ".join(dev_args)
dev_param = input("Enter the parameter ({}): ".format(dev_args)).lower()
print(dev_name_vocab.get(dev_param, "The parameter is missing"))