#!/usr/bin/python
 # -*- coding: utf-8 -*-
import ipdb
import re

'''
 “if”  xxx
·      “except” xx
·      “but” xxx
·      “provided” xx
·      “when” xx
·      “where” xx
·      “whenever” xx
·      “unless” xx
·       “notwithstanding” xx
·       “in no event” xxx
·      “in the event”
'''

decision_point_words = { 'if', 'when', 'where', 'whenever', 'unless', 'notwithstanding', 'except', 'but', 'provided' }
two_word_decision_points = set()
three_word_decision_points = { ( 'in', 'no', 'event' ), ( 'in', 'the', 'event') }

def count_paths( text ):
    words =  re.split('\W+', text.lower() );
    decision_points_in_text = [ word for word in words if word in decision_point_words ]
    for idx, word in enumerate( words[:-1] ):
        if ( words[idx], words[idx+1] ) in two_word_decision_points:
            decision_points_in_text.append( (words[idx], words[idx+1]) )

    for idx, word in enumerate( words[:-2] ):
        if ( words[idx], words[idx+1], words[ idx+2] ) in three_word_decision_points:
            decision_points_in_text.append( (words[idx], words[idx+1], words[ idx+2]) )


    #ipdb.set_trace()
    return len( decision_points_in_text )

if __name__ == "__main__":
    text_fragment = '''
That notwithstanding any other provision of this paragraph, the association may purchase for its own account shares of stock of a bank insured by the Federal Deposit Insurance Corporation or a holding company which owns or controls such an insured bank if the stock of such bank or company is owned exclusively (except to the extent directors’ qualifying shares are required by law) by depository institutions and such bank or company and all subsidiaries thereof are engaged exclusively in providing services for other depository institutions and their officers, directors, and employees, but in no event shall the total amount of such stock held by the association in any bank or holding company exceed at any time 10 per centum of its capital stock and paid in and unimpaired surplus and in no event shall the purchase of such stock result in an association's acquiring more than 5 per centum of any class of voting securities of such bank or company” for “Provided further, That, notwithstanding any other provision of this paragraph, the association may purchase for its own account shares of stock of a bank insured by the Federal Deposit Insurance Corporation if the stock of such bank is owned exclusively by other banks (except to the extent State law requires directors qualifying shares) and if such bank is engaged exclusively in providing banking services for other banks and their officers, directors, or employees, but in no event shall the total amount of such stock held by the association exceed at any time 10 per centum of its capital stock and paid in and unimpaired surplus, and in no event shall the purchase of such stock result in the association's acquiring more than 5 per centum of any class of voting securities of such bank
'''

    print count_paths( text_fragment )


