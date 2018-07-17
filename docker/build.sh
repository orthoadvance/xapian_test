#!/bin/sh
docker build . -t xapian_test:latest
docker run xapian_test:latest
