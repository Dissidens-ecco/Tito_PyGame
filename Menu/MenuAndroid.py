# -*- coding: utf-8 -*-

#Importar Biblioteca
import pygame
#import speech_recognition as sr
import android
import pyttsx3
import time
import webbrowser
import pyaudio

#Inicializar bibliotecas
pygame.init()
engine = pyttsx3.init()
voice_id_eng_h = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
voice_id_mxn_m = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-55)
engine.setProperty('voice', voice_id_mxn_m)
lang = 0

def lenguaje(leng):
    if leng == 'Esp':
        voice_len = voice_id_mxn_m
        lang=0
    elif leng == 'Eng':
        voice_len = voice_id_eng_h
        lang=1
    else:
        voice_len = voice_id_mxn_m
    engine.setProperty('voice', voice_len)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-55)
    return lang

#Solo Dialogos
def talk(text):
    engine.say(text)
    engine.runAndWait()

#interacciones
def interaccion():
    droid = android.Android()
    try:
        (id, result, error) = droid.recognizeSpeech()
        return result
    except:
        result = "Lo siento, no te entendí"
        return result
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        engine.runAndWait()
        audio = r.listen(source)

    try:
        resp = r.recognize_google(audio,language="es-ES")
        print("Tu: " + resp)
        return resp
    except sr.UnknownValueError:
        print("Lo siento, no te entendí. ¿Puedes repetirlo por favor?")
        return '   '
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    """
    
#Botones
class Button():
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self,surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image,(self.rect.x,self.rect.y))

        return action

def main():
    name = 'Tito'

    #Crear pagina principal
    width = 800
    height = 600
    id_al=''

    #Variables de menu
    menu_principal = False
    menu_state = "main"

    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption(name + " Asistente Anahuac")

    #Definir fuentes
    font = pygame.font.SysFont("calibri", 40,True)
    font2 = pygame.font.SysFont("calibri", 60,True)
    font3 = pygame.font.SysFont("calibri", 28,True)
    font4 = pygame.font.SysFont("calibri", 72,True)
    font5 = pygame.font.SysFont("calibri", 20,True)

    #Definir colores
    TEXT_COL = (255,131,0)

    #cargar botones
    img_bs = pygame.image.load("botones/bs.png").convert_alpha()
    img_id = pygame.image.load("botones/id.png").convert_alpha()
    img_mail = pygame.image.load("botones/mail.png").convert_alpha()
    img_wifi = pygame.image.load("botones/wifi.png").convert_alpha()
    img_sw = pygame.image.load("botones/sw.png").convert_alpha()
    img_ret = pygame.image.load("botones/salir.png").convert_alpha()
    img_retm = pygame.image.load("botones/ret.png").convert_alpha()
    img_esp = pygame.image.load("botones/esp.png").convert_alpha()
    # img_eng = pygame.image.load("botones/eng.png").convert_alpha()
    img_conf = pygame.image.load("botones/conf.png").convert_alpha()
    img_tito = pygame.image.load("botones/tito.png").convert_alpha()
    img_per = pygame.image.load("botones/per.png").convert_alpha()
    qr_bs = pygame.image.load("botones/qr_bs.png").convert_alpha()
    qr_correo = pygame.image.load("botones/qr_bs.png").convert_alpha()
    qr_sa = pygame.image.load("botones/qr_bs.png").convert_alpha()
    qr_wifi = pygame.image.load("botones/qr_bs.png").convert_alpha()
    img_mic_verde = pygame.image.load("botones/verde.png").convert_alpha()
    img_mic_rojo = pygame.image.load("botones/Rojo.jpg").convert_alpha()
    img_inicio = pygame.image.load("botones/inicio.png").convert_alpha()

    tamx = 250
    tamy = 250
    posix = 265
    posiy = 300
    qr_bs = pygame.transform.scale(qr_bs,(tamx,tamy))
    qr_correo = pygame.transform.scale(qr_correo,(tamx,tamy))
    qr_sa = pygame.transform.scale(qr_sa,(tamx,tamy))
    qr_wifi = pygame.transform.scale(qr_wifi,(tamx,tamy))

    tito_speech = 150
    per_speech = tito_speech+30

    #instancias
    escala = 0.60
    button_bs = Button(35,300,img_bs,escala) 
    button_id = Button(285,300,img_id,escala) 
    button_mail = Button(535,300,img_mail,escala) 
    button_wifi = Button(35,450,img_wifi,escala) 
    button_sw = Button(285,450,img_sw,escala) 
    button_ret = Button(535,450,img_ret,escala)
    button_retm = Button(600,500,img_retm,0.4) 
    button_esp = Button(285,350,img_esp,escala) 
    # button_eng = Button(450,250,img_eng,escala) 
    button_conf = Button(285,350,img_conf,escala) 
    button_tito = Button(10,tito_speech,img_tito,0.2)
    button_tito2 = Button(10,tito_speech+30,img_tito,0.2)
    button_tito3 = Button(10,tito_speech+60,img_tito,0.2) 
    button_per = Button(10,per_speech,img_per,0.2)
    button_per2 = Button(10,per_speech+60,img_per,0.2)
    button_verde = Button(700,10,img_mic_verde,0.2)
    button_rojo = Button(700,10,img_mic_rojo,0.08)
    button_inicio = Button(285,450,img_inicio,escala) 

    def draw_text(text,font,text_color,x,y):
        img = font.render(text,True,text_color)
        screen.blit(img,(x,y))

    def menu_idioma():
        menu_flag = True
        while(menu_flag):
            #Pregunta
            preg = "Hola soy Tito, por favor elige un idioma."
            draw_text(preg,font5,TEXT_COL,40,tito_speech)
            if button_rojo.draw(screen):
                repollo = 1
            pygame.display.update()
            if button_tito.draw(screen):
                repollo = 1
            pygame.display.update()
            talk(preg)
            if button_verde.draw(screen):
                repollo = 1
            pygame.display.update()
            texto = interaccion()
            if button_rojo.draw(screen):
                repollo = 1
            pygame.display.update()
            draw_text(texto,font5,TEXT_COL,40,per_speech)
            if button_per.draw(screen):
                repollo = 1
            pygame.display.update()
            
            #Condicionales
            if (texto.find('español')>-1):
                talk("Haz seleccionado el idioma español")
                menu_flag = False
                return "main"
            elif (texto.find('regresar')>-1 or texto.find('anterior')>-1 or texto.find('regresa')>-1):
                menu_flag = False
                return "regresar"
            else:
                talk("No te entendí")
                
    def menu_int_id():
        menu_flag = True
        while(menu_flag):
            #Pregunta
            if button_rojo.draw(screen):
                repollo = 1
            pygame.display.update()
            preg = "Por favor dame tu ID con todo y ceros."
            draw_text(preg,font5,TEXT_COL,40,tito_speech)
            if button_tito.draw(screen):
                repollo = 1
            pygame.display.update()
            talk(preg)
            if button_verde.draw(screen):
                repollo = 1
            pygame.display.update()
            texto = interaccion()
            if button_rojo.draw(screen):
                repollo = 1
            pygame.display.update()
            texto_p = texto.replace(' ','')
            pos_id = texto_p.find('0')
            per_id = texto_p[pos_id:pos_id+8]
            print(per_id)
            
            draw_text(per_id,font5,TEXT_COL,40,per_speech)
            if button_per.draw(screen):
                repollo = 1
            pygame.display.update()
            
            #Condicionales
            if (texto.find('atras')>-1 or texto.find('anterior')>-1 or texto.find('regresa')>-1):
                menu_flag = False
                return "regresar"
            else:
                return per_id
    
    def menu_int_id_conf():
        menu_flag = True
        pygame.display.update()
        while(menu_flag):
            #Pregunta
            if button_rojo.draw(screen):
                repollo = 1
            pygame.display.update()
            preg = "¿Puedes confirmar si es tu ID?"
            draw_text(preg,font5,TEXT_COL,40,tito_speech+60)
            if button_tito3.draw(screen):
                repollo = 1
            pygame.display.update()
            talk(preg)
            if button_verde.draw(screen):
                repollo = 1
            pygame.display.update()
            texto = interaccion()
            if button_rojo.draw(screen):
                repollo = 1
            pygame.display.update()
            draw_text(texto,font5,TEXT_COL,40,per_speech+60)
            if button_per2.draw(screen):
                repollo = 1
            pygame.display.update()
            #Condicionales
            if (texto.find('confirmo')>-1 or texto.find('sí')>-1 or texto.find('acepto')>-1 or texto.find('Sí')>-1 or texto.find('correcto')>-1or texto.find('bien')>-1 or texto.find('firmo')>-1 or texto.find('ese')>-1 or texto.find('perfecto')):
                pygame.display.update()
                menu_flag = False
                resp_m="Tu ID ha sido reiniciado, intenta ingresar nuevamente con dos dígitos para día, dos para mes y dos para año."
                talk(resp_m)
                return "main"
            if (texto.find('no')>-1 or texto.find('negativo')>-1 or texto.find('No')>-1) or texto.find('mal')>-1or texto.find('inocorrecto')>-1:
                pygame.display.update()
                menu_flag = False 
                id_al=''
                return "int_id"
            if (texto.find('regresa')>-1 or texto.find('atras')>-1 or texto.find('anterior')>-1):
                pygame.display.update()
                menu_flag = False
                id_al=''
                return "regresar"

    def menu_main():
        menu_flag = True
        iteracion1 = 0
        while(menu_flag):
            #Pregunta
            preg = "Hola, soy Tito, ¿En qué te puedo ayudar?"
            draw_text(preg,font5,TEXT_COL,40,tito_speech)
            iteracion1 = iteracion1 + 1
            print(iteracion1)
            if button_tito.draw(screen):
                repollo = 1
            pygame.display.update()
            talk(preg)
            if button_verde.draw(screen):
                repollo = 1
            pygame.display.update()
            texto = interaccion()
            if button_rojo.draw(screen):
                repollo = 1
            pygame.display.update()
            draw_text(texto,font5,TEXT_COL,40,per_speech)
            if button_per.draw(screen):
                repollo = 1
            pygame.display.update()

            #Condicionales
            if (texto.find('software')>-1) or (texto.find('programa')>-1):
                resp_m="Haz elegido Software."
                talk(resp_m)
                draw_text(resp_m,font5,TEXT_COL,40,tito_speech+60)
                if button_tito3.draw(screen):
                    repollo = 1
                pygame.display.update()
                time.sleep(2)
                menu_flag = False
                return "sw"
            elif (texto.find('brightspace')>-1) or (texto.find('bright')>-1) or (texto.find('Bright')>-1) or (texto.find('Space')>-1) or (texto.find('space')>-1) or (texto.find('plataforma')>-1):
                resp_m="Haz elegido Brightspace."
                talk(resp_m)
                draw_text(resp_m,font5,TEXT_COL,40,tito_speech+60)
                if button_tito3.draw(screen):
                    repollo = 1
                pygame.display.update()
                time.sleep(2)
                menu_flag = False
                return "bs"
            elif (texto.find('correo')>-1) or (texto.find('mail')>-1) or (texto.find('email')>-1) or (texto.find('institucional')>-1):
                resp_m="Haz elegido Correo."
                talk(resp_m)
                draw_text(resp_m,font5,TEXT_COL,40,tito_speech+60)
                if button_tito3.draw(screen):
                    repollo = 1
                pygame.display.update()
                time.sleep(2)
                menu_flag = False
                return "mail"
            elif (texto.find('wi-fi')>-1) or (texto.find('wi')>-1) or (texto.find('fi')>-1) or (texto.find('internet')>-1) or (texto.find('red')>-1):
                resp_m="Haz elegido Internet."
                talk(resp_m)
                draw_text(resp_m,font5,TEXT_COL,40,tito_speech+60)
                if button_tito3.draw(screen):
                    repollo = 1
                pygame.display.update()
                time.sleep(2)
                menu_flag = False
                return "wifi"
            elif (texto.find('regresa')>-1 or texto.find('atras')>-1 or texto.find('anterior')>-1 or texto.find('salir')>-1 or texto.find('terminar')>-1 or texto.find('no')>-1 or texto.find('No')>-1 or texto.find('nada')>-1) or texto.find('es todo')>-1:
                resp_m="Hasta luego, buen día."
                talk(resp_m)
                draw_text(resp_m,font5,TEXT_COL,40,tito_speech+60)
                if button_tito3.draw(screen):
                    repollo = 1
                pygame.display.update()
                time.sleep(2)
                menu_int_id = False
                id_al=''
                return "regresar"
            elif (texto.find('ID')>-1) or (texto.find('id')>-1) or (texto.find('matrícula')>-1):
                resp_m="Haz elegido reiniciar ID."
                talk(resp_m)
                draw_text(resp_m,font5,TEXT_COL,40,tito_speech+60)
                if button_tito3.draw(screen):
                    repollo = 1
                pygame.display.update()
                time.sleep(2)
                menu_flag = False
                return "int_id"
            else:
                rne="Lo siento, no te entendí"
                talk(rne)
                draw_text(rne,font5,TEXT_COL,40,tito_speech+60)
                if button_tito3.draw(screen):
                    repollo = 1
                pygame.display.update()
                time.sleep(1)
                if iteracion1 > 2:
                    return "regresar"
                else:
                    return "main"

    def menu_wifi():
        menu_flag = True
        while(menu_flag):
            #Preguntaáhuac, y la contraseña es:"
            preg = "Escaneando el siguiente QR podrás conectarte a la red."
            draw_text(preg,font5,TEXT_COL,40,tito_speech)
            if button_tito.draw(screen):
                repollo = 1
            draw_text("A202260_a", font4, TEXT_COL,350,300)
            pygame.display.update()
            screen.blit(qr_wifi, (75,300))
            pygame.display.update()
            talk(preg)
            talk("A mayúscula 20 22 60, _ a")
            time.sleep(10)
            return "regresar"

    def menu_mail():
        menu_flag = True
        while(menu_flag):
            #Pregunta
            preg = "Escaneando el siguiente QR encontrarás la información necesaria."
            draw_text(preg,font5,TEXT_COL,40,tito_speech)
            if button_tito.draw(screen):
                repollo = 1
            draw_text("También puedes visitar Centro de Cómputo en Torre 3 en campus sur",font5,TEXT_COL,40,tito_speech+30)
            if button_tito2.draw(screen):
                repollo = 1
            draw_text("O biblioteca en campus norte",font5,TEXT_COL,40,tito_speech+60)
            if button_tito3.draw(screen):
                repollo = 1
            pygame.display.update()
            screen.blit(qr_correo, (posix,posiy))
            pygame.display.update()
            talk(preg)
            talk("También puedes visitar Centro de Cómputo en Torre 3 en campus sur")
            talk("O biblioteca en campus norte")
            time.sleep(10)
            return "regresar"

    def menu_sw():
        menu_flag = True
        while(menu_flag):
            #Pregunta
            preg = "Escaneando el siguiente QR tendrás acceso al link donde encontrarás más información"
            draw_text(preg,font5,TEXT_COL,40,tito_speech)
            if button_tito.draw(screen):
                repollo = 1
            screen.blit(qr_sa, (posix,posiy))
            pygame.display.update()
            talk(preg)
            time.sleep(10)
            return "regresar"

    def menu_bs():
        menu_flag = True
        while(menu_flag):
            #Pregunta
            preg = "Puedes mandar un correo escaneando el código QR o manualmente a:"
            draw_text(preg,font5,TEXT_COL,40,tito_speech)
            if button_tito.draw(screen):
                repollo = 1
            draw_text("aprende@anahuac.mx",font5,TEXT_COL,40,tito_speech+30)
            if button_tito2.draw(screen):
                repollo = 1
            draw_text("Si necesitas más ayuda también puedes utilizar el chat en línea.",font5,TEXT_COL,40,tito_speech+60)
            if button_tito3.draw(screen):
                repollo = 1
            pygame.display.update()
            screen.blit(qr_bs, (posix,posiy))
            pygame.display.update()
            talk(preg)
            talk("aprende@anahuac.mx")
            talk("Si necesitas más ayuda también puedes utilizar el chat en línea.")
            time.sleep(10)
            return "regresar"

    #Ciclo del Menú
    run = True
    while run:
        screen.fill((255,255,255))
        if menu_principal == True:
            if menu_state == "idioma":
                screen.fill((255,255,255)) 
                draw_text(name + " Asistente Anáhuac", font4, TEXT_COL,45,50)
                if button_retm.draw(screen):
                    menu_principal = False
                    screen.fill((255,255,255)) 
                if button_esp.draw(screen):
                    menu_state = "main"
                    screen.fill((255,255,255)) 
                pygame.display.update()
                menu_state = menu_idioma()
                if menu_state == 'regresar':
                    menu_principal = False
                    menu_state = "idioma"
                    screen.fill((255,255,255)) 
            if menu_state == "main":
                screen.fill((255,255,255))
                draw_text(name + " Asistente Anáhuac", font4, TEXT_COL,45,50)
                if button_bs.draw(screen):
                    menu_state = "bs"
                if button_id.draw(screen):
                    menu_state = "int_id"
                if button_mail.draw(screen):
                    menu_state = "mail"
                if button_wifi.draw(screen):
                    menu_state = "wifi"
                if button_sw.draw(screen):
                    menu_state = "sw"
                if button_ret.draw(screen):
                    menu_principal = False
                    menu_state = "main"
                pygame.display.update()
                menu_state = menu_main()
                if menu_state == 'regresar':
                    menu_principal = False
            if menu_state == "bs":
                screen.fill((255,255,255)) 
                draw_text(name + " Asistente Anáhuac", font4, TEXT_COL,45,50)
                if button_retm.draw(screen):
                    menu_state = "main"
                pygame.display.update()
                menu_state = menu_bs()
                if menu_state == 'regresar':
                    menu_principal = False
                    menu_state = "main"
            if menu_state == "int_id":
                screen.fill((255,255,255)) 
                draw_text(name + " Asistente Anáhuac", font4, TEXT_COL,45,50)
                if button_retm.draw(screen):
                    menu_principal = "main"
                if button_conf.draw(screen):
                    menu_state = "main"
                pygame.display.update()
                id_al = menu_int_id()
                pygame.display.update()
                if id_al.find('00')>-1:
                    pygame.display.update()
                    menu_state = menu_int_id_conf()
                if id_al == 'regresar':
                    menu_state = "main"
                    id_al = ''
                    menu_principal = False
            if menu_state == "mail":
                screen.fill((255,255,255)) 
                draw_text(name + " Asistente Anáhuac", font4, TEXT_COL,45,50)
                if button_retm.draw(screen):
                    menu_state = "main"
                pygame.display.update()
                menu_state = menu_mail()
                if menu_state == 'regresar':
                    menu_principal = False
                    menu_state = "main"
            if menu_state == "wifi":
                screen.fill((255,255,255)) 
                draw_text(name + " Asistente Anáhuac", font4, TEXT_COL,45,50)
                if button_retm.draw(screen):
                    menu_state = "main"
                pygame.display.update()
                menu_state = menu_wifi()
                if menu_state == 'regresar':
                    menu_principal = False
                    menu_state = "main"
            if menu_state == "sw":
                screen.fill((255,255,255)) 
                draw_text(name + " Asistente Anáhuac", font4, TEXT_COL,45,50)
                if button_retm.draw(screen):
                    menu_state = "main"
                pygame.display.update()
                menu_state = menu_sw()
                if menu_state == 'regresar':
                    menu_principal = False
                    menu_state = "main"
        else:
            draw_text(name + " Asistente Anáhuac", font4, TEXT_COL,45,50)
            draw_text("Bienvenido", font2, TEXT_COL,270,250)
            draw_text("Presiona el botón para continuar", font, TEXT_COL,80,400)
            if button_inicio.draw(screen):
                    menu_state = "main"
                    menu_principal = True
            pygame.display.update()

        #Eventos
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                repollo = 1
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                run = False
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main() 
