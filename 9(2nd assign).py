def brute_force_otp(real_otp):
    for i in range(10000):
        otp = str(i).zfill(4)
        if otp == real_otp:
            print(f"OTP {otp} matched! Attempts: {i+1}")
            return otp
    print("OTP not found.")

brute_force_otp("2759")
