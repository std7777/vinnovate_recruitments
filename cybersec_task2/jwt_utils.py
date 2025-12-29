import jwt
from config import SECRET_KEY

def generate_token(username, role):
    payload = {
        "user": username,
        "role": role
        # ❌ No exp, no iss, no aud
        #The token never expires
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token


def decode_token(token):
    # ❌ Still insecure:
    # - No expiration validation
    # - No issuer / audience checks
    # - Trusts role from token
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#symmetric key