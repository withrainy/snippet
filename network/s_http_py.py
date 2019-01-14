# coding: utf-8

"""
网络http相关
"""

"""
# 1.构造一个http post form-data 请求(基于tornado.httpclient HTTPRequest)

看下标准的HTTP POST 请求
POST /user/image/upload HTTP/1.1
Host: 127.0.0.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW
cache-control: no-cache
         这是空行，请求头和body的隔离
Content-Disposition: form-data; name="test"; filename="undefined"
Content-Type: file

这里二进制数据（过长）
          这是空行，字段之间的分隔
Content-Disposition: form-data; name="itype"

132
------WebKitFormBoundary7MA4YWxkTrZu0gW--

"""
# ---------------
# Py2



def encode_multipart_formdata(self, fields, files):
    boundary = '------WebKitFormBoundaryh4QYhLJ34d60s2tD'  # 该字段固定即可
    crlf = '\r\n'  # 换行符号
    l = []
    for (key, value) in fields:
        l.append('--' + boundary)
        l.append('Content-Disposition: form-data; name="%s"' % key)
        l.append('')
        l.append(value)
    for (key, filename, value) in files:
        filename = filename.encode("utf8")
        l.append('--' + boundary)
        l.append(
                'Content-Disposition: form-data; name="%s"; filename="%s"' % (
                    key, filename
                )
        )
        l.append('Content-Type: %s' % mimetypes.guess_type(filename)[0])
        l.append('')
        l.append(value)
    l.append('--' + boundary + '--')
    l.append('')
    body = crlf.join(l)
    content_type = 'multipart/form-data; boundary=%s' % boundary
    return content_type, body
