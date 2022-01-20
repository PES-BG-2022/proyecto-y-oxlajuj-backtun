día1 = 1
mes1= 1
año1 = 1900
día2 = int(input("Ingrese el día de su nacimiento [1-31]: )"))
mes2= int(input("Ingrese el mes de su nacimiento [1-12]: )"))
año2 = int(input("Ingrese el año de su nacimiento [1900-2025]: )"))

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def dias(día1, mes1, año1, día2, mes2, año2):
   
    def bisiesto(año):
        return año % 4 == 0 and año % 100 != 0 or año % 400 == 0
    
    if (año1<año2):

        
        if bisiesto(año1) == False:
            mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            mes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
     
        restoMes = mes[mes1] - día1
    
        residuo = 0
        i = mes1 + 1
    
        while i <= 12:
            residuo = residuo + mes[i]
            i = i + 1
    
        primer_año = restoMes + residuo
    
        sum_año = año1 + 1
        total_dias = 0
    
        while (sum_año<año2):
            if bisiesto(sum_año) == False:
                total_dias = total_dias + 365
                sum_año = sum_año+ 1
            else:
                total_dias = total_dias + 366
                sum_año = sum_año + 1
    
    
        if bisiesto(año2) == False:
            mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            mes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
        mas_año = 0
        mas_año = 0
        i = 1
    
        while i < mes2:
            mas_año = mas_año + mes[i]
            i = i + 1
    
        ultimo_año = día2 + mas_año
    
        return total_dias + primer_año + ultimo_año
    
    
    else:
        
        if bisiesto(año1) == False:
            mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            mes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
        mas_año = 0
        total = 0
        i = mes1
        
        if i < mes2:
            while i < mes2:
                mas_año = mas_año + mes[i]
                i = i + 1
            total = día2 + mas_año - 1
            return total 
        else:
            total = día2 - día1
            return total

fecha =dias(1,1,1900,día2,mes2,año2)

