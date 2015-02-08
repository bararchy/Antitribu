@echo off
title Clear dir from trash

if exist *.bsp del /a /q *.bsp
if exist *.prt del /a /q *.prt
if exist *.lin del /a /q *.lin
if exist *.gl  del /a /q *.gl 
if exist *.vmx del /a /q *.vmx
if exist *.log del /a /q *.log

echo Trash deleted.
exit
