resource "yandex_lb_target_group" "target_group" {
  name      = "reddit-target-group"
  region_id = "ru-central1"

  dynamic "target" {
    for_each = yandex_compute_instance.app
    content {
      subnet_id = var.subnet_id
      address   = target.value.network_interface.0.ip_address
    }
  }

  depends_on = [
    yandex_compute_instance.app
  ]
}


resource "yandex_lb_network_load_balancer" "lb" {
  name = "reddit-lb"

  listener {
    name        = "reddit-listener"
    port        = var.listener_port
    target_port = var.listener_target_port
    external_address_spec {
      ip_version = "ipv4"
    }
  }

  attached_target_group {
    target_group_id = yandex_lb_target_group.target_group.id

    healthcheck {
      name = "http"
      http_options {
        port = var.listener_target_port
        path = "/"
      }
    }
  }

  depends_on = [
    yandex_lb_target_group.target_group
  ]
}
