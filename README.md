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

## Packer

* Добавлен базовый образ с ruby и mongodb
* Добавил `variable.json`, в котором содержаться необходимые переменные для образа
* Добавил bake-образ c запущенным приложением и всеми зависимостями
* Добавил скрипт `create-reddit-vm.sh` для создания инствнса с готовым приложением из bake-образа

## Terraform 1

* Добавлен `main.tf` файл с созданием 2-х инстансов reddit приложения
* Добавлен `lb.tf` файл с описанием целевой группы и балансировщика
* Добалены файлы `variables.tf` и `variables.tfvars` для описания и определения переменных
* Добавлен `output.tf` файл для выходных переменных терраформа

## Terraform 2

* Добавлены модули `app` и `db` для конфигурации приложения и базы данных, а также соответствующие образа `reddit-app-base` и `reddit-db-base`
* Добавлено описание s3 стораджа в `backend.tf` для хранения стейт файла (для работы юекенда нужно определить `AWS_SECRET_ACCESS_KEY` и `AWS_ACCESS_KEY_ID`)
* Проверено, что конфигурация видна вне репозитория
* Добавлены провижионеры для деплоя приложения
* Добавлена переменная `deploy_app` для отключения провижионеров

## Ansible 1

* Установлен ansible и был добавлен инвентори файл в разных форматах (ini, yaml, json)
* Добавлен `ansible.cfg` для конфигурации ansible
* Добавлен плейбук для выполнения клонирования репозитория reddit
* Добавлен скрипт `dynamic_inventory.py` для динамического создания инвентори

## Ansible 2

* Написаны плейбуки для деплоя приложения
* Первоначальный плейбук был разбит на несколько для более удобного управления
* Переписан скрипт `dynamic_inventory` с использованием `yandexcloud-sdk`, для более удобного получения хостов
* Заменил bash-скрипты на ansible плейбуки в конфигурационных файлах Packer-а
