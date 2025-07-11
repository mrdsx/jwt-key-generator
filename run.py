from jwcrypto import jwk
import json
import base64

from generate_hash import generate_hash

JWT_KEY_FILE_NAME = "jwks-es.json"
JWT_ALGO = "ES256"

decoded = None

key = jwk.JWK.generate(kty="EC", crv="P-256", use="sig", alg=JWT_ALGO)
key.kid = key.thumbprint()

jwk_set = {
    "keys": [json.loads(key.export(private_key=True))]
}

with open(JWT_KEY_FILE_NAME, "w", encoding="utf-8") as f:
    json.dump(jwk_set, f, ensure_ascii=False, indent=2)

with open(JWT_KEY_FILE_NAME, "rb") as f:
    encoded = base64.b64encode(f.read())
    decoded = encoded.decode("utf-8")


with open(".env", "w") as f:
    hash = generate_hash()
    f.write(f"SECRET_KEY={hash}\n"
            f"JWT_ALGO={JWT_ALGO}\n"
            f"ES256_KID={key.kid}\n\n"
            f"ES256_KEY={decoded}")