from libs.FingerPrint.fingerprint import FingerPrint

fingerprint = FingerPrint()
try:
    fingerprint.open()
    print("Please touch the fingerprint sensor")
    if fingerprint.verify():
        print("Authentication succeded!")
    else:
        print("Authentication failed!")
finally:
    fingerprint.close()