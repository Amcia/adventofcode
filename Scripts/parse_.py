def parse_(file_name):
    with open(file_name) as fp:
        for line in fp:
            if line.strip() == '!':
                continue
            else:
                yield line.strip().split(' ')

                #print(line.strip())



if __name__ == '__main__':
    with open('match_ip_pref_out', 'w'):
        pass
    for list_ in parse_('inp'):
        with open('match_ip_pref_out', 'a') as fp:
            fp.write('  match ip address prefix-list {} \n'.format(list_[2]))
