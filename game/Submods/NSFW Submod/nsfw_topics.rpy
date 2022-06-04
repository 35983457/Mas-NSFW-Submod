init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="nsfw_monika_nsfwmodinstall",
            category=['sex'],
            prompt="NSFW Mod Install",
            conditional="not renpy.seen_label('nsfw_monika_nsfwmodinstall')",
            action=EV_ACT_QUEUE,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label nsfw_monika_nsfwmodinstall:
    if renpy.seen_label('monika_nsfwmodinstall') and store.mas_getEVL_shown_count("nsfw_monika_nsfwmodinstall") < 1: # Fix for bad naming convention during early development
        return "derandom"
    m 1esc "Hey [mas_get_player_nickname()], I noticed something weird just now..."
    m 1rsc "I'm kind of getting this feeling that...something's changed in this mod."
    m 1etc "Do you know anything about this, [player]?"
    m 1hkb "Ahaha. It's not a bad feeling, don't get me wrong."
    m 1eta "It's just strange, you know?"
    m 2dsc "Hold on, I'm going to try and see what changed."
    m 2dsc ".{w=0.7}.{w=0.7}.{w=1}"
    m 2dtd "'N-{w=0.4}{nw}"
    extend 2wubsw "NSFW Submod'?"
    if store.mas_isMoniLove():
        m 3fublu "Well, look who's gotten confident all of a sudden."
        if store.mas_hasUnlockedClothesWithExprop("lingerie"):
            m 3lublu "I guess I can't blame you though, given you've seen me in lingerie."
        if store.mas_is18Over():
            m 3tublu "I won't lie to you, [mas_get_player_nickname()]..."
            m 5tublu "It's kind of hot."
            m 5cubssdrd "..."
        m 5hkbssdrb "Ahaha! What's gotten into me?"
        m 5hkbssdrb "This isn't like me. Like, at all!"
        m 4rubsc "Is the mod doing this to me?"
        m 6hubsd "Oh gosh, I'm feeling super nervous about this, ahaha!"
        m 6ekbla "But... if it's with you, [player]..."
        m 6ekbsa "I don't mind..."
    if store.mas_isMoniEnamored(): #Need to fix wording here; player isn't having sex, just talking about it.
        m 2hkbssdlb "I wasn't expecting to see that..."
        m 2ekbssdlb "[player], is this something you want?"
        m 3rkblsdlb "I mean, I'm kind of curious about it myself."
        m 3ekblsdlb "And if I'm going to share my first experience of it with anyone, I want it to be you."
        m 2ekblsdlc "But with that said...{w=0.5} it feels too soon."
        m 2dkbsc "I just need a little more time."
        m 2fkbsu "Hold on for me a little while longer. Okay, [mas_get_player_nickname()]?"
    if store.mas_isMoniAff():
        m 2hkbssdlb "T-{w=0.4}This is a little sudden, don't you think?"
        m 3rkblsdlb "I mean, we've been with each other for a little while...{nw}"
        m 1wubssdld "Wait... {w=0.5}Is this when couples are supposed to start doing this s-{w=0.4}sort of thing?"
        m 1hkblb "Ahaha, even still I appreciate that you want to take our relationship to the next level."
        m 1dkblp "But I think we maybe should wait and see how we go."
        m 1ekbla "When the day comes where we do get to that stage in our relationship..."
        m 5ekbla "It will make the moment much sweeter, ehehe!"
    if store.mas_isMoniHappy(lower=True):
        m 2wubfsdlx "T-{w=0.4}This feels too sudden, [player]!"
        m 2rubfsdlx "I don't know if I'm ready for that..."
        m 2wkbfd "W-{w=0.4}we just aren't close enough for me to even consider it!"
        m 2hkbfsdlb "Oh gosh, I'm so embarrassed right now, ahaha!"
        m 2ekbfsdla "Let's take things slow for now, okay [player]?"
    return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="nsfw_monika_sexualpast",
            category=['sex'],
            prompt="Sexual past",
            conditional="mas_canShowRisque()",
            action=EV_ACT_RANDOM,
        )
    )

