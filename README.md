# VLSM séma alapú alhálózat osztó

Nem célja kiváltani a hálózatok alapjai tantárgyra való tanulást és megértést. Szimplán azért írtam ezt a csodás scriptet mert nem volt kedvem állandóan számolgatni. Ember könnyen hibázik véletlenül, a gép már kevésbé.

## Így használd

- py subnet.py ip maszk_hossz
- ha két router közé kell egy **link** (összekötés) azt mindig **1** gépszámmal jelöld (furán lesz ugyan kiírva de így fogsz két címet kapni.)
- többi a lenti kép alapján egyértelmű

![preview](/assets/preview.png)

# IP MASZK mindent is tudó

Egy adott IP/maszk_hossz-ról megmondja a fontosabb információkat is.
Ha véletlen netid vagy broadcast címről lenne szó, olyan jófej a program, hogy még arra is figyelmeztet.

## Így használd

- py net_bc.py
- beiírod az ip/maszkot ebben a formában x.x.x.x/m ahol az **x.x.x.x** az IPv4 cím és az **m** a maszk hossz bitekben.
- többi itt van a képen

![preview](/assets/preview2.png)