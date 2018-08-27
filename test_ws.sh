#!/bin/bash

echo "GET root"
curl -i -X GET -H 'Content-Type: application/json' http://localhost:8100/
echo "GET funcOne:"
curl -i -X GET -H 'Content-Type: application/json' http://localhost:8100/funcOne/hello/world
echo "POST funcOne:"
curl -i -X POST -H 'Content-Type: application/json' -d '{"paramOne": "hello", "paramTwo": "world"}' http://localhost:8100/funcOne
echo "GET funcTwo"
curl -i -X GET -H 'Content-Type: application/json' http://localhost:8100/funcTwo/
