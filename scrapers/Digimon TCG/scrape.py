#!/usr/bin/env python3
# wget -O AllCards.json 'https://digimoncard.io/api-public/search.php'
import json, os, sys

sets = [
        ['BT1', 'New Evolution', ''],
        ['BT2', 'Ultimate Power', ''],
        ['BT3', 'Union Impact', ''],
        ['BT4', 'Great Legend', ''],
        ['BT5', 'Battle of Omega', ''],
        ['BT6', 'Double Diamond', ''],
        ['BT7', 'Next Adventure', ''],
        ['BT8', 'New Hero', ''],
        ['BT9', 'X-Record', ''],
        ['BT10', 'Xros Encounter', ''],
        ['BT11', 'Dimensional Phase', ''],
        ['BT12', 'Across Time', ''],
        ['BT13', 'Versus Royal Knights', ''],
        ['BT14', 'Blast Ace', ''],
        ['BT15', 'Exceed Apocalyps', ''],
        ['BT16', 'Beginning Observer', ''],
        ['BT17', 'Secret Crisis', ''],
        ['BT18', 'Special Booster Ver. 2.0', ''],
        ['BT19', 'Special Booster Ver. 2.0', ''],
        ['BT20', 'Special Booster Ver. 2.5', ''],
        ['BT21', 'World Convergence', ''],
        ['EX1', 'Classic Collection', ''],
        ['EX2', 'Digital Hazard', ''],
        ['EX3', 'Draconic Roar', ''],
        ['EX4', 'Alternative Being', ''],
        ['RB1', 'Resurgence Booster', ''],
        ['EX5', 'Animal COlosseum', ''],
        ['EX6', 'Internal Ascension', ''],
        ['EX7', 'Digimon Liberator', ''],
        ['EX8', 'Chain of Liberation', ''],
        ['EX9', 'Versus Monsters', ''],
        ['ST1', 'Gaia Red', ''],
        ['ST2', 'Cocytus Blue', ''],
        ['ST3', "Heaven's Yellow", ''],
        ['ST4', 'Giga Green', ''],
        ['ST5', 'Machine Black', ''],
        ['ST6', 'Venomous Violet', ''],
        ['ST7', 'Gallantmon', ''],
        ['ST8', 'Ulforceveedramon', ''],
        ['ST9', 'Ultimate Ancient Dragon', ''],
        ['ST10', 'Parallel World Tactician', ''],
        ['ST12', 'Jesmon', ''],
        ['ST13', 'Ragnaloardmon', ''],
        ['ST14', 'Beelzemon', ''],
        ['ST15', 'Dragon of Courage', ''],
        ['ST16', 'Wolf of Friendship', ''],
        ['ST17', 'Double Typhoon', ''],
        ['ST18', 'Guardian Vortex', ''],
        ['ST19', 'Fable Waltz', ''],
        ['ST20', 'Protector of Light', ''],
        ['ST21', 'Hero of Hope', ''],
        ['P', 'Promo', ''],
]

data = dict()

with open('AllCards.json', 'r') as file:
    data = json.load(file)
    file.close()

f = open('Digimon TCG.xml', "w")

f.write('<?xml version="1.0" encoding="UTF-8"?>\n<cockatrice_carddatabase version="4">\n<sets>\n')

for s in sets:
    f.write('<set>\n<name>%s</name>\n<longname>%s</longname>\n<settype>Digimon TCG</settype>\n<releasedate>%s</releasedate>\n</set>\n' % (s[0], s[1], s[2]))

f.write('</sets>\n<cards>\n')

