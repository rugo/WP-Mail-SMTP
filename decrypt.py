import base64
import sys

try:
    import nacl.secret
except ImportError:
    print("PyNaCl not installed", file=sys.stderr)
    sys.exit(1)


def main():
    if len(sys.argv) < 3:
        print(f"Use {sys.argv[0]} $wp_mail_smtp_mail_key_pass $wp_mail_smtp_mail_key")
        sys.exit(2)
    
    enc_pass = base64.b64decode(sys.argv[1])
    key = base64.b64decode(sys.argv[2])

    box = nacl.secret.SecretBox(key)
    plaintext = box.decrypt(
        enc_pass[nacl.secret.SecretBox.NONCE_SIZE:], 
        nonce=enc_pass[:nacl.secret.SecretBox.NONCE_SIZE]
    )

    print("Decrypted password:", plaintext)


if __name__ == "__main__":
    main()
