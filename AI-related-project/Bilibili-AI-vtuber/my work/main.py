# -*- coding: utf-8 -*-
import asyncio
import http.cookies

from typing import *

import aiohttp

import blive

#Cookie of any login bilibili account
SESSDATA = ''
session: Optional[aiohttp.ClientSession] = None


async def main():
    init_session()
    bilibililive = blive.Blive(session)

    try:
        await bilibililive.run_client()
    finally:
        await session.close()

def init_session():
    cookies = http.cookies.SimpleCookie()
    cookies['SESSDATA'] = SESSDATA
    cookies['SESSDATA']['domain'] = 'bilibili.com'

    global session
    session = aiohttp.ClientSession()
    session.cookie_jar.update_cookies(cookies)


if __name__ == '__main__':
    asyncio.run(main())
