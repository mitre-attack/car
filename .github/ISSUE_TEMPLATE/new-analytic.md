---
name: New Analytic
about: To propose a new analytic to add to CAR

---

## *Analytic Name*

*Describe what your analytic does and how it does it. A description is **required**.*

### ATT&CK Coverage
*Describe what ATT&CK techniques your analytic covers. This is **required**. Add as many rows as necessary*

|Technique |Level of Coverage |
|---|---|
|[technique_name](https://attack.mitre.org/techniques/technique_id/)|Moderate|

### Analytic Code
*The code for this analytic. CAR pseudocode is preferred, but any search syntax is fine. At least one type of code is **required** but more are encouraged (e.g. both pseudocode and a Splunk search).*

### Test Cases
*Optionally, one or more command lines or other actions that can be taken to test this analytic.*

### Data Model Mappings
*Elements from the CAR data model that are required for this analytic. This is **required**.*

|Object|Action|Field|
|---|---|---|
| object_name | action_name | field_name |

## Developer Certificate of Origin
*Insert your DCO signoff here, e.g. "DCO signed-off-by: Joe Smith <joe.smith@email.com>"*
