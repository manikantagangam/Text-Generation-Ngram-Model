from collections import defaultdict

class NGramLanguageModel:
    def __init__(self, n, corpus):
        self.n = n
        self.ngram_model = self.build_ngram_model(corpus)
    
    def generate_ngrams(self, words):
        ngrams = []
        for i in range(len(words) - self.n + 1):
            ngram = tuple(words[i:i+self.n])
            ngrams.append(ngram)
        return ngrams
    
    def build_ngram_model(self, tokenized_corpus):
        ngram_model = defaultdict(dict)
        
        for sentence in tokenized_corpus:
            ngrams = self.generate_ngrams(sentence)
            for i in range(len(ngrams) - 1):
                prefix = ngrams[i][:-1]
                next_word = ngrams[i][-1]
                if next_word in ngram_model[prefix]:
                    ngram_model[prefix][next_word] += 1
                else:
                    ngram_model[prefix][next_word] = 1
                    
        return ngram_model
    
    def predict_next_word(self, prefix):
        if prefix in self.ngram_model:
            next_words = self.ngram_model[prefix]
            max_prob_word = max(next_words, key=next_words.get)
            return max_prob_word
        else:
            return None
    
    def generate_and_print_next_word(self, input_sentence):
        tokenized_input = input_sentence.split()
        prefix = tuple(tokenized_input[-self.n+1:])
        predicted_word = self.predict_next_word(prefix)
        
        if predicted_word:
            predicted_sentence = " ".join(tokenized_input + [predicted_word])
            print("Predicted Sentence:", predicted_sentence)
        else:
            print("No prediction available")

corpus = [
    "The sun sets over the horizon, painting the sky with hues of orange and pink.",
    "In the heart of the forest, a gentle breeze rustles the leaves.",
    "She walked along the sandy shore, feeling the cool water on her feet.",
    "The old bookshop on the corner is filled with stories waiting to be discovered.",
    "As the rain falls outside, I sit by the window with a cup of hot tea."
]
user_input = input("Enter a sentence: ")

ngram_model = NGramLanguageModel(n=2, corpus=[sentence.split() for sentence in corpus])
ngram_model.generate_and_print_next_word(user_input)
