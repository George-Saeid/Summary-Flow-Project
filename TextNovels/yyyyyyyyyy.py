larger_strings = ["This is a larger string that contains Copyright © in the middle of it.",
                  "Only there's a police car parked at their motel so the Table Of Contents",
                  "His favorite shoes are Keds. .comeback",
                  "dickhead fingernails Page."
                 ]
stop_words = ["Copyright ©", "Table Of Contents", "title Page", "All rights reserved", "www.", ".com "]

for j in range(len(larger_strings)):
    for i in range(len(stop_words)):
        if stop_words[i].lower() in larger_strings[j].lower():
            print("we found this: ")
            print(larger_strings[j])
            print('...................................................')