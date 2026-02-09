def simple_rle(text):
    if not text: return "", "", 0, ""
    
    # --- COMPRESSION ---
    result = ""
    count = 1
    for i in range(len(text)):
        # If current char is same as next, keep counting
        if i + 1 < len(text) and text[i] == text[i+1]:
            count += 1
        else:
            # Rule: '#' for numbers, nothing for single chars
            char = f"#{text[i]}" if text[i].isdigit() else text[i]
            prefix = str(count) if count > 1 else ""
            result += prefix + char
            count = 1 
            
    # --- PERCENTAGE ---
    # (Initial - Final) / Initial * 100
    per = ((len(text) - len(result)) / len(text)) * 100

    # --- DECOMPRESSION ---
    decoded = ""
    num = ""
    i = 0
    while i < len(result):
        if result[i].isdigit():
            num += result[i] # Build the number (e.g., '1' then '2' for 12)
        elif result[i] == "#":
            # If we see #, the NEXT thing is the actual digit
            count = int(num) if num else 1
            decoded += result[i+1] * count
            num = ""
            i += 1 # Skip the digit we just used
        else:
            # It's a normal letter
            count = int(num) if num else 1
            decoded += result[i] * count
            num = ""
        i += 1
            
    return text, result, round(per, 1), decoded

# Test it
original, compressed, rate, decomp = simple_rle("aaaFyBssssssssssssazz")
print(f"Compressed: {compressed} | Rate: {rate}% | Back to: {decomp}")