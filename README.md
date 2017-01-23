# R1D1
Cool robot, that runs trough the office

## 1. Lights control 

### GPIO

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

### Modes

#### Cylon

```sh
$ sudo python lights.py --c
```

```sh
0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 1 0 0
0 0 0 0 0 1 0 0 0
0 0 0 0 1 0 0 0 0
0 0 0 1 0 0 0 0 0
0 0 1 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0
0 0 0 0 1 0 0 0 0
0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 
```

#### Charging

```sh
$ sudo python lights.py --h
```

```sh
0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 1 1
0 0 0 0 0 0 1 1 1
0 0 0 0 0 1 1 1 1
0 0 0 0 1 1 1 1 1
0 0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1 1
0 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 
```

#### Loading

```sh
$ sudo python lights.py --l
```

```sh
0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 1 0 0
0 0 0 0 0 1 0 0 0
0 0 0 0 1 0 0 0 0
0 0 0 1 0 0 0 0 0
0 0 1 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
```

#### Knight Rider

```sh
$ sudo python lights.py --k
```

```sh
0 0 0 0 1 0 0 0 0
0 0 0 1 0 1 0 0 0
0 0 1 0 0 0 1 0 0 
0 1 0 0 0 0 0 1 0
1 0 0 0 0 0 0 0 1
0 1 0 0 0 0 0 1 0
0 0 1 0 0 0 1 0 0
0 0 0 1 0 1 0 0 0
0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 
```

#### Warning

```sh
$ sudo python lights.py --w
```

```sh
1 0 1 0 1 0 1 0 1
0 1 0 1 0 1 0 1 0
```

#### Alert

```sh
$ sudo python lights.py --a
```

```sh
1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0
```

#### Demo

```sh
$ sudo python lights.py --d
```

Run trough all modes.

#### Help

```sh
$ sudo python lights.py --help
```
