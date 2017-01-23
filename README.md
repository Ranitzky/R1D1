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

### Usage

To run use

```sh
python lights.py <option>
--c           : cylon mode
--g           : charging mode
--l           : loading mode
--k           : Knight Rider mode
--w           : warning mode
--a           : alarm mode
--d           : demo mode. passes all individual light modes.
--help        : show this message
```

### Modes

#### Cylon

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
1 0 1 0 1 0 1 0 1
0 1 0 1 0 1 0 1 0
```

#### Alert

```sh
1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0
```
