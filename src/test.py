f = open('access_log', 'r')

count = 0
for line in f:
    if line == '\n':
        continue
    data = line.strip().split()
    if len(data) == 10:
        ip, dash1, dash2, date, someshit, request, asset, type, status, size, = data
    if not asset.startswith("/"):
        index = 0
        for c in asset:
            if c == "/" and asset.index(c) > 7:
                index = asset.index(c)
                break
        asset[index:]
        
    print("{0}\t{1}".format(asset, "1"))
