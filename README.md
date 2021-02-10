# Q-learning  
Af Camilla Frank og Sebastian Cloos Hylander
 - camillafrank10@gmail.com
 - hylandersebastian@gmail.com

**Biblioteker**  
For at køre dette program, skal der bruges bibliotekerne:  
 - numpy
 - pygame


**Kør programmet**  
Programmet køres via. en kommandoprompt, hvor der skal skrives:  
Windows:
```
python mouse_game.py
```
MacOS/Linux:
```
python3 mouse_game.py
```

**Selve programmet**  
Når programmet kører, kan man se en mus, der leder efter en ost, uden at blive fanget af kattene.  
Hvis du vil ændre på hastigheden af simulationen, kan du trykke på *+* eller *-*

**Skift bane**  
Inde i selve kode, er der mulighed for at skifte banen, musen løber i.
Der er 5 forskellige baner, den kan prøve:
 - *stage.png*
 - *stage_2.png*
 - *stage_3.png*
 - *stage_4.png*

Du ændrer banen ved at skrive den valgte bane ind i *mouse_game.py*, linje 8:  
```
stage = pg.image.load("stage.png")
```
