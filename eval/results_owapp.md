# AndroGuard on OWApp (18 in-scope apps)

Detected **14 of 18** (recall 0.778). OWApp has no fixed versions, so false alarms are not measured. 22 apps are out of scope (no rule for that MASTG test).

| App (MASTG test) | Expected category | Result |
|---|---|---|
| MASTG-TEST0001 | Insecure Data Storage | detected |
| MASTG-TEST0007 | Exported Components | detected |
| MASTG-TEST0009 | Insecure Data Storage | detected |
| MASTG-TEST0013 | Insecure Cryptography | detected |
| MASTG-TEST0014 | Insecure Cryptography | detected |
| MASTG-TEST0016 | Insecure Cryptography | missed |
| MASTG-TEST0019 | Cleartext Traffic or HTTP Endpoints | detected |
| MASTG-TEST0020 | Insecure SSL/TLS Configuration | detected |
| MASTG-TEST0021 | Improper SSL/TLS Validation | detected |
| MASTG-TEST0022 | Improper SSL/TLS Validation | missed |
| MASTG-TEST0024 | Insecure Permissions or Excessive API Permissions | detected |
| MASTG-TEST0025 | Injection | detected |
| MASTG-TEST0027 | Insecure WebView | missed |
| MASTG-TEST0030 | Insecure IPC | missed |
| MASTG-TEST0031 | Insecure WebView | detected |
| MASTG-TEST0032 | Insecure WebView | detected |
| MASTG-TEST0033 | Insecure WebView | detected |
| MASTG-TEST0039 | Debug Configuration | detected |

## Out of scope

| App | Why |
|---|---|
| MASTG-TEST0006 | keyboard cache: no rule |
| MASTG-TEST0008 | sensitive data shown in the UI: no rule |
| MASTG-TEST0011 | sensitive data in memory: runtime, not static |
| MASTG-TEST0015 | key purposes: no rule |
| MASTG-TEST0017 | confirm credentials: no rule |
| MASTG-TEST0018 | biometric authentication: no rule |
| MASTG-TEST0023 | security provider update: no rule |
| MASTG-TEST0026 | implicit intents carrying data: no rule |
| MASTG-TEST0028 | deep links: no rule |
| MASTG-TEST0035 | overlay attacks: no rule |
| MASTG-TEST0036 | enforced updating: no rule |
| MASTG-TEST0037 | WebView cleanup: no rule |
| MASTG-TEST0038 | app signing: no rule |
| MASTG-TEST0040 | debugging symbols in native code: no rule |
| MASTG-TEST0041 | debugging code and verbose logging: no rule |
| MASTG-TEST0043 | memory corruption in native code: no rule |
| MASTG-TEST0044 | native compiler security flags: no rule |
| MASTG-TEST0045 | root detection: resilience, no rule |
| MASTG-TEST0046 | anti-debugging: resilience, no rule |
| MASTG-TEST0048 | reverse-engineering tool detection: resilience, no rule |
| MASTG-TEST0049 | emulator detection: resilience, no rule |
| MASTG-TEST0051 | obfuscation: resilience, no rule |

## Method

OWApp (github.com/Mobile-IoT-Security-Lab/OWApp-Benchmarking-Suite, OWApp/apk/ListedAPKs, MIT). One intentionally vulnerable APK per OWASP MASTG test; there are no fixed versions, so only detection (recall) is measured. Unit = app. Detected if the scan has a finding in one of the expected categories. Expected categories were written from each test's MASTG title and README before any scan, and committed before the first run. 'out_of_scope' = no AndroGuard rule targets that test.
