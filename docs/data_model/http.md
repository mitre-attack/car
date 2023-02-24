---
title: "HTTP"
---
HTTP events represents requests made over the network via the HTTP protocol.

## Actions
|Action|Description|
|---|---|
|get|The event corresponding to an HTTP GET request.|
|post|The event corresponding to an HTTP POST request.|
|put|The event corresponding to an HTTP PUT request.|
|tunnel|The event corresponding to an HTTP TUNNEL request.|

## Fields
|Field|Description|Example|
|---|---|---|
hostname|hostname on which the request was seen.|HOST1
http_version|HTTP version that is specified in the header.|1.1
request_body_bytes|Integer value corresponding to the total number of bytes in the request.|180
request_body_content|Body of the HTTP request; usually specifies the exact content being requested.|
request_referrer|The URL from which the request was referred, if applicable.|http://cnn.com
requester_ip_address|IP address from which the request was made.|10.0.211.200
response_body_bytes|Integer value corresponding to the total number of bytes in the response.|2910
response_body_content|Content of the response (does not include header).|
response_status_code|HTTP protocol status code in response header|200
url_domain|Domain portion of the URL.|www.mitre.org
url_full|URL to which the HTTP request was sent|https://www.mitre.org/about/corporate-overview
url_remainder|the path after the root domain|/about/corporate-overview
url_scheme|type of user that initiated the request.|https
user_agent_device|Device type from which request was made, identified by user_agent substring|SM-G930VC (Samgsung Galaxy S7)
user_agent_full|User agent string associated with the request|HOST1\LOCALUSER1
user_agent_name|The user agent through which the request was made.|Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36
user_agent_version|User Agent Version. Note that some User Agent strings may not label versions in the same way.|4.0

## Coverage Map
<table>
  <tr>
    <th />
    <th>hostname</th>
    <th>http_version</th>
    <th>request_body_bytes</th>
    <th>request_body_content</th>
    <th>request_referrer</th>
    <th>requester_ip_address</th>
    <th>response_body_bytes</th>
    <th>response_body_content</th>
    <th>response_status_code</th>
    <th>url_domain</th>
    <th>url_full</th>
    <th>url_remainder</th>
    <th>url_scheme</th>
    <th>user_agent_device</th>
    <th>user_agent_full</th>
    <th>user_agent_name</th>
    <th>user_agent_version</th>
  </tr>
  <tr>
    <td>get</td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <td>post</td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <td>put</td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
  <tr>
    <td>tunnel</td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
    <td style="white-space: pre-wrap;"></td>
  </tr>
</table>