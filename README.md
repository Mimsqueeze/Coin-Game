# Coin Game

A Python simulation game that demonstrates Bayesian inference and optimal decision-making under uncertainty. Players must decide whether a coin is biased or unbiased based on limited flip observations, balancing the cost of gathering more information against the risk of making an incorrect guess.

## 🎯 Game Overview

In each game round:
1. A coin is randomly selected (50% chance of being biased with 75% heads probability)
2. You pay a cost to flip the coin and observe the result
3. After each flip, you decide whether to:
   - Continue flipping (paying more cost) to gather more information
   - Stop and make your guess about whether the coin is biased or unbiased
4. Correct guesses earn rewards; incorrect guesses incur penalties

## 🎮 Game Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| Prior Probability | 50% | Chance of selecting a biased coin |
| Biased Coin P(Heads) | 75% | Probability of heads for biased coin |
| Unbiased Coin P(Heads) | 50% | Probability of heads for fair coin |
| Reward | +30 | Points for correct guess |
| Penalty | -60 | Points deducted for incorrect guess |
| Flip Cost | -1 | Cost per coin flip |
| Max Flips | 15 | Maximum flips allowed per game |

## 📁 Project Structure

```
coin-game/
├── main.py              # Interactive game interface
├── coin_game.py         # Core game simulation logic
├── game_parameters.py   # Configurable game parameters
├── bayesian.py          # Optimal Bayesian strategy implementation
├── naive.py            # Simple baseline strategy
└── README.md           # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only standard library)

### Installation
1. Clone or download the project files
2. Ensure all Python files are in the same directory

### Running the Game

#### Interactive Mode
Play the game manually with decision prompts:
```bash
python main.py
```

#### Bayesian Strategy Simulation
Run 100,000 games using the optimal Bayesian strategy:
```bash
python bayesian.py
```

#### Naive Strategy Simulation
Run 100,000 games using a simple baseline strategy:
```bash
python naive.py
```

## 🧠 Strategies Explained

### Bayesian Strategy (`bayesian.py`)
The optimal strategy uses Bayesian inference to:
- Calculate posterior probabilities P(biased|observations) using Bayes' theorem
- Compute expected values for continuing vs. stopping at each decision point
- Use dynamic programming to solve the optimal stopping problem
- Make decisions that maximize expected reward

**Key Features:**
- Updates beliefs about coin bias after each flip
- Balances information gathering cost against decision confidence
- Implements optimal stopping theory with memoization for efficiency

### Naive Strategy (`naive.py`)
A simple baseline strategy that:
- Flips the coin exactly once
- Guesses "biased" if the first flip is heads
- Guesses "unbiased" if the first flip is tails

This strategy ignores the statistical properties of the problem and serves as a performance baseline.

## 📊 Expected Performance

Based on the game parameters:
- **Bayesian Strategy**: ~+6.4 points per game average
- **Naive Strategy**: ~-5.0 points per game average
- **Random Guessing**: ~-16.0 points per game average

The Bayesian approach significantly outperforms simpler strategies by making informed decisions about when to stop collecting information.

## 🔧 Customization

Modify `game_parameters.py` to experiment with different game settings:
- Change coin bias probability (`P`)
- Adjust reward/penalty structure (`REWARD`, `PENALTY`)
- Modify information cost (`COST`)
- Set different prior beliefs (`PRIOR`)

## 🧮 Mathematical Foundation

The Bayesian strategy implements the following key calculations:

**Posterior Probability Update:**
```
P(biased|h,n) = P(h,n|biased) × P(biased) / P(h,n)
```

**Expected Value Comparison:**
- E[guess] = REWARD × P(correct) - PENALTY × (1 - P(correct))
- E[continue] = -COST + P(heads) × E[reward(h+1,n+1)] + P(tails) × E[reward(h,n+1)]

## 📄 License

This project is provided for educational purposes. Feel free to use and modify for learning and research.

🤝 Improvements
The project may be improved by:

* Implementing additional decision strategies
* Developing different coin bias distributions
* Implementing strategies that don't assume the prior distribution in selecting the biased/unbiased coin, and instead approximate it

---

*This simulation demonstrates the power of Bayesian reasoning in decision-making under uncertainty, showing how mathematical principles can be applied to optimize real-world choices.*