mymember(X,[X|_]).
mymember(X,[_|T]) :- mymember(X,T).

/*
size/2 takes a list and a number N. The query is true if the number of
elements in the list is equal to N.

| ?- size([1,2,3,4], N).
    
N = 4
    
yes
*/
size([], 0).
size([_|T], N) :- size(T, NR), N is NR+1.


/*
sumlist/2 takes a list and a number. The query is true if the sum of the 
numbers in the list is equal to the number
    
| ?- sumlist([1, 2, 3], N).
    
N = 6
    
yes
    
*/

mysumlist([], 0).
mysumlist([H|T], N) :- mysumlist(T, NT), N is NT+H.


    
/*
addlists/3 takes three lists. The query is true if the three lists 
are all the same length and the third list is the result of doing 
element-wise addition of the first two lists 
    
| ?- addlists([1,2,3], [3, 4, 5], [4, 6, 8]).
    
yes
*/


addlists([],[],[]).
addlists([HO|TO], [HT|TT], [HR|TR]) :- addlists(TO,TT,TR), HR is HO+HT.
					
    
    
