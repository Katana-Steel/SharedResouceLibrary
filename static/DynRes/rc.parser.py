#!/usr/bin/python3
"""
    2018 (c) Rene 'Katana Steel' Kjellerup, distributed under the terms of
    the GNU General Public Licenses version 3 or later for details see:
    http://www.gnu.org/licenses/gpl.html
"""
from sys import argv
from os.path import exists, dirname
from string import Template 

str_table = []
text = []
defs = []


def parseRC(rcFile):
    ret_incl = []
    with open(rcFile, 'r') as f:
        cur_lst = None
        str_id = None
        txt = None
        for l in f.readlines():
            if l.lower().startswith('#include'):
                n = l.split('"')
                ret_incl.append(n[1].replace('\\', '/'))
            if 'stringtable' in l.lower():
                cur_lst = str_table
            if 'end' in l.lower():
                cur_lst = None
            if l.startswith(' ') and cur_lst is not None:
                n = l.strip('\n').split('"')
                if str_id is None:
                    str_id = n[0].strip()
                if len(n) is 1:
                    continue
                txt = '"'.join(n[1:-1])
                cur_lst.append((str_id, txt))
                str_id = None
                txt = None
    return ret_incl


def parseH(hFile):
    try:
        with open(hFile, 'r') as h:
            for l in h.readlines():
                defs.append(l.strip('\n'))
    except Exception:
        pass


def getIncludes(base, paths, includes):
    ret_incl = []
    # fetching includes and dropping them directly into the generated file
    for i in includes[:]:
        inc = ''
        for p in paths:
            if exists('/'.join([base, p, i])):
                inc = '/'.join([base, p, i])
                break
            if exists('/'.join([p, i])):
                inc = '/'.join([p, i])
                break
        if exists('/'.join([base, i])):
            inc = '/'.join([base, i])
        if len(inc) < 1:
            print('not found: {0}'.format(i))
            continue
        if '.h' in i.lower():
            print('including: {0}'.format(inc))
            parseH(inc)
        if '.rc' in i.lower():
            print('including: {0}'.format(inc))
            ret_incl.extend(parseRC(inc))
    return ret_incl


main_rc = ''
paths = ['.']
for p in argv:
    if p.lower().endswith('rc'):
        main_rc = p
        continue
    paths.append(p)

base = '/'.join(main_rc.split('/')[:-1])

includes = parseRC(main_rc)
while len(includes) > 0:
    includes = getIncludes(base, paths, includes[:])

static_res = ''
with open('/'.join([dirname(argv[0]),'StaticResTemplate.cpp']), 'r') as sres:
    static_res = sres.read().decode('utf-8')

make_pair = '    std::make_pair({0},"{1}"),'
tmpl_vals = {
    'defines': '\n'.join(defs),
    'string_table': '\n'.join([make_pair.format(x[0], x[1]) for x in str_table] )
}
s =Template (static_res)
with open(main_rc.split('/')[-1] + '.cpp', 'w') as o:
    o.write(s.substitute(tmpl_vals) )
