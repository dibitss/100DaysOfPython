print('''
       ---_ ......._-_--.
      (|\ /      / /| \  \\
      /  /     .'  -=-'   `.
     /  /    .'             )
   _/  /   .'        _.)   /
  / o   o        _.-' /  .'
  \          _.-'    / .'*|
   \______.-'//    .'.' \*|
    \|  \ | //   .'.' _ |*|
     `   \|//  .'.'_ _ _|*|
      .  .// .'.' | _ _ \*|
      \`-|\_/ /    \ _ _ \*\\
       `/'\__/      \ _ _ \*\\
      /^|            \ _ _ \*
     '  `             \ _ _ \      
                       \_
''')
print("Welcome to 100 days of Python.")
print("Your mission is to learn Python.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

if input("You start your challenge. Do you skip what you already know or try to actually learn something new? Type 'skip' or 'learn': ").lower() == "learn":
    if input("Do you type all of your code or just copy/paste from the solutions? Type 'write' or 'copy': ").lower() == "write":
        if input("By the end of the challenge you'll be a 'beginner', 'intermediate' or 'professional'?: ").lower() == "professional":
            print("Yassss! Yasss, you will be! You already Won!")
        else:
            print("With that attitude, for sure! Game Over!")
    else:
        print("There's no future for you. Game Over!")
else:
    print("Where's your learning hunger??? Game Over!")