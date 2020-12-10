% this generates a parse tree for a simple English grammar

sentence(sentence(X,Y)) -->
   noun_phrase(X), verb_phrase(Y).

noun_phrase(noun_phrase(X,Y,Z)) -->
   determiner(X), noun(Y), prepo_phrase(Z).

verb_phrase(verb_phrase(X,Y,Z)) -->
   verb(X), noun_phrase(Y), prepo_phrase(Z).

prepo_phrase(prepo_phrase([])) --> [].
prepo_phrase(prepo_phrase(X, Y)) -->
	prepo(X), noun_phrase(Y).

determiner(determiner(the)) --> [the].
determiner(determiner(a)) --> [a].
noun(noun(mouse)) --> [mouse].
noun(noun(mouse)) --> [student].
noun(noun(cat)) --> [cat].
noun(noun(course)) --> [course].
noun(noun(computer)) --> [computer].
verb(verb(hate)) --> [hated].
verb(verb(scare)) --> [scared].
verb(verb(pass)) --> [passed].
prepo(prepo(with)) --> [with].

