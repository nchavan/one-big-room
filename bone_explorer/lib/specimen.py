import digimorph
import json 

def get_view_data():
    specimen_url = 'http://digimorph.org/specimens/anas_platyrhynchos/skull'
    total_slices = 372
    slice_urls = digimorph.get_slice_urls(specimen_url, total_slices)
    return {  
      'imageUrl': digimorph.get_preview_url(specimen_url),
      'scientificName':'Anas platyrhynchos',
      'commonName': 'Domestic Mallard',
      'addedBy': 'Richard Ketcham',
      'addedFor': 'David Dufeau and Timothy Rowe',
      'addedByDate': '5/12/98',
      'classification' : ['Aves', 'Anseriformes', 'Anatidae'],
      'wikipedia': 'The mallard or wild duck (Anas platyrhynchos) is a dabbling duck which breeds throughout the temperate and subtropical Americas, Europe, Asia, and North Africa, and has been introduced to New Zealand, Australia, Peru, Brazil, Uruguay, Argentina, Chile, the Falkland Islands and South Africa.[2] This duck belongs to the subfamily Anatinae of the waterfowl family',
      'slice_data': {
            'slice_urls': json.dumps(slice_urls),
            'first_slice': slice_urls[0]
        }
    }