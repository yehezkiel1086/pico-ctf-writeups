#!/bin/bash

wget https://challenge-files.picoctf.net/c_fickle_tempest/19722024edeecca10f263776ab05c8b1235b136dcf25aa6e976d3860513ffcd5/garden.jpg
strings garden.jpg | grep picoCTF
