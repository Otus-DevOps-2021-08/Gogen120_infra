#!/usr/bin/python3

import argparse
import json
import subprocess


def list_dynamic_invemtory():
    dynamic_inventory = {}
    output = subprocess.Popen('yc compute instance list --format json', shell=True, stdout=subprocess.PIPE)
    json_output, _ = output.communicate()
    yandex_instnces = json.loads(json_output)
    for instance in yandex_instnces:
        service_name = instance['name'].split('-')[-1]
        service_ip = instance['network_interfaces'][0]['primary_v4_address']['one_to_one_nat']['address']
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
