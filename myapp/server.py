from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/check_headers', methods=['POST'])
def check_headers():
    data = request.get_json()
    results = {}
    url = data['url']
    try:
        headers = requests.get(url).headers
    except:
        results["Incorrect URL Format"] = "Please follow this URL format: https://www.example.com"
        
    

    


    if ("X-Frame-Options" in headers):
        results["X-Frame-Options"] = "X-Frame-Options header is active!"
    else:
        results["Missing X-Frame-Options Header!"] = '''
The X-Frame-Options header is a security measure that helps protect against clickjacking attacks. Clickjacking, also known as a UI redress attack, is a technique where an attacker tricks a user into clicking on a maliciously disguised element on a web page by overlaying it with another page or element.

The X-Frame-Options header allows a website to control how its pages are embedded in an iframe on another domain. It provides three possible values:

1. DENY: This value instructs the browser to not display the web page in any iframe, regardless of the domain.

2. SAMEORIGIN: With this value, the web page can only be displayed in an iframe if the request originates from the same origin (same domain).

3. ALLOW-FROM <uri>: This value specifies a specific URI that is allowed to display the web page in an iframe. It restricts iframe embedding to the specified URI.

If the X-Frame-Options header is missing or improperly configured, the following vulnerabilities can occur:

- Clickjacking Vulnerability: Without the X-Frame-Options header, an attacker can embed the web page in an iframe on another domain, making it susceptible to clickjacking attacks. This allows the attacker to trick users into performing actions they didn't intend, potentially leading to unauthorized actions, data leakage, or other malicious activities.

To ensure proper security, it is recommended to include the X-Frame-Options header with an appropriate value to prevent clickjacking attacks and protect the integrity and confidentiality of your web application.
'''

    if "Strict-Transport-Security" in headers:
        results["Strict-Transport-Security"] = "Strict-Transport-Security header is active!"
    else:
        results["Missing Strict-Transport-Security Header!"] = '''
The Strict-Transport-Security (HSTS) header is a security mechanism that helps protect against certain types of attacks, such as SSL-stripping and man-in-the-middle attacks. It ensures that a web page is only accessed over a secure HTTPS connection and prevents users' browsers from making insecure HTTP connections to the site.

When a web page includes the Strict-Transport-Security header, the browser will remember this information for a specified period of time. Subsequent requests to the same site will automatically be made over HTTPS, even if the user manually enters an HTTP URL.

If the Strict-Transport-Security header is missing or not configured correctly, the following vulnerabilities can occur:

- HTTP Browsing Vulnerability: In the absence of the Strict-Transport-Security header, the website is susceptible to potential downgrading attacks, where an attacker can intercept the initial HTTP request and prevent the browser from upgrading the connection to HTTPS. This allows the attacker to eavesdrop on the communication and potentially perform unauthorized actions or gain access to sensitive information.

To enhance the security of your web application, it is recommended to include the Strict-Transport-Security header with an appropriate configuration, specifying a sufficiently long max-age value to enforce HTTPS and protect against potential downgrading attacks.
'''

    if "Content-Security-Policy" in headers:
        results["Content-Security-Policy"] = "Content-Security-Policy header is active!"
    else:
        results["Missing Content-Security-Policy Header!"] = '''
The Content-Security-Policy (CSP) header is a security mechanism that allows web developers to control the resources and behaviors that are allowed to be loaded on a web page. It helps protect against various types of attacks, including cross-site scripting (XSS), data injection, and clickjacking.

The CSP header specifies a set of directives that define the sources from which certain types of content can be loaded. These directives can include policies for JavaScript, CSS, images, fonts, frames, media, and more.

By properly configuring the CSP header, web developers can enforce restrictions on what content is allowed to be executed or loaded on their web pages. This helps mitigate the risks associated with code injection attacks, malicious scripts, and other types of security vulnerabilities.

If the Content-Security-Policy header is missing or not configured correctly, the following vulnerabilities can occur:

- Cross-Site Scripting (XSS) Vulnerability: Without a proper CSP, an attacker may be able to inject and execute malicious scripts on the web page, leading to the theft of sensitive information, session hijacking, or unauthorized actions on behalf of the user.

- Data Injection Vulnerability: In the absence of CSP, an attacker can inject or modify content, such as forms, URLs, or AJAX requests, leading to data leakage, data manipulation, or unauthorized access to sensitive information.

- Clickjacking Vulnerability: Without CSP, an attacker can use clickjacking techniques to trick users into interacting with hidden or disguised elements on the web page, potentially performing unintended actions or disclosing sensitive information.

To enhance the security of your web application, it is strongly recommended to include the Content-Security-Policy header and properly configure it with appropriate directives to restrict the sources of content, prevent code injection, and protect against various types of attacks.
'''
    if "X-Content-Type-Options" in headers:
        results["X-Content-Type-Options"] = "X-Content-Type-Options header is active!"
    else:
        results["Missing X-Content-Type-Options Header!"] = '''
The X-Content-Type-Options header is a security measure that helps mitigate MIME type sniffing attacks. MIME type sniffing, also known as content sniffing, is a browser behavior where it attempts to determine the content type of a response based on its content rather than relying solely on the Content-Type header.

By including the X-Content-Type-Options header with the value "nosniff", web developers can instruct the browser to not perform MIME type sniffing and strictly adhere to the declared content type provided in the Content-Type header.

If the X-Content-Type-Options header is missing, the following vulnerabilities can occur:

- MIME Type Sniffing Vulnerability: In the absence of the X-Content-Type-Options header, browsers may attempt to guess the content type of a response, which can lead to misinterpretation and potential security issues. Attackers can abuse this behavior to trick the browser into executing or rendering content in unintended ways, potentially leading to cross-site scripting (XSS) attacks or the disclosure of sensitive information.

To enhance the security of your web application, it is recommended to include the X-Content-Type-Options header with the value "nosniff" to prevent MIME type sniffing and enforce the declared content type specified in the Content-Type header.
'''

    if "Referrer-Policy" in headers:
        results["Referrer-Policy"] = "Referrer-Policy header is active!"
    else:
        results["Missing Referrer-Policy Header!"] = '''
The Referrer-Policy header allows web developers to control how the browser handles the Referer header when making requests from one site to another. The Referer header contains information about the source of the request, including the URL of the previous web page.

By setting the Referrer-Policy header, web developers can specify whether the Referer header should be included, excluded, or modified when navigating between different sites. This helps protect user privacy and provides control over the information disclosed in the Referer header.

If the Referrer-Policy header is missing, the following vulnerabilities can occur:

- Information Leakage: In the absence of the Referrer-Policy header, the browser may send the full URL of the previous page in the Referer header when navigating to a different site. This can potentially expose sensitive information, such as session IDs, user credentials, or personally identifiable information (PII), to the target site or third-party trackers.

To enhance the privacy and security of your web application, it is recommended to include the Referrer-Policy header and configure it to an appropriate value based on your specific requirements. This can help minimize the information disclosed in the Referer header and protect user privacy.
'''

    if "Permissions-Policy" in headers:
        results["Permissions-Policy"] = "Permissions-Policy header is active!"
    else:
        results["Missing Permissions-Policy Header!"] = '''
The Permissions-Policy header is a security mechanism that allows web developers to control and limit the permissions and capabilities of web features and APIs. It provides a way to define a set of policies that govern the access and usage of various browser features, such as geolocation, camera, microphone, and more.

By specifying the Permissions-Policy header with appropriate directives, web developers can restrict or grant permissions to specific features and APIs based on the origin or context of the web page. This helps protect user privacy, prevent abuse, and reduce the risk of unauthorized access or data leakage.

If the Permissions-Policy header is missing, the following vulnerabilities can occur:

- Unrestricted Access to Features: In the absence of the Permissions-Policy header, the browser may allow unrestricted access to various features and APIs, potentially exposing sensitive user data or enabling malicious activities. This can result in unauthorized access to device capabilities, tracking of user activities, or abuse of APIs for malicious purposes.

To enhance the security and privacy of your web application, it is recommended to include the Permissions-Policy header and define appropriate policies for each feature and API used by your website. By carefully managing permissions, you can control access to sensitive capabilities and reduce the risk of abuse or unauthorized access.
'''


    return jsonify({'headers': results})

# if __name__ == '__main__':
#     app.run()
