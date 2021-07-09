from imports import *

r = sr.Recognizer()
Ashley = p.init()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    text = r.listen(source)

    try:
        recognised_text = r.recognize_google(text)
        print(recognised_text)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")

Ashley.say("Hey Dora, what can I do for you?")
Ashley.runAndWait()

ri = sr.Recognizer()
with sr.Microphone() as source:
    ri.adjust_for_ambient_noise(source)
    instruction = ri.listen(source)
    try:
        recognised_instruction = ri.recognize_google(instruction)
        print(recognised_instruction)

        r1 = sr.Recognizer()
        if "info" in recognised_instruction:
            Ashley.say("About what?")
            Ashley.runAndWait()
            with sr.Microphone() as source1:
                r1.adjust_for_ambient_noise(source1)
                text = r1.listen(source1)
                try:
                    about_info = r1.recognize_google(text)
                    print(about_info)
                    info_bot = Info()
                    info_bot.get_info(about_info)

                except sr.UnknownValueError:
                    print("")
                except sr.RequestError as e:
                    print("")

        r2 = sr.Recognizer()
        if "review" in recognised_instruction:
            Ashley.say("About which movie?")
            Ashley.runAndWait()
            with sr.Microphone() as source2:
                r2.adjust_for_ambient_noise(source)
                text = r2.listen(source2)
                try:
                    movie = r2.recognize_google(text)
                    print(movie)
                    movie_bot = Movie()
                    movie_bot.movie_review(movie)

                except sr.UnknownValueError:
                    print("")
                except sr.RequestError as e:
                    print("")

        r3 = sr.Recognizer()
        if "music" in recognised_instruction:
            Ashley.say("Which music?")
            Ashley.runAndWait()
            with sr.Microphone() as source3:
                r3.adjust_for_ambient_noise(source3)
                text = r3.listen(source3)
                try:
                    music = r3.recognize_google(text)
                    print(music)
                    music_bot = Music()
                    music_bot.playMusic(music)

                except sr.UnknownValueError:
                    print("")
                except sr.RequestError as e:
                    print("")

        r_rec = sr.Recognizer()
        if "record" in recognised_instruction:
            Ashley.say("For how many seconds do you wanna record?")
            Ashley.runAndWait()
            with sr.Microphone() as duration_source:
                r_rec.adjust_for_ambient_noise(duration_source)
                duration = r_rec.listen(duration_source)
                try:
                    recorder = Record()
                    recorder.record_voice(duration)

                except sr.UnknownValueError:
                    print("")
                except sr.RequestError as e:
                    print("")

        if "clap" in recognised_instruction:
            playsound('one-man-clapping.wav')

        if "recommend" in recognised_instruction:
            recommend_bot = Recom()
            recommend_bot.movieRecom()

        r4 = sr.Recognizer()
        if "calculate" in recognised_instruction:
            Ashley.say("Which calculation?")
            Ashley.runAndWait()
            with sr.Microphone() as source4:
                r4.adjust_for_ambient_noise(source4)
                text = r4.listen(source4)
                try:
                    if "product" in text:
                        try:
                            Ashley.say("Tell me the first number.")
                            Ashley.runAndWait()
                            r5 = sr.Recognizer()
                            with sr.Microphone() as src:
                                r5.adjust_for_ambient_noise(src)
                                first_num = r5.listen(src)
                                try:
                                    first_num = r5.recognize_google(first_num)
                                except sr.UnknownValueError:
                                    print("")
                                except sr.RequestError as e:
                                    print("")
                            Ashley.say("Now to second number.")
                            Ashley.runAndWait()
                            r6 = sr.Recognizer()
                            with sr.Microphone() as src1:
                                r6.adjust_for_ambient_noise(src1)
                                second_num = r6.listen(src1)
                                try:
                                    second_num = r6.recognize_google(second_num)
                                except sr.UnknownValueError:
                                    print("")
                                except sr.RequestError as e:
                                    print("")
                            Ashley.say(str(first_num * second_num))
                            Ashley.runAndWait()

                        except sr.UnknownValueError:
                            print("")
                        except sr.RequestError as e:
                            print("")

                    if "square root" in text:
                        try:
                            Ashley.say("Tell me number that you wanna take square root.")
                            Ashley.runAndWait()
                            r7 = sr.Recognizer()
                            with sr.Microphone() as src2:
                                r7.adjust_for_ambient_noise(src2)
                                num = r7.listen(src2)
                                try:
                                    num = r7.recognize_google(num)
                                except sr.UnknownValueError:
                                    print("")
                                except sr.RequestError as e:
                                    print("")
                            Ashley.say(str(sqrt(num)))
                            Ashley.runAndWait()

                        except sr.UnknownValueError:
                            print("")
                        except sr.RequestError as e:
                            print("")

                    if "square" in text:
                        try:
                            Ashley.say("Tell me the number that you wanna square.")
                            Ashley.runAndWait()
                            r8 = sr.Recognizer()
                            with sr.Microphone() as src3:
                                r8.adjust_for_ambient_noise(src3)
                                num = r8.listen(src3)
                                try:
                                    num = r.recognize_google(num)
                                except sr.UnknownValueError:
                                    print("")
                                except sr.RequestError as e:
                                    print("")
                            Ashley.say(str(num ** 2))
                            Ashley.runAndWait()

                        except sr.UnknownValueError:
                            print("")
                        except sr.RequestError as e:
                            print("")
                    if "cube" in text:
                        try:
                            Ashley.say("Tell me the number that you wanna cube.")
                            Ashley.runAndWait()
                            r9 = sr.Recognizer()
                            with sr.Microphone() as src4:
                                r9.adjust_for_ambient_noise(src4)
                                num = r9.listen(src4)
                                try:
                                    num = r9.recognize_google(num)
                                except sr.UnknownValueError:
                                    print("")
                                except sr.RequestError as e:
                                    print("")
                            Ashley.say(str(num ** 3))
                            Ashley.runAndWait()

                        except sr.UnknownValueError:
                            print("")
                        except sr.RequestError as e:
                            print("")
                    if "sum" in text:
                        try:
                            Ashley.say("Tell me the first number.")
                            Ashley.runAndWait()
                            r10 = sr.Recognizer()
                            with sr.Microphone() as src5:
                                r10.adjust_for_ambient_noise(src5)
                                first_num = r10.listen(src5)
                                try:
                                    first_num = r10.recognize_google(first_num)
                                except sr.UnknownValueError:
                                    print("")
                                except sr.RequestError as e:
                                    print("")
                            Ashley.say("Now to second number.")
                            Ashley.runAndWait()
                            r11 = sr.Recognizer()
                            with sr.Microphone() as src6:
                                r11.adjust_for_ambient_noise(src6)
                                second_num = r11.listen(src6)
                                try:
                                    second_num = r11.recognize_google(second_num)
                                except sr.UnknownValueError:
                                    print("")
                                except sr.RequestError as e:
                                    print("")
                            Ashley.say(str(first_num + second_num))
                            Ashley.runAndWait()

                        except sr.UnknownValueError:
                            print("")
                        except sr.RequestError as e:
                            print("")
                    if "divi" in text:
                        try:
                            Ashley.say("Tell me the first number.")
                            Ashley.runAndWait()
                            r12 = sr.Recognizer()
                            with sr.Microphone() as src7:
                                r12.adjust_for_ambient_noise(src7)
                                first_num = r12.listen(src7)
                                try:
                                    first_num = r12.recognize_google(first_num)
                                except sr.UnknownValueError:
                                    print("")
                                except sr.RequestError as e:
                                    print("")
                            Ashley.say("Now to second number.")
                            Ashley.runAndWait()
                            r13 = sr.Recognizer()
                            with sr.Microphone() as src8:
                                r13.adjust_for_ambient_noise(src8)
                                second_num = r13.listen(src8)
                                try:
                                    second_num = r13.recognize_google(second_num)
                                except sr.UnknownValueError:
                                    print("")
                                except sr.RequestError as e:
                                    print("")
                            Ashley.say(str(first_num / second_num))
                            Ashley.runAndWait()

                        except sr.UnknownValueError:
                            print("")
                        except sr.RequestError as e:
                            print("")
                    if "subtract" in text:
                        try:
                            Ashley.say("Tell me the first number.")
                            Ashley.runAndWait()
                            r14 = sr.Recognizer()
                            with sr.Microphone() as src9:
                                r14.adjust_for_ambient_noise(src9)
                                first_num = r14.listen(src9)
                                try:
                                    first_num = r14.recognize_google(first_num)
                                except sr.UnknownValueError:
                                    print("")
                                except sr.RequestError as e:
                                    print("")
                            Ashley.say("Now to second number.")
                            Ashley.runAndWait()
                            r15 = sr.Recognizer()
                            with sr.Microphone() as src10:
                                r15.adjust_for_ambient_noise(src10)
                                second_num = r15.listen(src10)
                                try:
                                    second_num = r15.recognize_google(second_num)
                                except sr.UnknownValueError:
                                    print("")
                                except sr.RequestError as e:
                                    print("")
                            Ashley.say(str(first_num - second_num))
                            Ashley.runAndWait()

                        except sr.UnknownValueError:
                            print("")
                        except sr.RequestError as e:
                            print("")
                except sr.UnknownValueError:
                    print("")
                except sr.RequestError as e:
                    print("")

        r5 = sr.Recognizer()
        if "random number" in recognised_instruction:
            random_factor = [-1, -2, -5, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100, 1, 2, 5, 10, 20, 30, 40, 50,
                             60, 70, 80, 90, 100]
            random_number = ra.random() * ra.choice(random_factor)
            print(f"I generated the number {random_number}")
            Ashley.say(f"I generated the number {random_number}")
            Ashley.runAndWait()

        if "cmd" in recognised_instruction:
            os.system("start /wait cmd /c {command}")

        if "date" in recognised_instruction:
            today_ = date.today()
            # dd/mm/YY
            date = today_.strftime("%m/%d/%Y")
            print(f"Today is {date}")
            Ashley.say(f"Today is {date}")
            Ashley.runAndWait()

        if "you" in recognised_instruction:
            Ashley.say("My name is Ashley. I am from US and I am 16.")
            Ashley.runAndWait()

        if "old" in recognised_instruction:
            today_ = date.today()
            # dd/mm/YY
            date = today_.strftime("%d/%m/%Y")
            if int(date[-6] + date[-5]) >= 6:
                year = int(date[-4] + date[-3] + date[-2] + date[-1])
            else:
                year = int(date[-4] + date[-3] + date[-2] + date[-1]) - 1
            age = year - 2006
            Ashley.say(f"You are {age}.")
            Ashley.runAndWait()
            print(f"You are {age}.")

        if "me" in recognised_instruction:
            today_ = date.today()
            # dd/mm/YY
            date = today_.strftime("%d/%m/%Y")
            if int(date[-6] + date[-5]) >= 6:
                year = int(date[-4] + date[-3] + date[-2] + date[-1])
            else:
                year = int(date[-4] + date[-3] + date[-2] + date[-1]) - 1
            age = year - 2006

            Ashley.say("Your name is Dora Saylikoglu.")
            Ashley.runAndWait()
            Ashley.say(f"You are {age} and from Izmir, Turkey.")
            Ashley.runAndWait()

    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")
