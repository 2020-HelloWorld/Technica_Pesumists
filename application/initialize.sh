#!/bin/bash
cd tcp_override
make clean
make
cd ..

cd ttl_detect
make clean
make 
cd ..

cd ttl_prevent
make clean
make 
cd ..

