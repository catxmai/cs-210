sentence(L0,L2) :-
     noun_phrase(L0,L1),
     verb_phrase(L1,L2).
    
% A noun phrase, e.g. a practical student with a computer
noun_phrase(L0,L4) :- 
     det(L0,L1),
     adjectives(L1,L2),
     noun(L2,L3),
     pp(L3,L4).
    
% Adjectives consist of a (possibly empty) sequence of adjectives.
adjectives(L,L).
adjectives(L0,L2) :- 
     adj(L0,L1),
     adjectives(L1,L2).
    
% An optional prepositional phrase is either nothing or a preposition followed by a noun phrase.
pp(L,L).
pp(L0,L2) :- 
     preposition(L0,L1),
     noun_phrase(L1,L2).
    
% A verb phrase is a verb followed by a noun phrase and an optional
% prepositional phrase.
verb_phrase(L0,L4) :- 
     verb(L0,L1),
     noun_phrase_two(L1,L2),
     adverbial_phrase(L2,L3),
     pp(L3,L4).
    
% Noun phrase for verb phrase.
noun_phrase_two(L,L).
noun_phrase_two(L0,L4) :- 
     det(L0,L1),
     adjectives(L1,L2),
     noun(L2,L3),
     pp(L3,L4).

% adverbial phrase: adverbial phrase is made of both an adjective (very) and an adverb (late).
adverbial_phrase(L,L).
adverbial_phrase(L0, L2) :-
     adv_adj(L0,L1),
     adv(L1,L2).

% A simple dictionary with parts of speech
det(L,L).
det([a|T],T).
det([the|T],T).
noun([student|T],T).
noun([course|T],T).
noun([computer|T],T).
adv_adj([very|T],T).
adv_adj([extremely|T],T).
adv([late|T],T).
adj([practical|T],T).
adj([dedicated|T],T).
verb([studies|T],T).
verb([passed|T],T).
preposition([with|T],T).
    
