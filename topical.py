#! /usr/bin/env python

# https://towardsdatascience.com/end-to-end-topic-modeling-in-python-latent-dirichlet-allocation-lda-35ce4ed6b3e0

import re
import numpy as np
from cli import cli
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction import text as sktext
from sklearn.decomposition import LatentDirichletAllocation as LDA


sns.set_style('whitegrid')


def validate_infile(infile):
    import os
    if not os.path.isfile(infile):
        print(
            cli.colors.FAIL + 'fail' + cli.colors.ENDC + ' ' +
            'the file {} does not exist'.format(infile)
        )
        exit(1)
    if(infile[-4:] != '.txt'):
        print(
            cli.colors.FAIL + 'fail' + cli.colors.ENDC + ' ' +
            'topical currently supports only text files'
        )
        exit(1)


def validate_outdir(outdir):
    import os
    if not os.path.isdir(outdir):
        print(
            cli.colors.FAIL + 'fail' + cli.colors.ENDC + ' ' +
            'the directory {} does not exist'.format(outdir)
        )
        exit(2)


def create_wordcloud(s):
    from wordcloud import WordCloud

    wc = WordCloud(background_color="white", max_words=500, width=1920, height=1080, scale=5)
    wc.generate(s)

    if(cli.args.outdir):
        wc.to_file(cli.args.outdir + '/wordcloud.jpg')
    else:
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.show()


def graph_common_words(count_data, count_vectorizer):
    words = count_vectorizer.get_feature_names()
    total_counts = np.zeros(len(words))

    for t in count_data:
        total_counts += t.toarray()[0]

    count_dict = (zip(words, total_counts))
    count_dict = sorted(count_dict, key=lambda x: x[1], reverse=True)[0:15]
    words = [w[0] for w in count_dict]
    counts = [w[1] for w in count_dict]
    x_pos = np.arange(len(words))

    plt.figure(2, figsize=(15, 15/1.6180))
    plt.subplot(title='15 most common words')
    sns.set_context("notebook", font_scale=1.25, rc={"lines.linewidth": 2.5})
    sns.barplot(x_pos, counts, palette='husl')
    plt.xticks(x_pos, words, rotation=90)
    plt.xlabel('words')
    plt.ylabel('counts')

    if(cli.args.outdir):
        plt.ioff()
        plt.savefig(cli.args.outdir + '/common-words.jpg')
    else:
        plt.show()


# Helper function
def get_topics(model, count_vectorizer, n_top_words):
    words = count_vectorizer.get_feature_names()
    topics = []
    for topic_idx, topic in enumerate(model.components_):
        topics.append(" ".join([words[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
    return topics


def main():

    # Validate the infile
    validate_infile(cli.args.infile)

    # Validate the outfile if it exists
    if cli.args.outdir:
        validate_outdir(cli.args.outdir)

    # Read the infile into memory
    infile_as_str = ''
    with open(cli.args.infile, 'r') as f:
        infile_as_str = f.read()

    # Standardize data
    document_delimiter = cli.args.document_delimiter
    data = infile_as_str.split(document_delimiter)
    data = list(map(lambda x: re.sub("[,.!?';-]", '', x), data))  # remove punctuation
    data = list(map(lambda x: x.lower(), data))  # lowercase everything
    data_as_string = ','.join(data)
    count_vectorizer = sktext.CountVectorizer(stop_words='english')
    count_data = count_vectorizer.fit_transform(data)

    # Produce a wordcloud if desired
    if(cli.args.create_wordcloud):
        create_wordcloud(data_as_string)

    # Produce a graph of common words if desired
    if(cli.args.graph_common_words):
        graph_common_words(count_data, count_vectorizer)

    # Tweak the two parameters below
    number_topics = int(cli.args.number_topics)
    number_words = int(cli.args.words_per_topic)

    # Create and fit the LDA model
    lda = LDA(n_components=number_topics, n_jobs=-1)
    lda.fit(count_data)

    # Print the topics found by the LDA model
    topics = get_topics(lda, count_vectorizer, number_words)
    print('Topics found via LDA:')
    for topic_idx, topic in enumerate(topics):
        print('\nTopic #%d:' % topic_idx)
        print(topic)
    print('\n')


if __name__ == "__main__":
    main()
