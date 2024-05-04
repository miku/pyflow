
# Bounded Context Example

> In the airline industry, a “flight” can have multiple meanings. There is a
> flight that is defined as a single takeoff and landing, where the aircraft is
> flown from one airport to another. There is a different kind of flight that
> is defined in terms of aircraft maintenance.  And there is yet another flight
> that is defined in terms of passenger ticketing, either nonstop or one-stop.
> Because each of these uses of “flight” is clearly understood only by its
> context, each should be modeled in a separate Bounded Context. To model all
> three of these in the same Bounded Context would lead to a confusing tangle

Bounded context, ubiquitous language:

> One is the Bounded Context and the other is the Ubiquitous Language.
> Employing a Bounded Context forces us to answer the question “What is core?”
> The Bounded Context should hold closely all concepts that are core to the
> strategic initiative and push out all others. The concepts that remain are
> part of the team’s Ubiquitous Language. You will see how DDD works to avoid
> the design of monolithic applications.

Interpretation:

* the context need things that it does not do, but requires
* the systems boundary can be whatever is physically required
    * a version HTTP API provides a kind of contract and isolates a service
    * a set of tools that work on the same data, but focus of different aspects
* once the system boundary is clear, teams can focus on one thing
* ok to build dependencies of useful services

About language:

* most code should provide a clear story, that also relates to the business
  case, even if it is a very technical piece; e.g. we are using "blocking technique to improve data quality", "users have high expectations on data quality"
* describe in detail a concept in the language of the stakeholder; the technical translation is usually a bit simpler (ex: [embargo](https://github.com/miku/span/blob/f7d8fb798e8676e59d21a4608302c4d1430c887a/licensing/embargo.go#L29-L90)
* do not invent too much own language and concepts

> A program is generally exponentially complicated by the number of notions
> that it invents for itself. To reduce this complication to a minimum, you
> have to make the number of notions zero or one, which are two numbers that
> can be raised to any power without disturbing this concept. Since you cannot
> achieve much with zero notions, it is my belief that you should base systems
> on a single notion.

## Perlis-Thompson-Principle

* Consider using **fewer** concepts, data structures, and types in foundational software.
* This style allows for more **composition** and ad hoc **reuse**. It evolves and scales more gracefully.
* When introducing a new concept, define a way to **reduce** it to an existing concept.

## Linus' on data structures

* better to have 100 programs work on a single data structure, than 10 programs
  working on 10 different data structures

> bad programmers worry about the code. Good programmers worry about data structures and their relationships. -- cf. [Torvalds' quote about good programmer [closed]](https://softwareengineering.stackexchange.com/questions/163185/torvalds-quote-about-good-programmer)

Context was git:

> git actually has a simple design, with stable and reasonably well-documented
> data structures. In fact, I'm a huge proponent of designing your code around
> the data, rather than the other way around, and I think it's one of the
> reasons git has been fairly successful […] I will, in fact, claim that the
> difference between a bad programmer and a good one is whether he considers
> his code or his data structures more important.


