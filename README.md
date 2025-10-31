# Market Regime Detection with Unsupervised Learning

This project implements an unsupervised learning approach to detect market regimes using a combination of technical features and macro indicators, followed by analyzing regime-specific return characteristics.

## Features

- **Data Pipeline**: Automated fetching and preprocessing of market data (SPY, VIX, TLT, GLD)
- **Feature Engineering**: Rolling volatility, correlations, risk metrics, and technical indicators
- **Regime Detection**: PCA for dimension reduction + Gaussian Mixture Model for regime identification
- **Analysis Tools**: Forward return analysis, regime characteristics, interactive visualizations
- **Visualization**: Interactive plots using plotly, static visualizations with seaborn/matplotlib

## Setup

1. Create and activate a virtual environment:
```powershell
python -m venv pylap-venv
.\pylap-venv\Scripts\Activate.ps1
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

## Usage

### Interactive Notebook
Open and run `unsupervised_market_hidden_regime.ipynb` in VS Code or Jupyter:
```powershell
jupyter notebook unsupervised_market_hidden_regime.ipynb
# or
code unsupervised_market_hidden_regime.ipynb
```

### Headless Execution
Run analysis without UI and export results:
```powershell
python run_analysis.py
```

## Project Structure

- `unsupervised_market_hidden_regime.ipynb` - Main analysis notebook
- `run_analysis.py` - Headless execution script
- `requirements.txt` - Python dependencies
- `backtest.h5` - (Optional) Saved backtest results
- `LRVectorBacktester.py` - Vector backtest utilities

## Analysis Pipeline

1. **Data Collection**: Downloads daily data for SPY, VIX, TLT, and GLD using yfinance
2. **Feature Engineering**: Creates rolling features (volatility, correlations, etc.)
3. **Regime Detection**: 
   - Standardizes features
   - Reduces dimensionality with PCA
   - Identifies regimes using GMM
4. **Performance Analysis**:
   - Computes regime-specific forward return statistics
   - Generates return distribution plots
   - Calculates annualized metrics per regime

## Results & Visualization

- PCA scatter plots showing regime clusters
- Time series plot of SPY with regime markers
- Forward return distributions by regime
- Summary statistics including counts, mean returns, volatility, and Sharpe ratios

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- yfinance for market data access
- scikit-learn for ML tools
- plotly/seaborn for visualization
- pandas/numpy for data processing