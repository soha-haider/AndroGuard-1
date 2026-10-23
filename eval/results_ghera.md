# AndroGuard on Ghera (35 in-scope benchmarks scanned as source)

Detected **20 of 35** (recall 0.571). The fixed version was still flagged in the same category in **8 of 35** (false-alarm rate on fixed apps 0.229). 25 benchmarks are out of scope (no rule for that weakness).

| Benchmark | Expected category | Vulnerable app | Fixed app |
|---|---|---|---|
| Crypto/BlockCipher-ECB-InformationExposure-Lean | Insecure Cryptography | detected | clean |
| Crypto/BlockCipher-NonRandomIV-InformationExposure-Lean | Insecure Cryptography | missed | clean |
| Crypto/ConstantKey-ForgeryAttack-Lean | Insecure Cryptography | detected | clean |
| ICC/DynamicRegBroadcastReceiver-UnrestrictedAccess-Lean | Insecure IPC | missed | clean |
| ICC/EmptyPendingIntent-PrivEscalation-Lean | Insecure IPC | missed | clean |
| ICC/ImplicitPendingIntent-IntentHijack-Lean | Insecure IPC | missed | clean |
| ICC/InadequatePathPermission-InformationExposure-Lean | Exported Components | detected | still flagged |
| ICC/IncorrectHandlingImplicitIntent-UnauthorizedAccess-Lean | Exported Components | detected | clean |
| ICC/StickyBroadcast-DataInjection-Lean | Insecure IPC | detected | clean |
| ICC/TaskAffinityAndReparenting-PhishingAndDoSAttack-Lean | Insecure IPC | missed | clean |
| ICC/UnprotectedBroadcastRecv-PrivEscalation-Lean | Exported Components | detected | clean |
| Networking/CheckValidity-InformationExposure-Lean | Improper SSL/TLS Validation | detected | still flagged |
| Networking/IncorrectHostNameVerification-MITM-Lean | Improper SSL/TLS Validation | detected | clean |
| Networking/InsecureSSLSocket-MITM-Lean | Improper SSL/TLS Validation | detected | still flagged |
| Networking/InsecureSSLSocketFactory-MITM-Lean | Improper SSL/TLS Validation | detected | clean |
| Networking/InvalidCertificateAuthority-MITM-Lean | Improper SSL/TLS Validation | detected | clean |
| NonAPI/OutdatedLibrary-DirectoryTraversal-Lean | Vulnerable Dependency | missed | clean |
| Permission/UnnecesaryPerms-PrivEscalation-Lean | Excessive API Permissions | missed | clean |
| Permission/WeakPermission-UnauthorizedAccess-Lean | Insecure Permissions | detected | clean |
| Storage/ExternalStorage-DataInjection-Lean | Insecure Data Storage | missed | clean |
| Storage/ExternalStorage-InformationLeak-Lean | Insecure Data Storage | missed | clean |
| Storage/InternalStorage-DirectoryTraversal-Lean | Injection | missed | clean |
| Storage/InternalToExternalStorage-InformationLeak-Lean | Insecure Data Storage | missed | clean |
| Storage/SQLite-execSQL-Lean | Injection | detected | still flagged |
| Storage/SQLlite-RawQuery-SQLInjection-Lean | Injection | missed | clean |
| Storage/SQLlite-SQLInjection-Lean | Injection | missed | clean |
| System/ClipboardUse-InformationExposure-Lean | Insecure Data Storage | detected | still flagged |
| System/DynamicCodeLoading-CodeInjection-Lean | Dynamic Code Loading | missed | clean |
| Web/HttpConnection-MITM-Lean | HTTP Endpoints | detected | clean |
| Web/JavaScriptExecution-CodeInjection-Lean | Insecure WebView | detected | clean |
| Web/WebViewAllowContentAccess-UnauthorizedFileAccess-Lean | Insecure WebView | detected | still flagged |
| Web/WebViewAllowFileAccess-UnauthorizedFileAccess-Lean | Insecure WebView | detected | still flagged |
| Web/WebViewIgnoreSSLWarning-MITM-Lean | Improper SSL/TLS Validation | detected | clean |
| Web/WebViewLoadDataWithBaseUrl-UnauthorizedFileAccess-Lean | Insecure WebView | detected | still flagged |
| Web/WebViewProceed-UnauthorizedAccess-Lean | Weak Authentication Configuration | missed | clean |

