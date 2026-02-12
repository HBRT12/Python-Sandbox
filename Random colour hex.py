import random  # Needed for generating random numbers

def main():
    code = random.randint(0, 0xFFFFFF)  # Generate a random integer between 0 and 0xFFFFFF (inclusive)
    hex_code = f"#{code:06X}" # Format the integer as a 6-digit hexadecimal string with a '#' prefix
    print(f"Random hex colour code: {hex_code}")

if __name__ == "__main__":  # Check if the script is being run directly (instead of imported as a module)
    main()