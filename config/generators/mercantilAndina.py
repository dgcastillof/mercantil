import os
import json

__data = {
    "ambiente":
        {
            "url": "https://www.mercantilandina.com.ar/",
        }
}

try:
    with open(os.path.join(os.path.dirname(__file__), r'JSONS\mercantilAndina.json'), 'w', encoding='utf-8') as file:
        json.dump(__data, file, indent=4, ensure_ascii=False)
        print("El archivo 'mercantilAndina.json' se ha generado correctamente.")
except Exception as e:
    print("Error al intentar ejectuar 'mercantilAndyna.py': ", e)
