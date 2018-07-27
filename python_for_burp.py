#!/usr/bin/python
# author:Shelly
# time:2018-03-28
def getRequestInfo(messageIsRequest,messageInfo,helpers):
    result = {}
    if messageIsRequest:
        httpService = messageInfo.getHttpService()
        host = httpService.getHost()
        port = httpService.getPort()
        protocol = httpService.getProtocol()
        request = messageInfo.getRequest()
        analyzeRequest = helpers.analyzeRequest(httpService,request)
        headers = analyzeRequest.getHeaders()
        body = request[analyzeRequest.getBodyOffset():]
        body_str = body.tostring()
        url = analyzeRequest.getUrl()
        result = {'url':url,'host':host,'port':port,'protocol':protocol,'headers':headers,'body':body_str}
        return result
    else:
        print 'not request'
        pass


def getResponseInfo(messageIsRequest,messageInfo,helpers):
    result = {}
    if not messageIsRequest:
        response = messageInfo.getResponse()
        analyzedResponse = helpers.analyzeResponse(response)
        headers = analyzedResponse.getHeaders()
        body = response[analyzedResponse.getBodyOffset():]
        body_str = body.tostring()
        result = {'headers':headers,'body':body_str}
        return result
    else :
        print 'not response'
        pass

def changeRequest(messageInfo,helpers,new_headers,new_body):
    messageInfo.setRequest(helpers.buildHttpMessage(new_headers, new_body))

def changeResponse(messageInfo,helpers,new_headers,new_body):
    messageInfo.setResponse(helpers.buildHttpMessage(new_headers, new_body))

if messageIsRequest:
    request = getRequestInfo(messageIsRequest,messageInfo,helpers)
    new_requestHeaders = request['headers']
    new_requestBody = request['body']
    changeRequest(messageInfo,helpers,new_requestHeaders,new_requestBody)

if not messageIsRequest:
    response = getResponseInfo(messageIsRequest,messageInfo,helpers)
    new_responseHeaders = response['headers']
    new_responseBody = 'hello ! burp script!'
    changeResponse(messageInfo,helpers,new_responseHeaders,new_responseBody) 
'''
print request
> {'headers': [GET / HTTP/1.1, Host: 127.0.0.1, Cache-Control: max-age=0, Upgrade-Insecure-Requests: 1, User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36, Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8, Accept-Language: zh-CN,zh;q=0.9, Connection: close], 'body': '', 'url': http://127.0.0.1:80/, 'protocol': u'http', 'port': 80, 'host': u'127.0.0.1'}

print response
> {'headers': [HTTP/1.0 200 OK, Server: BaseHTTP/0.3 Python/2.6.6, Date: Wed, 28 Mar 2018 01:51:29 GMT, Content-type: text/html; charset=utf-8, Content-Length: 9], 'body': 'it works!'}
'''