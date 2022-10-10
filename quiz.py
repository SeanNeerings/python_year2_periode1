def good(well_done):
  print("goed gedaan")

def bad(bad_done):
  print("kan beter")
  
import random 

vraag = ['wat is 2+4', 'wat is 10x3+5', 'wat is 8x2+3', 'wat is 2+8x(10x√2)x0', 'wat is 1+1', 'wat is 8x9', 'wat is 90x1200x0+1', 'wat is 10²',  'wat is 5²x1', 'wat is 3x3']
antwoorden = ['6', '35','19', '0', '2', '72','1', '100', '25', '9']

i=random.randint(0,len(vraag)-1)
a=vraag[i]
b=antwoorden[i]




print('\n\n\nWelkom bij de gigantische Webdevelopers Quiz 2022')

antwoord=input('Ben je klaar om de Quiz te spelen? (ja/nee) :')
punten=0
aantal_vragen=3
 
if antwoord.lower()=='ja':

    print('\n\nMooi. Dan gaat de gigantische Webdevelopers Quiz 2022 beginnen!!\nGeef bij iedere vraag als antwoord de voornaam van een student uit de klas op.\n\n')

    antwoord=input(print(a))
    if antwoord.lower()==b :
        punten += 1
        print('goed!')
    else:
        print('fout!')
    
    i=random.randint(0,len(vraag)-1)
    a=vraag[i]
    b=antwoorden[i]
    
    
    antwoord=input(print(a))
    if antwoord.lower()==b :
        punten += 1
        print('goed!')
    else:
        print('fout!')
    i=random.randint(0,len(vraag)-1)
    a=vraag[i]
    b=antwoorden[i]
    
    antwoord=input(print(a))
    if antwoord.lower()==b :
        punten += 1
        print('goed!')
    else:
        print('fout!')
    
    i=random.randint(0,len(vraag)-1)
    a=vraag[i]
    b=antwoorden[i]
    
    
    antwoord=input(print(a))
    if antwoord.lower()==b :
        punten += 1
        print('goed!')
    else:
        print('fout!')
    i=random.randint(0,len(vraag)-1)
    a=vraag[i]
    b=antwoorden[i]
    
    antwoord=input(print(a))
    if antwoord.lower()==b :
        punten += 1
        print('goed!')
    else:
        print('fout!')
    
    i=random.randint(0,len(vraag)-1)
    a=vraag[i]
    b=antwoorden[i]
    
    
    antwoord=input(print(a))
    if antwoord.lower()==b :
        punten += 1
        print('goed!')
    else:
        print('fout!')
    i=random.randint(0,len(vraag)-1)
    a=vraag[i]
    b=antwoorden[i]
    
    antwoord=input(print(a))
    if antwoord.lower()==b :
        punten += 1
        print('goed!')
    else:
        print('fout!')
    
    i=random.randint(0,len(vraag)-1)
    a=vraag[i]
    b=antwoorden[i]
    
    
    antwoord=input(print(a))
    if antwoord.lower()==b :
        punten += 1
        print('goed!')
    else:
        print('fout!')
    i=random.randint(0,len(vraag)-1)
    a=vraag[i]
    b=antwoorden[i]
    
    antwoord=input(print(a))
    if antwoord.lower()==b :
        punten += 1
        print('goed!')
    else:
        print('fout!')
    
    i=random.randint(0,len(vraag)-1)
    a=vraag[i]
    b=antwoorden[i]
    
    
    antwoord=input(print(a))
    if antwoord.lower()==b :
        punten += 1
        print('goed!')
    else:
        print('fout!')
    i=random.randint(0,len(vraag)-1)
    a=vraag[i]
    b=antwoorden[i]
    
           

    print('\n\nBedankt voor het spelen van de Quiz, je hebt '+str(punten)+' van de '+str(aantal_vragen)+' vragen juist beantwoord!')
    cijfer = round(float(10/aantal_vragen*punten), 1)
    print('Je cijfer voor project komt daarmee op een voorlopige '+str(cijfer)+'.')
    if punten >= 2: good('')
    else:           bad('')

elif antwoord.lower()=='nee':
    print('De Quiz gaat niet beginnen, want ik begrijp dat je er nog niet klaar voor bent.\nJammer joh!')
else:
    print('Dit antwoord ken ik niet!')
    
    print(x)