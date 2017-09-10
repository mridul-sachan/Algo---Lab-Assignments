
import sys

def calculateFrequencies(string):
  """returns unsorted list of dictionaries [{character, frequency}, ...]"""
  temporary_dict = {}
  frequency_list = []
  for char in string:
    try:
      temporary_dict[char] += 1
    except:
      temporary_dict[char] = 1
  for char in temporary_dict:
    frequency_list.append({'character':char, 'frequency':temporary_dict[char]})
  return frequency_list

def sortByKey(dictionary_list, key):
  """returns list of dictionaries sorted by provided dictionary key"""
  try:
    return sorted(dictionary_list, key=lambda k: k[key])
  except:
    return None #TODO

def generateTree(frequency_list):
  """returns list tree of character frequencies"""
  frequency_list = sortByKey(frequency_list, 'frequency')
  if frequency_list:
    while len(frequency_list) > 1:
      if len(frequency_list) > 2:
        frequency_list = sortByKey(frequency_list, 'frequency')
      el1 = frequency_list[0]
      el2 = frequency_list[1]
      frequency_sum = el1['frequency'] + el2['frequency']
      character_arr = [el1, el2]
      del frequency_list[0]
      frequency_list[0] = {'frequency':frequency_sum, 'character':character_arr}
    return frequency_list[0]['character']
  else:
    return None #TODO

def signCodeMap(frequency_tree, code = ''):
  if len(frequency_tree) > 1:
    cm0 = signCodeMap(frequency_tree[0]['character'], code + '1')
    cm1 = signCodeMap(frequency_tree[1]['character'], code + '0')
    return dict(cm0.items() + cm1.items())
  elif type( frequency_tree ) == str:
    return {frequency_tree: code}
  return {}

def generateCodeMap(string):
  frequency_list = calculateFrequencies(string)
  if len(frequency_list) == 1:
    return None #TODO
  if len(frequency_list) == 2:
    return None #TODO
  frequency_tree = generateTree(frequency_list)
  return signCodeMap(frequency_tree);

def encode(string):
  code_map = generateCodeMap(string)
  encoded_string = ''
  for char in string:
    encoded_string += code_map[char]
  return {'encoded_string': encoded_string, 'code_map': code_map}

def decode(encoded_string, code_map):
  try:
    reversed_code_map = dict((code,character) for character,code in code_map.iteritems())
    if len(code_map) <> len(reversed_code_map):
      return None #TODO
  except:
    return None #TODO
  decoded_string = ''
  temporary_slug = ''
  for bit in encoded_string:
    bit = temporary_slug + bit
    try:
      decoded_string += reversed_code_map[bit]
      temporary_slug = ''
    except:
      temporary_slug = bit
  return decoded_string

try:
  string = sys.argv[1]
except:
  print "Enter a message to encode: "
  string = sys.stdin.readline().rstrip('\n')

code = encode(string)

print "Original message: " + string
print "Encoded message:  " + code['encoded_string']
#print code['code_map']
print "Decoded message:  " + decode(code['encoded_string'], code['code_map'])