for i in data:
    if i['id'].startswith('BO-') or i['id'].startswith('DD-') or i['id'].startswith('DM-') or i['id'].startswith('DV-') or i['id'].startswith('LM-') or i['id'].startswith('MD-') or i['id'].startswith('MO-') or i['id'].startswith('ST-'):
        continue

    f.write('<card>\n')
    f.write('<name>%s (%s%s)</name>\n' % (i['name'].replace('&', '&amp;').replace('<', '').replace('>', ''), i['id'], i['rarity'].upper()))

    xros_req = ''
    main_effect = ''
    source_effect = ''
    alt_effect = ''
    if i['xros_req']:
        xros_req = i['xros_req'].replace('&', '&amp;').replace('<', '[').replace('>', ']')+'\n'
    if i['main_effect']:
        main_effect = i['main_effect'].replace('&', '&amp;').replace('<', '[').replace('>', ']')+'\n'
    if i['source_effect']:
        source_effect = i['source_effect'].replace('&', '&amp;').replace('<', '[').replace('>', ']')+'\n'
    if i['alt_effect']:
        alt_effect = i['alt_effect'].replace('&', '&amp;').replace('<', '[').replace('>', ']')+'\n'
        
    f.write('<text>%s%s%s%s</text>' % (xros_req, main_effect, source_effect, alt_effect))
    f.write('<prop>\n')
    if i['play_cost']:
        f.write('<cmc>%s</cmc>\n' % i['play_cost'])
    if i['dp']:
        f.write('<pt>%s</pt>\n' % i['dp'])
    if i['level']:
        f.write('<loyalty>%s</loyalty>\n' % i['level'])
    if i['evolution_cost']:
        f.write('<Evolution_Cost>%s</Evolution_Cost>\n' % i['evolution_cost'])
    if i['evolution_color']:
        f.write('<Evolution_Color>%s</Evolution_Color>\n' % i['evolution_color'][0])
    if i['evolution_level']:
        f.write('<Evolution_Level>%s</Evolution_Level>\n' % i['evolution_level'])
    f.write('<maintype>%s</maintype>\n' % i['type'])
    if i['digi_type'] or i['digi_type2'] or i['attribute']:
        f.write('<type>%s - %s%s%s%s</type>\n' % (i['type'], i['digi_type'] if i['digi_type'] else '', ' - %s' % i['digi_type2'] if i['digi_type2'] else '', ' - %s' % i['attribute'] if i['attribute'] else '', ' - %s' % i['form'] if i['form'] else ''))
    if i['color']:
        f.write('<colors>%s%s</colors>\n' % (i['color'][0], i['color2'][0] if i['color2'] else ''))
    f.write('</prop>\n')
    # FIXME: Use re.sub to avoid this extra nonsense
    f.write('<set rarity="%s" picurl="https://world.digimoncard.com/images/cardlist/card/%s.png">%s</set>\n' % (i['rarity'].lower().replace('uncommon', 'u').replace('common', 'c').replace('r', 'rare').replace('sec', 'secret rare').replace('p', 'promo').replace('c', 'common').replace('u', 'uncommon').replace('sr', 'super rare').replace('rareare', 'rare').replace('secommonret', 'secret'), i['id'], i['id'].split('-')[0]))

    f.write('<tablerow>%s</tablerow>\n' % ('0' if i['type'] == 'Digi-Egg' else '2' if i['type'] == 'Digimon' else '1'))
    f.write('</card>\n')

f.write('</cards>\n</cockatrice_carddatabase>\n')

#        try:
#            f.write('<text>%s%s%s%s%s%s</text>' % 
#                    ('%s\n' % database[j][16] if database[j][16] else '', 'Digivolve Cost 1: %s\n' % database[j][7] if database[j][7] else '', 'Digivolve Cost 2: %s\n' % database[j][8] if database[j][8] else '', 'Effect: %s\n' % database[j][9] if database[j][9] else '', 'Digivolve effect: %s\n' % database[j][10] if database[j][10] else '', '%s\n' % database[j][11] if database[j][11] else ''))
#        except:
#            f.write('<text>%s%s%s%s%s</text>' % 
#                    ('Digivolve Cost 1: %s\n' % database[j][7] if database[j][7] else '', 'Digivolve Cost 2: %s\n' % database[j][8] if database[j][8] else '', 'Effect: %s\n' % database[j][9] if database[j][9] else '', 'Digivolve effects: %s\n' % database[j][10] if database[j][10] else '', '%s\n' % database[j][11] if database[j][11] else ''))
#        f.write('<type>%s%s%s%s</type>' % (database[j][15], ' - %s' % 
#            database[j][2].replace('Digi-Egg', 'DigiEgg') if database[j][2] else '', ' - %s' % database[j][3] if database[j][3] else '', ' - %s' % database[j][4] if database[j][4] else ''))
#
f.close()

