# Installation Guide

## Prerequisites
- Anaconda installation version 12.0 or higher

## Step-by-step Guide

1. Navigate to the folder where you would like to install the software and open a terminal \
(if anaconda is not in your $env:PATH environemental variable, you need to either add it or open the anconda3 prompt instead of the system terminal)
2. Enter the following command to clone the repository: 
```
git clone https://github.com/kyk37/ECE1140.git
```
3. Navigate to the new folder titled ECE1140 using the opened terminal
4. Use the following command to create the anaconda environment 'trains': 
```
conda env create -f trains.yml
```
5. The software is now ready to run. The launch the program, run the following commands:
```
conda activate trains
python main.py
```