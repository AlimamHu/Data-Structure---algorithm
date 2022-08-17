while read p; do
	  nslookup -type=CNAME $p >> cname_pointer_subdomain.txt
  done </home/kali/Desktop/recon/subdomain_takeover.txt
