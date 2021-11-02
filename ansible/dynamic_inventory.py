#!/usr/bin/python3

import argparse
import json


def list_dynamic_invemtory():
    with open('hosts.json') as host_file:
        yandex_instnces = json.load(host_file)

    dynamic_inventory = {}
    for service_name, service_ip in yandex_instnces.items():
        dynamic_inventory[service_name] = {
            'hosts': [service_ip]
        }

    return dynamic_inventory


def host_dynamic_invemtory():
    return {}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--host', action='store')
    args = parser.parse_args()

    if args.list:
        dynamic_inventory = list_dynamic_invemtory()
    elif args.host:
        dynamic_inventory = host_dynamic_invemtory()
    else:
        dynamic_inventory = {}

    with open('inventory.json', 'w') as inventory_file:
        json.dump(dynamic_inventory, inventory_file, indent=2)
    print(json.dumps(dynamic_inventory, indent=2))


if __name__ == '__main__':
    main()
