#!/bin/bash
apt update && apt install -y git
git clone https://github.com/express42/reddit.git
cd reddit && bundle install
