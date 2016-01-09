# -*- coding: utf-8 -*-

from __future__ import division

def get_MLUm(index_to_tiers, participant='CHI'):
    """Mean length of utterance (MLU) in morphemes"""
    total_utterance_count = 0
    total_morpheme_count = 0

    for i in range(len(index_to_tiers)):
        if '%mor' in index_to_tiers[i] and participant in index_to_tiers[i]:
            total_utterance_count += 1
            morphs = index_to_tiers[i]['%mor'].split()
            total_morpheme_count += len(morphs)

            for morph in morphs:
                total_morpheme_count += morph.count('-')
                total_morpheme_count += morph.count('~')

    if total_utterance_count:
        return total_morpheme_count / total_utterance_count
    else:
        return 0


def get_MLUw(sents):
    """Mean length of utterance (MLU) in words"""
    # *sents* are already filtered for the desired participant like 'CHI'
    total_utterance_count = 0
    total_word_count = 0

    for sent in sents:
        total_utterance_count += 1
        total_word_count += len(sent)

    if total_utterance_count:
        return total_word_count / total_utterance_count
    else:
        return 0


def get_TTR(word_freq_dict):
    """Type-token ratio (TTR)"""
    # *word_freq_dict* already filtered for the desired participant like 'CHI'
    return len(word_freq_dict) / sum(word_freq_dict.values())


def get_IPSyn(tagged_sents, participant='CHI'):
    """Index of Productive Syntax (IPSyn)"""
    return  # TODO: work in progress
