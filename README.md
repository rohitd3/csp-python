<!-- https://rohitd3.github.io/rohit-csp3-algo/

https://replit.com/@rohittde -->


<!-- {% include navbar.html %} -->

<!-- ## Week 08 > May 9 - 13
## Week 07 > May 2 - 6
## Week 06 > April 25 - 29
## Week 05 > April 18 - 22
## Week 04 > April 4 - 8
## Week 03 > March 28 - April 1
## Week 02 > March 21 - 25
## Week 01 > March 14 - 18
## Week 00 > March 7 - 11 -->

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@rohittde/rohit-csp3-algo?embed=true"></iframe>

## 5.1 Actions

1.
- One benefit is that people can find ways to automate aspects of life using programs. The harm in this is that people will become lazy and rely on computers to do everything for them.
- One benefit is that communication is faster and more efficient between devices. The harm in this is that people will be more likely to use digital communication rather than in person interaction.
- One benefit is that information on virtually anything is readily accessible. The harm in this is that the spreading and consuming of misinformation is much more likely. 

2. I think that dopamine issues are very real, especially for high school students with heavy work loads. Students may be more inclined to relax and give themselves some down time in between assignments than to focus and get their work done. I am distracted by YouTube and other platforms on my phone when trying to do my homework sometimes, which makes it take longer. It is a problem that probably many people face, and we need to learn to overcome it.

## 5.2 Actions

1. To empower yourself in the digital world, one must be willing to use technology in useful, innovative ways and also responsibly. Using their skills to solve problems and benefit others is a great example of what makes someone empowered. Being empowered in the digital world also requires someone to have access to technology and internet services, and due to the digital divide, not everyone does.

2. An empowered person can help a non-empowered person by helping them solve problems that they would not normally be able to address. At DNHS, something I could do is build a website that benefits a group of people that may not be able to create one themselves or help make planners to keep people effcient and prevent them from procrastinating.

3. I believe red tape does contribute to blocking digital empowerment. At Del Norte, for example, certain websites are blocked by the school wifi and these links are determined by the school district. This blocks potentially useful sites, which could prevent certain classes from being digitally empowered.


## 5.1 Notes
- Flow charts
- Flow charts and UML diagrams go with the different coding styles
- Flow charts can be used to illustrate procedures, conditionals, and return values. It represents the entire code sequence.
- Flow charts are a healthy substitution for wireframing; good for team planning.
- UML diagrams
- Relate to the data of a program
- Unified Modeling Language (UML)
- Visualizes the design of a system

## 5.2 Notes

- Internet access depends on socioeconomic, geographic, demographic, and country related situations
- Digital divide is based on the different amount of access to computers and the internet
- Socioeconomic - amount of income to the household
- Geographic - If their aren't many people where someone lives, they may not have access to fast internet
- Demographics - Things like age and religion
- Some countries
- Computers uncommon in rural areas
- Limited number of websites
- Internet can only be used if protecting and advocating for the government
- High surveillance on the internet
- Digital divide affects groups and individuals
- Digital divide brings up issues of equity, access, and influence
- Digital divide affected by actions of individuals, organizations, and governments


## Code Snippet

Menu:
```
main_menu = [
    ["American Flag", americanflag.flagfunc],
    ["Swap", swap.test_swapNum],
    ["Keypad", keypad.format_tester],
    ["Tree", tree.treefunc],
    ["Pattern", pattern.patternfunc],
]
```

Building menu choices:
```
for op in options:
        index = len(prompts)
        prompts[index] = op
```

Tree height changes and the bottom is the same lenght of the height:
```
def build_tree(height):
  i = 1
  while i <= height:
    print(" " * (height - i) + "* " * i)
    #creates the spacing before each star
    i = i + 1
  print(" " * (height - 2) + "{}{}{}")
```



## Create Task

Console game which highlights a "color" string in a different color and asks the user to identify the color that is used to highlight

![image](https://user-images.githubusercontent.com/44128572/158149743-cac87140-6d79-4caf-a498-3e94fc00d6c9.png)
