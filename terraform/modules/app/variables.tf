variable public_key_path {
  description = "Path to the public key used for ssh access"
}
variable private_key_path {
  description = "Path to the private key used for ssh connection"
}
variable app_disk_image {
  description = "Disk image for reddit app"
  default     = "reddit-app-base"
}
variable subnet_id {
  description = "Subnets for modules"
}
variable database_ip {
  description = "Database IP to connect"
}
variable deploy_app {
  description = "If true than use provisioners to deploy app"
  default = true
}
