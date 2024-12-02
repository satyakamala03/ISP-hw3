import oqs

print(dir(oqs))

def main():
    # Step 1: Enumerate supported post-quantum signature mechanisms
    print("Available Signature Mechanisms:")
    for sig in oqs.get_enabled_sig_mechanisms():
        print(sig)

    # Use a specific post-quantum signature mechanism, e.g., 'Dilithium3'
    signature_algorithm = "Dilithium3"

    # Step 2: Source Device - Generate a key pair
    print("\nSource Device: Generating Key Pair...")
    with oqs.Signature(signature_algorithm) as signer:
        public_key = signer.generate_keypair()
        private_key = signer.export_secret_key()
        print(f"Public Key: {len(public_key)} bytes")
        print(f"Private Key: {len(private_key)} bytes")

        # Step 3: Sign a message
        message = b"This is a secure message from the source device."
        print(f"\nMessage to be signed: {message.decode()}")
        signature = signer.sign(message)
        print(f"Signature: {len(signature)} bytes")

    # Step 4: Transmit public key, message, and signature to the target device

    # Step 5: Target Device - Verify the signature
    print("\nTarget Device: Verifying Signature...")
    with oqs.Signature(signature_algorithm) as verifier:
        is_valid = verifier.verify(message, signature, public_key)
        if is_valid:
            print("Signature verification successful! The message is authentic.")
        else:
            print("Signature verification failed! The message may have been tampered with.")

if __name__ == "__main__":
    main()