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
        if xbmc.getInfoLabel('Container.NumItems'):
            items = [
                (
                    f'plugin://{ADDON_ID}/?action=jump&pos={l}',
                    xbmcgui.ListItem(label=l, offscreen=True),
                    False
                )
                for l in ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            ]
            xbmcplugin.addDirectoryItems(handle=int(sys.argv[1]), items=items)
        xbmcplugin.endOfDirectory(handle=int(sys.argv[1]))
    elif action == 'jump':
        try:
            xbmcplugin.setResolvedUrl(
                handle=int(sys.argv[1]),
                succeeded=False,
                listitem=xbmcgui.ListItem()
            )
        except Exception:
            pass

        pos = params.get('pos', '#')
        # If not '#' find the valid entry or preceding if no matching first letter
        if pos != '#':
            lastc = '#'
            xbmc.log(msg=f'[{ADDON_ID}] container.numitems: {xbmc.getInfoLabel("Container.NumItems")}, pos: {pos}', level=xbmc.LOGINFO)

            for i in range(int(xbmc.getInfoLabel('Container.NumItems'))):
                c = xbmc.getInfoLabel(f'ListItem({i}).SortLetter').upper()
                xbmc.log(msg=f'[{ADDON_ID}] i: {i}, c: {c}, pos: {pos}', level=xbmc.LOGINFO)
                if c >= pos:
                    if c > pos:
                        pos = lastc
                    break
                lastc = c

        if pos == '#':
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
            if pos in ['#', xbmc.getInfoLabel('ListItem.SortLetter').upper()]:
                break

if __name__ == '__main__':
    main()