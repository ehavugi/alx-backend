#!/bin/bash
# with npm run dev 100-seat.js 
# running, the the following commands
#get available seats
curl localhost:1245/available_seats ; echo ""

# reseve a seat
curl localhost:1245/reserve_seat ; echo ""

# get process
curl localhost:1245/process ; echo ""

curl localhost:1245/available_seats ; echo ""

# Reseve all seats
for n in {1..50}; do curl localhost:1245/reserve_seat ; echo ""; done