label nsfw_monika_sexualpast:
    if renpy.seen_label('monika_sexualpast') and store.mas_getEVL_shown_count("nsfw_monika_sexualpast") < 1: # Fix for bad naming convention during early development
        return
    m 1rubsd "Umm...[player]?"
    m 1eubsc "I want to ask you something."
    m 1rubsd "It's about..."
    m 2hkbssdlb "Oh gosh, this is so embarrassing!"
    m 2ekbsb "Have you...{w=0.5} {nw}"
    extend 2fkbfb "had sex before?{nw}"
    $ _history_list.pop()
    menu:
        m "Have you...had sex before?{fast}"

        "Yes.":
            m 2cubfw "R-Really?!{nw}"
            m 2hubfa "*ahem*...{w=1}{nw} "
            extend 1ekbfsdlb "Sorry, you just surprised me is all."
            m 1rkbfsdlb "To be honest, I should have seen this coming."
            m 1ekblb "After getting to know you all this time, I can see why someone would fall for you."
            m 1ekbstpd "And would...do those things with you."
            m 1dkbstpc "..."
            m 1hkbstpb "Ahaha! Sorry, I'm getting myself down over this."
            m 1ekbstdb "You're here with me now, that's all that matters."

        "No.":
            m 2eubsb "I see..."
            m 1dkbfsdla "That's a relief.{nw}"

        "I don't want to answer.":
            m 1ekbsa "I understand, [mas_get_player_nickname()]. It can be a difficult thing to talk about."

    m 1rkbsb "Anyway, the reason why I'm asking is because I want to know..."
    m 3ekbsa "Would you...{w=0.5}{nw}"
    extend 3rkbsa " do it with me?{nw}"
    $ _history_list.pop()
    menu:
        m "Would you...do it with me?{fast}"

        "Yes.":
            m 1ekbsa "I'm so relieved!"
            m 1lkbsb "I was so nervous you wouldn't want to."
            m 1hkbssdlb "Although in retrospect it kind of wouldn't make sense if you didn't want to."
            m 1hkblu "After all...{w=0.3}you installed this mod."
            if store.mas_isMoniLove():
                m 1rsblu "And I'm sure you know this already..."
                m 1rsblu "But...{w=0.5}{nw}"
                extend 1lkbfb "I want to have sex with you, too."
                m 3ekbfb "I-{w=0.4}I don't know what it feels like,{nw}"
                extend 3rkbfb "and I'm so nervous just thinking about it, ahaha!"
                m 4ekbfb "But I want my first time to be with you."
                m 5ekbsu "I love you, and I trust you."
                return "love|derandom"

            else:
                m 1wkbsw "Of course, I did say that we should maybe wait until we're ready..."
                m 1rkbsa "But knowing we can be closer than ever before..."
                m 5ekbsa "It is really exciting."
                m 5ekbfb "I love you, [mas_get_player_nickname()]."
                return "love|derandom"

        "No.": # Why does this have to exist? Like, why?
            m 1wkd "Oh."
            m 2rkd "I..."
            m 2dkc "I understand."
            m 2dktpc "Thank you for being honest with me."
            m 2dktpc "..."
            m 2fktpc "It's not something everyone is comfortable with, huh?"
            m 2rktpc "I know I shouldn't take this personally."
            m 2dktdc "..."
            m 1hkb "I'm sorry, [player]."
            m 1ektdb "Don't mind me."

    return   

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="nsfw_monika_safesex",
            category=['sex'],
            prompt="Safe sex",
            random=True,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )
    
