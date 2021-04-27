#!/bin/python3.6


def get_row(sip_login_str, user_name_str, ip_addr_str):
    sip_login = bytearray(sip_login_str, 'utf-8')
    user_name = bytearray(user_name_str, 'utf-8')
    ip_addr = bytearray(ip_addr_str, 'utf-8')
    group_name = bytearray('Books', 'utf-8')

    sip_login_len = len(sip_login)
    user_name_len = len(user_name)
    ip_addr_len = len(ip_addr)
    group_name_len = len(group_name)

    full_sip_login_len = 16
    full_user_name_len = 2 * 16
    full_ip_addr_len = 16
    full_group_len =  4 * 16 + 8 
    empty_space_len = 6 * 16

    len_sip_login_ending = full_sip_login_len - sip_login_len
    len_sip_user_name_endings = full_user_name_len - user_name_len
    len_ip_addr_endings = full_ip_addr_len - ip_addr_len
    len_group_name_endings = full_group_len - group_name_len

    sip_login += bytearray(len_sip_login_ending)
    user_name += bytearray(len_sip_user_name_endings)
    ip_addr += bytearray(len_ip_addr_endings)
    group_name += bytearray(len_group_name_endings)

    sip_row = bytearray()
    sip_row += sip_login
    sip_row += user_name
    sip_row += ip_addr
    sip_row += bytearray(empty_space_len)
    sip_row += group_name
    return sip_row


if __name__ == '__main__':
    f = open("my_arch.dat", "wb")
    ip_list_file = open("list_address.txt", "r")
    user_name = 2000
    ip_str = ip_list_file.readline()
    while ip_str:
         sip_row = get_row(str(user_name), str(user_name), ip_str)
         user_name += 1
         f.write(sip_row)
         ip_str = ip_list_file.readline()
    ip_list_file.close()   
    f.close()
