# Gogen120_infra
Gogen120 Infra repository

## Знакомство с облачной инфраструктурой

**Адреса для подключения**

`bastion_IP = 178.154.223.68`
`someinternalhost_IP = 10.128.0.25`

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
