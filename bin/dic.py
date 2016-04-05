#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import xml.etree.ElementTree

if sys.version_info.major == 3:
    from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, Request, build_opener
    from urllib.parse import urlencode
else:
    from urllib2 import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, Request, build_opener
    from urllib import urlencode


# import codecs
# sys.stdout = codecs.getwriter(sys.stdout.encoding)(sys.stdout, errors='backslashreplace')
# set PYTHONIOENCODING=cp932:backslashreplace

def curl(url, params=None, auth=None, req_type="GET", data=None, headers=None):
    post_req = ["POST", "PUT"]
    get_req = ["GET", "DELETE"]

    if params is not None:
        url += "?" + urlencode(params)

    if req_type not in post_req + get_req:
        raise IOError("Wrong request type \"%s\" passed" % req_type)

    _headers = {}
    handler_chain = []

    if auth is not None:
        manager = HTTPPasswordMgrWithDefaultRealm()
        manager.add_password(None, url, auth["user"], auth["pass"])
        handler_chain.append(HTTPBasicAuthHandler(manager))

    if req_type in post_req and data is not None:
        _headers["Content-Length"] = len(data)

    if headers is not None:
        _headers.update(headers)

    director = build_opener(*handler_chain)

    if req_type in post_req:
        if sys.version_info.major == 3:
            _data = bytes(data, encoding='utf8')
        else:
            _data = bytes(data)

        req = Request(url, headers=_headers, data=_data)
    else:
        req = Request(url, headers=_headers)

    req.get_method = lambda: req_type
    result = director.open(req)

    return {
        "httpcode": result.code,
        "headers": result.info(),
        "content": result.read()
    }


if len(sys.argv) > 1:
    word = sys.argv[1]

    Learners = "http://www.dictionaryapi.com/api/v1/references/learners/xml/{0}?key=cec77055-c067-4718-9be7-b9ca0a281d26"
    Students = "http://www.dictionaryapi.com/api/v1/references/sd4/xml/{0}?key=ee2c7bf5-e306-4874-9dc8-ca6ae610aab1"

    url = Students.format(word) if "-2" in sys.argv else Learners.format(word)

    result = curl(url)
    xmlstr = result["content"]
    e = xml.etree.ElementTree.fromstring(xmlstr)
    # for child in e:
    #    print(child.tag, child.attrib)

    for entry in e.findall("./entry"):

        if not entry.attrib["id"].startswith(word):
            continue

        # print(entry.find("pr").text)
        for dt in entry.iter("dt"):
            if dt.text is not None:
                print(str(dt.text).replace("\n", " "))
            else:
                print(str(dt.find("un").text).replace("\n", " "))
                # for vi in dt.iter("vi"):
                #    print(str(vi.text).replace("\n", " "))
else:
    pass

