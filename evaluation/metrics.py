def hit_at_k(retrieved_sources,relevant_sources,k):

    retrieved_top_k = retrieved_sources[:k]

    relevant_set = {
        (
            source["filename"],
            source["page"]
        ) for source in relevant_sources
    }

    for source in retrieved_top_k:

        key = (
            source["filename"],
            source["page"]
        )

        if key in relevant_set:

            return 1

    return 0

def recall_at_k(retrieved_sources,relevant_sources,k):

    if not relevant_sources:
        return 0.0

    retrieved_top_k = retrieved_sources[:k]

    relevant_set = {
        (
            source["filename"],
            source["page"]
        ) for source in relevant_sources
    }

    retrieved_set = {
        (
            source["filename"],
            source["page"] 
        ) for source in retrieved_top_k
    }

    relevant_retrieved = relevant_set.intersection(retrieved_set)

    return(len(relevant_retrieved)/len(relevant_set))

def reciprocal_rank(retrieved_sources,relevant_sources):

    relevant_set = {
        (
            source["filename"],
            source["page"]
        ) for source in relevant_sources
    }

    for index, source in enumerate(retrieved_sources,start=1):

        key = (source["filename"],source["page"])

        if key in relevant_set:

            return 1/index

    return 0.0