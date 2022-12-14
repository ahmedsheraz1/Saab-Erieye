Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import hmac, hashlib
m = hmac.new(b'secret key', digestmod=hashlib.blake2s)
m.update(b'Saab Eieye AEW&C')
m.hexdigest()
'e56597574fecf9b128fab54a452abb352dc28728d36b4238cd20f03dffac8d14'
