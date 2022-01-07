# EkosScripts
A repository of simple job scripts for Ekos

uncap.py:
Simple script to close a dustcover in Ekos

This script requires a motorized dust cover or flat field cover like a FlipFlat

I created this because Ekos does not uncover the scope after taking Flats or Darks, the recommended method is to take the calibration frames at the end of a sequence but this is not practical for focusing reasons especially after a long night and with multiple filters.
This script will uncap the scope if it is capped. The best way to use this script is:
1- as a pre-job script for your first light frame job
2- as a post-job script for your flat frame jobs.
