import apache_beam as beam

def tokenize(text):
    return text.split()

if __name__ == '__main__':
    with beam.Pipeline() as pipeline:
        (
            pipeline
            | 'Read lines' >> beam.Create([
                'hello world',
                'I am learning apache beam',
                'this is a sample',
            ])
            | 'Tokenize' >> beam.FlatMap(tokenize)
            | 'Pair words with 1' >> beam.Map(lambda x: (x, 1))
            | 'Group and sum' >> beam.CombinePerKey(sum)
            | 'Print results' >> beam.Map(print)
        )