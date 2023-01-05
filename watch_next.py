import spacy


def get_similar_movie(description):
    # Load the English model in spaCy
    nlp = spacy.load('en_core_web_md')

    # Read in movies from the movies.txt file
    with open('movies.txt', 'r') as f:
        movies = f.readlines()

    # Initialize variables to keep track of the most similar movie and its similarity score
    most_similar_movie = ''
    highest_similarity_score = 0

    # Iterate through each movie and calculate the similarity score to the provided description
    for movie in movies:
        title, _, movie_description = movie.partition(':')
        movie_description = nlp(movie_description)
        similarity_score = movie_description.similarity(nlp(description))

        # If the similarity score is higher than the current highest, update the most similar movie and its similarity score
        if similarity_score > highest_similarity_score:
            highest_similarity_score = similarity_score
            most_similar_movie = title

    return most_similar_movie


# Test the function with the provided description
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
print(get_similar_movie(description))
