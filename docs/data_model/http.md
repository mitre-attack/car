<!--  To Do - Write up missing http.md file, using data from car/data_model/http.yaml -->

---
title: "File"
---

HTTP events represents requests made over the network via the HTTP protocol.

## Actions

|Action|Description|
|---|---|
|pet|The event corresponding to an HTTP GET request.
|post|The event corresponding to an HTTP POST request.
|put|The event corresponding to an HTTP PUT request.
|tunnel|The event corresponding to an HTTP TUNNEL request.

## Fields

|Field|Description|Example|
|---|---|---|
|hostname|hostname on which the request was seen.|HOST1
|request_body_bytes|
|http_version|
|request_body_content|
|request_referrer|
|requester_ip_address|
|response_body_types|
|response_body_content|
|response_status_code|
|url_full|
|url_domain|
|url_remainder|
|url_scheme|
|user_agent_full|
|user_agent_name|
|user_agent_device|
|user_agent_version|
<!--
 - name: hostname
    
  - name:  request_body_bytes
    description: Integer value corresponding to the total number of bytes in the request.
    example: 180
  - name: http_version
    description: HTTP version that is specified in the header.
    example: 1.1
  - name: request_body_content
    description: Body of the HTTP request; usually specifies the exact content being requested.
  - name: request_referrer
    description: The URL from which the request was referred, if applicable.
    example: http://cnn.com
  - name: requester_ip_address
    description: IP address from which the request was made.
    example: 10.0.211.200
  - name: response_body_bytes
    description: Integer value corresponding to the total number of bytes in the response.
    example: 2910
  - name: response_body_content
    description: Content of the response (does not include header).
  - name: response_status_code
    description: HTTP protocol status code in response header
    example: 200
  - name: url_full
    description: URL to which the HTTP request was sent
    example: https://www.mitre.org/about/corporate-overview
  - name: url_domain
    description: Domain portion of the URL.
    example: www.mitre.org
  - name: url_remainder
    description: the path after the root domain
    example: /about/corporate-overview
  - name: url_scheme
    description: type of user that initiated the request.
    example: https
  - name: user_agent_full
    description: User agent string associated with the request
    example: HOST1\LOCALUSER1
  - name: user_agent_name
    description: The user agent through which the request was made.
    example: "Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"
  - name: user_agent_device
    description: Device type from which request was made, identified by user_agent substring
    example: SM-G930VC (Samgsung Galaxy S7)
  - name: user_agent_version
    description: User Agent Version. Note that some User Agent strings may not label versions in the same way.
    example: 4.0
-->