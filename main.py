""" main.py
Author			: Naichun Ding
Email			: naichun@gmail.com
Script Version		: 0.0.1
Last Modified Date	: 2015-06-04

Precondition:
    PRODUCTS_FILE: default sets to 'products.txt'
    LISTINGS_FILE: default sets to 'listings.txt'

Postcondition:
    This script generates two files:
    'result.txt' :
        A file full of Result objects. A Result associates a Product
        with a list of matching Listing objects.
   'result.formatted.txt':
        This file contains the same information as 'result.txt' has but
        more human-readable'

Tested under OS:
    OS X - Version 10.8.5
    Processor : 1.3 GHz Intel Core i5
    Memory    : 4GB 1600 MHz DDR3
Python Version: Python 2.7.2
Average Rum time: 7248.072 ms

Notes:
    1) Some list in the listings.txt cannot find any matching product
       under products.txt

Improvements/Suggestions:
    1) For the data collection, it is better to use a Database instead
       of a file. It will greatly reduce the parsing time as well as
       duplicated matching process.
    2) Timing functions is used to monitor time cost, it could be commented
       out to further reduce the running time.
    3) unit-test could be used to maintain the code reliability
    4) pylint could be used to improve and unify the coding style

Script Protocode:
    1) Scan PRODUCTS_FILE and parse it into a dictionary and
       use the 'manufacturer' as the key (convert all characters to lowercase)
    2) Scan LISTINGS_FILE and parse it into a dictionary and
       use selected substrings as the key (convert all characters to lowercase)
    3) Apply default filter to find the matching product of each give list,
       save matching list into a new dictionary ( named as 'result'),
       delete all matching list from the original dictionary
    4) Apply customized filter to find specific products' list,
       save matching list into a new dictionary ( named as 'result'),
       delete all matching list from the original dictionary
       e.g.
       a) panasonic and sony's model name sometimes use a shortened format
       b) Fijifile's manufacturer name some times is written as 'Fiji'
    5) Parse the 'result' variable and save the content into a file as required
       e.g. 'result.txt'
   *6) In addition, also same the 'result' in to another txt file with
       more human readable format for debugging purpose
       e.g. 'result.formatted.txt'

Notes:
    1) Timing function is copied from:
       http://stackoverflow.com/questions/5478351/python-time-measure-function
"""

import json, time
from env import PRODUCTS_FILE, LISTINGS_FILE,\
                product_mappings, models_blacklist

def timing(func):
    """ Timing function call
    ref:
    http://stackoverflow.com/questions/5478351/python-time-measure-function
    """
    def wrap(*args):
        """ Wrap Function
        """
        time1 = time.time()
        ret = func(*args)
        time2 = time.time()
        print '--%s function took %0.3f ms' % (
            func.func_name, (time2-time1)*1000.0
        )
        return ret
    return wrap

@timing
def read_file(file_name):
    """ Read file into a list of dictionaries
        Each dictionary repersentes to one line in the given file
        Returns: a list of dictionaries
    """
    lines = []
    with open(file_name, "r") as ins:
        for line in ins:
            lines.append(json.loads(line))
    return lines

def length_listings(listings):
    """ List the length of all unidentified listings
    """
    listings_len = len(listings)
    print "Current length of the unidentified listings is %s " % listings_len
    return listings_len

def parse_key_string(give_dict):
    """ Parse the given dictionary save value into a string separated with ','
        Returns: a string
    """
    key_string = ''
    for name in give_dict:
        if name == 'announced-date' or name == 'currency' or name == 'price':
            continue
        name_value = give_dict[name].lower()
        name_value = ' '.join(name_value.split())
        key_string = "%s %s" % (key_string, name_value)
    # To simplify the matching script:
    # the first and last character of the key has to be a whitespace
    return "%s " % key_string

@timing
def parse_products(products_raw):
    """ Parse given products
        Returns: products = {
            <manufacturer1> : [
                <product1>, <product2>, ... <productX>
            ]
            ...
            <manufacturerX> : [
                <product1>, <product2>, ... <productX>
            ]
        }
        Notes: under this variable all characters are converted to lowercase
    """
    products = {}
    for product in products_raw:
        manufacturer = product['manufacturer'].lower()
        if manufacturer not in products:
            products[manufacturer] = []
        products[manufacturer].append([
            {k.lower():v.lower() for k, v in product.items()},
            product, # original formatting
        ])
    with open('products.modified.txt', 'w') as file_:
        file_.write(json.dumps(products, sort_keys=True, indent=2))
    return products

