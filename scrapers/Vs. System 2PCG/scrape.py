#!/usr/bin/env python3
import json, re, requests, urllib.request, sys

sets = [
        ['The Marvel Battles', 'MNB', 112, '2015'],
        ['The Defenders', 'DEF', 58, '2016-04'],
        ['A-Force', 'AFF', 59, '2016-05'],
        ['The Alien Battles', 'ALN', 60, '2016-06'],
        ['Legacy', 'LEG', 74, '2017-05-24'],
        ['Monsters Unleashed', 'MMU', 135, '2017'],
        ['The Predator Battles', 'PRD', 65, '2017-08'],
        ['S.H.I.E.L.D. vs. Hydra', 'SVH', 63, '2017-11-29'],
        ['Deadpool &amp; Friends', 'MFM', 25, '2018'],
        ['Brotherhood of Mutants', 'BOM', 19, '2018'],
        ['New Mutants', 'NEW', 19, '2018'],
        ['The MCU Battles', 'MCU1', 66, '2018'],
        ['MCU Heroes', 'MCU2', 22, '2018'],
        ['MCU Villains', 'MCU3', 22, '2018'],
        ['Spider-Friends', 'SPF', 22, '2018-08'],
        ['Sinister Syndicate', 'SYN', 19, '2018-09'],
        ['The New Defenders', 'DFX', 19, '2018-10'],
        ['The Buffy Battles', 'TBB', 61, ''],
        ['Crossover v1', 'CV1', 22, '2018-12'],
        ['Cosmic Avengers', 'COS', 22, '2019-02-27'],
        ['Galactic Guardians', 'GAL', 19, '2019-03-13'],
        ['Black Order', 'BLK', 24, '2019-04'],
        ['The Utopia Battles', 'TUB', 64, '2019-05'],
        ['Resistance', 'RES', 19, '2019-06'],
        ['H.A.M.M.E.R.', 'HAM', 19, '2019-07'],
        ['Power &amp; Reality', 'MCU4', 28, '2019-08'],
        ['Space &amp; Time', 'MCU6', 20, '2019-09'],
        ['Mind &amp; Soul', 'MCU5', 28, '2019-10'],
        ['The X-Files Battles', 'XFB', 70, '2019-11'],
        ['Crossover v2', 'CV2', 22, '2019-12'],
        ['Friendly Neighborhood', 'MCU7', 22, '2020-03-25'],
        ['Spidey Foes', 'SFO', 16, '2020-03-18'],
        ['Web-Heads', 'WEB', 28, '2020-04-15'],
        ['The Fantastic Battles', 'FAN', 61, '2020-05-13'],
        ['The Herald', 'HER', 19, '2020-06-17'],
        ['The Frightful', 'FRI', 19, '2020-07-15'],
        ['Futures Past', 'FUT', 27, '2020-08'],
        ['Freedom Force', 'FRE', 19, '2020-09'],
        ['Omegas', 'OGA', 16, '2020-10'],
        ['Crossover v3', 'CV3', 43, '2020-12-16'],
        ['Masters of Evil', 'MOE', 22, '2021-03-24'],
        ['Mystic Arts', 'MYS', 27, '2021-03-31'],
        ['Into the Darkness', 'DAR', 22, '2021-04-14'],
        ['Civil War Battles', 'CIV', 58, '2021-05-16'],
        ['Secret Avengers', 'SEC', 19, '2021-06-30'],
        ['Thunderbolts', 'THU', 19, '2021-07-14'],
        ['Lethal Protector', 'LET', 19, '2021-10-27'],
        ['Maximum Carnage', 'CAR', 19, '2021-11-17'],
        ['Spider-Verse', 'VER', 28, '2021-11-24'],
        ['Crossover v4', 'CV4', 40, '2022'],
        ['Wandavision', 'WDV', 22, '2022-11-02'],
        ['Falcon &amp; the Winter Soldier', 'FWS', 55, '2022-11-23'],
        ['Loki', 'LKI', 55, '2022-12-14'],
        ['Heroes of X', 'HOX', 200, '2023-02-08'],
        ['The New Brotherhood', 'NBX', 55, '2023-03-15'],
        ['X-Force', 'XFC', 55, '2023-04-12'],
        ['Mortal Kombat 11', 'MKE', 200, '2023-03-19'],
        ['The Boys', 'BOY', 200, '2023-07-12'],
        ['All Elite Wrestling', 'AEW', 200, '2023-08-02'],
        ['Fractured Family', 'FRF', 55, '2023-08-02'],
        ['Frightful Foes', 'FFO', 55, '2023-11-13'],
        ['Future Foundation', 'FND', 55, '2023-10'],
        ['Marvel Zombies', 'ZOM', 55, '2023-11'],
        ['Crossover v5', 'CV5', 200, '2023-12'],
]

f = open('Vs. System 2PCG.xml', 'w')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n<cockatrice_carddatabase version="4">\n<sets>\n')

for s in sets:
    f.write('<set>\n<name>%s</name>\n<longname>%s</longname>\n<settype>Custom</settype>\n<releasedate>%s</releasedate>\n</set>\n' % (s[1], s[0], s[3]))

f.write('</sets>\n<cards>\n')

for i in range(1, 2448+1):
    with urllib.request.urlopen("https://vs.tcgbrowser.com/server/card.php?action=getCard&cardid=%d" % i) as url:
        data = json.load(url)

        colors = ''
        if data.get('text'):
            if 'Intellect' in data.get('text'):
                colors += 'I'
            elif 'Skill' in data.get('text'):
                colors += 'S'
            elif 'Energy' in data.get('text'):
                colors += 'E'
            elif 'Might' in data.get('text'):
                colors += 'M'
            elif 'Humanity' in data.get('text'):
                colors += 'H'
            elif 'Alien' in data.get('text'):
                colors += 'A'

        f.write('<card>\n')
        f.write('<name>%s (%s)</name>\n' % (data.get('name'), data.get('guid')))
        if data.get('text'):
            f.write('<text>%s</text>\n' % data.get('text').replace('<p><p>', '\n').replace('<p>', '\n').replace('\n\n', '\n'))
        f.write('<prop>\n')
        if data.get('type'):
            f.write('<maintype>%s</maintype>\n' % data.get('type').replace(' L1', '').replace(' L2', '').replace(' L3', ''))
            f.write('<type>%s%s</type>\n' % (data.get('type').replace(' L1', '').replace(' L2', '').replace(' L3', ''), ' - '+data.get('faction') if data.get('faction') else ''))
        if data.get('cost'):
            f.write('<manacost>%s</manacost>\n' % data.get('cost'))
        if colors:
            f.write('<colors>%s</colors>\n' % colors)
        if data.get('health'):
            f.write('<loyalty>%s</loyalty>\n' % data.get('health'))
        if data.get('attack'):
            f.write('<pt>%s/%s</pt>\n' % (data.get('attack'), data.get('defense')))
        if data.get('type'):
            if data.get('type').endswith(' L1') or data.get('type').endswith(' L2') or data.get('type').endswith(' L3'):
                f.write('<cmc>%s</cmc>\n' % data.get('type')[-1:])
        if data.get('traits'):
            f.write('<coloridentity>%s</coloridentity>\n' % data.get('traits').replace(' ', ' - '))
        f.write('</prop>\n<set picurl="http://vs.tcgbrowser.com/images/cards/big/%s.jpg" num="%s">%s</set>\n</card>\n' % (data.get('guid'), data.get('guid').split('-')[-1] if data.get('guid') else "", data.get('setcode').upper() if data.get('setcode') else ""))

f.write('</cards>\n</cockatrice_carddatabase>\n')
f.close

