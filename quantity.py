def Fertilizer(Fertilizer):
    n=0
    p=0
    k=0
    m=0
    s=0
    Fe=0
    if Fertilizer == 'Urea':
        n=46
    if Fertilizer == 'DAP':
        n=18
        p=46
    if Fertilizer == 'MOP':
        k=61
    if Fertilizer == '10:26:26 NPK':
        n=10
        p=26
        k=26
    if Fertilizer == 'SSP':
        p=18
    if Fertilizer == 'Magnesium Sulphate':
        m=9
        s=12
    if Fertilizer == '13:32:26 NPK':
        n=13
        p=32
        k=26
    if Fertilizer == '12:32:16 NPK':
        n=12
        p=32
        k=16
    if Fertilizer == '50:26:26 NPK':
        n=50
        p=26
        k=26
    if Fertilizer == '19:19:19 NPK':
        n=19
        p=19
        k=19
    if Fertilizer == '18:46:00 NPK':
        n=18
        p=46
    if Fertilizer == 'Sulphur':
        s=92
    if Fertilizer == '20:20:20 NPK':
        n=20
        p=20
        k=20
    if Fertilizer == 'Ammonium Sulphate':
        n=21
        s=24
    if Fertilizer == 'Ferrous Sulphate':
        Fe=25
    if Fertilizer == 'White Potash':
        k=61
    if Fertilizer == '10:10:10 NPK':
        n=10
        p=10
        k=10
    if Fertilizer == '14-35-14':
        n=14
        p=35
        k=14
    if Fertilizer == '28-28':
        n=28
        p=28
    if Fertilizer == '17-17-17':
        n=17
        p=17
        k=17
    if Fertilizer == '20-20':
        n=20
        p=20
    if Fertilizer == '10-26-26':
        n=10
        p=26
        k=26
    return n
fer_n = Fertilizer('Urea')

def Crop_Nutrients(Crop):
    if Crop == 'Sugarcane':
        n=175
        k=175
        p=65
    if Crop == 'Jowar':
        n=70
        p=35
        k=50
    if Crop == 'Cotton':
        n=110
        p=50
        k=60
    if Crop == 'Rice':
        n=100
        p=40
        k=50
    if Crop == 'Wheat':
        n=175
        p=40
        k=45
    if Crop == 'Groundnut':
        n=25
        p=50
        k=50
    if Crop == 'Maize':
        n=190
        p=70
        k=90
    if Crop == 'Urad':
        n=30
        p=40
        k=50
    if Crop == 'Ginger':
        n=90
        p=40
        k=80
    if Crop == 'Turmeric':
        n=100
        p=50
        k=80
    if Crop == 'Grapes':
        n=80
        p=40
        k=100
    if Crop == 'chickpea':
        n=30
        p=40
        k=40
    if Crop == 'kidneybeans':
        n=50
        p=40
        k=50
    if Crop == 'pigeonpeas':
        n=30
        p=50
        k=50
    if Crop == 'mothbeans':
        n=30
        p=40
        k=40
    if Crop == 'mungbean':
        n=30
        p=40
        k=40
    if Crop == 'blackgram':
        n=30
        p=40
        k=40
    if Crop == 'lentil':
        n=30
        p=40
        k=40
    if Crop == 'pomegranate':
        n=80
        p=50
        k=125
    if Crop == 'banana':
        n=175
        p=50
        k=250
    if Crop == 'mango':
        n=100
        p=50
        k=100
    if Crop == 'grapes':
        n=80
        p=40
        k=100
    if Crop == 'watermelon':
        n=175
        p=40
        k=100
    if Crop == 'muskmelon':
        n=100
        p=40
        k=100
    if Crop == 'apple':
        n=175
        p=50
        k=175
    if Crop == 'orange':
        n=175
        p=65
        k=175
    if Crop == 'papaya':
        n=125
        p=40
        k=175
    if Crop == 'coconut':
        n=125
        p=65
        k=250
    if Crop == 'jute':
        n=100
        p=40
        k=80
    if Crop == 'coffee':
        n=125
        p=50
        k=175
    if Crop == 'Tobacco':
        n=125
        p=65
        k=100
    if Crop == 'Barley':
        n=100
        p=40
        k=40
    if Crop == 'Millets':
        n=60
        p=40
        k=45
    if Crop == 'Oil seeds':
        n=100
        p=40
        k=80
    return n,p,k

N,P,K=Crop_Nutrients('Rice')
def fertilzerquantity(N,n,no_of_acres,fer_n):
    N=N*no_of_acres
    n=n*no_of_acres
    Nitrogen_defiency = N-n
    fertilizer_rate = (Nitrogen_defiency * 100)/fer_n
    return fertilizer_rate

no_of_acres=2
a=(fertilzerquantity(N,20,no_of_acres,fer_n))/2.20

print(f"Fertilizer quantity ={a:.1f} kg")
def fertilzerquantity(N,n,no_of_acres,fer_p):
    N=N*no_of_acres
    n=n*no_of_acres
    Phosphosos_defiency = N-n
    fertilizer_rate = (Phosphosos_defiency * 100)/fer_p
    return fertilizer_rate

no_of_acres=2
#b=(fertilzerquantity(rice_n,soil_n,no_of_acres,fer_p))/2.20

#print(f"Fertilizer quantity ={b:.1f} kg")

def fertilzerquantity(N,n,no_of_acres,fer_k):
    N=N*no_of_acres
    n=n*no_of_acres
    Pottassium_defiency = N-n
    #fertilizer_rate = (Potassium_defiency * 100)/fer_n
    #return fertilizer_rate

no_of_acres=2
#c=(fertilzerquantity(rice_n,soil_n,no_of_acres,fer_n))/2.20

#print(f"Fertilizer quantity ={c:.1f} kg")

