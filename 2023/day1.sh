#!/bin/sh
sed 's/[^0-9]//g' | awk '{x+=int(substr($0,length($0),1))+10*int(substr($0,1,1))} END {print x}'
