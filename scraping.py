r=requests.get("http://www.ecmpcb.in/ocems/mahul")
soup=bs(r.content)
names=[]
for i in soup.find_all("span"):
  names.append(i.text.replace('\n', '').strip())
name=["BPC","BORIVALI","SEALORD","COLABA","AEGIS","HPC","TROMBAY"] 

for n, tt in zip(name, soup.find_all("table", attrs={"id":"sub-table"})):
  
  b=tt.find("thead")
  trr=b.find("tr")
  thh=trr.find_all("th")
  head=[]
  for i in thh:
    head.append(i.text.replace('\n', '').strip())
  l = []
  main=tt.find("tbody")
  for tr in main.find_all("tr"):
      td = tr.find_all('td')
      row = [tr.text.replace('\n','').strip() for tr in td]
      l.append(row)
  exec('{}= pd.DataFrame(l, columns=head)'.format(n))
 
  loc = []; no = 30; v = n

  for j in range(no):
      loc.append(v)
  exec('{}["Location"]=loc'.format(n))
print(COLABA) 
 
