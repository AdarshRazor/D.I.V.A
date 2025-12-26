# Key Insights on AI Hallucinations (The Critical 20%)

## What Are Hallucinations?
- AI hallucinations are fabricated, non-factual outputs that an AI presents as true despite not being grounded in its training data or provided context
- They occur when models generate plausible-sounding but incorrect information with high confidence

## Why Hallucinations Happen
1. **Statistical pattern matching limitations**: Models predict likely next tokens without true understanding
2. **Training incentives**: Models are trained to produce fluent, confident responses even with uncertainty
3. **Knowledge boundaries**: When asked about topics beyond training data, models extrapolate rather than admit ignorance

## Most Common Types
- **Factual confabulations**: Inventing false facts, dates, statistics, or citations
- **Logical inconsistencies**: Creating contradictory statements within the same response
- **Phantom references**: Citing non-existent sources or publications

## Detection and Mitigation
- **Retrieval-augmented generation (RAG)**: Grounding responses in verified external information
- **Self-consistency checking**: Having models evaluate their own outputs for accuracy
- **Explicit uncertainty**: Training models to express confidence levels appropriately

## Practical Implications
- Critical applications require human verification of AI outputs
- Hallucinations represent a fundamental limitation of current generative AI technology
- The problem worsens when models are asked to reason beyond their training or provide specialized expertise

Understanding these core concepts will give you a solid foundation in how and why AI hallucinations occur and their practical significance.