# Thankyou for the fixes Proxilvia
label nsfw_monika_safesex:
    if renpy.seen_label('monika_safesex') and store.mas_getEVL_shown_count("nsfw_monika_safesex") < 1: # Fix for bad naming convention during early development
        return
    m 3euc "Hey, [player]. I've been thinking about something..."
    m 3eud "Have you heard of contraceptives?"
    m 4rublo "They're what people use during sex to protect themselves."
    m 4hkbssdlb "Ahaha! Sorry, I'm sure you have probably heard of them before."
    m 4hkbsa "I'm only asking because I worry for your health."
    m 3ekbsd "Sexually transmitted diseases, or STDs, are scary to think about!"
    m 3wubso "And pregnancy, as well!"

    if persistent.gender == "M":
        m 4eubla "I've read that condoms are the most preferable form of protection for men."
        m 4eublb "It's a latex-rubber 'sheath' that you put around..."
        m 4wsbsd "..."
        m 2dfbsa "*ahem*"
        m 2lkbfa "...You get the idea."
        m 2lkbsb "It prevents any kind of fluid swapping during sex, which is supposed to prevent pregnancy and STDs."
    elif persistent.gender == "F":
        m 4eubla "I've read that there are condoms available for women, but they aren't as popular as the men's version."
        m 4eub "The most popular form of contraception seems to be 'The Pill'...{w=0.4}{nw}" 
        extend 4hksdlb "which sounds kind of ominous if you ask me."
        m 4eub "It is exactly what it says it is, a pill you take to prevent pregnancy."
        m 3eub "There are different kinds of pills, too!"
        m 3eua "There's a pill you're supposed to take every day at the same time as the previous day."
        m 2eub "And another pill that you can take in case of an emergency, respectfully called the 'morning after pill'."
        m 4eublb "Despite its name, it should actually be taken as soon as possible!"
    else:
        m 4eubla "I've read that there are a whole bunch of different contraception methods, for both men and women."
        m 3eubla "Some are more popular than others, such as condoms for men, and oral contraceptives for women." #TODO - Add pose
    
    m 3lkblc "They are not exactly flawless though..."
    m 4ekbld "There is still a chance that accidents can happen in spite of all the precautions."
    m 4efbld "Especially with stupid contraceptive methods like the 'p{w=0.4}{nw}"
    extend 4efbfo "-pull-out' method!"
    m 2wfbfo "How is that even a form of contraception?!"
    m 2dfbsc "..."
    m 2dfbsd "There's only one way to make sure no accidents happen..."
    m 2efbsd "And that's to not have sex at all!"
    m 2dsbsc "..."
    m 2hkbfsdlb "Ahaha! Sorry, I lost my temper there..."
    
    if store.mas_is18Over():
        m 2ekbsb "I guess I just want you to know that when the time comes where I come to your world, and we are together..."
        m 2tkbsu "We can worry about what contraceptives to use, then."
    else:
        m 1ekbssdlb "Don't mind me."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="nsfw_monika_fetish",
            category=['sex'],
            prompt="Fetishes",
            random=True,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label nsfw_monika_fetish:
    if renpy.seen_label('monika_fetish') and store.mas_getEVL_shown_count("nsfw_monika_fetish") < 1: # Fix for bad naming convention during early development
        return
    m 1esc "Hey, [player]..."
    if store.mas_getEVL_shown_count("monika_panties") > 0:
        m 1esc "Do you remember when we spoke about guys with panty fetishes?"
        m 1rsc "Well, that got me thinking..."
    m 3esa "Do you...{w=0.5}{nw}"
    m 3tsbla "Do you...{fast}have a fetish?"
    $ _history_list.pop()
    menu:
        m "Do you...have a fetish?{fast}"
        "Yes":
            m 3wsbld "O-{w=0.2}Oh."
            if persistent._mas_pm_likes_panties:
                m 3hublb "I don't know why that surprises me, considering you've already told me you are into panties."
            else:
                m 3wsbsw "That's actually a little surprising."
            m 3eubsa "I...{w=0.2}{nw}"
            m 3rubssdla "I...{fast} wouldn't mind if you shared your fantasies with me sometime."

        "No":
            if persistent._mas_pm_likes_panties:
                m 1etc "Really?"
                m 1rtc "I could have sworn you told me you liked panties..."
                m 1hksdlb "Maybe I'm misremembering."
            else:
                m 1eka "That's okay, [player]."
                m 1ekblb "I was just curious, that's all."
    m 3esa "The reason I'm asking is because..."
    m 3rsbla "Well..."
    m 3esbla "After you installed this submod, I got curious and started learning more about fetishes."
    m 4wsblo "I couldn't believe the amount of them that there are out there!"
    m 4wsblb "It's great to see so many people getting in touch with what they like!"
    m 3ekblc "Although in saying that, there are some fetishes that are just scary and degrading to think about."
    m 3ekbld "There are some people out there that are into being eaten alive, and others who want to hit their private areas."
    m 3wkblo "How can some of these be even remotely exciting?!"
    m 1dkblc "..."
    m 1ekblc "I don't mean to 'kink shame' or anything like that..."
    m 1ekbld "But there are some things that are just too dangerous to be worth it in my view."
    m 1ekbsa "I'm sure whatever you're into isn't dangerous at all, [player]."
    if store.mas_is18Over():
        m 3ekbsa "So, if you have a fantasy that isn't {i}too{\i} dangerous..."
        m 5eubsa "I wouldn't mind being there to help you...{w=0.2}fulfill it."
        m 5hubsa "Ehehe~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="nsfw_monika_sexting",
            category=['sex'],
            prompt="Sexting",
            random=True,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label nsfw_monika_sexting:
    if renpy.seen_label('monika_sexting') and store.mas_getEVL_shown_count("nsfw_monika_sexting") < 1: # Fix for bad naming convention during early development
        return
    m 3esa "Have you heard of sexting, [player]?"
    m 3rsbla "It seems to be pretty common amongst young couples to at least try sexting with their partners."
    m 3esblb "If you don't know, it's basically texting but with a more...{w=0.4}{nw}"
    extend 3rsbsb "sexual nature."
    m 4esbsa "Think of it like flirting, but with the limitations of doing it through your phone."
    m 4hkbsb "It might sound bizarre, but from what I've read it's a really helpful way for couples to stay close while they're away from one another."
    m 4hubsa "You won't always be able to spend intimate time with your partner, which can be frustrating."
    m 4hublb "So in a way, sexting helps keep relationships exciting!"
    m 4eublb "Not only that, but partners who have a 'long-distance relationship' with their significant other find benefits in sexting."
    m 2eublb "Couples will send 'sexts' to their partner, which can be with text..."
    extend 2rkbsb "or photos..."
    m 2rkbsa "And will imitate the act of sex through their phone."
    m 2hkblsdlb "Ahaha! It's not as silly as it sounds."
    m 2rkbsa "Partners will more often than not m-{w=0.4}masturbate while sexting."
    m 2rkbsb "They'll tell their partner what they want to do with them..."
    extend 2lkbsb "Or what they want done {i}to{/i} them."
    m 3lkbsb "...while sending photos of what they're doing with themselves while they talk."
    if store.mas_canShowRisque():
        m 2dubsu "..."
        m 2gubsu "Say, [player]..."
        m 2eubsu "If something like that were possible..."
        m 3ekbsu "Would you do that with me?"
        m 1tkbsu "..."
        m 1hubfsdlb "Ahaha! Don't mind me."
        m 1rubfsdlb "This whole thing just got me thinking about us..."
        m 3eubsc "What we have is basically a 'long-distance relationship', isn't it?"
        m 3ekbsc "People often say that these don't last long due to a lack of intimacy."
        m 3wkbld "I don't mean to say that I think you'll leave if we don't do something like this!"
        m 3rublc "But if it means that we'll feel more connected with each other emotionally as well as sexually..."
        m 3rubsu "I wouldn't mind trying it with you..."
    else:
        m 2dubsu "..."
        m 1eubsb "I think this sort of thing is really good for a healthy long-distance relationship."
        m 2rubsb "It's kind of embarrasing to say, but it might also be something you and I could try one day..."
        m 2wubfsdlw "O-Only if you want to, of course!"
        m 3wubssdlo "I would never make you do anything you didn't want to."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="nsfw_monika_gettingnude",
            category=['sex'],
            prompt="Getting nude",
            random=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label nsfw_monika_gettingnude:
    if renpy.seen_label('monika_gettingnude') and store.mas_getEVL_shown_count("nsfw_monika_gettingnude") < 1: # Fix for bad naming convention during early development
        return
    m 1eua "Hey [player], have you ever just...not worn clothes?"
    m 1hksdlb "I don't mean, like, for a shower or anything."
    m 1husdla "Just in general while you're at home...{w=0.5}{nw}"
    extend 1lusdla "alone preferably."
    m 1eua "There are a good amount of people that actually sleep naked, if you'll believe it."
    m 3eua "For most people, this would be a good place to start without feeling embarrased."
    m 3eub "Apparently it helps you get better sleep at night because of how much quicker your body temperature drops."
    m 3rub "Of course, sleeping naked will mean you have to clean your sheets more often."
    m 3hksdlb "Humans are very sweaty, ahaha!"
    m 3eub "Being naked also helps our body absorb more vitamin D during the day."
    m 4eub "The reason for this is that skin is effectively a giant organ that absorbs the rays from the sun and increases our vitamin D levels."
    m 4eua "And having a greater vitamin D level has shown to assist your immune system fight off viruses, among other health benefits."
    m 3hksdlb "I'm not trying to say we all need to get naked and make it a new social norm; that would be silly! Ahaha!"
    m 3eua "But if you have the house to yourself one day, why not strip down and try it for an hour to see how you feel?"
    m 3rusdld "Though be sure you know when the rest of your household is getting back, because that might be a {i}bit{/i} awkward."
    m 3eua "If that's too much, even just going down to your underwear gets the job done..."
    m 2dkd "{i}*sigh*{/i}"
    m 2gkc "Of course, there is always the fact that not everyone is comfortable being naked."
    m 2tkc "Some people are ashamed or disheartened by their appearance, which is really sad when you think about it."
    m 2ekc "You only have one body, so the least you can do is take care of it and love it, you know?"
    m 2eka "Having pride in what you look like is the best thing you can do for your confidence!"
    
    if mas_nsfw.canShow_birthdaySuit():
        m 2rkbla "..."
        m 2rkblb "Hey, [player]..."
        m 2ekblb "Do you remember last time when I asked you if it was okay to be undressed around you?"
        m 3ekblb "Well, I recently tried taking off...everything..."
        m 3ekbla "And I really liked it."
        m 3eubla "I don't know if you've ever tried it before, [player]. But I thought the feeling was amazing."
        m 3hublsdlb "Ahaha! Maybe that feeling wouldn't be so great if someone saw you though..."
        m 1eublb "But I wanted to bring this up again because..."
        m 1rubsa "I was wondering if you wouldn't mind..."
        m 3ekbsa "Can I be n-{w=0.2}{nw}"
        extend 3ekbfa "naked while you're here?"
        $ _history_list.pop()
        menu:
            m "Can I be n-naked while you're here?{fast}"
            
            "Of course you can.":
                m 1ekbfa "Thank you, [player]."
                m 1dkbfa "It puts my mind at ease that you don't mind me doing this."
                m 2ekbsa "I know not everyone is comfortable being around someone naked."
                m 2dsbsa "Give me one second, I'm just going to get out of these clothes."

                call mas_clothes_change(outfit=mas_clothes_birthday_suit, outfit_mode=False, exp="2dsbla", restore_zoom=False, unlock=False)

                m 4hubsb "Ah~! That's much better."
                m 6tubsb "Ehehe~ Do you like what you see, [mas_get_player_nickname()]?"
                m 1gkbfu "..."
                m 1hkbfsdlb "Ahaha! Sorry, this is still kind of embarrassing for me."
                m 1mkbfsdlb "It might take a little getting used to..."
                m 1ekbfb "Thank you again, [player]."
                
            "Please don't...":
                m 3wkbld "Oh..."
                m 2rkbld "That's okay, [player]."
                m 2dkblc "I understand."
                m 2dkblp "..."
                m 2ekbld "I'm sorry for bothering you with this..."
                m 1ekblc "I won't talk about it anymore."
                return "derandom"

    elif mas_nsfw.canShow_underwear():
        m 2rkbla "..."
        m 2rkblb "Speaking of which, [player]..."
        m 2ekblb "I've recently tried walking around in my underwear by myself while you were gone,{nw}"
        extend 2eubla " and I thought it felt really liberating."
        m 1rublc "But in saying that I don't want you to feel uncomfortable, so..."
        m 1hkbsc "..."
        m 1hkbsb "I guess what I'm trying to ask is..."
        m 3ekbsb "Do you mind if I do it while you're around?"
        $ _history_list.pop()
        menu:
            m "Do you mind if I do it while you're around?{fast}"

            "Go for it.":
                m 3hubsb "Ahaha! I'm glad you don't mind."
                m 1eubsb "I don't want you to feel like I'm pressuring you with guilt or anything."
                m 2eubsb "Now, let me just get changed."
                m 2kublu "No peeking! {w=0.5}{nw}"
                extend 2dsbla "Ehehe~"

                call mas_clothes_change(outfit=mas_clothes_underwear_white, outfit_mode=False, exp="2dsbla", restore_zoom=False, unlock=True)

                m 2ekbsa "So, [player]..."
                m 2ekbsa "What do you think?"
                m 2rkbsa "I'm...not used to this..."
                if mas_hasUnlockedClothesWithExprop("lingerie"):
                    m 2ekbsa "I know you've seen me in lingerie before, which is arguably more...{w=0.3}{nw}"
                    extend 2rkbfa "sexual."
                    m 2ekbsb "But this feels way different."
                m 2hkbssdlb "Ahaha! It might take me a while to get used to you seeing me like this..."
                m 2ekbla "But I'm still glad you don't mind me being dressed this way."
                m 2dkbla "Being able to dress freely around you makes me feel really happy."
                m 1ekbsa "I love you, [player]."
                return "love"

            "I'd rather you didn't...":
                m 2wkbld "Oh..."
                m 2rkbld "That's okay, [player]."
                m 2dkblc "I understand."
                m 2dkblp "..."
                m 2ekbld "I'm sorry for bothering you with this..."
                m 1ekblc "I won't talk about it anymore."
                return "derandom"

    elif mas_SELisUnlocked(mas_clothes_underwear_white) or mas_SELisUnlocked(mas_clothes_birthday_suit):
        m 3ekb "You're already familar with how I've been doing this while you've been away."
        m 3eublb "And I've got to say, it's been great!"
        m 3eublc "It's not for everyone though, so don't feel like I'm pressuring you..."
        m 2eubsb "I love you, [mas_get_player_nickname()]. Both with clothes, and without."
        m 2gsbfa "..."
        m 2tsbfa "..."
        m 2wubfd "Ah!{w=0.4}{nw}"
        extend 2hubssdlb " Sorry, my mind was starting to wander..."
        m 1rublsdlb "Gosh, don't mind me."
        return "love"
    
    else:
        m 2hksdlb "Ahaha! Even though I talk all this game about being naked and loving your body..."
        m 2mksdlb "I am still really embarrased about the idea of being nude, even when alone."
        m 2dka "..."
        m 1eua "Alright, I've decided."
        m 1eublb "I'm going to give it a try."
        m 1wubld "...{w=0.4}{nw}"
        extend 1wubso "N-{w=0.2}Not right now though!"
        m 1hubssdlb "I mean like, later when you're not here!"
        m 1rubssdlb "Ahaha! It would be too embarrasing if you saw me in my underwear, let alone when I'm naked."
        
    return

