#!/usr/bin/env python
import yaml
import iso3166
import sys

data = yaml.safe_load(open(sys.argv[1]).read())

out = {}

for k, v in data.items():
    k = k.upper()
    k = k.replace("’", "'")

    if k == 'BOLIVIA':
        k = 'BOLIVIA, PLURINATIONAL STATE OF'
    if k == 'CZECHIA (CZECH REPUBLIC)':
        k = 'CZECHIA'
    if k == 'CZECH REPUBLIC':
        k = 'CZECHIA'
    if k == 'DEMOCRATIC REPUBLIC OF THE CONGO':
        k = 'CONGO, DEMOCRATIC REPUBLIC OF THE'
    if k == 'IRAN':
        k = 'IRAN, ISLAMIC REPUBLIC OF'
    if k == 'PALESTINE STATE':
        k = 'PALESTINE, STATE OF'
    if k == 'RUSSIA':
        k = 'RUSSIAN FEDERATION'
    if k == 'REPUBLIC OF KOREA':
        k = 'KOREA, REPUBLIC OF'
    if k == 'SOUTH KOREA':
        k = 'KOREA, REPUBLIC OF'
    if k == 'SYRIA':
        k = 'SYRIAN ARAB REPUBLIC'
    if k == 'TAIWAN':
        k = 'TAIWAN, PROVINCE OF CHINA'
    if k == 'TANZANIA':
        k = 'TANZANIA, UNITED REPUBLIC OF'
    if k == 'TURKEY':
        k = 'TÜRKIYE'
    if k == 'UNITED KINGDOM':
        k = 'UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND'
    if k == 'VIETNAM':
        k = 'VIET NAM'
    if k == 'SCOTLAND':
        k = 'UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND'
    if k == 'SWAZILAND':
        k = 'ESWATINI'
    if k == 'THE NETHERLANDS':
        k = 'NETHERLANDS'
    if k == 'UNITED STATES':
        k = 'UNITED STATES OF AMERICA'
    if k == 'USA':
        k = 'UNITED STATES OF AMERICA'
    if k == 'WALES':
        k = 'UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND'
    if k == 'VENEZUELA':
        k = 'VENEZUELA, BOLIVARIAN REPUBLIC OF'

    country = iso3166.countries_by_name[k.upper()]
    if country.alpha3 in out:
        out[country.alpha3] += v
    else:
        out[country.alpha3] = v

print(yaml.dump(out))
