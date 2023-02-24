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
hostname|hostname on which the request was seen.|<code>HOST1</code>
http_version|HTTP version that is specified in the header.|<code>1.1</code>
request_body_bytes|Integer value corresponding to the total number of bytes in the request.|<code>180</code>
request_body_content|Body of the HTTP request; usually specifies the exact content being requested.|
request_referrer|The URL from which the request was referred, if applicable.|<code>http://cnn.com</code>
requester_ip_address|IP address from which the request was made.|<code>10.0.211.200</code>
response_body_bytes|Integer value corresponding to the total number of bytes in the response.|<code>2910</code>
response_body_content|Content of the response (does not include header).|
response_status_code|HTTP protocol status code in response header|<code>200</code>
url_domain|Domain portion of the URL.|<code>www.mitre.org</code>
url_full|URL to which the HTTP request was sent|<code>https://www.mitre.org/about/corporate-overview</code>
url_remainder|the path after the root domain|<code>/about/corporate-overview</code>
url_scheme|type of user that initiated the request.|<code>https</code>
user_agent_device|Device type from which request was made, identified by user_agent substring|<code>SM-G930VC (Samgsung Galaxy S7)</code>
user_agent_full|User agent string associated with the request|<code>HOST1\LOCALUSER1</code>
user_agent_name|The user agent through which the request was made.|<code>Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36</code>
user_agent_version|User Agent Version. Note that some User Agent strings may not label versions in the same way.|<code>4.0</code>

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
    <th>get</th>
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
    <th>post</th>
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
    <th>put</th>
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
    <th>tunnel</th>
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