def nahual(día1,mes1,año1,día2, mes2, año2):
    fecha=dias(día1,mes1,año1,día2, mes2, año2)
    if fecha%260==0:
        return "4 Tijax"
    elif fecha%260==1:
        return "5 Kawoq"
    elif fecha%260==2:
        return "6 Ajpu"
    elif fecha%260==3:
        return "7 Imox"
    elif fecha%260==4:
        return "8 Iq'"
    elif fecha%260==5:
        return "9 Aq'ab'al"
    elif fecha%260==6:
        return "10 K'at"
    elif fecha%260==7:
        return "11 Kan"
    elif fecha%260==8:
        return "12 Keme"
    elif fecha%260==9:
        return "13 Keej"
    elif fecha%260==10:
        return "1 Q'anil"
    elif fecha%260==11:
        return "2 Toj"
    elif fecha%260==12:
        return "3 Tz'i"
    elif fecha%260==13:
        return "4 Batz'"
    elif fecha%260==14:
        return "5 E"
    elif fecha%260==15:
        return "6 Aj"
    elif fecha%260==16:
        return "7 I'x"
    elif fecha%260==17:
        return "8 Tz'kin"
    elif fecha%260==18:
        return "9 Ajmaq"
    elif fecha%260==19:
        return "10 No'j"
    elif fecha%260==20:
        return "11 Tijax"
    elif fecha%260==21:
        return "12 Kawoq"
    elif fecha%260==22:
        return "13 Ajpu"
    elif fecha%260==23:
        return "1 Imox"
    elif fecha%260==24:
        return "2 Iq'"
    elif fecha%260==25:
        return "3 Aq'ab'al"
    elif fecha%260==26:
        return "4 K'at"
    elif fecha%260==27:
        return "5 Kan"
    elif fecha%260==28:
        return "6 Keme"
    elif fecha%260==29:
        return "7 Keej"
    elif fecha%260==30:
        return "8 Q'anil"
    elif fecha%260==31:
        return "9 Toj"
    elif fecha%260==32:
        return "10 Tz'i'"
    elif fecha%260==33:
        return "11 Batz'"
    elif fecha%260==34:
        return "12 E"
    elif fecha%260==35:
        return "13 Aj"
    elif fecha%260==36:
        return "1 I'x"
    elif fecha%260==37:
        return "2 Tz'ikin"
    elif fecha%260==38:
        return "3 Ajmaq"
    elif fecha%260==39:
        return "4 No'j"
    elif fecha%260==40:
        return "5 Tijax"
    elif fecha%260==41:
        return "6 Kawoq"
    elif fecha%260==42:
        return "7 Ajpu"
    elif fecha%260==43:
        return "8 Imox"
    elif fecha%260==44:
        return "9 Iq'"
    elif fecha%260==45:
        return "10 Aq'ab'al"
    elif fecha%260==46:
        return "11 K'at"
    elif fecha%260==47:
        return "12 Kan"
    elif fecha%260==48:
        return "13 Keme"
    elif fecha%260==49:
        return "1 Keej"
    elif fecha%260==50:
        return "2 Q'anil"
    elif fecha%260==51:
        return "3 Toj"
    elif fecha%260==52:
        return "4 Tz'i'"
    elif fecha%260==53:
        return "5 Batz'"
    elif fecha%260==54:
        return "6 E"
    elif fecha%260==55:
        return "7 Aj"
    elif fecha%260==56:
        return "8 Ix'"
    elif fecha%260==57:
        img = mpimg.imread('tzikin.png')
        imgplot = plt.imshow(img)
        plt.show()
        return "9 Tz'ikin"

    elif fecha%260==58:
        return "10 Ajmaq"
    elif fecha%260==59:
        return "11 No'j"
    elif fecha%260==60:
        return "12 Tijax"
    elif fecha%260==61:
        return "13 Kawoq"
    elif fecha%260==62:
        return "1 Ajpu"
    elif fecha%260==63:
        return "2 Imox"
    elif fecha%260==64:
        return "3 Iq'"
    elif fecha%260==65:
        return "4 Aq'ab'al"
    elif fecha%260==66:
        return "5 K'at"
    elif fecha%260==67:
        return "6 Kan"
    elif fecha%260==68:
        return "7 Keme"
    elif fecha%260==69:
        return "8 Keej"
    elif fecha%260==70:
        return "9 Q'anil"
    elif fecha%260==71:
        return "10 Toj"
    elif fecha%260==72:
        return "11 Tz'i'"
    elif fecha%260==73:
        return "12 Batz'"
    elif fecha%260==74:
        return "13 E"
    elif fecha%260==75:
        return "1 Aj"
    elif fecha%260==76:
        return "2 I'x"
    elif fecha%260==77:
        return "3 Tz'ikin"
    elif fecha%260==78:
        return "4 Ajmaq"
    elif fecha%260==79:
        return "5 No'j"
    elif fecha%260==80:
        return "6 Tijax"
    elif fecha%260==81:
        return "7 Kawoq"
    elif fecha%260==82:
        return "8 Ajpu"
    elif fecha%260==83:
        return "9 Imox"
    elif fecha%260==84:
        return "10 Iq'"
    elif fecha%260==85:
        return "11 Aq'ab'al"
    elif fecha%260==86:
        return "12 K'at"
    elif fecha%260==87:
        return "13 Kan"
    elif fecha%260==88:
        return "1 Keme"
    elif fecha%260==89:
        return "2Keej"
    elif fecha%260==90:
        return "3 Q'anil"
    elif fecha%260==91:
        return "4 Toj"
    elif fecha%260==92:
        return "5 Tz'i'"
    elif fecha%260==93:
        return "6 Batz'"
    elif fecha%260==94:
        return "7 E"
    elif fecha%260==95:
        return "8 Aj"
    elif fecha%260==96:
        return "9 I'x"
    elif fecha%260==97:
        return "10 Tz'ikin"
    elif fecha%260==98:
        return "11 Ajmaq"
    elif fecha%260==99:
        return "12 No'j"
    elif fecha%260==100:
        return "13 Tijax"
    elif fecha%260==101:
        return "1 Kawoq"
    elif fecha%260==102:
        return "2 Ajpu"
    elif fecha%260==103:
        return "3 Imox"
    elif fecha%260==104:
        return "4 Iq'"
    elif fecha%260==105:
        return "5 Aq'ab'al"
    elif fecha%260==106:
        return "6 K'at"
    elif fecha%260==107:
        return "7 Kan"
    elif fecha%260==108:
        return "8 Keme"
    elif fecha%260==109:
        return "9 Keej"
    elif fecha%260==110:
        return "10 Q'anil"
    elif fecha%260==111:
        return "11 Toj"
    elif fecha%260==112:
        return "12 Tz'i'"
    elif fecha%260==113:
        return "13 Batz'"
    elif fecha%260==114:
        return "1 E"
    elif fecha%260==115:
        return "2 Aj"
    elif fecha%260==116:
        return "3 I'x"
    elif fecha%260==117:
        return "4 Tz'ikin"
    elif fecha%260==118:
        return "5 Ajmaq"
    elif fecha%260==119:
        return "6 No'j"
    elif fecha%260==120:
        return "7 Tijax"
    elif fecha%260==121:
        return "8 Kawoq"
    elif fecha%260==122:
        return "9 Ajpu"
    elif fecha%260==123:
        return "10 Imox"
    elif fecha%260==124:
        return "11 Iq'"
    elif fecha%260==125:
        return "12 Aq'ab'al"
    elif fecha%260==126:
        return "13 K'at"
    elif fecha%260==127:
        return "1 Kan"
    elif fecha%260==128:
        return "2 Keme"
    elif fecha%260==129:
        return "3 Keej"
    elif fecha%260==130:
        return "4 Q'anil"
    elif fecha%260==131:
        return "5 Toj"
    elif fecha%260==132:
        return "6 Tz'i'"
    elif fecha%260==133:
        return "7 Batz'"
    elif fecha%260==134:
        return "8 E"
    elif fecha%260==135:
        return "9 Aj"
    elif fecha%260==136:
        return "10 I'x"
    elif fecha%260==137:
        return "11 Tz'ikin"
    elif fecha%260==138:
        return "12 Ajmaq"
    elif fecha%260==139:
        return "13 No'j"
    elif fecha%260==140:
        return "1 Tijax"
    elif fecha%260==141:
        return "2 Kawoq"
    elif fecha%260==142:
        return "3 Ajpu"
    elif fecha%260==143:
        return "4 Imox"
    elif fecha%260==144:
        return "5 Iq'"
    elif fecha%260==145:
        return "6 Aq'ab'al"
    elif fecha%260==146:
        return "7 K'at"
    elif fecha%260==147:
        return "8 Kan"
    elif fecha%260==148:
        return "9 Keme"
    elif fecha%260==149:
        return "10 Keej"
    elif fecha%260==150:
        return "11 Q'anil"
    elif fecha%260==151:
        return "12 Toj"
    elif fecha%260==152:
        return "13 Tz'i'"
    elif fecha%260==153:
        return "1 Batz'"
    elif fecha%260==154:
        return "2 E"
    elif fecha%260==155:
        return "3 Aj"
    elif fecha%260==156:
        return "4 I'x"
    elif fecha%260==157:
        return "5 Tz'ikin"
    elif fecha%260==158:
        return "6 Ajmaq"
    elif fecha%260==159:
        return "7 No'j"
    elif fecha%260==160:
        return "8 Tijax"
    elif fecha%260==161:
        return "9 Kawoq"
    elif fecha%260==162:
        return "10 Ajpu"
    elif fecha%260==163:
        return "11 Imox"
    elif fecha%260==164:
        return "12 Iq'"
    elif fecha%260==165:
        return "13 Aq'ab'al"
    elif fecha%260==166:
        return "1 K'at"
    elif fecha%260==167:
        return "2 Kan"
    elif fecha%260==168:
        return "3 Keme"
    elif fecha%260==169:
        return "4 Keej"
    elif fecha%260==170:
        return "5 Q'anil"
    elif fecha%260==171:
        return "6 Toj"
    elif fecha%260==172:
        return "7 Tz'i'"
    elif fecha%260==173:
        return "8 Batz'"
    elif fecha%260==174:
        return "9 E"
    elif fecha%260==175:
        return "10 Aj"
    elif fecha%260==176:
        return "11 I'x"
    elif fecha%260==177:
        return "12 Tz'ikin"
    elif fecha%260==178:
        return "13 Ajmaq"
    elif fecha%260==179:
        return "1 No'j"
    elif fecha%260==180:
        return "2 Tijax"
    elif fecha%260==181:
        return "3 Kawoq"
    elif fecha%260==182:
        return "4 Ajpu"
    elif fecha%260==183:
        return "5 Imox"
    elif fecha%260==184:
        return "6 Iq'"
    elif fecha%260==185:
        return "7 Aq'ab'al"
    elif fecha%260==186:
        return "8 K'at"
    elif fecha%260==187:
        return "9 Kan"
    elif fecha%260==188:
        return "10 Keme"
    elif fecha%260==189:
        return "11 Keej"
    elif fecha%260==190:
        return "12 Q'anil"
    elif fecha%260==191:
        return "13 Toj"
    elif fecha%260==192:
        return "1 Tz'i'"
    elif fecha%260==193:
        return "2 Batz'"
    elif fecha%260==194:
        return "3 E"
    elif fecha%260==195:
        return "4 Aj"
    elif fecha%260==196:
        return "5 I'x"
    elif fecha%260==197:
        return "6 Tz'ikin"
    elif fecha%260==198:
        return "7 Ajmaq"
    elif fecha%260==199:
        return "8 No'j"
    elif fecha%260==200:
        return "9 Tijax"
    elif fecha%260==201:
        return "10 Kawoq"
    elif fecha%260==202:
        return "11 Ajpu"
    elif fecha%260==203:
        return "12 Imox"
    elif fecha%260==204:
        return "13 Iq'"
    elif fecha%260==205:
        return "1 Aq'ab'al"
    elif fecha%260==206:
        return "2 K'at"
    elif fecha%260==207:
        return "3 Kan"
    elif fecha%260==208:
        return "4 Keme"
    elif fecha%260==209:
        return "5 Keej"
    elif fecha%260==210:
        return "6 Q'anil"
    elif fecha%260==211:
        return "7 Toj"
    elif fecha%260==212:
        return "8 Tz'i'"
    elif fecha%260==213:
        return "9 Batz'"
    elif fecha%260==214:
        return "10 E"
    elif fecha%260==215:
        return "11 Aj"
    elif fecha%260==216:
        return "12 I'x"
    elif fecha%260==217:
        return "13 Tz'ikin"
    elif fecha%260==218:
        return "1 Ajmaq"
    elif fecha%260==219:
        return "2 No'j"
    elif fecha%260==220:
        return "3 Tijax"
    elif fecha%260==221:
        return "4 Kawoq"
    elif fecha%260==222:
        return "5 Ajpu"
    elif fecha%260==223:
        return "6 Imox"
    elif fecha%260==224:
        return "7 Iq'"
    elif fecha%260==225:
        return "8 Aq'ab'al"
    elif fecha%260==226:
        return "9 K'at"
    elif fecha%260==227:
        return "10 Kan"
    elif fecha%260==228:
        return "11 Keme"
    elif fecha%260==229:
        return "12 Keej"
    elif fecha%260==230:
        return "13 Q'anil"
    elif fecha%260==231:
        return "1 Toj"
    elif fecha%260==232:
        return "2 Tz'i'"
    elif fecha%260==233:
        return "3 Batz'"
    elif fecha%260==234:
        return "4 E"
    elif fecha%260==235:
        return "5 Aj"
    elif fecha%260==236:
        return "6 I'x"
    elif fecha%260==237:
        return "7 Tz'ikin"
    elif fecha%260==238:
        return "8 Ajmaq"
    elif fecha%260==239:
        return "9 No'j"
    elif fecha%260==240:
        return "10 Tijax"
    elif fecha%260==241:
        return "11 Kawoq"
    elif fecha%260==242:
        return "12 Ajpu"
    elif fecha%260==243:
        return "13 Imox"
    elif fecha%260==244:
        return "1 Iq'"
    elif fecha%260==245:
        return "2 Aq'aba'l"
    elif fecha%260==246:
        return "3 K'at"
    elif fecha%260==247:
        return "4 Kan"
    elif fecha%260==248:
        return "5 Keme"
    elif fecha%260==249:
        return "6 Keej"
    elif fecha%260==250:
        return "7 Q'anil"
    elif fecha%260==251:
        return "8 Toj"
    elif fecha%260==252:
        return "9 Tz'i'"
    elif fecha%260==253:
        return "10 Batz'"
    elif fecha%260==254:
        return "11 E"
    elif fecha%260==255:
        return "12 Aj"
    elif fecha%260==256:
        return "13 I'x"
    elif fecha%260==257:
        return "1 Tz'ikin"
    elif fecha%260==258:
        return "2 Ajmaq"
    elif fecha%260==259:
        return "3 No'j"

nahual=nahual(1,1,1900,día2,mes2,año2)   
print(nahual)




