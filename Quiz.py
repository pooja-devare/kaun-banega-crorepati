questions=[["Cold brew, Latte, Espresso are all examples of which beverage?","Tea", "Fruit juice", "Coffee","Lassi",3],
           
           ["Which of these is a term for a score used in racquet sports?", "Hate", "Love", "Down","Up",2],

           ["Rajat Sharma, Sonia Singh, Rahul Kanwal and Sumit Awasthi are all associated with which profession?", "Astrology", "Journalism", "Medicine", "Law",2],

           [" In Sept 2020, which iconic motorcycle brand announced that it is shutting down its manufacturing facilities in India?", "Harley Davidson", "Triumph", "Indian", "Arctic cat",1],

           [" Which was the colour of the saree worn by Madhuri Dixit in the song 'Didi tera dewar deewana,' which triggered a fashion trend in the country?" , "Green", "Red", "Yellow","Purple",4],

           [" Which of these does not feature in the five pillars of Islam?","Salat", "Zakat", "Hadith","Hajj",3],

           [" In which state of India is the town of Jamtara located?","Jharkhand", "Odisha", "Bihar","West Bengal",1],

           ["Which novel, made into a TV series by Mira Nair in 2020, revolves around the lives of four Indian families -- the Mehras, the Kapoors, the Khans and the Chatterjis?","Great Indian Novel", "A Suitable Boy", "A Fine Balance","The Golden Gate",2],

           [" The leader heard in this audio clip has never served in which of these ministries?", "Human Resource Development", "Women and Child Development", "Textiles and Law", "Justice",4],

           [" The 2020 film Gul Makai is a biopic of which of these personalities?"," Benazir Bhutto", "Aisha Chaudhary", "Greta Thunberg","Malala Yousafzai",4],

           ["Which of the following dynasties did the Kanva dynasty overthrow to come to power around 73 BCE in Magadha?", "Maurya dynasty", "Shunga dynasty", "Pala dynasty","Chera dynasty",2],


           ["The trophy which is awarded to the winners of the women's singles at the Australian open is named after which legendary tennis star?", "Daphne Akhurst", "Margaret Court", "Evonne Goolagong Cawley","Lesley Bowrey",1],

           [" Who became the first chancellor of the Aligarh Muslim University in 1920?" ,"Sultan Jahan Begum", "Maulana Abul Kalam Azad", "Sir Syed Ahmad Khan","Mir Usman Ali Khan",1] ,

           ["Who is the first woman and also former astronaut to reach the deepest point of the ocean, Mariana trench?","Sally Ride", "Valentina Tereshkova", "Svetlana Savitskaya","Kathryn D Sullivan",4],

           ["Where in Singapore did Netaji Subhash Chandra Bose make the first proclamation of an Azad Hind government?","Cathay cinema hall", "Fort Canning park", "National University of Singapore","National Gallery of Singapore",1]
           
           ]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,16000,320000,640000,1250000,2500000,5000000,10000000]
money=0
for i in range(0, len(questions)):
    question=questions[i]
    print(f"\n\nquestions for  rs. {levels[i]}")
    print(f"a. {question[1]}                 b. {question[2]}")
    print(f"c. {question[3]}                 d. {question[4]}")
    reply=int(input("Enter your answer from 1 to 4  or 0 to quit:\n"))
    if (reply==0):
        money=levels[i-1]
        break
    if (reply == question[-1]):
        print(f"coreect answer you have won rs {levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
    else:
        print("Wrong answer")
        break

print(f"Your take home money is {money}")