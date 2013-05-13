#!/usr/bin/env bash

apt-get update
apt-get install -y build-essential ruby1.9.1 ruby1.9.1-dev 
gem install rdiscount --no-rdoc --no-ri 
gem install jekyll