#!/usr/bin/env bash
HOST=$1

ssh-copy-id -i ~/.ssh/pi_rsa.pub pi@${HOST}