import os, json

filename = ".fs"

def set(name, value):
  if os.path.exists(filename):
    with open(filename, "r") as file:
      data = json.load(file)
  else:
    data = {}
    
  data.update({name: value})
  with open(filename, "w") as file:
    json.dump(data, file, indent=4)

def get(name):
  if os.path.exists(filename):
    with open(filename, "r") as file:
      data = json.load(file)
      return data[name]
  else:
    return None
      
