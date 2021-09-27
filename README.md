# Gogen120_infra
Gogen120 Infra repository

## Знакомство с облачной инфраструктурой

**Адреса для подключения**

bastion_IP = 178.154.223.68
someinternalhost_IP = 10.128.0.25

### Дополнительное задание №1

**Подключение в одну команду**

Подключиться можно с помощью опции `-J`: `ssh -i ~/.ssh/appuser -A -J appuser@<bastion_IP> appuser@<someinternalhost_IP>`

**Подключение через алиас**

Для подключения через команду `ssh someinternalhost` нужно добавить следующие строки в ssh конфиг файл (`~/.ssh/config`)

```bash
Host bastion
    HostName 178.154.223.68
    User appuser
    Port 22
    IdentityFile ~/.ssh/appuser

Host someinternalhost
    HostName 10.128.0.25
    User appuser
    Port 22
    IdentityFile ~/.ssh/appuser
    ProxyJump bastion
```

### Дополнительное задание №2

Сертификат выдан для https://178.154.223.68.sslip.io/

## Деплой тестового приложения

testapp_IP = 62.84.116.216
testapp_port = 9292

### Дополнительное задание

Для создания сервера со всем необходимым для запуска тестового приложения можно использовать `startup_script.sh` или следующую команду в CLI:

```bash
yc compute instance create \
  --name reddit-app \
  --hostname reddit-app \
  --memory=4 \
  --create-boot-disk image-folder-id=standard-images,image-family=ubuntu-1604-lts,size=10GB \
  --network-interface subnet-name=default-ru-central1-a,nat-ip-version=ipv4 \
  --metadata serial-port-enable=1 \
  --metadata-from-file user-data=./metadata.yml
```
