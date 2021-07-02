# Challenge

## Pre-requisitos
- Tener [Python](https://www.python.org/) instalado
- Tener [pip](https://pip.pypa.io/en/stable/installing/) instalado

## Instalar dependencias
En la ruta `(Directorio local)/mercantilAndina/`
```sh
$ pip install -r requirements.txt
```

## Descargar ChromeDriver

Click [acá](https://chromedriver.chromium.org/) para descargar ChromeDriver.
Luego, descomprimir el archivo y pegar `chromedriver.exe` en `(Directorio local)/mercantilAndina/`

> Tener en cuenta que la versión del ChromeDriver debe ser la misma que la versión del Chrome instalado en nuestra PC.
Es recomentable usar siempre la última versión estable de ambos.

## Ejecutar tests individuales

Para ejecutar los tests individuales, se deberá abrir una terminal y ejecutar el comando deseado en la ruta `(Directorio local)/mercantilAndina/`

```sh
$ behave -D test=mercantilAndina --tags=cotizar
```

## Etiquetas

```sh
@cotizar
```

## Tests Backend

Para correr los test de backend sólamente se debe ejecutar `backend.py`

