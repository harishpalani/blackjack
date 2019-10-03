### Design Document

#### What is this?
This is a single-player, terminal-based blackjack game built using Python.

#### How do I run it?
Simply clone the repository, navigate to the root in your terminal, and run `python blackjack.py` to begin playing.

#### What were some of the key design choices made?
Approaching the problem from a product launch mindset, I chose to prioritize modularity as I completed this engineering challenge. In doing so, however, I had to be careful not to make sacrifices on the user experience end, as having an eye on the future is no excuse for a lackluster product in the present.

Breaking blackjack down into its requisite components, I zeroed in on five core objects that build upon one another to form a complete experience: `Card`, `Deck`, `Player`, `Dealer` (as a subclass of Player), and `Game`. Once set on those building blocks, I shifted my focus to ease of use, both in terms of code readability as well as the final program.

Thanks to its modularity, this design greatly eases product development moving forward. For example, say we want to build in multiplayer support. The grunt work is already done — all that's left is to generate as many Player objects as necessary and tweak the gameplay accordingly!

#### Why Python?
In completing this engineering challenge, I wanted my program to be lightweight, straightforward, and easy to use. Python proved ideal for this purpose, providing all necessary modularity as an object-oriented programming language while still allowing me to get started quickly with its scripting functionality and write clean, readable code.
