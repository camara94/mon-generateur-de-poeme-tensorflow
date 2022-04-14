def charger_modele(lien_model="./../save_model/poeme_generator_90.61_pourcent.h5"):

    from tensorflow.keras.models import load_model

    import tensorflow as tf
    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    import numpy as np

    model_70_63_percent = load_model(lien_model)

    return (tf, Tokenizer, pad_sequences, np, model_70_63_percent)


tf, Tokenizer, pad_sequences, np, model = charger_modele()


def data_preprocessing(lien_fichier='./../data/poeme.txt', tokenizer=Tokenizer(), pad_sequences=pad_sequences):

    # Charger le jeu de données
    data = open(lien_fichier, "r",  encoding='utf-8').read()

    # Mettre en minuscules et diviser le texte
    corpus = data.lower().split("\n")

    # Initialiser la classe Tokenizer
    #tokenizer = Tokenizer()

    # Générer le dictionnaire d'index de mots
    tokenizer.fit_on_texts(corpus)

    word_index = tokenizer.word_index

    total_words = len(tokenizer.word_index) + 1

    # Initialiser la liste des séquences
    input_sequences = []

    # Boucle sur chaque ligne
    for line in corpus:

        # Tokeniser la ligne courante
        token_list = tokenizer.texts_to_sequences([line])[0]

        # Bouclez plusieurs fois sur la ligne pour générer les sous-phrases
        for i in range(1, len(token_list)):

            # Générer la sous-expression
            n_gram_sequence = token_list[:i+1]

            # Ajouter la sous-phrase à la liste des séquences
            input_sequences.append(n_gram_sequence)

    # Obtenir la longueur de la ligne la plus longue
    max_sequence_len = max([len(x) for x in input_sequences])

    # Pad toutes les séquences
    input_sequences = np.array(pad_sequences(
        input_sequences, maxlen=max_sequence_len, padding='pre'))

    # Créez des entrées et une étiquette en divisant le dernier jeton dans les sous-phrases
    xs, labels = input_sequences[:, :-1], input_sequences[:, -1]

    # Convertir l'étiquette en tableaux one-hot
    ys = tf.keras.utils.to_categorical(labels, num_classes=total_words)

    return tokenizer, max_sequence_len, token_list, xs, ys, word_index


tokenizer, max_sequence_len, token_list, xs, ys, word_index = data_preprocessing()


def generer_poeme(seed_text, next_words=100, token_list=token_list, model=model, tokenizer=tokenizer, max_sequence_len=max_sequence_len):

    for _ in range(next_words):
        # Convert the text into sequences
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        # Pad the sequences
        token_list = pad_sequences(
            [token_list], maxlen=max_sequence_len-1, padding='pre')
        # Get the probabilities of predicting a word
        predicted = model.predict(token_list, verbose=0)
        # Choose the next word based on the maximum probability
        predicted = np.argmax(predicted, axis=-1).item()
        # Get the actual word from the word index
        output_word = tokenizer.index_word[predicted]
        # Append to the current text
        seed_text += " " + output_word

    return seed_text


def get_word_index():
    return [{'name': word, 'weight': key} for word, key in dict(word_index).items()]
