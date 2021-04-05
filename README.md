# pyelectron
Prototipo que junta una aplicacion web con un navegador hecho en pyqt5 "simulando" una aplicacion hecha como en electron


## Como miercoles uso esto

Primero instala las librerias

```
pip install -r requirements.txt
```

despues ejecutas el archivo app.py
```
python app.py
```

y por ultimo pyqtbrowser.py
```
python pyqtbrowser.py
```

Sino me equivoco en GNU/Linux tienes que cambiar ```python``` por ```python3``` y ```pip``` por ```pip3```

### funciona en python 3.8.9

![image](https://user-images.githubusercontent.com/58951699/113525922-1c711600-958e-11eb-99fc-4d91e0618049.png)

### Errores
Si tienes un error abre un Issue, lo mas probable es que no te lo responda porque ni yo tengo idea de como funciona esta cosa pero bueno XD

### Licencia
no lo vendas (a quien se lo vendia re poronga esto) pero libre de usar en lo que quieras

### Notas

ya se que no tiene nada que ver esto con electron pero me hace recordar la forma en como funciona electron y no pude resistirme

Al parecer PyQt5 da error al no cargar un icono (favicon.ico) (?

Otra cosa que vi es que si intento correr el archivo ```pyqtbrowser.py``` sin antes abrirlo en Visual Studio Code, me da error y pone ```Python a dejado de funcionar``` deberia investigar eso