def ignore_listings(name_key):
    """ Ignore listings for debugging and testing purpose
        !!! Uncomment the for loop below to enable blacklisting
    """
    # for blacklist_str in models_blacklist:
    #     if blacklist_str in name_key:
    #         return True
    return False

@timing
def parse_listings(listings_raw):
    """ Parse given listings
        Returns listings = {
            <key_content1> : list1,
            ...
            <key_contentX> : listX,
        }
    """
    listings = {}
    for alist in listings_raw:
        name_key = parse_key_string(alist)
        if ignore_listings(name_key):
            continue
        if name_key not in listings:
            listings[name_key] = []
        listings[name_key].append(alist)
    with open('listings.modified.txt', 'w') as file_:
        file_.write(json.dumps(listings, sort_keys=True, indent=2))
    length_listings(listings)
    return listings

def find_manufacturer(products, alist):
    """ Find the manufacturer name of the given list
    """
    for manufacturer in products:
        if manufacturer in alist:
            if manufacturer in product_mappings:
                other_manufacturers = \
                    product_mappings[manufacturer]['other_manufacturers']
                if other_manufacturers:
                    return manufacturer, ', '.join(other_manufacturers)
            return manufacturer, manufacturer
    for manufacturer in product_mappings:
        other_manufacturers = \
            product_mappings[manufacturer]['other_manufacturers']
        for other_name in other_manufacturers:
            if other_name in alist:
                return manufacturer, ', '.join(other_manufacturers)
    return False, None

def remove_matched_list(listings, matched_lists):
    """ Remove lists that have already been identified
    """
    for matched_list in matched_lists:
        if matched_list in listings:
            del listings[matched_list]
    return listings

def does_list_contains_model(alist, model, manufacturer,
                             simplified_model=False):
    """ Check if the given model is in the list
    """
    if " %s " % model not in alist:
        model_no_space = model.replace(' ', '')
        if " %s " % (model_no_space) in alist or\
            " %s " % (model_no_space) in alist.replace('-', '') or\
            " %s " % (model_no_space.replace('-', '')) in \
                alist.replace('-', '') or\
            " %s " % (model_no_space.replace('-', ' ')) in \
                alist.replace('-', ''):
            return True
        elif simplified_model:
            return False
        elif manufacturer in product_mappings:
            for prefix in product_mappings[manufacturer]['model_prefixs']:
                model = model.replace(prefix, '')
            return does_list_contains_model(
                alist, model, manufacturer, simplified_model=True)
        return False
    return True

@timing
def filter_generic(products, listings, result=None):
    """ Generic filter for generic cases
    """
    print "Apply Generic Filtering "
    if result == None:
        result = {}
    matched_listings = []
    for alist in listings:
        manufacturer, renamed_manufacturer = find_manufacturer(products, alist)
        if manufacturer == False:
            continue
        for product in products[manufacturer]:
            product = product[0] # get product information all in lower case
            if not does_list_contains_model(\
                alist, product['model'], manufacturer):
                continue
            if product['product_name'] not in result:
                result[product['product_name']] = []
            for matched_list in listings[alist]:
                matched_manufacturer =\
                    matched_list['manufacturer'].lower()
                if manufacturer not in  matched_manufacturer and\
                    matched_manufacturer not in renamed_manufacturer:
                    continue
                result[product['product_name']].append(matched_list)
                matched_listings.append(alist)
    remove_matched_list(listings, matched_listings)
    length_listings(listings)
    return result

@timing
def save_result(result, file_name='result.txt', formatted=False):
    """ Save result into a file
    """
    print "Save result into %s" % file_name
    with open(file_name, 'w') as file_:
        for product_name in result:
            if formatted:
                file_.write(json.dumps({
                    'product_name' : product_name,
                    'listings' : result[product_name]
                }, sort_keys=True, indent=2))
            else:
                file_.write(json.dumps({
                    'product_name' : product_name,
                    'listings' : result[product_name]
                }))

@timing
def main():
    """ Main Function """
    print "Hello world!"
    result = {}
    products = parse_products(read_file(PRODUCTS_FILE))
    listings = parse_listings(read_file(LISTINGS_FILE))
    filter_generic(products, listings, result)
    save_result(result)
    save_result(result, 'result.formatted.txt', True)

if __name__ == "__main__":
    main()
