# Get sizes
while True:
    try:
        indexSize = int(raw_input("Index Size: "))
        offsetSize = int(raw_input("Offset size: "))
        break
    except ValueError:
        print 'Invalid size input, please enter an integer > 0'

tagEnd = 32 - indexSize - offsetSize
offsetStart = 32 - offsetSize

# Start main loop
while True:
    addr = raw_input("Enter 32 bit address (hex or dec) or press enter to exit: ")

    # Enter pressed?
    if not addr:
        exit()

    try:
        # Dec value?
        addr = int(addr)
    except ValueError:
        try:
            # Hex value?
            if addr[2:] == '0x':
                addr = int(addr[2:], 16)
            else:
                addr = int(addr, 16)
        except:
            print 'Unknown format, try again'
            continue

    binary = '{0:032b}'.format(addr)
    print "Binary = ", binary

    tag = binary[:tagEnd]
    print "Tag =", int(tag, 2)

    index = binary[tagEnd:offsetStart]
    print "Index =", int(index, 2)

    if offsetSize > 0:
        offset = binary[offsetStart:]
        print "Offset =", int(offset, 2)

    # New line separates calculations
    print ''
