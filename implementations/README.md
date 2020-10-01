# Analytic Implementations

Some analytics are built as source code for specific products. For these analytics, rather than integrating them into the main CAR site, we've collected them under this set of implementations.

## Bro/Zeek ATT&CK-Based Analytics (BZAR)

[BZAR](https://github.com/mitre-attack/bzar) is a collection of analytics for Bro primarily aimed at detecting ATT&CK techniques that leverage RPC and SMB.

Reporting for Windows Admin shares (T1077)
Reporting: Write to Zeek Notice Log
– “ ::Lateral_Movement”
– “ :: R to admin file share”
– IP addresses & TCP/UDP ports
– Zeek connection ID
– Full Universal Naming Convention (UNC) path and file name
