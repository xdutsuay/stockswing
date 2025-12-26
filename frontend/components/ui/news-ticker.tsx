
"use client";

import { motion } from "framer-motion";
import { TrendingUp, TrendingDown, Minus } from "lucide-react";

interface NewsItem {
    ticker: string;
    headline: string;
    sentiment: "positive" | "negative" | "neutral";
    change?: number;
}

// Simulated data for the ticker - in real app, could come from context or props
const tickerData: NewsItem[] = [
    { ticker: "NIFTY", headline: "Market hits all-time high", sentiment: "positive", change: 1.2 },
    { ticker: "SBIN", headline: "Q3 Results Expected Tomorrow", sentiment: "neutral", change: 0.0 },
    { ticker: "TCS", headline: "New Deal with UK Govt", sentiment: "positive", change: 0.8 },
    { ticker: "INFY", headline: "Margins under pressure", sentiment: "negative", change: -0.5 },
    { ticker: "RELIANCE", headline: "Oil to Chemical business spin-off discussions", sentiment: "positive", change: 1.5 },
    { ticker: "HDFCBANK", headline: "Merger synergies taking time", sentiment: "negative", change: -0.2 },
];

export function NewsTicker() {
    return (
        <div className="w-full bg-black/40 border-b border-white/5 backdrop-blur-md overflow-hidden py-2 flex items-center z-50">
            <div className="flex whitespace-nowrap">
                {/* Scroll twice to create seamless loop */}
                {[...Array(2)].map((_, i) => (
                    <motion.div
                        key={i}
                        className="flex gap-12 px-6"
                        initial={{ x: 0 }}
                        animate={{ x: "-100%" }}
                        transition={{
                            repeat: Infinity,
                            ease: "linear",
                            duration: 30, // Adjust speed here
                            repeatType: "loop"
                        }}
                    >
                        {tickerData.map((item, idx) => (
                            <div key={idx} className="flex items-center gap-3 text-sm">
                                <span className="font-bold text-gray-200">{item.ticker}</span>
                                <span className={
                                    item.sentiment === "positive" ? "text-green-400" :
                                        item.sentiment === "negative" ? "text-red-400" :
                                            "text-gray-400"
                                }>
                                    {item.change && item.change > 0 ? "+" : ""}{item.change}%
                                </span>
                                <span className="text-gray-400 border-l border-white/10 pl-3">{item.headline}</span>
                            </div>
                        ))}
                    </motion.div>
                ))}
            </div>
        </div>
    );
}
