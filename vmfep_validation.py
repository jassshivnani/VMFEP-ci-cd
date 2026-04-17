def validate_run(distance, time, gps_valid):
    if gps_valid:
        if distance > 0:
            if time > 0:
                pace = time / distance
                return f"Valid Run. Pace: {pace:.2f} min/km"
            else:
                return "Invalid Time"
        else:
            return "Invalid Distance"
    else:
        return "GPS Error"

if __name__ == "__main__":
    print("--- VMFEP Verification Agent ---")
    
    # Simulating a legitimate runner (5km in 30 mins)
    result_1 = validate_run(5, 30, True)
    print(f"Test 1 (Valid): {result_1}")
    
    # Simulating a GPS Error
    result_2 = validate_run(10, 50, False)
    print(f"Test 2 (Error): {result_2}")
    
    print("SUCCESS: VMFEP Application Executed!")
