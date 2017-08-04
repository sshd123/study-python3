# -*- coding: utf-8 -*-

message_zh_cn = '~/messages.properties'
message_zh_tw = '~/messages2.properties'


def get_maps(message_file):
    maps = {}
    for line in open(message_file):
        if '=' in line:
            split = line.split('=')
            k, v = split[0], split[1]
            maps[k] = v
    return maps


def write_file(message_file, data):
    with open(message_file, 'a') as f:
        f.writelines(data)


def get_lines(keys, maps):
    return ['{}={}'.format(k, maps.get(k)) for k in keys]


if __name__ == '__main__':
    zh_cn_maps = get_maps(message_zh_cn)
    zh_tw_maps = get_maps(message_zh_tw)
    not_in_tw = zh_cn_maps.keys() - zh_tw_maps.keys()
    not_in_cn = zh_tw_maps.keys() - zh_cn_maps.keys()
    print(not_in_tw)
    print(not_in_cn)
    write_file(message_zh_tw, get_lines(not_in_tw, zh_cn_maps))
    write_file(message_zh_cn, get_lines(not_in_cn, zh_tw_maps))
