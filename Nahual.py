
día1=1
mes1=1
año1=1900
día2= int(input("Ingresa tu día de nacimiento [1-31]"))
mes2= int(input("Ingresa tu mes de nacimiento [1-12]"))
año2= int(input("Ingresa tu año de nacimiento [1900-2025]"))

def dias(día1,mes1,año1,día2, mes2, año2):

    def bisiesto(año):
        return año%4==0 and año%100 !=0 or año%400 !=0
    if año1<año2:
        if bisiesto(año1)==False:
            mes=[0,31,28,31,30,31,30,31,31,30,31,30,31]
        else:
            mes=[0,31,29,31,30,31,30,31,31,30,31,30,31]
        
        residuo_mes=mes[mes1]-día1
        residuo_año=0
        i=mes1+1

        while i<=12:
            residuo_año=residuo_año+mes[i]
            i=i+1
            primeraño=residuo_mes+residuo_año

            sum_año=año1+1
            total_días=0

            while (sum_año<año2):
                if bisiesto(sum_año)==False:
                    total_días=total_días+365
                    sum_año=sum_año+1
                else:
                    total_días=total_días+366
                    sum_año=sum_año+1

            if bisiesto(año2)==False:
                mes=[0,31,28,31,30,31,30,31,31,30,31,30,31]
            else:
                mes=[0,31,29,31,30,31,30,31,31,30,31,30,31]

                mas_año=0
                ultimo_año=0
                i=1
                while i<mes2:
                    mas_año=mas_año+mes[i]
                    i=i+1
                ultimo_año=día2+mas_año
                return total_días+primeraño+ultimo_año

        else:

            if bisiesto(año1)==False:
                mes=[0,31,28,31,30,31,30,31,31,30,31,30,31]
            else:
                mes=[0,31,29,31,30,31,30,31,31,30,31,30,31]
            
            mas_año=0
            total=0
            i=mes1

            if i<mes2:
                while i<mes2:
                    mas_año=mas_año+mes[i]
                    i=i+1
                total=día2+mas_año-1
                return total
            else:
                total = día2-día1
                return total
dias(1,1,1900,26, 10, 1999)

                




