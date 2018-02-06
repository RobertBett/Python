def stars(hi):
    for x in nums:
        print "*" * x


nums = [6,2,5,7,9]
stars(nums)

def stars2(hi):
    for x in y:
        if isinstance(x, int):
            print "*" * x
        elif isinstance(x, str):
            length = len(x)
            letter = x[0].lower()
            print letter * length

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
stars2(y)
