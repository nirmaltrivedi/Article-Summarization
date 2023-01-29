# import spacy
# from spacy.lang.en.stop_words import STOP_WORDS
# from string import punctuation
# from heapq import nlargest
#
text = """Anthony Edward Stark, more commonly known as Tony Stark, is a fictional character primarily portrayed by Robert Downey Jr. in the Marvel Cinematic Universe (MCU) media franchise—based on the Marvel Comics character of the same name—commonly known by his alias, Iron Man. Stark is initially depicted as an industrialist, genius inventor, and playboy who is CEO of Stark Industries. Initially the chief weapons manufacturer for the U.S. military, he has a change of heart and redirects his technical knowledge into the creation of mechanized suits of armor which he uses to defend against those that would threaten peace around the world. He becomes a founding member and leader of the Avengers. Following his failed Ultron Program, the internal conflict within the Avengers due to the Sokovia Accords, and Thanos successfully erasing half of all life in the Blip, Stark retires, marries Pepper Potts, and they have a daughter named Morgan. However, Stark rejoins the Avengers on a final mission to undo Thanos' actions. He creates time travel, and the Avengers successfully restore trillions of lives across the universe. However, Stark inevitably sacrifices his life to defeat Thanos and his army. Stark chooses Peter Parker as a successor."""
# def summarymodel(text):
# 	stopwords = list(STOP_WORDS)
# 	nlp = spacy.load('en_core_web_sm')
# 	doc = nlp(text)
# 	tokens = [tokens.text for tokens in doc]
# 	word_freq = {}
# 	for word in doc:
# 		if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
# 			if word.text not in word_freq.keys():
# 				word_freq[word.text] = 1
# 			else:
# 				word_freq[word.text] += 1
# 	max_freq = max(word_freq.values())
# 	for word in word_freq.keys():
# 		word_freq[word] = word_freq[word] / max_freq
# 	sent_tokens = [sent for sent in doc.sents]
# 	sent_scores = {}
# 	for sent in sent_tokens:
# 		for word in sent:
# 			if word.text in word_freq.keys():
# 				if sent not in sent_scores.keys():
# 					sent_scores[sent] = word_freq[word.text]
#
# 				else:
# 					sent_scores[sent] += word_freq[word.text]
# 	select_len = int(len(sent_tokens) * 0.3)
# 	summary = nlargest(select_len, sent_scores, key=sent_scores.get)
# 	final_summary = [word.text for word in summary]
# 	summary = ' '.join(final_summary)
# 	print(summary)
# 	return summary
# summarymodel(text)

from transformers import pipeline
summarizer = pipeline('summarization')
output = summarizer(text,max_length=250,min_legth=30,do_stable=False)
print(output)