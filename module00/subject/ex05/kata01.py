kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Ramsus Lerdorf',
}

if __name__=="__main__":
    for language, creator in kata.items():
        print(f"{language} was created by: {creator}")