import hashlib
secret = "ckczppom"
notDone = True
i = 0

while notDone:
  string = "%s%i" % (secret, i)
  m = hashlib.md5()
  m.update(string)
  if m.hexdigest()[:5] == "00000":
    print i
    notDone = False 
  i += 1