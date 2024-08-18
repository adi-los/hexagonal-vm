#!/bin/bash
HOSTNAME=$(hostname)
CPU=$(nproc)
RAM=$(free -m | awk '/^Mem:/{print $2}')
DISK=$(df -h --total | grep total | awk '{print $2}')

API_URL="http://your_api_endpoint/vm_data"
API_KEY="your_api_key"

curl -X POST "$API_URL" \
     -H "Authorization: Bearer $API_KEY" \
     -H "Content-Type: application/json" \
     -d "{\"hostname\":\"$HOSTNAME\",\"cpu\":\"$CPU\",\"ram\":\"$RAM\",\"disk\":\"$DISK\"}"
