import json
import os


class Parameters:

    __json_file = None
    __filename = None

    @classmethod
    def execute_file(cls, filename):
        """Si filename coincide con algún generador, lo ejecuta."""
        try:
            cls.__json_file = None
            file = open(os.path.join(os.path.dirname(__file__), 'generators', '{}.py'.format(filename)))
            exec(file.read())
            file.close()
            cls.__filename = filename
            print("El archivo '{}.json' se ha cargado correctamente.".format(os.path.splitext(filename)[0]))
        except FileExistsError:
            print("No se encontró el archivo {} en 'configs/generators/'" .format(filename))

    @classmethod
    def __load_json(cls, filename):
        """Carga la variable si está vacía y la devuelve, sino sólo la devuelve."""
        if cls.__json_file is None:
            with open(os.path.join(os.path.dirname(__file__), 'JSONS\{}.json'.format(filename)), encoding='utf-8') as file:
                cls.__json_file = json.load(file)
        return cls.__json_file

    @classmethod
    def get_ambiente(cls):
        """Devuelve los parametros de ambiente."""
        data = Parameters.__load_json(cls.__filename)
        return data['ambiente']