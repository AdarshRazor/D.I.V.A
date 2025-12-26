# Tokenization: The 20% That Explains 80%

## Core Concepts

1. **Definition**: Tokenization is the process of breaking text into smaller units called tokens (words, subwords, characters, or symbols) that can be processed by computers.

2. **Purpose**: It transforms unstructured text into structured data that machine learning models can understand and process.

3. **Token Types**:
   - Word tokens (simplest form: splitting on spaces)
   - Subword tokens (parts of words)
   - Character tokens (individual characters)
   - Special tokens ([CLS], [SEP], [MASK], etc. for specific model functions)

4. **Vocabulary**: A fixed set of tokens a model recognizes, typically ranging from a few thousand to 50,000+ tokens.

## Key Tokenization Methods

1. **Word-level**: Splits text at word boundaries (spaces, punctuation)
   - Simple but struggles with out-of-vocabulary words and morphology

2. **Subword-level**: Breaks words into meaningful subunits
   - BPE (Byte-Pair Encoding): Iteratively merges most frequent character pairs
   - WordPiece (used by BERT): Similar to BPE but uses likelihood instead of frequency
   - SentencePiece/Unigram: Treats text as a sequence of characters and learns optimal subwords

3. **Character-level**: Treats each character as a token
   - Handles any word but requires more processing and loses word-level meaning

## Practical Implications

1. **Context Window**: The number of tokens a model can process at once (e.g., GPT-4 can handle 8,000-32,000 tokens).

2. **Token Economy**: In commercial APIs, costs are typically calculated per token.

3. **Language Efficiency**: Different languages tokenize differently:
   - English is token-efficient
   - Character-based languages (Chinese, Japanese) require more tokens
   - Agglutinative languages (Finnish, Turkish) with long compound words need more tokens

4. **Tokenization Artifacts**: 
   - Spaces often become part of tokens (e.g., " hello" vs "hello")
   - Case sensitivity affects tokenization
   - Special characters may be split unusually

## Why It Matters

1. **Model Performance**: Good tokenization directly impacts model understanding and generation quality.

2. **Cost and Efficiency**: Efficient tokenization reduces computational requirements and API costs.

3. **Cross-lingual Capability**: How well models handle different languages depends largely on tokenization.

4. **Prompt Engineering**: Understanding tokenization helps craft more effective prompts within token limits.