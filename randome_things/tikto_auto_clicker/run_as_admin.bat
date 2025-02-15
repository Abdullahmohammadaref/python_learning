@echo off
PowerShell -Command "Start-Process cmd -ArgumentList '/k python \"%~dp0auto_clicker_v2.py\"' -Verb RunAs"