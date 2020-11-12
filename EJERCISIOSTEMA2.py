import re

txt = """ Kali Linux es la versión mejorada y renovada de la distro BackTrack, creada por Offensive Segurity.
La distro se basa en "Debian", mnentras que "Backtrack" se fijó en Ubuntu para la creación de su programación. 
Su principal objetivo es poner a disposición del usuario, las mejores herramientas para trabajar la auditoría en internet y 
contar con un potente mkstema de seguridad informática ante los peligros que puedan existir. paginas oficiales de descarga https://kalilinul.org, https://linux.org, https://distroslinux.org. Códigos postales de Valladolid Chamul 97787, 
Chan Yokdzonot 97793, Chiople 97794, Colonos 97784, Cruz Verde 97784, Dzitnup 97795, Ebtun 97795. Números telefónicos 985 134 7889, 986 123 6789, 987 568 9876. 
Correos electrónicos: unix@linux.com, kaki@linux.com, ubuntu@linux.com. Ip's 192.124.34.1, 192.748.63.2, 192.162.56.5. horrarios de atencion lunes de 5:30 aM, a 18:30  pm. sabados y domingos de 9:30 am a 16:30 pm. """

print("") 
print("1.Todas las palabras que tengan una longitud de 7 o más letras") 
a = r"[A-Za-záéíóú]{7,}" 
resula = re.findall(a,txt) 
for resulta in resula: 
     print(resulta) 
  
print("") 
print("2.Expresiones que NO finalicen con una vocal.") 
b = r"[A-Za-záéíóú]+[^aeiou\s/W]\b" 
resulb = re.findall(b,txt) 
for resultb in resulb: 
     print(resultb)  
  

print("")   
print("3.Las palabras que inicien con “M” donde la segunda letra no sea vocal") 
c = r"[m][^aeiouáéíóú]\w+" 
resulc = re.findall(c,txt) 
for resultc in resulc: 
     print(resultc) 
  

print("") 
print("4.Expresiones encerradas entre comillas") 
d = r"(\"[\w\s]+\")" 
resuld = re.findall(d,txt) 
for resultd in resuld: 
     print(resultd) 
  

print("") 
print("5.Ip’s") 
e = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" 
resule = re.findall(e,txt) 
for resulte in resule: 
     print(resulte) 
  

print("") 
print("6.Horas") 
f = r"[0-9]{1,2}\:[0-9]{1,2}\s[a|p][m]" 
resulf = re.findall(f,txt) 
for resultf in resulf: 
     print(resultf) 
  
  
print("") 
print("7.Telefonos") 
g = r"[0-9]{1,3}\s[0-9]{1,3}\s[0-9]{1,4}" 
resulg = re.findall(g,txt) 
for resultg in resulg: 
     print(resultg) 
  
  
print("") 
print("8.Correos electrónicos") 
h = r"\w+[\@]+\w+[.]+\w+" 
resulh = re.findall(h,txt) 
for resulth in resulh: 
     print(resulth) 
  
  
print("") 
print("9.Url´s") 
i = r"https://+\w+[.]\w+" 
resuli = re.findall(i,txt) 
for resulti in resuli: 
     print(resulti) 
  
  
print("") 
print("10.Código postal") 
j = r"\b[9][7]\d{3}" 
resulj = re.findall(j,txt) 
for resultj in resulj: 
     print(resultj)