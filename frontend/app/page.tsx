"use client";

import { useState, useEffect } from 'react';
import { GlassCard } from '@/components/ui/glass-card';
import { StockChart } from '@/components/dashboard/stock-chart';
import { SearchDropdown } from '@/components/ui/search-dropdown';
import { Activity, RefreshCw, TrendingUp, TrendingDown, Minus, Zap, Clock, Database, Cog } from 'lucide-react';
import { motion } from 'framer-motion';


import { NewsTable } from '@/components/dashboard/news-table';
import { NewsTicker } from '@/components/ui/news-ticker';
import { Sidebar } from '@/components/dashboard/sidebar';
import { Newspaper } from 'lucide-react';

export default function Home() {
  const [ticker, setTicker] = useState("SBIN.NS");
  const [history, setHistory] = useState([]);
  const [prediction, setPrediction] = useState<any>(null);
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(false);
  const [syncing, setSyncing] = useState(false);
  const [predicting, setPredicting] = useState(false);

  // ... (fetchData and handleSync functions remain the same) ...

  const fetchNews = async (symbol: string) => {
    try {
      const protocol = window.location.protocol;
      const hostname = window.location.hostname;
      const res = await fetch(`${protocol}//${hostname}:8000/api/v1/news/${symbol}`);
      if (res.ok) {
        const data = await res.json();
        setNews(data);
      }
    } catch (e) {
      console.error("Failed to fetch news:", e);
    }
  };

  const fetchData = async (symbol?: string) => {
    const targetTicker = symbol || ticker;
    setLoading(true);
    // Fetch news in parallel
    fetchNews(targetTicker);

    try {
      const protocol = window.location.protocol;
      const hostname = window.location.hostname;
      const res = await fetch(`${protocol}//${hostname}:8000/api/v1/history/${targetTicker}`);
      if (res.ok) {
        const data = await res.json();
        setHistory(data);
      } else if (res.status === 404) {
        // Auto-sync
        console.log(`No data found for ${targetTicker}, auto-syncing...`);
        setHistory([]);
        await handleSync();
      } else {
        setHistory([]);
      }
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  // ... (rest of the functions remain the same) ...

  // Inside return statement, add News Section below StockChart GlassCard

  {/* News Section */ }
  <GlassCard className="mt-8">
    <h3 className="text-lg font-medium mb-4 flex items-center gap-2">
      <Newspaper className="w-5 h-5 text-gray-300" />
      Latest Market News
    </h3>
    <NewsTable news={news} isLoading={loading} />
  </GlassCard>


  const handleSync = async () => {
    setSyncing(true);
    try {
      const protocol = window.location.protocol;
      const hostname = window.location.hostname;
      await fetch(`${protocol}//${hostname}:8000/api/v1/sync/${ticker}`, { method: 'POST' });
      // Poll or wait, for now just wait 2s
      setTimeout(() => fetchData(), 2000);
    } catch (e) {
      console.error(e);
    } finally {
      setSyncing(false);
    }
  };

  const handlePredict = async () => {
    setPredicting(true);
    try {
      const protocol = window.location.protocol;
      const hostname = window.location.hostname;
      const res = await fetch(`${protocol}//${hostname}:8000/api/v1/predict`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ticker: ticker, days: 7 })
      });
      if (res.ok) {
        const data = await res.json();
        setPrediction(data);
      } else {
        const error = await res.json();
        console.error('Prediction error:', error);
        alert(`Error: ${error.detail || 'Failed to generate predictions'}`);
      }
    } catch (e) {
      console.error(e);
      alert('Failed to connect to prediction service');
    } finally {
      setPredicting(false);
    }
  }

  const handleTickerSelect = (symbol: string) => {
    setTicker(symbol);
    setPrediction(null); // Clear old prediction
    fetchData(symbol);
  };

  useEffect(() => {
    fetchData();
  }, []);

  const getTrendIcon = (trend: string) => {
    switch (trend) {
      case 'bullish':
        return <TrendingUp className="w-5 h-5 text-green-400" />;
      case 'bearish':
        return <TrendingDown className="w-5 h-5 text-red-400" />;
      default:
        return <Minus className="w-5 h-5 text-gray-400" />;
    }
  };

  const getTrendColor = (trend: string) => {
    switch (trend) {
      case 'bullish':
        return 'text-green-400 bg-green-500/10 border-green-500/20';
      case 'bearish':
        return 'text-red-400 bg-red-500/10 border-red-500/20';
      default:
        return 'text-gray-400 bg-gray-500/10 border-gray-500/20';
    }
  };

  const formatDateTime = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <main className="min-h-screen p-8 md:p-12 relative">
      <div className="fixed top-0 left-0 w-full z-50">
        <NewsTicker />
      </div>
      {/* Header - moved down slightly to account for fixed ticker */}
      <header className="flex justify-between items-center mb-12 mt-8">
        <div className="flex items-center gap-3">
          <div className="p-2 bg-blue-500/20 rounded-lg">
            <Activity className="w-8 h-8 text-blue-400" />
          </div>
          <h1 className="text-3xl font-bold tracking-tighter text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300">
            StockSwing AI
          </h1>
        </div>
        <div className="flex items-center gap-4">
          {/* Search Bar with Autocomplete */}
          <SearchDropdown
            value={ticker}
            onSelect={handleTickerSelect}
            placeholder="Search Ticker..."
          />
          <button onClick={handleSync} disabled={syncing} className="p-2 hover:bg-white/5 rounded-full transition-colors relative">
            <RefreshCw className={`w-5 h-5 text-gray-400 ${syncing ? 'animate-spin text-blue-400' : ''}`} />
          </button>
        </div>
      </header>

      {/* Content Layout */}
      <div className="flex gap-8">
        {/* Sidebar - Visible on XL screens */}
        <Sidebar onSelect={handleTickerSelect} currentTicker={ticker} />

        {/* Main Content Area */}
        <div className="flex-1 grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Main Chart Section */}
          <section className="lg:col-span-2 space-y-8">
            <GlassCard className="min-h-[500px] flex flex-col relative overflow-hidden">
              <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-green-500 to-emerald-400 opacity-50" />

              <div className="flex justify-between items-center mb-6">
                <div>
                  <h2 className="text-2xl font-semibold text-white">{ticker}</h2>
                  <p className="text-sm text-gray-400">Real-time Prediction Engine</p>
                </div>
                <div className="flex gap-2">
                  <button
                    onClick={handlePredict}
                    disabled={predicting || loading}
                    className="px-6 py-2 bg-gradient-to-r from-emerald-600 to-green-600 rounded-lg text-sm font-medium hover:shadow-[0_0_20px_rgba(16,185,129,0.5)] transition-all flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    <Zap className="w-4 h-4" />
                    {predicting ? 'Predicting...' : 'Run Prediction'}
                  </button>
                </div>
              </div>

              <StockChart
                data={history}
                predictionData={prediction?.predictions ?
                  prediction.predictions.map((price: number, index: number) => ({
                    date: new Date(Date.now() + (index + 1) * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
                    value: price
                  })) : undefined
                }
              />

              {/* Data Metadata Section */}
              {prediction && (
                <div className="mt-6 pt-6 border-t border-white/10 space-y-4">
                  <h3 className="text-sm font-medium text-gray-300 flex items-center gap-2">
                    <Database className="w-4 h-4" />
                    Data Processing Information
                  </h3>
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div className="bg-white/5 rounded-lg p-3 border border-white/10">
                      <div className="flex items-center gap-2 mb-2">
                        <Clock className="w-4 h-4 text-blue-400" />
                        <span className="text-xs text-gray-400">Data Loaded</span>
                      </div>
                      <p className="text-sm text-white">{formatDateTime(prediction.data_loaded_at)}</p>
                    </div>
                    <div className="bg-white/5 rounded-lg p-3 border border-white/10">
                      <div className="flex items-center gap-2 mb-2">
                        <Database className="w-4 h-4 text-cyan-400" />
                        <span className="text-xs text-gray-400">Data Points Used</span>
                      </div>
                      <p className="text-sm text-white">{prediction.data_points_used} historical records</p>
                    </div>
                    <div className="bg-white/5 rounded-lg p-3 border border-white/10">
                      <div className="flex items-center gap-2 mb-2">
                        <Clock className="w-4 h-4 text-purple-400" />
                        <span className="text-xs text-gray-400">Last Price Date</span>
                      </div>
                      <p className="text-sm text-white">{formatDateTime(prediction.last_updated)}</p>
                    </div>
                  </div>

                  {/* Processing Steps */}
                  <div className="bg-white/5 rounded-lg p-4 border border-white/10">
                    <div className="flex items-center gap-2 mb-3">
                      <Cog className="w-4 h-4 text-green-400" />
                      <span className="text-xs text-gray-400 font-medium">Processing Steps</span>
                    </div>
                    <div className="space-y-2">
                      {prediction.processing_steps.map((step: string, index: number) => (
                        <div key={index} className="flex items-start gap-2 text-xs text-gray-300">
                          <span className="text-blue-400 font-mono">{index + 1}.</span>
                          <span>{step}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              )}
            </GlassCard>
          </section>

          {/* Sidebar / Stats */}
          <section className="space-y-6">
            <GlassCard>
              <h3 className="text-lg font-medium mb-4 flex items-center gap-2">
                {prediction && getTrendIcon(prediction.trend)}
                AI Insights
              </h3>
              <div className="space-y-4">
                {prediction && prediction.predictions ? (
                  <div className="space-y-4">
                    {/* Trend Analysis */}
                    <div className={`p-4 rounded-lg border ${getTrendColor(prediction.trend)}`}>
                      <span className="text-xs uppercase tracking-wider">Current Trend</span>
                      <div className="flex items-center justify-between mt-2">
                        <div className="text-2xl font-bold capitalize">{prediction.trend}</div>
                        <div className="text-sm">
                          {Math.round(prediction.trend_confidence * 100)}% confidence
                        </div>
                      </div>
                    </div>

                    {/* Predictions */}
                    <div className="space-y-2">
                      <p className="text-sm text-gray-400">Predicted next 7 days:</p>
                      <div className="flex flex-wrap gap-2">
                        {prediction.predictions.map((p: number, i: number) => (
                          <span key={i} className="text-xs py-1 px-2 rounded bg-white/5 border border-white/10">
                            Day {i + 1}: {p.toFixed(2)}
                          </span>
                        ))}
                      </div>
                    </div>
                  </div>
                ) : (
                  <div className="text-sm text-gray-500 text-center py-8">
                    No prediction data available. Run the engine to see insights.
                  </div>
                )}
              </div>
            </GlassCard>

            <GlassCard>
              <h3 className="text-lg font-medium mb-4">Stock Details</h3>
              <div className="space-y-3">
                <div className="flex justify-between text-sm">
                  <span className="text-gray-400">Latest Close</span>
                  <span>{history.length > 0 ? history[history.length - 1].close.toFixed(2) : '-'}</span>
                </div>
                <div className="flex justify-between text-sm">
                  <span className="text-gray-400">Volume</span>
                  <span>{history.length > 0 ? (history[history.length - 1].volume / 1000000).toFixed(2) + 'M' : '-'}</span>
                </div>
              </div>
            </GlassCard>
          </section>
        </div>
      </div>
    </main>
  );
}

