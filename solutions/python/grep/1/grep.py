def grep(pattern, flags, files):
    found = ""

    len_files = len(files)
    for file_name in files:
        with open(file_name) as f:
            for line_number, line in enumerate(f, start=1):
                result = ""

                if "-i" in flags:
                    match_pattern = pattern.lower()
                    match_line = line.lower()
                else:
                    match_pattern = pattern
                    match_line = line

                if "-v" in flags:
                    match = match_pattern not in match_line
                elif "-x" in flags:
                    match = match_pattern == match_line.strip("\n")
                else:
                    match = match_pattern in match_line
                    
                    
                if "-l" in flags and match:
                    if file_name not in found:
                        result = f"{file_name}\n"
                else:
                    if "-x" in flags and match:
                        result = line
                        
                    if "-x" not in flags and match:
                        result = line

                    if result and "-n" in flags:
                        result = ':'.join((f"{line_number}", result))

                    if result and len_files > 1:
                        result = ':'.join((f"{file_name}", result))
                
                if result:
                    found += result

    return found