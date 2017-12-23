#def configuration_options(option='trunk', vpc=False, vrf=False):
def configuration_options(option='L2', vpc='yes', vrf=False, pc=False):
    if option == 'L2' and pc:
        return """!
                interface ethernet {int_number}
                 description :NAME={desc_name} :LN={link_number} :PEER_DEVICE={peer_device} :PEER_PORT={peer_port}
                 channel-group {pc_number} force mode {pc_mode}
                 no shutdown
                !\n"""
    elif option == 'L2' and not pc:
        return """!
                interface ethernet {int_number}
                 description :NAME={desc_name} :LN={link_number} :PEER_DEVICE={peer_device} :PEER_PORT={peer_port}
                 switchport
                 switchport mode trunk
                 switchport trunk allowed vlan {allowed_vlans}
                 no shutdown
                !\n"""
    elif option == 'L3' and pc:
        return """!
                interface ethernet {int_number}
                 description :NAME={desc_name} :LN={link_number} :PEER_DEVICE={peer_device} :PEER_PORT={peer_port}
                 channel-group {pc_number} force mode {pc_mode}
                 no shutdown
                !\n"""
    elif option == 'L3' and not pc and not vrf:
        return """!
                    interface ethernet {int_number}
                     description :NAME={desc_name} :PEER_DEVICE={peer_device} :PEER_PORT={peer_port}
                     no switchport
                     ip address {ip_address}
                     no shutdown
                    !\n"""
    elif option == 'L3' and not pc and vrf:
        return """!
                    interface ethernet {int_number}
                     description :NAME={desc_name} :PEER_DEVICE={peer_device} :PEER_PORT={peer_port}
                     no switchport
                     vrf member {vrf_name}
                     ip address {ip_address}
                     no shutdown
                    !\n"""
    elif option == 'not_in_use':
        return """!
                    interface ethernet {int_number}
                     shutdown
                    !\n"""