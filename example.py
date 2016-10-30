#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ringZer0

def ch42():
    ch, s = 42, ringZer0.login()
    ch_url = ringZer0.get_url('/challenges/{0}'.format(int(ch)))
    r = s.get(ch_url, cookies={'flag':'1'})
    response = ringZer0.get_response(r.text)
    print(response)

if __name__ == '__main__':
    ch42()