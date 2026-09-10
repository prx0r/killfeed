ok save this u can access agent-vault right ? POST /token HTTP/1.1
Host: oauth2.googleapis.com
Content-length: 317
content-type: application/x-www-form-urlencoded
user-agent: google-oauth-playground

code=4%2F0ATsMZqBkpgqSDQ0Gk6IJHOdSePByzGhS0AidIt5gdm3TTB7KymNSpozj-vQ_O07UKPGi_g&redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&client_id=REDACTED.apps.googleusercontent.com&client_secret=REDACTED&scope=&grant_type=authorization_code

HTTP/1.1 200 OK
Content-length: 528
X-xss-protection: 0
X-content-type-options: nosniff
Transfer-encoding: chunked
Expires: Mon, 01 Jan 1990 00:00:00 GMT
Vary: Origin, X-Origin, Referer
Server: scaffolding on HTTPServer2
-content-encoding: gzip
Pragma: no-cache
Cache-control: no-cache, no-store, max-age=0, must-revalidate
Date: Thu, 03 Sep 2026 01:46:40 GMT
X-frame-options: SAMEORIGIN
Alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
Content-type: application/json; charset=utf-8

{
  "access_token": "REDACTED", 
  "refresh_token_expires_in": 604799, 
  "expires_in": 3599, 
  "token_type": "Bearer", 
  "scope": "https://mail.google.com/", 
  "refresh_token": "REDACTED"
}  store this in agent vault and use it to access my gmail and get the zip i want and import it
