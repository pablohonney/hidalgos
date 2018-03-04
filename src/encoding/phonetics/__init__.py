"""
Phonetic algorithms? Is that about singing? No.

Imagine you're an employee at the local restaurant. You get a call for table reservation.
The customer tells you his name which you happily put in your booking app.
Later on, possibly after you've already gone, the customer comes in.
Your fellow assistant checks him up in the table, but he can't find him there.
It comes out there was a typo.

Unlike common dictionary words that we hopefully know quite well
proper names may heavily vary in spelling, also they're hard to spell check.

That said, we need a way to encode the pronunciation, bypassing spelling pitfalls.
Encoding requires rules. Languages have grammatical rules. everyone's happy? no way.

Consider English orthography.
one sound - many writings. this is polygraphy
e.g. pIt, retrIEve, sYstem. also crEEk, recEIve, pEAk

many sounds - one writing. this is polyphony
brEAk, brEAkfast, pEAk

This discrepancy means no single set of rules will cover all the use cases.
As such we need to get rid of the most polymorphic and irregular sounds. In English those are vowels.
Carefully picked up rules may cover most of the cases while keeping the code reasonably small.

That's the core of sound encoding.

observations:
    languages with irregular orthography may strongly benefit from these.

    These algorithms are language, culture and anthroponymy* specific.
    *(I know that's scary. it's just stats on what human names are in use)

    I believe with corpus linguistics (statistics on the language usage in the wild) and some clever
    AI/dynamicProgramming at hand it'd be possible to generate phonetic algorithm rule sets with tolerable
    false-positivity rate.

resources:
http://www.dropby.com/NYSIIS.html
http://ntz-develop.blogspot.am/2011/03/phonetic-algorithms.html

TODO mutable strings needed. list would suffice. but it lacks many conventional string funcs ;(
"""
