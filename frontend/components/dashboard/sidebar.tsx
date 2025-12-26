
"use client";

import { GlassCard } from "@/components/ui/glass-card";
import { TrendingUp, TrendingDown, Search, Star } from "lucide-react";
import { useState } from "react";

interface Stock {
    ticker: string;
    name: string;
    price: number;
    change: number;
}

const POPULAR_STOCKS: Stock[] = [
    { ticker: "RELIANCE.NS", name: "Reliance Industries", price: 2985.45, change: 1.2 },
    { ticker: "TCS.NS", name: "Tata Consultancy Svc", price: 4120.30, change: -0.5 },
    { ticker: "HDFCBANK.NS", name: "HDFC Bank", price: 1450.60, change: 0.8 },
    { ticker: "INFY.NS", name: "Infosys", price: 1680.20, change: -1.2 },
    { ticker: "ICICIBANK.NS", name: "ICICI Bank", price: 1085.10, change: 0.4 },
    { ticker: "SBIN.NS", name: "State Bank of India", price: 780.50, change: 2.1 },
    { ticker: "TATAMOTORS.NS", name: "Tata Motors", price: 980.25, change: 1.5 },
    { ticker: "ADANIENT.NS", name: "Adani Enterprises", price: 3250.00, change: -0.8 },
];

interface SidebarProps {
    onSelect: (ticker: string) => void;
    currentTicker: string;
}

export function Sidebar({ onSelect, currentTicker }: SidebarProps) {
    const [searchTerm, setSearchTerm] = useState("");

    const filteredStocks = POPULAR_STOCKS.filter(stock =>
        stock.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        stock.ticker.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <GlassCard className="h-[calc(100vh-8rem)] sticky top-24 overflow-hidden flex flex-col p-4 w-64 hidden xl:flex">
            <div className="mb-4">
                <h3 className="text-sm font-semibold text-gray-400 uppercase tracking-wider mb-3 flex items-center gap-2">
                    <Star className="w-4 h-4 text-yellow-500" />
                    Market Watch
                </h3>
                <div className="relative">
                    <Search className="w-4 h-4 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2" />
                    <input
                        type="text"
                        placeholder="Filter..."
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                        className="w-full bg-white/5 border border-white/10 rounded-lg pl-9 pr-3 py-2 text-sm text-white focus:outline-none focus:border-blue-500/50"
                    />
                </div>
            </div>

            <div className="flex-1 overflow-y-auto space-y-2 pr-2 custom-scrollbar">
                {filteredStocks.map((stock) => (
                    <div
                        key={stock.ticker}
                        onClick={() => onSelect(stock.ticker)}
                        className={`p-3 rounded-lg cursor-pointer transition-all border ${currentTicker === stock.ticker
                                ? "bg-blue-500/20 border-blue-500/50"
                                : "bg-white/5 border-transparent hover:bg-white/10"
                            }`}
                    >
                        <div className="flex justify-between items-start mb-1">
                            <span className="font-bold text-sm text-white">{stock.ticker.replace('.NS', '')}</span>
                            <span className={`text-xs font-medium flex items-center gap-1 ${stock.change >= 0 ? 'text-green-400' : 'text-red-400'}`}>
                                {stock.change >= 0 ? <TrendingUp className="w-3 h-3" /> : <TrendingDown className="w-3 h-3" />}
                                {Math.abs(stock.change)}%
                            </span>
                        </div>
                        <div className="flex justify-between items-center text-xs text-gray-400">
                            <span className="line-clamp-1">{stock.name}</span>
                            <span>₹{stock.price.toFixed(0)}</span>
                        </div>
                    </div>
                ))}
            </div>
        </GlassCard>
    );
}
