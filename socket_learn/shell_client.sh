#!/bin/sh

#echo "hh Message" > /dev/tcp/127.0.0.1/65432

SOCKET_ADDR='127.0.0.1'
SOCKET_PORT=65432

notify_she() {
  TRIED=0
  while [ $TRIED -lt 3 ]; do
    RESP="$(echo "$1" | nc $SOCKET_ADDR $SOCKET_PORT)"
    echo "resp ${RESP}"

    if [ "$RESP" = "received" ]; then
      echo 'success'
      break
    else
      echo 'fail, sleep 1s and retry'
      TRIED=$((TRIED+1))
      sleep 1
    fi
  done
}


notify_she 'start'



