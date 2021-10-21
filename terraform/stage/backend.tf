terraform {
  backend "s3" {
    endpoint = "storage.yandexcloud.net"
    bucket   = "tfstate-bucket"
    region   = "eu-central-1"
    key      = "terraform.tfstate.stage"

    skip_region_validation      = true
    skip_credentials_validation = true
  }
}
