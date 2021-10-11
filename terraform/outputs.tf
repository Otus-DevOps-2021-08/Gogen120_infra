output "external_ip_address_app" {
  value = [for value in yandex_compute_instance.app : value.network_interface.0.nat_ip_address]
}

output "external_ip_address_lb" {
  value = [for value in yandex_lb_network_load_balancer.lb.listener : tolist(value.external_address_spec).0.address].0
}
