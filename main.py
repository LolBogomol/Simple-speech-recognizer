import subprocess
import speech_recognition
import pyaudio
import psutil
import os
MODE = True # Да да да я знаю что глобальные переменные это плохо. Все притензии сюда телеграм: @Lol_Bogomol, почта: adanbekov06@gmail.com 


class record_and_recognize():
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.microphone = speech_recognition.Microphone()
    def record_and_recognizer(self):
        with self.microphone:
                # игнорирование шума
                self.recognizer.adjust_for_ambient_noise(self.microphone,duration=2)
                try:
                    print('Слушаю....')
                    audio = self.recognizer.listen(self.microphone,5,5)
                    print('Начинаю преобразование...')
                    recognized_data = self.recognizer.recognize_google(audio,language='ru').lower()
                    return recognized_data
                # Обработка исключений
                except speech_recognition.WaitTimeoutError or speech_recognition.UnknownValueError:
                    print('Видимо произошла ошибка или Ты не говорил. %b Перезагружаю!')
                    self.record_and_recognizer()





class command_functions():
    def __init__(self):
        self.proggrams_for_close = ['chrome.exe','firefox.exe'] #добовляйте название процесса сюда! Они будут закрываться на слово очистка
    def turn_off():
        global MODE
        MODE = False
    def open_google():
        subprocess.call('"C:\Program Files\Google\Chrome\Application\chrome.exe"')
        return True
    def close_everything(self): #сейчас закрывает только гугл. Потом исправлю :) исправил, я держу своё слово!)
        for process in (process for process in psutil.process_iter() if process.name() in self.proggrams_for_close):
            process.kill()
        return True
class main:
    def __init__(self):
        self.сommand_dict = {'commands':{
        # Нужно добавлять название функции а в значения указать список ключевых слов
        # Можно добовлять только по однмому  слову в значение! Без фраз!
        'close_everything':['закрыть','очистка','очистить'],
        'open_google':['google','интернет','открой браузер'],
        'turn_off':["вырубись", "выключись", "отключись", "вырубайся", "вырубить","выключились","отключить","выключить"],}}
    def compare_commands(self,voice_input):
        splited_audio = voice_input.split()
        command_func = command_functions()
        for k,v in self.сommand_dict['commands'].items(): # "k" это ключи а "v" это значение
            '''Я знаю что для некоторых if воняет но оно работает'''
            if len(splited_audio) < 2:
                for i in voice_input.split():
                    if i in v:
                        getattr(command_func,k)()
                        break
            elif len(splited_audio) >= 2:
                    for i in range(1,len(splited_audio)):
                        if splited_audio[i-1] + ' ' + splited_audio[i] in v:
                         getattr(command_func,k)()
                         break
    def main(self):
        while MODE == True:
        # старт записи речи с последующим выводом распознанной речи 
            try:
                record_data = record_and_recognize()
                audio = record_data.record_and_recognizer()
                print(audio)
                self.compare_commands(audio)
            except speech_recognition.UnknownValueError:
                print("Не удалось распознать речь!")





if __name__ == "__main__":
    start = main()
    start.main()
