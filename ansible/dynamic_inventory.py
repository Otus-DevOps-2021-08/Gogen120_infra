#! /usr/bin/env python3

import argparse
import json

import yandexcloud
from yandex.cloud.compute.v1.instance_service_pb2 import ListInstancesRequest
from yandex.cloud.compute.v1.instance_service_pb2_grpc import InstanceServiceStub


def list_dynamic_inventory(folder_id):
    with open('key.json') as key_file:
        key = json.loads(key_file.read())

    sdk = yandexcloud.SDK(service_account_key=key)
    instance_service = sdk.client(InstanceServiceStub)
    yandex_insances = instance_service.List(ListInstancesRequest(folder_id=folder_id))
    dynamic_inventory = {}
    internal_db_ip = '127.0.0.1'
    for instance in yandex_insances.instances:
        service_name = instance.name.split('-')[-1]
        service_ip = instance.network_interfaces[0].primary_v4_address.one_to_one_nat.address
        dynamic_inventory[service_name] = {
            'hosts': [service_ip]
        }

        if service_name == 'db':
            internal_db_ip = instance.network_interfaces[0].primary_v4_address.address

    dynamic_inventory['app']['vars'] = {
        'internal_db_ip': internal_db_ip
    }

    return dynamic_inventory


def host_dynamic_invemtory():
    return {}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--host', action='store')
    parser.add_argument('--folder_id', default='b1g33la9fjrrotg3o4n9')
    args = parser.parse_args()

    if args.list:
        dynamic_inventory = list_dynamic_inventory(args.folder_id)
    elif args.host:
        dynamic_inventory = host_dynamic_invemtory()
    else:
        dynamic_inventory = {}

    with open('inventory.json', 'w') as inventory_file:
        json.dump(dynamic_inventory, inventory_file, indent=2)
    print(json.dumps(dynamic_inventory, indent=2))


if __name__ == '__main__':
    main()
