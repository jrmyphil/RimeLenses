# RimeLenses
A short Python program to count and list all the valid configurations of the lens contraption to view linking books in the Rime Age in Myst (2021).

The gorgeous 2021 Myst remake added an extra age that was not in the original, but was created for RealMyst. In the age -- which is named [Rime](https://cyan.com/2025/03/18/press-release-new-age-brings-additional-intrigue-to-2020-myst-remake/) -- there is a contraption that passes light from an aurora through colored lenses in order to allow the user to see into the age that a book is linked to. If you're not up on your Myst lore, don't worry about it. The point is this: there's this puzzle that has several variables and rules for how they can be combined, and how they should be combined to solve a puzzle. There are a lot of possible combinations and only one successful combination to view each of the linking books, so the games has clues lying around that key the reader in to the specific solutions for each book, mostly in the form of partially-completed charts and notes about rules for valid combinations. That's the actual puzzle part of the puzzle.

But... what if there were an unknown linking book and we wanted to view the world connected to it? Could we accomplish it through trial and error?

Short answer: no. It would take too long. But how do I know that? I built a Python script to figure out how many valid set-ups there are by applying all the rules to the given variables! Admittedly, the game never makes it clear whether some of the rules are universal or apply only to the solutions for the specific linking book in question. I took most of them to be universal.

Here's what we have:
1. The contraption has four lenses stacked vertically, and the colors of the lenses are chosen by the user.
2. There are six colors of lenses. The colors are (in ascending order of frequency in this alternate reality): White, Yellow, Magenta, Blue, Cyan, and Green.
3. Each lens has an aperture, which is either small, medium, or large.
4. The top lens always has the smallest aperture.
5. The rod holding the lenses has heights marked from 1 to 20, and the height of each arm can be adjusted.
6. Each arm takes up 3 marks worth of room on the rod.

And here are the rules for making valid combinations:
1. No two lenses can be the same color.
2. The lenses must either ascend or descend through the spectrum.
3. Adjacent lenses must not have the same aperture size.
4. There must be 11 or fewer marks worth of height between the highest and lowest lens.
5. If a lens is between two lenses that both have the smallest aperture, the middle lens must be equidistant between them.

So yeah, that's a lot. Turns out after combining all the variables and applying those rules, my script came up with 20,400 possible valid combinations. I elected not to try them all.

Check out the script! My goal was not only to count all the combinations but to list them all, so if you run it, be prepared to have a lot of lines of text in your console.

  - jrmyphil
