record_collection = {
  2548: {
    'albumTitle': 'Slippery When Wet',
    'artist': 'Bon Jovi',
    'tracks': ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    'albumTitle': '1999',
    'artist': 'Prince',
    'tracks': ['1999', 'Little Red Corvette']
  },
  1245: {
    'artist': 'Robert Palmer',
    'tracks': []
  },
  5439: {
    'albumTitle': 'ABBA Gold'
  }
}

def update_records(record_collection, id, property, value):

  if id in record_collection:
    album = record_collection[id]
  
    if property != "tracks" and value != "":
      album[property] = value

    elif property == "tracks" and "tracks" not in album:
      album["tracks"] = []
      album["tracks"].append(value)
   
    elif property == "tracks" and value != "":
      album["tracks"].append(value)
       
    elif value == "":
      print("delete property: ", property)
      del album[property]
  else:
    if value != "":
      record_collection[id] = {property: value}

  return record_collection
