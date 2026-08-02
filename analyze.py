import pandas

codes_for_questions = pandas.read_csv("./codes_for_questions.csv")
codes_for_answers = pandas.read_csv("./codes_for_answers.csv")
list_of_answers = pandas.read_csv("./list_of_answers.csv")


def support_in_one_party_elections(party:str)->int:
    """
    Return the number of supporters of party in question Q2.

    >>> isinstance(support_in_one_party_elections("מחל"), int)
    True
    """
    question = codes_for_questions[
        codes_for_questions["Variable"].str.startswith("Q3_") &
        codes_for_questions["Label"].str.startswith(party + " -")
    ]["Variable"].iloc[0]
    return int((list_of_answers["Q2"] == int(question[3:])).sum())


def support_in_multi_party_elections(party:str)->int:
    """
    Return the number of supporters of party in question Q3.

    >>> isinstance(support_in_multi_party_elections("מחל"), int)
    True
    """
    question = codes_for_questions[
        codes_for_questions["Variable"].str.startswith("Q3_") &
        codes_for_questions["Label"].str.startswith(party + " -")
    ]["Variable"].iloc[0]
    return int(list_of_answers[question].sum())


def parties_with_different_relative_order()->tuple:
    """
    Return two parties whose relative order is different in Q2 and Q3.

    >>> result = parties_with_different_relative_order()
    >>> result is None or len(result) == 2
    True
    """
    questions = codes_for_questions[
        codes_for_questions["Variable"].str.startswith("Q3_") &
        codes_for_questions["Label"].str.contains(" -")
    ]

    parties = questions["Label"].str.split(" -").str[0].to_numpy()
    one = list_of_answers["Q2"].value_counts().reindex(
        range(1, len(questions) + 1), fill_value=0
    ).to_numpy()
    multi = list_of_answers[questions["Variable"].tolist()].sum().to_numpy()

    votes = pandas.DataFrame({"party": parties, "one": one, "multi": multi})
    pairs = votes.merge(votes, how="cross", suffixes=("_a", "_b"))
    pairs = pairs.query("one_a > one_b and multi_a < multi_b")

    if len(pairs) == 0:
        return None

    pair = pairs.iloc[0]
    return pair["party_a"], pair["party_b"]

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

    # Use this code for testing via console input-output:
    # party = input()
    # if party == "parties_with_different_relative_order":
    #     print(parties_with_different_relative_order())
    # else:
    #     print(support_in_one_party_elections(party), support_in_multi_party_elections(party))
