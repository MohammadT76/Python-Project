
# question link :
# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python
# ex) ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 

def find_needle(haystack):
    for index,value in enumerate(haystack):
        if value.lower()=='needle':
            return f"found the needle at position {index}"

print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))


# solution 2
def find_needle_v2 (haystack):
    return f"found the needle at position {haystack.index('needle')}"

print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))
