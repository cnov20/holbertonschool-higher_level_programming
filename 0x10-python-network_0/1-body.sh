#!/bin/bash
#Sends 'curl' request to URL / displays response body - only w/ 200 OK status
curl -iL "$1"
