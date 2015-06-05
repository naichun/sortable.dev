""" env.py 
Author			: Naichun Ding
Email			: naichun@gmail.com
Script Version		: 0.0.1
Last Modified Date	: 2015-06-04

Usage: This file is used to define all static variables which could be managed
       by Puppet and upload to servers.
       E.g. You can have one for Production server, one for Dev server etc ...
"""

PRODUCTS_FILE = 'products.txt'
LISTINGS_FILE = 'listings.txt'

product_mappings = {
	'panasonic' : {
		'model_prefixs' : ['dmc-',],
		'other_manufacturers' : [
			'panasonic',
			'tcr gmbh - bundle',
		],
	},
	'sony' : {
		'model_prefixs' : ['dslr-', 'dsc-'],
		'other_manufacturers' : [
			'sony',
		],
	},
	'fujifilm' : {
		'model_prefixs' : [],
		'other_manufacturers' : [
			'fuji',
			'fuji photo film europe gmbH',
			'fujifilm',
			'FUJIFILM',
		],
	},
	'hp' : {
		'model_prefixs' : [],
		'other_manufacturers' : [
			'hp',
			'hewlett packard',
		],
	},
	'olympus' : {
		'model_prefixs' : [],
		'other_manufacturers' : [
			'olympus',
			'olympus pptical co. (uk) ltd',
		],
	},
	'ricoh' : {
		'model_prefixs' : [],
		'other_manufacturers' : [
			'ricoh',
		],
	},
}


# I created this blacklist to reduce the testings time as no product family
# could be found. This blacklist can also be use to filter certain products
# which i think is good to leave here
models_blacklist = [

	# Very Agressive blacklist
    'dmc-lx3/s 10.1mp', 'rollei', 'delkin', 'exilim ex-v7', 'vivitar',
    'polaroid', 'sunset', 'arctic', 'agfaphoto', 'lexibook', 'svp svp ',
    'mustek', 'next base,next base ', 'vistaquest', 'benq',
    'mitsubishi', 'praktica', 'prime entertainment', 'dbroth', 
    'duragadget', 'jazz', 'takashi',
    'concord', 'bosch',
    'ge a', # ge,"ge a1030 10.1mp red digital camera (smile

    # For Nikon
    'nikon d90', 'nikon d80', 'nikon d40', 'nikon coolpix s200', 'nikon d40x',
    'nikon coolpix l10 ', 'nikon nikon coolpix s210', 'nikon - d3x ',
    'nikon coolpix p2 5.1mp ',

    # For Samsung
    'samsung pl65', 'samsung samsung digimax l73', 'samsung digimax 210 se ',
    'tl34hd', 'samsung st70 digitalkamera', 'samsung digimax s500 digital',
    'samsung es 75', 'samsung st1000 ',

    # For Sanyo
    'sanyo blue sanyo vpc-x1400', 'sanyo e760 ',

    # For Olympus
    'olympus fe-4000', 'olympus m:robe', 'olympus x-920', 'olympus fe-340 ',
    'olympus fe-190 ',
    'olympus fe-4050 ', 'olympus t-10 ', 'olympus c-360z', 'olympus d560 ',
    'olympus evolt e510 ', 'olympus c-765uz', 'olympus stylus 820',

    # For Panasonic
    'panasonic dmc-fx100', 'panasonic lumix dmc fz 18 ', 'panasonic dmc-fz7bb',
    'panasonic dmc-fz30eb-k ', 'panasonic lumix dmc-lz2eg-s ',
    'panasonic lumix dmc-fs35',

    # For Kodak
    'kodak easyshare c183', 'kodak easyshare m1033', 'kodak easyshare c6',
    'kodak - easyshare m522 ',
    'kodak - c195 ', 'kodak easyshare m863', 'kodak dx3600', 'z7590',

    # For Noname
    'noname easypix',

    # For Sony
    'sony dsc-wx7w', 'sony a (alpha) dslr-a300k ', 'sony cyber-shot dsc-s650',
    'sony cybershot dsc-t10 ', 'cyber-shot dsc-t70 ', 'sony dsc-p120',
    'sony cyber-shot dsc-p43 ', 'sony dsctx5g ',
    'sony a nex 5a - ', 'sony mvccd500 cd ', 'sony alpha a560/l',

    # For Casio
    'casio exilim ex-zs5', 'casio exilim ex-f1 ', 'casio exilim ex-z1 ',
    'casio exilim ex-zs10 ', 'casio exilim ex-s10rd ', 'casio exilim ex-z450',
    'casio exilim ex-z300', 'casio exilim ex-z2 -',

    # For Pentax
    'pentax optio m40', 'pentax optio s50', 'pentax - optio wg1',
    'pentax optio s7',

    # For FujiFilm
    'fujifilm finepix z100fd', 'fujifilm,fujifilm finepix a350',
    'fujifilm finepix z80', 'fujifilm finepix z30fd', 'fuji s8100fd ',
    'fujifilm finepix a500',

    # For Canon
    'canon,canon eos rebel xsi', 'canon digital slr ', 'canon powershot a470 ',
    'canon powershot sd550 ', 'canon - eos 40d a',
    'canon eos rebel xs black slr 10.1 mp digital camera wit',

    # For other brands
    'd+n,fototasche',
    'oregon scientific',
    'braun photo technik',
    'konica minolta dimage z3 ', 'konica minolta dimage x50 5mp digital ',
    'ricoh - grd ii ',
    ' tough-3000 ',
    'hp pb 360 ',
    'digital olympus pen e-p1 12.3',
    'general electric ge e1486tw',
]

