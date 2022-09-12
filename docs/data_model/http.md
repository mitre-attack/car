---
title: "File"
---

HTTP events represents requests made over the network via the HTTP protocol.

## Actions

|Action|Description|
|---|---|
|get|The event corresponding to an HTTP GET request.
|post|The event corresponding to an HTTP POST request.
|put|The event corresponding to an HTTP PUT request.
|tunnel|The event corresponding to an HTTP TUNNEL request.

## Fields

|Field|Description|Example|
|---|---|---|
|hostname|hostname on which the request was seen.|HOST1
|request_body_bytes|Integer value corresponding to the total number of bytes in the request.|180
|http_version|HTTP version that is specified in the header.|1.1
|request_body_content|Body of the HTTP request; usually specifies the exact content being requested.|varies as content is unique. If referrer is http://cnn.com as in example below, expect the body content to likely be an article from CNN.
|request_referrer|The URL from which the request was referred, if applicable.|http://cnn.com
|requester_ip_address|IP address from which the request was made.|151.101.131.5
|response_body_types|Integer value corresponding to the total number of bytes in the response.|2910
|response_body_content|Content of the response (does not include header).|
|response_status_code|HTTP protocol status code in response header|200
|url_full|URL to which the HTTP request was sent|https://www.mitre.org/about/corporate-overview
|url_domain|Domain portion of the URL.|www.mitre.org
|url_remainder|the path after the root domain|/about/corporate-overview
|url_scheme|type of user that initiated the request.|https
|user_agent_full| User agent string associated with the request|HOST1\LOCALUSER1
|user_agent_name|The user agent through which the request was made.|"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv)</br>AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"
|user_agent_device|Device type from which request was made, identified by user_agent substring|SM-G930VC (Samgsung Galaxy S7)
|user_agent_version|User Agent Version. Note that some User Agent strings may not label versions in the same way.|4.0

## Coverage Map

| | **hostname** | **request_body_bytes** | **http_version** | **request_body_content** | **request_referrer** | **requester_ip_address** | **response_body_types** | **response_body_content** | **response_status_codes** | **url_full** | **url_domain** | **url_remainder** | **url_scheme** | **user_agent_full** | **user_agent_device** | **user_agent_version** |
| --- | --- | ---| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **get** | | | | | | | | | | | | | | | | |
| **post** | | | | | | | | | | | | | | | | |
| **put** | | | | | | | | | | | | | | | | |
| **tunnel** | | | | | | | | | | | | | | | | |