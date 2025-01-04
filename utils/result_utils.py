import numpy as np

def get_recomendations(Q, movies, movie_list, num_recs = 5):
    # get recomendations for any number of input movies

    user_movs = Q[movie_list,:]
    rec_indexes = np.argpartition(-np.sum(user_movs, axis=0), kth=(num_recs+len(movie_list)))[:num_recs+len(movie_list)]
    movie_recs =  [rec for rec, id in movies.items() if id[0] in rec_indexes]
    return movie_recs[:num_recs]