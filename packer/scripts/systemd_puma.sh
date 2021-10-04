#!/bin/bash
mv /tmp/puma.service /etc/systemd/system/puma.service
systemctl daemon-reload
systemctl enable puma
