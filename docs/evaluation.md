# Evaluation

## Evaluation Method

The system evaluates retrieval quality using a manual labeled dataset containing questions and relevant document sources.

## Metrics

- Hit@K
- Recall@K
- Mean Reciprocal Rank
- Retrieval latency
- Answer relevance
- Faithfulness
- Context relevance

## Retrieval Evaluation 

Results from the current local evaluation run:

| Metric | Result |
|---|---:|
| Hit@5 | 0.8 |
| Recall@K | 0.67 |
| MRR | 0.6 |
| Average retrieval latency | 344.64 ms |

## Answer Evaluation

| Metric | Result |
|---|---:|
| Answer relevance | 0.8 |
| Faithfulness | 0.8 |
| Context relevance | 0.8 |

## Limitations

- Evaluation quality depends on the manually labeled dataset.
- LLM as a judge scores are approximate quality signals.