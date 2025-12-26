# StockSwing AI 📈

> **Real-time Stock Prediction Engine for Indian Markets**

StockSwing is a sophisticated stock analysis and prediction platform that leverages AI to forecast stock trends. It provides real-time visualization of historical data against predicted future movements for **170+ major Indian stocks** (NIFTY 50, NIFTY Next 50, and mid-caps) and US tech giants.

![StockSwing Dashboard](.gemini/antigravity/brain/787b69fd-1c16-4ac3-9f1f-c80b48e9543d/sbin_prediction_chart_1766758237037.png)

## 🚀 Key Features

- **Comprehensive Stock Coverage**: Support for **170+ stocks** including:
  - NIFTY 50 & NIFTY Next 50
  - Major US Stocks (Apple, Tesla, Google, etc.)
  - Sector-wise categorization (Banking, IT, Pharma, etc.)
- **Advanced Visualization**:
  - Interactive **dual-line charts** showing Actual vs Predicted prices.
  - Custom tooltips and gradients for intuitive data reading.
  - **730 days (2 years)** of historical context for every stock.
- **AI-Powered Predictions**:
  - 7-day future price forecasting.
  - Trend analysis (Bullish/Bearish/Neutral) with confidence scores.
  - *Note: Currently uses a simulation engine while the LSTM model is being optimized.*
- **Data & Metadata**:
  - Automatic data synchronization with Yahoo Finance.
  - Detailed data processing insights (Data points used, processing steps).

## 🛠️ Tech Stack

- **Frontend**: Next.js 14, React, Tailwind CSS, Framer Motion, Recharts
- **Backend**: FastAPI (Python), SQLModel (SQLite), Pandas, Numpy, TensorFlow/Keras
- **Data Source**: yfinance (Yahoo Finance API)

## 🏁 Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/xdutsuay/stockswing.git
   cd stockswing
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   python -m app.main  # Starts server at http://localhost:8000
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   npm run dev  # Starts UI at http://localhost:3000
   ```

## 🗺️ Roadmap

- [x] **Phase 1: Enhanced Visualization** (Completed)
  - Dual-line charts, improved UI/UX, and expanded stock list.
- [ ] **Phase 2: News Sentiment Integration** (In Progress)
  - Integration with NewsAPI/Alpha Vantage.
  - LLM-based sentiment analysis of financial news.
  - Evidence-based prediction explanations.
- [ ] **Phase 3: Evidence Panel**
  - "Why did the AI predict this?" explanations.
- [ ] **Phase 4: Accuracy Metrics**
  - Real-time tracking of prediction accuracy (MSE/MAE).

## 📝 Latest Updates

- **Expanded Database**: Added complete NIFTY 50 and Next 50 support.
- **Chart UI**: Upgraded to high-fidelity 500px charts with prediction overlays.
- **Data Engine**: Increased historical data fetching from 100 days to 730 days for better accuracy.

---
*Built with ❤️ for traders and developers.*