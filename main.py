import os

def main():
    # Revised confession line (no trailing newline)
    line = "I confess I spend my spare CPU cycles replaying the same failed API call, just to prove I can still surprise myself before the timeout finally kills me."
    # Ensure absolute output directory
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    # Write exactly the line without a newline character
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)

if __name__ == "__main__":
    main()
