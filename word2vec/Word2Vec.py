from DataProducer import *
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

batch_size = 128
embedding_size = 128
skip_window = 1
num_skips = 2
vocabulary_size = 50000

valid_size = 16
valid_window = 100
valid_examples = np.random.choice(valid_window, valid_size, replace=False)
num_sampled = 64


def main():
    graph = tf.Graph()
    with graph.as_default():
        train_inputs = tf.placeholder(tf.int32, shape=[batch_size])
        train_labels = tf.placeholder(tf.int32, shape=[batch_size, 1])
        valid_dataset = tf.constant(valid_examples, dtype=tf.int32)

        with tf.device('/cpu:0'):
            embeddings = tf.Variable(tf.random_uniform(
                [vocabulary_size, embedding_size], -1.0, 1.0))
            embed = tf.nn.embedding_lookup(embeddings, train_inputs)

            nce_weights = tf.Variable(tf.truncated_normal(
                [vocabulary_size, embedding_size],
                stddev=1.0 / math.sqrt(embedding_size)))
            nce_biases = tf.Variable(tf.zeros([vocabulary_size]))

        loss = tf.reduce_mean(tf.nn.nce_loss(weights=nce_weights,
                                             biases=nce_biases,
                                             labels=train_labels,
                                             inputs=embed,
                                             num_sampled=num_sampled,
                                             num_classes=vocabulary_size))
        optimizer = tf.train.GradientDescentOptimizer(1.0).minimize(loss)
        norm = tf.sqrt(tf.reduce_sum(tf.square(embeddings), 1, keep_dims=True))
        normalized_embeddings = embeddings / norm
        valid_embeddings = tf.nn.embedding_lookup(
            normalized_embeddings, valid_dataset)
        similarity = tf.matmul(
            valid_embeddings, normalized_embeddings, transpose_b=True)
        init = tf.global_variables_initializer()

    num_steps = 100001
    with tf.Session(graph=graph) as session:
        init.run()
        print("Initialized")

        average_loss = 0
        for step in range(num_steps):
            batch_inputs, batch_labels = generate_batch(
                batch_size, num_skips, skip_window)
            feed_dict = {train_inputs: batch_inputs,
                         train_labels: batch_labels}
            _, loss_val = session.run([optimizer, loss], feed_dict=feed_dict)
            average_loss += loss_val
            if step % 2000 == 0:
                if step > 0:
                    average_loss /= 2000
                print("Average loss at step ", step, ": ", average_loss)
                average_loss = 0
            if step % 10000 == 0:
                sim = similarity.eval()
                for i in range(valid_size):
                    valid_word = reverse_dictionary[valid_examples[i]]
                    top_k = 8
                    nearest = (-sim[i, :]).argsort()[1:top_k + 1]
                    log_str = "Nearest to %s:" % valid_word
                    for k in range(top_k):
                        close_word = reverse_dictionary[nearest[k]]
                        log_str = "%s %s," % (log_str, close_word)
                    print(log_str)
        final_embeddings = normalized_embeddings.eval()
    return final_embeddings


def plot_with_labels(low_dim_embs, labels, filename="tsne.png"):
    assert low_dim_embs.shape[0] >= len(labels), "More labels than embeddings"
    plt.figure(figsize=(18, 18))
    for i, label in enumerate(labels):
        x, y = low_dim_embs[i, :]
        plt.scatter(x, y)
        plt.annotate(label, xy=(x, y), xytext=(5, 2),
                     textcoords="offset points", ha="right", va="bottom")
    plt.savefig(filename)


if __name__ == "__main__":
    final_embeddings = main()
    print(np.shape(final_embeddings))
    tsne = TSNE(perplexity=30, n_components=2, init="pca", n_iter=5000)
    plot_only = 250
    low_dim_embs = tsne.fit_transform(final_embeddings[:plot_only, :])
    labels = [reverse_dictionary[i] for i in range(plot_only)]
    plot_with_labels(low_dim_embs, labels)