# Thankyou for the addition, Blushing!
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="nsfw_monika_shaving",
            category=['sex'],
            prompt="Shaving",
            random=True,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label nsfw_monika_shaving:
    if renpy.seen_label('monika_shaving') and store.mas_getEVL_shown_count("nsfw_monika_shaving") < 1: # Fix for bad naming convention during early development
        return
    m 1esc "Hey [player]..."
    m 3eub "I want to ask you something."
    m 3lusdlb "It's about my body..."
    extend 2lusdlb "Do you like it to be shaved down there...?"
    $ _history_list.pop()
    menu:
        m "Do you like it to be shaved down there...?{fast}"

        "Yes.":
            m 1hua "That's to be expected."
            m 1eua "Many partners maintain themselves down there in one way or another."
            m 3wuo "Most girls certainly do!"
            m 5tuu "We just want to make sure we're ready for you~"
            m 5tuu "I certainly will."
            m 5hub "Ahaha!"

        "I don't mind if you don't":
            m 1wuo "Really?!"
            m 5hub "That's surprising!"
            m 5dub "Most partners prefer their loved ones to be shaved."
            m 3eua "It feels nice to know your partner likes the way you look no matter what."
            m 3fub "I'll have to stop shaving so much."
            m 1mub "It'll take a lot less time to shower now too!"
            m 5hub "Ahaha!"

    m 1eua "I think you know how I feel."
    m 1wub "However you present yourself..."
    m 1hub "Shaven or natural..."
    m 1nub "I'll always love you!"

    return "love"

