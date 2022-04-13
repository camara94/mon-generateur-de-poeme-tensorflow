def charger_modele(lien_model="./../save_model/poeme_generator_74_37_pourcent.h5"):

    from tensorflow.keras.models import load_model

    import tensorflow as tf
    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    import numpy as np

    model_70_63_percent = load_model(lien_model)

    return (tf, Tokenizer, pad_sequences, np, model_70_63_percent)


tf, Tokenizer, pad_sequences, np, model = charger_modele()
