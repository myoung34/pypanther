# pypanther-starter-kit

Detection-As-Code V2 examples and starter kit.


```
poetry run pypanther test --verbose
AWS.GuardDuty.SeverityTooHigh:
   FAIL: Guardduty severity is too high
     - Expected rule() to return 'True', but got 'False'
   PASS: Guardduty severity is too high
   FAIL: Guardduty: TOR client
     - Expected rule() to return 'True', but got 'False'
   PASS: Guardduty: TOR client

Failed Tests:
   1. AWS.GuardDuty.SeverityTooHigh:
     - Guardduty severity is too high
     - Guardduty: TOR client

Test Summary:
   Skipped rules:   0
   Passed rules:    0
   Failed rules:    1
   Total rules:     1

   Passed tests:    2
   Failed tests:    2
   Total tests:     4
```