Not scanned (no source project for both versions): ICC/UnprotectedBroadcastRecv-PrivEscalation-Fat

## Out of scope

| Benchmark | Why |
|---|---|
| Crypto/ExposedCredentials-InformationExposure-Lean | keystore entries without a protection parameter: no rule |
| Crypto/PBE-ConstantSalt-InformationExposure-Lean | constant PBE salt: no rule |
| ICC/FragmentInjection-PrivEscalation-Lean | fragment injection: no rule |
| ICC/HighPriority-ActivityHijack-Lean | intent-filter priority: no rule |
| ICC/NoValidityCheckOnBroadcastMsg-UnintendedInvocation-Lean | missing validity check in receiver logic: no rule |
| ICC/OrderedBroadcast-DataInjection-Lean | ordered broadcast priority: no rule |
| ICC/TaskAffinity-ActivityHijack-Lean | taskAffinity/launchMode: no rule |
| ICC/TaskAffinity-LauncherActivity-PhishingAttack-Lean | taskAffinity/launchMode: no rule |
| ICC/TaskAffinity-PhishingAttack-Lean | taskAffinity/launchMode: no rule |
| ICC/UnhandledException-DOS-Lean | unhandled exceptions: no rule |
| ICC/WeakChecksOnDynamicInvocation-DataInjection-Lean | ContentProvider.call() checks: no rule |
| Networking/OpenSocket-InformationLeak-Lean | open server socket: no rule |
| Networking/UnEncryptedSocketComm-MITM-Lean | plain TCP sockets: no rule |
| Networking/UnpinnedCertificates-MITM-Lean | missing certificate pinning: no rule |
| NonAPI/MergeManifest-UnintendedBehavior-Lean | behaviour inherited through manifest merging: no rule |
| System/CheckCallingOrSelfPermission-PrivilegeEscalation-Lean | runtime permission-check APIs: no rule |
| System/CheckPermission-PrivilegeEscalation-Lean | runtime permission-check APIs: no rule |
| System/EnforceCallingOrSelfPermission-PrivilegeEscalation-Lean | runtime permission-check APIs: no rule |
| System/EnforcePermission-PrivilegeEscalation-Lean | runtime permission-check APIs: no rule |
| System/UniqueIDs-IdentityLeak-Lean | device identifiers: no rule |
| Web/UnsafeIntentURLImpl-InformationExposure-Lean | Intent.parseUri handling: no rule |
| Web/WebView-CookieOverwrite-Lean | WebView cookie handling: no rule |
| Web/WebView-NoUserPermission-InformationExposure-Lean | WebView geolocation prompt: no rule |
| Web/WebViewInterceptRequest-MITM-Lean | unvalidated shouldInterceptRequest: no rule |
| Web/WebViewOverrideUrl-MITM-Lean | unvalidated shouldOverrideUrlLoading: no rule |

## Method

Ghera (bitbucket.org/secure-it-i/android-app-vulnerability-benchmarks, commit ea1dbe2, BSD-3). Each benchmark has a vulnerable app (Benign/) and a fixed app (Secure/), as Android Studio source projects. Unit = benchmark. Detected if the vulnerable app's scan has a finding in the expected category; a false alarm if the fixed app's scan still has one in that category. Expected categories were written from each benchmark's README before any scan, and committed before the first run. 'out_of_scope' = no AndroGuard rule targets that weakness; those benchmarks are listed but not scored.
