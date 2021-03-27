from tkinter import *
#click function
def click():
    entered_text = textentry.get()
    dropdown_text = clicked.get()
    entered_text = entered_text.replace(" ","")
    entered_text = entered_text.lower()
    output.delete(0.0, END)
    if dropdown_text in cats and entered_text in cats and dropdown_text != entered_text:
        definition = "Please only choose one cat breed at a time."
    elif entered_text in cats:
        definition = cats[entered_text]
    elif dropdown_text in cats:
        definition = cats[dropdown_text]
    else:
        definition = "Sorry, we don't have that cat breed in our database!"
    output.insert(END, definition)
#exit function
def close_window():
    window.destroy()
    exit()
#dictionary
cats = {
    "abyssinian": "Abyssinians are highly intelligent and intensely inquisitive. They love to investigate and will leave no nook or cranny unexplored. They’re sometimes referred to as “Aby-grabbys” because they tend to take things that grab their interest. The playful Aby loves to jump and climb. Keep a variety of toys on hand to keep her occupied, including puzzle toys that challenge her intelligence.",
    "americanshorthair": "Formerly used to keep rodents and vermin away from food stores, the American Shorthair still enjoys exercising her hunting skills on unsuspecting insects. As a smart, moderately active feline, she enjoys learning tricks and challenging her intelligence with puzzles and interactive toys.",
    "bengal": "Bengal Cats are curious and confident with the tameness of a domestic tabby and the beauty of an Asian Leopard Cat. Learn more about Bengals and their playful personality, plus information on their health and how to feed them.",
    "chartreux": "Often called the smiling cat of France, the Chartreux has a sweet, smiling expression. This sturdy, powerful cat has a distinctive blue coat with a resilient wooly undercoat. Historically known as fine mousers with strong hunting instincts, the Chartreux enjoys toys that move. This is a slow-maturing breed that reaches adulthood in three to five years. A loving, gentle companion, the Chartreux forms a close bond with her family.",
    "mainecoon": "The Maine Coon is solid, rugged, and can endure a harsh climate. A distinctive characteristic of this cat is the smooth, shaggy coat. This breed is well-proportioned, has a balanced appearance, and has adapted to varied environments.",
    "burmese": "The Burmese thrives on companionship with her humans and other cats. Like her Siamese ancestors, she enjoys conversation, but has a much softer, sweeter voice.",
    "siamese": "Siamese Cats are incredibly social, intelligent and vocal—they’ll talk to anyone who wants to listen, and even those who don’t. They also play well with other cats, dogs and children. In fact, they thrive on companionship, so it’s a good idea to get them a playmate to interact with throughout the day. Although they’re active and curious, they also love curling up on their human’s lap or snuggling up next to them in bed.",
    "americanbobtail": "The American Bobtail is an athletic breed that looks like a bobtailed wildcat and has many dog-like tendencies.",
    "americancurl": "With unique ears that curl back, and an inquisitive expression reminiscent of happy surprise, the American Curl brings a smile to everyone who meets her.",
    "americanwirehair": "Intelligent and highly adaptable, the American Wirehair is an American original, with a completely unique wired coat.",
    "balinesejavanese": "The Balinese, also known as Javanese depending on coat color and pattern, is regal and aristocratic in appearance, but a curious kitten at heart.",
    "bengal": "Bengal Cats are curious and confident with the tameness of a domestic tabby and the beauty of an Asian Leopard Cat. Learn more about Bengals and their playful personality, plus information on their health and how to feed them.",
    "birman": "The Birman is a cat of distinction as well as legend. With their exotic ancestry, luxurious pointed coats, “#f1f7f9 gloved” paws and mesmerizing blue eyes, this is a breed with undeniable charisma.",
    "bombay": "The Bombay is an easy-going, yet energetic cat. She does well in quiet apartments where she’s the center of attention as well as in lively homes with children and other pets. She’ll talk to you in a distinct voice, and you’re likely to find her in the warmest spot in your home, whether that’s in the sunlight from a window or curled up under the covers in bed with you.",
    "britishshorthair": "The British Shorthair is an easygoing feline. She enjoys affection but isn’t needy and dislikes being carried. She’ll follow you from room to room, though, out of curiosity. British Shorthairs aren’t lap cats, but they do enjoy snuggling next to their people on the couch.",
    "cornishrex": "Bat-eared, big-eyed and wavy-coated, the Cornish Rex has a distinctive look and exceptionally silky coat due to not having guard hairs like other breeds. This active cat has a small, whippetlike body and loves to climb, leap and sprint. With kittenlike antics that last a lifetime, this feline likes to be where the action is. The Cornish Rex is perfect for those who want a cat to participate in their family life.",
    "devonrex": "Because of her curly coat and her tail, which wags when she is happy, the Devon Rex is sometimes called a poodle who purrs.",
    "egyptianmau": "The Egyptian Mau is fiercely devoted to her humans and vocally shows signs of happiness and affection by meowing in a pleasant voice. She’ll also slowly swish her tail and knead with her front paws. She loves to display her hunting skills by chasing and retrieving a toy. As a moderate- to highly active breed, you may find her on top of your refrigerator or bookshelves.",
    "himalayan": "The Himalayan Cat is a sweet and mild-tempered feline. She’s affectionate but selective. Although she loves lying in your lap and being pet, she may be reserved around guests. Serene, quiet environments with few day-to-day changes are best for the Himmie.",
    "persian": "The docile Persian is a quiet feline who enjoys a calm and relaxing environment. Although she enjoys sitting in her humans’ laps and being pet, she’s just as happy to sit and observe everyone’s comings and goings from afar. Persians are independent and selective in who they show affection to.",
    "munchkin": "They may have short legs, but Munchkin Cats don’t let it hold them back. Although they can’t make big leaps like other breeds, they can make small jumps, climb and even sit back on their haunches to get a better look at something.",
    "oriental": "The Oriental is a sleek, elegant cat with large, flaring ears and almond-shaped eyes, often associated with the Siamese breeds.",
    "savannah": "The Savannah Cat’s personality is playful, adventurous and loyal. Unlike most cats, she loves to play in water and can even be trained to walk on a leash and play fetch. Don’t be fooled by her dog-like personality, though.",
    "russianblue": "The Russian Blue is gentle, quiet and even shy around strangers, but she’s affectionate and loyal toward her people. She’ll follow you around and even ride on your shoulder.",
    "ragdoll": "Ragdolls are loving, smart and playful. They show affection to their people by greeting them, following them around, sitting in their laps and snuggling in bed. Ragdoll cats can also learn tricks and certain behaviors with positive reinforcement.",
    "scottishfold": "The smart and friendly Scottish Fold loves playing with challenging, puzzling toys to test her intelligence. She also loves human interaction with her people and loves attention. Scottish Folds prefer the company of their humans or other cats (or cat-friendly dogs), rather than being left alone for hours at a time.",
    "siberian": "This friendly and affectionate feline will follow you around as you go about your day, and purr in your lap as you comb her coat. Siberian Cats love their humans but aren’t shy around strangers.",
    "sphynx": "The hairless Sphynx is muscular with broad ears, a wide-eyed, friendly expression, and an affectionate personality to match.",
    "toyger": "With her beautiful bold stripes and powerful body, the Toyger looks like a jungle tiger. This breed has a friendly, outgoing temperament and delights in being with people, even strangers, and gets along well with other pets. Highly intelligent, the Toyger is easy to train to go on leash walks and to play fetch. The Toyger is generally robust and healthy.",
    "ragamuffin": "A gorgeous, massive breed with large, expressive eyes, the RagaMuffin is sweet and loving, often described as being like a teddy bear. This feline thrives on attention and is a wonderful family pet that gets along well with other cats and cat friendly dogs. The RagaMuffin has an easygoing, calm temperament and can be trained to walk on a leash, play fetch and sit up to beg. This healthy breed reaches adulthood at 4 years old."
}
#configure window
window = Tk()
window.iconbitmap("suscat.ico")
window.title("Cats")
window.configure(background = "#161513", padx = "5", pady = "5")
window.resizable(0, 0)
#add cat photo
cat1 = PhotoImage(file = "cat.gif")
Label(window, image = cat1, bg = "#161513").grid(row = 0, column = 0, sticky = W)
#create label
Label(window, text = "Use the dropdown menu or text entry to enter a type of cat.", bg = "#161513", fg = "#f1f7f9", font = "none 12 bold").grid(row = 1, column = 0, sticky = W)
#dropdown
clicked = StringVar()
clicked.set("Cats")
drop = OptionMenu(window, clicked, *cats)
drop.configure(relief = "flat", bg = "#f1f7f9", fg = "#161513", borderwidth = "0", activebackground = "#f1f7f9", activeforeground = "#161513")
drop.grid(row = 2, column = 0, sticky = W)
#text entry
Label(window, text = "\n", bg = "#161513", fg = "#f1f7f9", font = "none 6 bold").grid(row = 3, column = 0, sticky = W)
textentry = Entry(window, width = 20, bg = "#f1f7f9")
textentry.grid(row = 3, column = 0, sticky = W)
#submit button
Label(window, text = "\n", bg = "#161513", fg = "#f1f7f9", font = "none 6 bold").grid(row = 4, column = 0, sticky = W)
Button(window, text = "Submit", width = 6, command = click, relief = "flat", bg = "#fcd757", fg = "#161513", borderwidth = "0", activebackground = "#fcd757", activeforeground = "#161513").grid(row = 4, column = 0, sticky = W)
#create another label
Label(window, text = "\n", bg = "#161513", fg = "#f1f7f9", font = "none 10 bold").grid(row = 5, column = 0, sticky = W)
Label(window, text = "Cat facts:", bg = "#161513", fg = "#f1f7f9", font = "none 12 bold").grid(row = 5, column = 0, sticky = W)
#create a text box
output = Text(window, width = 75, height = 6, wrap = WORD, background = "#f1f7f9")
output.grid(row = 6, column = 0, columnspan = 2, sticky = W)
#citation
Label(window, text = "\n", bg = "#161513", fg = "#f1f7f9", font = "none 6 bold").grid(row = 8, column = 0, sticky = W)
Label(window, text = "Definitions courtesy of Purina.", bg = "#161513", fg = "#f1f7f9", font = "none 10 bold").grid(row = 8, column = 0, sticky = W)
#exit
Label(window, text = "\n", bg = "#161513", fg = "#f1f7f9", font = "none 6 bold").grid(row = 9, column = 0, sticky = W)
Button(window, text = "Quit", width = 6, command = close_window, relief = "flat", bg = "#fc7a57", fg = "#161513", borderwidth = "0", activebackground = "#fc7a57", activeforeground = "#161513").grid(row = 9, column = 0, sticky = W)
#initialize window
window.mainloop()