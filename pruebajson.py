import json

filename = 'manager.json'
entry = {
  "Pepe": {
    "Edad": 34,
    "Hobbies": ["Patinaje","Hockey"]
  }
}
    # Intentamos abrir el archivo JSON para cargar los datos existentes
with open(filename, 'r') as file:
    data = json.load(file)
        # Cargamos los datos existentes del archivo en un diccionario llamado data

# Actualizamos el diccionario data con la nueva entrada
data.update(entry)

# Guardamos el diccionario actualizado en el archivo JSON
with open(filename, 'w') as file:
    json.dump(data, file, indent=4)

print("Nueva entrada guardada correctamente junto con los datos existentes.")