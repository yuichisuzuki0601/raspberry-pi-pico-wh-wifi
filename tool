#!/bin/sh
cd `dirname $0`

function ip() {
	ifconfig en0 | awk '$1 == "inet" {print $2}'
}

function device() {
    ./device-ts/tool s
}

function server() {
    yarn start
}

. ./lib/shell/execute
