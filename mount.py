import urllib.request, json, re, sys, inspect, logging



logging.basicConfig(stream=sys.stderr, level=logging.ERROR)

#print(data)

with open('/home/alx/projects/albion/items.json') as file:
	a_items = json.load(file)


with open('/home/alx/projects/albion/mount_calc/recipes_horizontal.json') as file:
	recipes = json.load(file)

def autolog(message):
    "Automatically log the current function details."

    # Get the previous frame in the stack, otherwise it would
    # be this function!!!
    func = inspect.currentframe().f_back.f_code
    # Dump the message + the name of this function to the log.
    logging.debug("%s: %s" % (
        func.co_name,
        message
    ))

def query_auction(item,city=False,quality=False):
	query = 'http://albion-online-data.com/api/v2/stats/prices/'+item
	if city: 
		query = query+'?locations='+city
	if quality:
		query = query+'&qualities='+quality
	autolog('Query is: '+query)
	request = urllib.request.urlopen(query)
	prices = json.loads(request.read())
	autolog(prices)
	return(prices)


def get_key_value(data,key):
	for item in data:
		value = item.get(key)
		print(value)

def get_name(recipes,item_id):
	for recipe_item in recipes:
		if recipe_item.get('item_id') == item_id:
			return recipe_item.get('name')


def get_dependency(recipes,item_id):
	for recipe_item in recipes:
		if recipe_item.get('item_id') == item_id:
			dependencies = recipe_item.get('dependencies')
			if dependencies:
				autolog('found dependencies:')
				autolog(dependencies)
				return(dependencies)
			#for dependency in recipe_item.get('dependencies'):

	#	if type(a_item.get('LocalizedNames')) == type(dict()):
	#		en_us_name = a_item.get('LocalizedNames').get('EN-US')
	#		if re.match(pattern, en_us_name):
	#			item_id = a_item.get('LocalizationNameVariable')
	#			print(item_id+' : '+en_us_name)
				#item_obj = CraftableItem(item_id,False)
				#items.append(item_obj)

def get_current_price(item_id,city=False,quality=False):
	query = query_auction(item_id, city, quality)
	for item in query:
		autolog(item)
		min_price = item.get('sell_price_min')
		autolog(min_price)
		print('Current price of %s : %i' % (item_id,min_price))
		return(min_price)


def get_dependency_price(dependencies,city=False,quality=False,focus=True):
	autolog('Dependencies:')
	autolog(dependencies)
	total_price = 0
	for dependency in dependencies:
		autolog('Dependency:')
		autolog(dependency)
		query = query_auction(dependency.get('item_id'), city, quality)
		for item in query:
			full_price = item.get('sell_price_min')
			quantity = dependency.get('quantity')
			if focus:
				discount = dependency.get('focus')
			else:
				discount = dependency.get('return')
			autolog(quantity)
			discount_price  = full_price   * discount
			item_price      = (full_price - discount_price) * quantity
			total_price = total_price+item_price
			print('%s : ( %i - (%i x %.2f ) x %i  = %i' % (item.get('item_id'),full_price,full_price,discount,quantity,item_price))
	print('Total dependencies price: %i' % (total_price))
	return(total_price)



		#autolog(dependency_min_price)
		#autolog('bla')

#def get_material_price(data):
#	for item in recipes:
	

def search_item_id(a_items,name):
	pattern = re.compile(name)
	for a_item in a_items:
		if type(a_item.get('LocalizedNames')) == type(dict()):
			en_us_name = a_item.get('LocalizedNames').get('EN-US')
			if re.match(pattern, en_us_name):
				item_id = a_item.get('LocalizationNameVariable')
				print(item_id+' : '+en_us_name)
				#item_obj = CraftableItem(item_id,False)
				#items.append(item_obj)


mount = 'T6_MOUNT_GIANTSTAG_MOOSE'
cities = ['martlock','lymhurst','bridgewatch','fortsterling', 'caerleon']
mount_name = get_name(recipes,mount)
cities_string = ', '.join(cities)

print('Querying for item: %s \nIn cities: %s' %(mount_name, cities_string))

for city in cities:
	print('City: '+city)
	current_price = get_current_price(mount,city,'1')
	dependencies = get_dependency(recipes,mount)
	if dependencies: 
		dependencies_price = get_dependency_price(dependencies,city,'1')
		difference = current_price - dependencies_price
		profit = difference / current_price
		print('Profit : %i  (%.3f)' % (difference,profit))
		print('Remember the Auction house charges 3%')

#for item in recipes:
#	item_id = item.get('item_id')
#	autolog('Item: '+item_id)
#	#query = query_auction(item_id,'lymhurst')
#	#print(query)
#	#get_key_value(query,'sell_price_min')
#	dependencies = get_dependency(recipes,item_id)
#	if dependencies: 
#		get_dependency_price(dependencies,'lymhurst')
#	#print(item.keys())

	





#print(d)

#d = search_item_id(a_items,'.*Swiftclaw Cub.*')
#print(d)

#print(items[0].dependencies)
#items[0].add_dependency('blabla')
#print(items[0].dependencies)

#for a_item in a_items:
	#print(a_item.keys())
#	if a_item.get('Index') == '46':
#		print(a_item.get('LocalizedNames').keys())
	#print(a_item)
	#if item.() == 46:
		#print(item)
	#print(item.keys())
	#for key in item.keys():
		#if key == 'LocalizedNames':
			#print(key)
	#print(item.keys())


#def search_item_id(items,name):