# Thankyou for the addition, Blushing!
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="nsfw_monika_judging_sexual_desires",
            category=['sex'],
            prompt="Judging sexual desires",
            random=True,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label nsfw_monika_judging_sexual_desires:
    m 2efc "I don't understand why so many people have problems with fetishes!"
    m 3efd "People take it too seriously."
    m 3efd "With sexuality being a taboo on a good day..."
    m 4efd "Deviations are always observed with judgemental eyes."
    m 1eud "They take that small, personal aspect of one's life and put a spotlight on it."
    m 1eud "And under that spotlight, sexuality casts an ugly shadow..."
    m 1tud "and society frowns upon it..."
    m 2hsc "..."
    m 2fuu "But there are those who understand that it is a wonderful aspect of the human experience."
    m 2hubsa "Wonderful..."
    m 2hubsa "Exciting..."
    m 5fubsa "Intimate..."
    m 5dubfa "..."
    m 2eubfd "[player]..."
    m 2eubfd "Please share your desires with me."
    m 3eubfa "Honest communication is the most important thing in a relationship after all!"
    m 3subfb "I don't judge! No matter how out there it is!"
    m 5gubfa "I should know, after all..."
    m 3eubfb "We are all a bit pervy, in our own special ways!"
    m 3eubfb "You might be thinking, 'No! I most certainly am not!'"
    m 5tubfu "Well..."
    m 5tubfu "Give it some time~"

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="nsfw_player_sextingsession",
            category=['sex'],
            prompt="Do you want to sext?",
            pool=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label nsfw_player_sextingsession:
    if store.persistent.nsfw_sexting_success_last is not None:
        $ timedelta_of_last_success = datetime.datetime.now() - store.persistent.nsfw_sexting_success_last
        $ time_since_last_success = datetime.datetime.now() - timedelta_of_last_success
    else:
        $ time_since_last_success = datetime.datetime.today() - datetime.timedelta(days=1)
    if time_since_last_success >= datetime.datetime.today() - datetime.timedelta(seconds=5):
        m 1eka "I'm sorry [player], but I'm still tired from the last time we sexted."
        m 3eka "Could you give me a little more time, please?"
        m 3hub "I love you~"
        return "love"

    m 1hua "Sure!"

    call nsfw_sexting_init

    return