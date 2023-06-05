# Security-HTTP-Header-Checker (Live at: https://faizan12123.github.io/Security-HTTP-Header-Checker/)

The Security HTTP Header Checker is a tool built with Python, Flask, HTML, CSS, and JavaScript that allows you to assess the security headers of a website. It helps you identify missing or misconfigured security headers, providing valuable information about their purpose and associated vulnerabilities.


## Features
* X-Frame-Options: Checks if the website has the X-Frame-Options header, which prevents clickjacking attacks by controlling how the page is embedded in iframes on other domains.
* Strict-Transport-Security: Verifies if the website utilizes HSTS (HTTP Strict Transport Security) to enforce secure connections over HTTPS and mitigate man-in-the-middle (MITM) attacks.
* Content-Security-Policy: Examines the presence and validity of the Content-Security-Policy header, which helps prevent cross-site scripting (XSS) and other code injection attacks.
* X-Content-Type-Options: Validates if the X-Content-Type-Options header is implemented, which prevents MIME type sniffing and helps mitigate certain types of XSS attacks.
* Referrer-Policy: Checks the Referrer-Policy header, which controls how much information is included in the Referer header when navigating to external websites.
* Permissions-Policy: Verifies the presence of the Permissions-Policy header, which allows a website to control browser permissions for specific features and APIs.


By using the Security HTTP Header Checker, you can easily assess the security posture of a website and gain insights into potential vulnerabilities. The tool provides clear descriptions of each security header and their associated risks, enabling you to make informed decisions and take necessary steps to enhance your website's security.