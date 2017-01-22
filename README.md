# R1D1
Cool robot, that runs trough the office

### 1. Running lights 

#### <i class="icon-refresh"></i> GPIO

connect LEDs to following ports and plug 330 ohm resistance to each LED.

LED id     | GPIO id
-------- | ---
0 | 03
1 | 05
2 | 07
3 | 11
4 | 13
5 | 15
6 | 17
7 | 19
8 | 21
9 | 23  

To run use

```sh
$ sudo python lights.py
```