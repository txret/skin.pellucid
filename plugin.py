#!/usr/bin/python
# coding: utf-8

########################

import sys, json
import urllib.parse as urlparse
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')

########################

def main():
    try:
        params = dict(urlparse.parse_qsl(sys.argv[2][1:]))
    except Exception:
        params = {}
    
    action = params.get('action', None)
    if action == 'list':
        li = _list(params.get('showall', 'false') == 'true')
        xbmcplugin.addDirectoryItems(handle=int(sys.argv[1]), items=li)
        xbmcplugin.endOfDirectory(handle=int(sys.argv[1]))
    elif action == 'jump':
        _jump(params.get('pos', '#'))

########################

def _list(showall):
    if not xbmc.getInfoLabel('Container.NumItems'):
        return []
    
    chars = {}
    for i in range(int(xbmc.getInfoLabel('Container.NumItems'))):
        c = xbmc.getInfoLabel(f'Listitem({i}).SortLetter').upper()
        if c.isnumeric():
            chars['#'] = True
        else:
            chars[c] = True

    list_ = []
    if len(chars) > 1:
        ll = '#'
        for l in ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            li = xbmcgui.ListItem(label=l, offscreen=True)
            if l in chars:
                url = f'plugin://{ADDON_ID}/?action=jump&pos={l}'
                ll = l
            elif showall:
                url = f'plugin://{ADDON_ID}/?action=jump&pos={ll}'
                li.setProperty('NotAvailable', 'true')
            else:
                continue
            list_.append((url, li, False))
        
    return list_

########################

def _jump(pos):
    try:
        xbmcplugin.setResolvedUrl(handle=int(sys.argv[1]), succeeded=False, listitem=xbmcgui.ListItem())
    except Exception:
        pass

    if pos in ['#', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        cmd = 'firstpage' if xbmc.getInfoLabel('Container.SortOrder') != 'Descending' else 'lastpage'
    elif pos in ['A', 'B', 'C']:
        cmd = 'jumpsms2'
    elif pos in ['D', 'E', 'F']:
        cmd = 'jumpsms3'
    elif pos in ['G', 'H', 'I']:
        cmd = 'jumpsms4'
    elif pos in ['J', 'K', 'L']:
        cmd = 'jumpsms5'
    elif pos in ['M', 'N', 'O']:
        cmd = 'jumpsms6'
    elif pos in ['P', 'Q', 'R', 'S']:
        cmd = 'jumpsms7'
    elif pos in ['T', 'U', 'V']:
        cmd = 'jumpsms8'
    elif pos in ['W', 'X', 'Y', 'Z']:
        cmd = 'jumpsms9'
    else:
        return

    xbmc.executebuiltin('SetFocus(50)')
    for _ in range(4):
        xbmc.executeJSONRPC(json.dumps({
            'jsonrpc': '2.0',
            'id': 1,
            'method': 'Input.ExecuteAction',
            'params': {'action': cmd}
        }))
        xbmc.sleep(50)
        if pos in ['0', xbmc.getInfoLabel('ListItem.SortLetter').upper()]:
            break

if __name__ == '__main__':
    main()